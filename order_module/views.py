import json
import time
import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from eshop_project.settings import *
from product_module.models import Product
from .models import Order, OrderDetail


@login_required
def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        context = {'status': 'invalid_count', 'text': 'مقدار وارد شده معتبر نمی باشد', 'confirm_button_text': 'باشه', 'icon': 'warning'}
        return JsonResponse(context)
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.order_details.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                OrderDetail.objects.create(order_id=current_order.id, product_id=product_id, count=count)
            context = {'status': 'success', 'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد', 'confirm_button_text': 'باشه', 'icon': 'success'}
            return JsonResponse(context)
        else:
            context = {'status': 'not_found', 'text': 'محصول مورد نظر یافت نشد', 'confirm_button_text': 'باشه', 'icon': 'error'}
            return JsonResponse(context)
    else:
        context = {'status': 'not_auth', 'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید', 'confirm_button_text': 'ورود به سایت', 'icon': 'error'}
        return JsonResponse(context)


@login_required
def request_payment(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()
    if total_price == 0:
        return redirect(reverse('users:user_basket_page'))
    request_header = {'accept': 'application/json', 'content-type': 'application/json'}
    request_data = {'merchant_id': MERCHANT, 'callback_url': CallbackURL, 'amount': total_price * 10, 'description': description}
    request_ = requests.post(url=ZP_API_REQUEST, data=json.dumps(request_data), headers=request_header)
    authority = request_.json()['data']['authority']
    if len(request_.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        error_code = request_.json()['errors']['code']
        error_message = request_.json()['errors']['message']
        return HttpResponse(f"Error code: {error_code}, Error Message: {error_message}")


@login_required
def verify_payment(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()
    status = request.GET.get('Status')
    authority = request.GET.get('Authority')
    if status == 'OK':
        request_header = {'accept': 'application/json', 'content-type': 'application/json'}
        request_data = {'merchant_id': MERCHANT, 'amount': total_price * 10, 'authority': authority}
        request_ = requests.post(url=ZP_API_VERIFY, data=json.dumps(request_data), headers=request_header)
        if len(request_.json()['errors']) == 0:
            text_status = request_.json()['data']['code']
            if text_status == 100:
                current_order.is_paid = True
                current_order.payment_date = time.time()
                current_order.save()
                ref_str = request_.json()['data']['ref_id']
                context = {'success': f'تراکنش شما با کد پیگیری {ref_str} با موفقیت انجام شد'}
                return render(request, 'order_module/payment_result.html', context)
            elif text_status == 101:
                context = {'info': 'این تراکنش قبلا ثبت شده است'}
                return render(request, 'order_module/payment_result.html', context)
            else:
                error_message = str(request_.json()['data']['message'])
                context = {'error': error_message}
                return render(request, 'order_module/payment_result.html', context)
        else:
            error_code = request_.json()['errors']['code']
            error_message = request_.json()['errors']['message']
            context = {'error': error_message, 'error_code': error_code}
            return render(request, 'order_module/payment_result.html', context)
    else:
        context = {'error': 'پرداخت با خطا مواجه شد یا کاربر از پرداخت ممانعت کرد'}
        return render(request, 'order_module/payment_result.html', context)

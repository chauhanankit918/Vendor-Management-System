from django.shortcuts import render
import razorpay

from vendor_mgmt_sys import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


def create_order(request):
    order_amount = 50000  # Amount in paise
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'

    response = client.order.create({
        'amount': order_amount,
        'currency': order_currency,
        'receipt': order_receipt,
        'payment_capture': '1'
    })

    return render(request, 'payment.html', {'order': response})

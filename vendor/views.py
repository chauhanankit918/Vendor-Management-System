# from django.http import HttpResponseBadRequest
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# import razorpay
# from vendor_mgmt_sys import settings
from django.http import HttpResponseBadRequest
import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')


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

    context = {
        'order_id': response['id'],
        'amount': order_amount,
        'currency': order_currency,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID
    }

    return render(request, 'home.html', context)


# views.py
@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            # Payment is successful, proceed with your logic
            return render(request, 'success.html')
        except razorpay.errors.SignatureVerificationError as ex:
            # Payment failed, handle accordingly
            print(ex)
            return HttpResponseBadRequest()

    return HttpResponseBadRequest()

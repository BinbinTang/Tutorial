from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.template import RequestContext, loader

from django.views import generic

from transactions.models import Account, Transaction

from django.db import transaction
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'transactions/index.html'
    context_object_name = 'all_account_list'

    def get_queryset(self):
        """Return the last five published polls."""
        # return Poll.objects.order_by('-pub_date')[:5]
        return Account.objects.all()


class DetailView(generic.DetailView):
    model = Account
    template_name = 'transactions/detail.html'


class ResultsView(generic.DetailView):
    model = Account
    template_name = 'transactions/results.html'


class FlowView(generic.ListView):
    template_name = 'transactions/flow.html'
    context_object_name = 'all_transaction_list'

    def get_queryset(self):
        return Transaction.objects.all()


@transaction.non_atomic_requests
def deal(request, account_id):
    selected_account = get_object_or_404(Account, pk=account_id)
    try:
        input_amount = request.POST['transaction_amount']
    except(KeyError, Account.DoesNotExist):
        return render(request, 'transactions/detail.html', {
            'account': selected_account,
            'error_message': "You didn't input the correct amount.",
        })
    else:
        try:
            transact_balance = float(input_amount)
        except ValueError:
            return render(request, 'transactions/detail.html', {
                'account': selected_account,
                'error_message': "Input a number",
            })

        else:
            if (transact_balance == 0):
                return render(request, 'transactions/detail.html', {
                    'account': selected_account,
                    'error_message': "Input a non-zero number",
                })
            with transaction.atomic():
                lock_account = Account.objects.select_for_update().get(pk=account_id)

                if (lock_account.balance + transact_balance < 0):
                    lock_account.balance -= transact_balance
                    return render(request, 'transactions/detail.html', {
                                                                        'account': lock_account,
                                                                        'error_message': "Insufficient balance",
                                                                        })
                    
                lock_account.balance += transact_balance
                lock_account.save()
                
                Transaction.objects.create(
                    account=lock_account,
                    amount=input_amount, endBalance=lock_account.balance)

                return HttpResponseRedirect(reverse(
                                            'transactions:results',
                                            args=(lock_account.id,)))

            return HttpResponse("Transaction failed!", status_code=400)

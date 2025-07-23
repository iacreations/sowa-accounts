from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from . models import Newcustomer, Newsupplier,Newclient,Newemployee,Newasset,Newinvoice,InvoiceItem

# Create your views here.
# index view
def home(request):

    return render(request, 'Home.html', {})

# assets view
def assets(request):
    assets = Newasset.objects.all()
      
    return render(request, 'Assets.html', {'assets':assets})
# assets form 
def add_assests(request):
    if request.method=='POST':
        asset_name = request.POST.get('asset_name')
        asset_tag = request.POST.get('asset_tag')
        asset_category = request.POST.get('asset_category')
        asset_description = request.POST.get('asset_description')
        department = request.POST.get('department')
        custodian = request.POST.get('custodian')
        asset_status = request.POST.get('asset_status')
        purchase_price = request.POST.get('purchase_price')
    # purchase_date = request.POST.get('purchase_date')
        supplier = request.POST.get('supplier')
        funding_source = request.POST.get('funding_source')
        life_span = request.POST.get('life_span')
        depreciation_method = request.POST.get('depreciation_method')
        residual_value = request.POST.get('residual_value')
        accumulated_depreciation = request.POST.get('accumulated_depreciation')
        remaining_value = request.POST.get('remaining_value')
        asset_account = request.POST.get('asset_account')
        capitalization_date = request.POST.get('capitalization_date')
        cost_center = request.POST.get('cost_center')
        asset_condition = request.POST.get('asset_condition')
        maintenance_schedule = request.POST.get('maintenance_schedule')
        insurance_details = request.POST.get('insurance_details')
        notes = request.POST.get('notes')
        asset_attachments =request.FILES.get('asset_attachments')
# handling the date 
        capitalization_date_str = request.POST.get('capitalization_date')
        capitalization_date = None
        if capitalization_date_str:
            try:

               capitalization_date = datetime.strptime(capitalization_date_str, '%d/%m/%Y')
            except ValueError:
                capitalization_date = None  # Or handle error
# purchase date
        purchase_date_str = request.POST.get('purchase_date')
        purchase_date = None
        if purchase_date_str:
            try:
                purchase_date = datetime.strptime(purchase_date_str, '%d/%m/%Y')
            except ValueError:
                purchase_date = None 

    # waranty date
        warranty_str = request.POST.get('warranty')
        warranty = None
        if warranty_str:
            try:
                warranty = datetime.strptime(warranty_str, '%d/%m/%Y')
            except ValueError:
                warranty = None 

    # saving the assets
        asset = Newasset(asset_name=asset_name,asset_tag=asset_tag,asset_category=asset_category,asset_description=asset_description,department=department,custodian=custodian,asset_status=asset_status,purchase_price=purchase_price,purchase_date=purchase_date,supplier=supplier,warranty=warranty,funding_source=funding_source,life_span=life_span,depreciation_method=depreciation_method,residual_value=residual_value,accumulated_depreciation=accumulated_depreciation,remaining_value=remaining_value,asset_account=asset_account,capitalization_date=capitalization_date,cost_center=cost_center,asset_condition=asset_condition,maintenance_schedule=maintenance_schedule,insurance_details=insurance_details,notes=notes,asset_attachments=asset_attachments,)

        asset.save()

    return render(request, 'assets_form.html', {})
# editing assets
def edit_asset(request, pk):
    asset = get_object_or_404(Newasset,pk=pk)
    if request.method=='POST':
        asset.asset_name = request.POST.get('asset_name',asset.asset_name)
        asset.asset_tag = request.POST.get('asset_tag',asset.asset_tag)
        asset.asset_category = request.POST.get('asset_category',asset.asset_category)
        asset.asset_description = request.POST.get('asset_description',asset.asset_description)
        asset.department = request.POST.get('department',asset.department)
        asset.custodian = request.POST.get('custodian',asset.custodian)
        asset.asset_status = request.POST.get('asset_status',asset.asset_status)
        asset.purchase_price = request.POST.get('purchase_price',asset.purchase_price)
        asset.purchase_date = request.POST.get('purchase_date',asset.purchase_date)
        asset.supplier = request.POST.get('supplier',asset.supplier)
        # asset.warranty = request.POST.get('warranty',asset.warranty)
        asset.funding_source = request.POST.get('funding_source',asset.funding_source)
        asset.life_span = request.POST.get('life_span',asset.life_span) 
        asset.depreciation_method = request.POST.get('depreciation_method',asset.depreciation_method)
        asset.residual_value = request.POST.get('residual_value',asset.residual_value)
        asset.accumulated_depreciation = request.POST.get('accumulated_depreciation',asset.accumulated_depreciation)
        asset.remaining_value = request.POST.get('remaining_value',asset.remaining_value)
        asset.asset_account = request.POST.get('asset_account',asset.asset_account)
        asset.cost_center = request.POST.get('cost_center',asset.cost_center)
        asset.asset_condition = request.POST.get('asset_condition',asset.asset_condition)
        asset.maintenance_schedule = request.POST.get('maintenance_schedule',asset.maintenance_schedule)
        asset.insurance_details = request.POST.get('insurance_details',asset.insurance_details)
        asset.notes = request.POST.get('notes',asset.notes)
        # handling the date 
        capitalization_date_str = request.POST.get('capitalization_date')
        if capitalization_date_str:
            try:
                asset.capitalization_date = datetime.strptime(capitalization_date_str, '%d/%m/%Y')
            except ValueError:
                pass  # Keep the original value or handle error

        purchase_date_str = request.POST.get('purchase_date')
        if purchase_date_str:
            try:
                asset.purchase_date = datetime.strptime(purchase_date_str, '%d/%m/%Y')
            except ValueError:
                pass  # Keep the original value or handle error

        warranty_str = request.POST.get('warranty')
        if warranty_str:
            try:
                asset.warranty = datetime.strptime(warranty_str, '%d/%m/%Y')
            except ValueError:
                pass  # Keep the original value or handle error


    
    
# working on the files
        if 'asset_attachments' in request.FILES:
            asset.asset_attachments = request.FILES['asset_attachments']
        asset.save()

        return redirect('assets')
    return render(request, 'assets_form.html', {'asset': asset})
# customer view

def customers(request):
    customers = Newcustomer.objects.all()

    return render(request, 'Customers.html', {'customers':customers})

# customer form view

def add_customer(request):
    if request.method == 'POST':
        logo =request.FILES.get('logo')
        customer_name =request.POST.get('name')
        company_name =request.POST.get('company')
        email =request.POST.get('email')
        phone_number =request.POST.get('phonenum')
        mobile_number =request.POST.get('mobilenum')
        website =request.POST.get('website')
        tin_number =request.POST.get('tin')
        opening_balance =request.POST.get('balance')
        registration_date =request.POST.get('today')
        street_one =request.POST.get('street1')
        street_two =request.POST.get('street2')
        city =request.POST.get('city')
        province =request.POST.get('province')
        postal_code =request.POST.get('postalcode')
        country =request.POST.get('country')
        actions =request.POST.get('actions')
        notes =request.POST.get('notes')
        attachments =request.FILES.get('attachments')
        new_customer = Newcustomer(logo=logo,customer_name=customer_name,company_name=company_name,email=email,phone_number=phone_number,mobile_number=mobile_number,website=website,tin_number=tin_number,opening_balance=opening_balance,registration_date=registration_date,street_one=street_one,street_two=street_two,city=city,province=province,postal_code=postal_code,country=country,actions=actions,notes=notes,attachments=attachments)
        new_customer.save()
        # adding save actions
        save_action = request.POST.get('save_action')
        if save_action == 'save&new':
            return redirect('add-customer')
        elif save_action == 'save&close':
            return redirect('customers')
       
    return render(request, 'customers_form.html', {})
# editing the customer table

def edit_customer(request, pk):
    customer = get_object_or_404(Newcustomer, pk=pk)

    if request.method == 'POST':
        customer.customer_name = request.POST.get('name',customer.customer_name)
        customer.company_name = request.POST.get('company',customer.company_name)
        customer.email = request.POST.get('email', customer.email)
        customer.phone_number = request.POST.get('phonenum',customer.phone_number)
        customer.mobile_number = request.POST.get('mobilenum')
        customer.website = request.POST.get('website',customer.website)
        customer.tin_number = request.POST.get('tin',customer.tin_number)
        customer.opening_balance = request.POST.get('balance',customer.opening_balance)
        customer.registration_date = request.POST.get('today',customer.registration_date)
        customer.street_one = request.POST.get('street1',customer.street_one)
        customer.street_two = request.POST.get('street2',customer.street_two)
        customer.city = request.POST.get('city',customer.city)
        customer.province = request.POST.get('province',customer.province)
        customer.postal_code = request.POST.get('postalcode',customer.postal_code)
        customer.country = request.POST.get('country',customer.country)
        customer.actions = request.POST.get('actions',customer.actions)
        customer.notes = request.POST.get('notes',customer.notes)

        if 'logo' in request.FILES:
         customer.logo = request.FILES['logo']
        if 'attachments' in request.FILES:

            customer.attachments = request.FILES['attachments']

        customer.save()

        return redirect('customers')

    return render(request, 'customers_form.html', {'customer': customer})

# Delete view
def delete_customer(request, pk):
    customer = get_object_or_404(Newcustomer, pk=pk)
    customer.delete()
    return redirect('customers')

# clients view

def clients(request):
    clients = Newclient.objects.all()
    return render(request, 'Clients.html', {'clients':clients})

# client form view

def add_client(request):
    if request.method=='POST':
        logo =request.FILES.get('logo')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        company_email = request.POST.get('company_email')
        address = request.POST.get('address')
        country = request.POST.get('country')
        reg_number = request.POST.get('reg_number')
        start_date = request.POST.get('start_date')
        contact_name = request.POST.get('contact_name')
        position = request.POST.get('position')
        contact = request.POST.get('contact')
        contact_email = request.POST.get('contact_email')
        tin = request.POST.get('tin')
        credit_limit = request.POST.get('credit_limit')
        payment_terms = request.POST.get('payment_terms')
        currency = request.POST.get('currency')
        industry = request.POST.get('industry')
        status = request.POST.get('status')
        notes = request.POST.get('notes')
        # saving the client
        client = Newclient(logo=logo,company=company,phone=phone,company_email=company_email,address=address,country=country,reg_number=reg_number,start_date=start_date,contact_name=contact_name,position=position,contact=contact,contact_email=contact_email,tin=tin,credit_limit=credit_limit,payment_terms=payment_terms,currency=currency,industry=industry,status=status,notes=notes)
        client.save()

    return render(request, 'Clients_form.html', {})
# editing the client
def edit_client(request, pk):
    client = get_object_or_404(Newclient, pk=pk)

    if request.method == 'POST':
        client.company = request.POST.get('company', client.company)
        client.phone = request.POST.get('phone', client.phone)
        client.company_email = request.POST.get('company_email', client.company_email)
        client.address = request.POST.get('address', client.address)
        client.country = request.POST.get('country', client.country)
        client.reg_number = request.POST.get('reg_number', client.reg_number)
        client.start_date = request.POST.get('start_date', client.start_date)
        client.contact_name = request.POST.get('contact_name', client.contact_name)
        client.position = request.POST.get('position', client.position)
        client.contact = request.POST.get('contact', client.contact)
        client.contact_email = request.POST.get('contact_email', client.contact_email)
        client.tin = request.POST.get('tin', client.tin)
        client.credit_limit = request.POST.get('credit_limit', client.credit_limit)
        client.payment_terms = request.POST.get('payment_terms', client.payment_terms)
        client.currency = request.POST.get('currency', client.currency)
        client.industry = request.POST.get('industry', client.industry)
        client.status = request.POST.get('status', client.status)
        client.notes = request.POST.get('notes', client.notes)

        # ✅ Only update logo if a new one is uploaded
        if 'logo' in request.FILES:
            client.logo = request.FILES['logo']

        client.save()
        return redirect('clients')  # Or wherever your list view is

    return render(request, 'clients_form.html', {'client': client})
# client delete view
def delete_client(request, pk):
    client = get_object_or_404(Newclient, pk=pk)
    client.delete()
    return redirect('clients')

# employee view
def employee(request):
    employees = Newemployee.objects.all()

    return render(request, 'Employees.html', {'employees': employees})
# add employee form 
def add_employees(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        nin_number = request.POST.get('nin_number')
        tin_number = request.POST.get('tin_number')
        profile_picture = request.FILES.get('profile_picture')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        residential_address = request.POST.get('residential_address')
        emergency_person = request.POST.get('emergency_person')
        emergency_contact = request.POST.get('emergency_contact')
        relationship = request.POST.get('relationship')
        job_title = request.POST.get('job_title')
        department = request.POST.get('department')
        employment_type = request.POST.get('employment_type')
        status = request.POST.get('status')
        hire_date = request.POST.get('hire_date')
        supervisor = request.POST.get('supervisor')
        salary = request.POST.get('salary')
        payment_frequency = request.POST.get('payment_frequency')
        payment_method = request.POST.get('payment_method')
        bank_name = request.POST.get('bank_name')
        bank_account = request.POST.get('bank_account')
        bank_branch = request.POST.get('bank_branch')
        nssf_number = request.POST.get('nssf_number')
        insurance_provider = request.POST.get('insurance_provider')
        taxable_allowances = request.POST.get('taxable_allowances')
        intaxable_allowances = request.POST.get('intaxable_allowances')
        additional_notes = request.POST.get('additional_notes')
        doc_attachments = request.FILES.get('doc_attachments')
        # saving the new employee
        employee = Newemployee(first_name=first_name,last_name=last_name,gender=gender,dob=dob,nationality=nationality,nin_number=nin_number,tin_number=tin_number,profile_picture=profile_picture,phone_number=phone_number,email_address=email_address,residential_address=residential_address,emergency_person=emergency_person,emergency_contact=emergency_contact,relationship=relationship,job_title=job_title,department=department,employment_type=employment_type,status=status,hire_date=hire_date,supervisor=supervisor,salary=salary,payment_frequency=payment_frequency,payment_method=payment_method,bank_name=bank_name,bank_account=bank_account,bank_branch=bank_branch,nssf_number=nssf_number,insurance_provider=insurance_provider,taxable_allowances=taxable_allowances,intaxable_allowances=intaxable_allowances,additional_notes=additional_notes,doc_attachments=doc_attachments,)

        employee.save()
    
    return render(request, 'employees_form.html', {})

# editing the employee
def edit_employee(request, pk):
    employee = get_object_or_404(Newemployee, pk=pk)

    if request.method == 'POST':
        employee.first_name = request.POST.get('first_name', employee.first_name)
        employee.last_name = request.POST.get('last_name', employee.last_name)
        employee.gender = request.POST.get('gender', employee.gender)
        employee.dob = request.POST.get('dob', employee.dob)
        employee.nationality = request.POST.get('nationality', employee.nationality)
        employee.nin_number = request.POST.get('nin_number', employee.nin_number)
        employee.tin_number = request.POST.get('tin_number', employee.tin_number)
        employee.phone_number = request.POST.get('phone_number', employee.phone_number)
        employee.email_address = request.POST.get('email_address', employee.email_address)
        employee.residential_address = request.POST.get('residential_address', employee.residential_address)
        employee.emergency_person = request.POST.get('emergency_person', employee.emergency_person)
        employee.emergency_contact = request.POST.get('emergency_contact', employee.emergency_contact)
        employee.relationship = request.POST.get('relationship', employee.relationship)
        employee.job_title = request.POST.get('job_title', employee.job_title)
        employee.department = request.POST.get('department', employee.department)
        employee.employment_type = request.POST.get('employment_type', employee.employment_type)
        employee.status = request.POST.get('status', employee.status)
        employee.hire_date = request.POST.get('hire_date', employee.hire_date)
        employee.department = request.POST.get('department', employee.department)
        employee.supervisor = request.POST.get('supervisor', employee.supervisor)
        employee.salary = request.POST.get('salary', employee.salary)
        employee.payment_frequency = request.POST.get('payment_frequency', employee.payment_frequency)
        employee.payment_method = request.POST.get('payment_method', employee.payment_method)
        employee.bank_name = request.POST.get('bank_name', employee.bank_name)
        employee.bank_account = request.POST.get('bank_account', employee.bank_account)
        employee.bank_branch = request.POST.get('bank_branch', employee.bank_branch)
        employee.nssf_number = request.POST.get('nssf_number', employee.nssf_number)
        employee.insurance_provider = request.POST.get('insurance_provider', employee.insurance_provider)
        employee.taxable_allowances = request.POST.get('taxable_allowances', employee.taxable_allowances)
        employee.intaxable_allowances = request.POST.get('intaxable_allowances', employee.intaxable_allowances)
        employee.additional_notes = request.POST.get('additional_notes', employee.additional_notes)

        # ✅ Only update logo if a new one is uploaded
        if 'profile_picture' in request.FILES:
           employee.profile_picture = request.FILES['profile_picture']

        if 'doc_attachments' in request.FILES:
           employee.doc_attachments = request.FILES['doc_attachments']

        employee.save()
        return redirect('employees')  # Or wherever your list view is

    return render(request, 'employees_form.html', {'employee': employee})

# employee delete view
def delete_employee(request, pk):
    employee  = get_object_or_404(Newemployee, pk=pk)
    employee.delete()
    return redirect('employees')

# expenses view
def expenses(request):

    return render(request, 'Expenses.html', {})

# millecious view
def miscellaneous(request):

    return render(request, 'Miscellaneous.html', {})
# reports view 
def reports(request):

    return render(request, 'Reports.html', {})
# sales view
def sales(request):
    invoices = Newinvoice.objects.all().prefetch_related('invoiceitem_set')  # Optimized for related items
    return render(request, 'Sales.html', {'invoices': invoices})

# invoice form view

def add_invoice(request):
    customers = Newcustomer.objects.all()

    if request.method == 'POST':
        try:
            # Parse and validate dates
            invoice_date = datetime.strptime(request.POST.get('invoice_date', ''), '%d/%m/%Y') if request.POST.get('invoice_date') else None
            invoice_due = datetime.strptime(request.POST.get('invoice_due', ''), '%d/%m/%Y') if request.POST.get('invoice_due') else None

            # Get customer by ID (recommended approach)
            customer_id = request.POST.get('customer')
            customer = Newcustomer.objects.get(id=customer_id)

            # Create invoice object first
            invoice = Newinvoice.objects.create(
                invoice_date=invoice_date,
                invoice_due=invoice_due,
                customer=customer,
                email=request.POST.get('email'),
                billing_address=request.POST.get('billing_address'),
                shipping_address=request.POST.get('shipping_address'),
                terms=request.POST.get('terms'),
                sales_rep=request.POST.get('sales_rep'),
                location=request.POST.get('location'),
                tags=request.POST.get('tags'),
                po_number=request.POST.get('po_number') or None,
                item_details=request.POST.get('item_details'),
                memo=request.POST.get('memo'),
                customs_notes=request.POST.get('customs_notes'),
                attachments=request.FILES.get('attachments'),
                sub_total=request.POST.get('sub_total') or None,
                discount=request.POST.get('discount') or None,
                shipping=request.POST.get('shipping'),
                total_due=request.POST.get('total_due') or None,
            )
            invoice.save()

            # Saving the item rows — must be outside the .create() block
            products = request.POST.getlist('product[]')
            descriptions = request.POST.getlist('description[]')
            qtys = request.POST.getlist('qty[]')
            rates = request.POST.getlist('rate[]')
            amounts = request.POST.getlist('amount[]')
            billables = request.POST.getlist('billable[]')
            taxes = request.POST.getlist('tax[]')

            for i in range(len(products)):

                item =InvoiceItem.objects.create(
                    invoice=invoice,
                    product=products[i],
                    description=descriptions[i],
                    qty=int(qtys[i]) if qtys[i] else 0,
                    rate=float(rates[i]) if rates[i] else 0,
                    amount=float(amounts[i]) if amounts[i] else 0,
                    billable=(str(i) in billables),  # Adjust logic as needed
                    tax=(str(i) in taxes)  # Adjust logic as needed
                )
                item.save()

            return redirect('sales')

        except Newcustomer.DoesNotExist:
            error = "The selected customer does not exist."
            return render(request, 'invoice_form.html', {'customers': customers, 'error': error})

        except Exception as e:
            return render(request, 'invoice_form.html', {'customers': customers, 'error': str(e)})

    return render(request, 'invoice_form.html', {'customers': customers})

# receipt form view

def add_receipt(request):
    
    return render(request, 'Receipt_form.html', {})
# receive payment form view

def add_payment(request):
    
    return render(request, 'receive_payment_form.html', {})
#add new product form view

def add_products(request):
    
    return render(request, 'Products_and_services_form.html', {})

# supplier view
def supplier(request):
    suppliers = Newsupplier.objects.all()
     
    return render(request, 'Supplier.html', {'suppliers':suppliers})

#add new supplier form view
def add_suppliers(request):
    if request.method == 'POST':
        logo =request.FILES.get('logo')
        company_name = request.POST.get('company_name')
        supplier_type = request.POST.get('supplier_type')
        status = request.POST.get('status')
        contact_person = request.POST.get('contact_person')
        contact_position = request.POST.get('contact_position')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        open_balance = request.POST.get('open_balance')
        website = request.POST.get('website')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        bank = request.POST.get('bank')
        bank_account = request.POST.get('bank_account')
        bank_branch = request.POST.get('bank_branch')
        payment_terms = request.POST.get('payment_terms')
        currency = request.POST.get('currency')
        payment_method = request.POST.get('payment_method')
        tin = request.POST.get('tin')
        reg_number = request.POST.get('reg_number')
        tax_rate = request.POST.get('tax_rate')
        attachments =request.FILES.get('attachments')
        new_supplier = Newsupplier(logo=logo,company_name=company_name,supplier_type=supplier_type,status=status,contact_person=contact_person,contact_position=contact_position, contact=contact,email=email,open_balance=open_balance,website=website,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,country=country,bank=bank,bank_account=bank_account,bank_branch=bank_branch,payment_terms=payment_terms,currency=currency,payment_method=payment_method,tin=tin,reg_number=reg_number,tax_rate=tax_rate,attachments=attachments)
        new_supplier.save()
         # adding save actions
        save_action = request.POST.get('save_action')
        if save_action == 'save&new':
            return redirect('add-suppliers')
        elif save_action == 'save&close':
            return redirect('suppliers')
    return render(request, 'suppliers_entry_form.html', {})
# editing supplier information
def edit_supplier(request, pk):
    supplier = get_object_or_404(Newsupplier, pk=pk)
    if request.method == 'POST':
        supplier.company_name = request.POST.get('company_name',supplier.company_name)
        supplier.supplier_type = request.POST.get('supplier_type',supplier.supplier_type)
        supplier.status = request.POST.get('status',supplier.status)
        supplier.contact_person = request.POST.get('contact_person',supplier.contact_person)
        supplier.contact_position = request.POST.get('contact_position',supplier.contact_position)
        supplier.contact = request.POST.get('contact',supplier.contact)
        supplier.email = request.POST.get('email',supplier.email)
        supplier.open_balance = request.POST.get('open_balance',supplier.open_balance)
        supplier.website = request.POST.get('website',supplier.website)
        supplier.address1 = request.POST.get('address1',supplier.address1)
        supplier.address2 = request.POST.get('address2',supplier.address2)
        supplier.city = request.POST.get('city',supplier.city)
        supplier.state = request.POST.get('state',supplier.state)
        supplier.zip_code = request.POST.get('zip_code',supplier.zip_code)
        supplier.country = request.POST.get('country',supplier.country)
        supplier.bank = request.POST.get('bank',supplier.bank)
        supplier.bank_account = request.POST.get('bank_account',supplier.bank_account)
        supplier.bank_branch = request.POST.get('bank_branch',supplier.bank_branch)
        supplier.payment_terms = request.POST.get('payment_terms',supplier.payment_terms)
        supplier.currency = request.POST.get('currency',supplier.currency)
        supplier.payment_method = request.POST.get('payment_method',supplier.payment_method)
        supplier.tin = request.POST.get('tin',supplier.tin)
        supplier.reg_number = request.POST.get('reg_number',supplier.reg_number)
        supplier.tax_rate = request.POST.get('tax_rate',supplier.tax_rate )
        if request.FILES.get('logo'):
            supplier.logo = request.FILES.get('logo')
        if request.FILES.get('attachments'):
            supplier.attachments = request.FILES.get('attachments')

        supplier.save()
        return redirect('suppliers')

    return render(request, 'suppliers_entry_form.html', {'supplier': supplier})

    # Delete view
def delete_supplier(request, pk):
    supplier = get_object_or_404(Newsupplier, pk=pk)
    supplier.delete()
    return redirect('suppliers')    
# tasks view
def tasks(request):

    return render(request, 'tasks.html', {})
# taxes view
def taxes(request):

    return render(request, 'Taxes.html', {})
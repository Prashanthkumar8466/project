from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
class contact_u(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class role(models.Model):
    role_name=models.TextField()
    SetMaster =models.BooleanField(default=False)
    company_creation=models.BooleanField(default=False)
    set_up=models.BooleanField(default=False)
    project_type_creation=models.BooleanField(default=False)
    area_type_creation=models.BooleanField(default=False)
    profession=models.BooleanField(default=False)
    currency_Configuration=models.BooleanField(default=False)
    Bank_master=models.BooleanField(default=False)
    country_master=models.BooleanField(default=False)
    company_bank_creation=models.BooleanField(default=False)
    customer_bank_creation=models.BooleanField(default=False)
    loan_bank_creation=models.BooleanField(default=False)
    mortgage_bank_creation=models.BooleanField(default=False)
    employee_login_creation=models.BooleanField(default=False)
    employee=models.BooleanField(default=False)
    department=models.BooleanField(default=False)
    employee_Information=models.BooleanField(default=False)
    employee_Report=models.BooleanField(default=False)
    Set_Manager=models.BooleanField(default=False)
    Team_Manager=models.BooleanField(default=False)
    Set_Team_Head=models.BooleanField(default=False)
    Team_Head_Detail=models.BooleanField(default=False)
    Employee_Tree=models.BooleanField(default=False)
    create_login=models.BooleanField(default=False)
    view_login=models.BooleanField(default=False)
    broker_login_creation=models.BooleanField(default=False)
    documents=models.BooleanField(default=False)
    document_type_creation=models.BooleanField(default=False)
    document_dispatch_master=models.BooleanField(default=False)
    customized_letter=models.BooleanField(default=False)
    create_letter=models.BooleanField(default=False)
    security=models.BooleanField(default=False)
    password=models.BooleanField(default=False)
    login_history=models.BooleanField(default=False)
    ip_based_security=models.BooleanField(default=False)
    enable_ip=models.BooleanField(default=False)
    add_ip=models.BooleanField(default=False)
    role_and_menu=models.BooleanField(default=False)
    role_creation=models.BooleanField(default=False)
    role_wise_menu=models.BooleanField(default=False)
    administration=models.BooleanField(default=False)
    receipt_locking=models.BooleanField(default=False)
    customer_audit_track=models.BooleanField(default=False)
    customer_history=models.BooleanField(default=False)
    set_projects=models.BooleanField(default=False)
    create_project=models.BooleanField(default=False)
    add_tower=models.BooleanField(default=False)
    add_base_floor=models.BooleanField(default=False)
    floor_creation=models.BooleanField(default=False)
    unit_type_creation=models.BooleanField(default=False)
    floor_wise_unit_allocation=models.BooleanField(default=False)
    pre_attach_charges=models.BooleanField(default=False)
    address_owner=models.BooleanField(default=False)
    unit_location_creation=models.BooleanField(default=False)
    address_owner_master=models.BooleanField(default=False)
    address_owner_unit_wise=models.BooleanField(default=False)
    edit_project=models.BooleanField(default=False)
    edit_project_edit=models.BooleanField(default=False)
    edit_block=models.BooleanField(default=False)
    edit_floor=models.BooleanField(default=False)
    add_plot=models.BooleanField(default=False)
    add_plot_edit=models.BooleanField(default=False)
    allocate_plot=models.BooleanField(default=False)
    change_unit_type=models.BooleanField(default=False)
    change_floor_wise_unit_allocation=models.BooleanField(default=False)
    change_no_plot=models.BooleanField(default=False)
    edit_unit_address=models.BooleanField(default=False)
    address_indexing=models.BooleanField(default=False)
    detach_unit_address=models.BooleanField(default=False)
    change_unit_area=models.BooleanField(default=False)
    unit_wise_area=models.BooleanField(default=False)
    unit_wise_area_report=models.BooleanField(default=False)
    payment_plan_setup=models.BooleanField(default=False)
    new_payment_plan=models.BooleanField(default=False)
    stage_master=models.BooleanField(default=False)
    payment_plan_creation=models.BooleanField(default=False)
    set_booking_amount=models.BooleanField(default=False)
    create_installement=models.BooleanField(default=False)
    customer_wise_timely_discount=models.BooleanField(default=False)
    cancel_demand=models.BooleanField(default=False)
    edit_payment_plan=models.BooleanField(default=False)
    installment=models.BooleanField(default=False)
    plc_charges=models.BooleanField(default=False)
    other_charges=models.BooleanField(default=False)
    edit_personal_installment=models.BooleanField(default=False)
    personalise_installment=models.BooleanField(default=False)
    view_payment_plan=models.BooleanField(default=False)
    raised_demand_stage=models.BooleanField(default=False)
    view_payment_plan_view=models.BooleanField(default=False)
    payment_setup=models.BooleanField(default=False)
    reminder_days_config=models.BooleanField(default=False)
    demand_format_customiz=models.BooleanField(default=False)
    set_rate=models.BooleanField(default=False)
    change_rate=models.BooleanField(default=False)
    change_charge_rate=models.BooleanField(default=False)
    unit_wise_rate=models.BooleanField(default=False)
    rate_report=models.BooleanField(default=False)
    project_setup=models.BooleanField(default=False)
    charge_master=models.BooleanField(default=False)
    setup_other_charges=models.BooleanField(default=False)
    prefered_location_charges=models.BooleanField(default=False)
    intrest_free_maintainance=models.BooleanField(default=False)
    addon_charges=models.BooleanField(default=False)
    stage_wise_due=models.BooleanField(default=False)
    tower_wise_due=models.BooleanField(default=False)
    plan_stage_wise_due=models.BooleanField(default=False)
    customerwise_stagewise_due=models.BooleanField(default=False)
    wavie_off_other_charges=models.BooleanField(default=False)
    service_tax_master=models.BooleanField(default=False)
    tax_master=models.BooleanField(default=False)
    tax_information=models.BooleanField(default=False)
    tax_configuration_report=models.BooleanField(default=False)
    gst=models.BooleanField(default=False)
    gst_process_user=models.BooleanField(default=False)
    gst_configeration=models.BooleanField(default=False)
    itc_configeration=models.BooleanField(default=False)
    set_invoice_prefix=models.BooleanField(default=False)
    gst_number_configeration=models.BooleanField(default=False)
    customer_wise_gst=models.BooleanField(default=False)
    help=models.BooleanField(default=False)
    completion_certificate=models.BooleanField(default=False)
    tower_wise_completion=models.BooleanField(default=False)
    unit_wise_completion=models.BooleanField(default=False)
    automated_manual=models.BooleanField(default=False)
    booking_authentication=models.BooleanField(default=False)
    receipt_no=models.BooleanField(default=False)
    registration_no=models.BooleanField(default=False)
    transfer_authentication=models.BooleanField(default=False)
    customer_classfication=models.BooleanField(default=False)
    project_configuration_details=models.BooleanField(default=False)
    broker=models.BooleanField(default=False)
    Broker_broker=models.BooleanField(default=False)
    broker_aplication=models.BooleanField(default=False)
    broker_view=models.BooleanField(default=False)
    broker_project_mapping=models.BooleanField(default=False)
    sub_broker_mapping=models.BooleanField(default=False)
    broker_address=models.BooleanField(default=False)
    broker_report=models.BooleanField(default=False)
    broker_summary=models.BooleanField(default=False)
    broker_summary_sold=models.BooleanField(default=False)
    broker_brokerreport=models.BooleanField(default=False)
    broker_wise_booking=models.BooleanField(default=False)
    broker_hierarchy=models.BooleanField(default=False)
    broker_investor=models.BooleanField(default=False)
    broker_hold_unit=models.BooleanField(default=False)
    broker_unhold_unit=models.BooleanField(default=False)
    broker_wise_hold=models.BooleanField(default=False)
    unhold_unit_details=models.BooleanField(default=False)
    application=models.BooleanField(default=False)
    booking=models.BooleanField(default=False)
    booking_form=models.BooleanField(default=False)
    edit_booking_form=models.BooleanField(default=False)
    approval_status=models.BooleanField(default=False)
    booking_status=models.BooleanField(default=False)
    editing_status=models.BooleanField(default=False)
    unit_shift_process=models.BooleanField(default=False)
    shift_units=models.BooleanField(default=False)
    shift_units_report=models.BooleanField(default=False)
    application_add_dele_process=models.BooleanField(default=False)
    head_wise_cost=models.BooleanField(default=False)
    edit_customer_address=models.BooleanField(default=False)
    customer_registration=models.BooleanField(default=False)
    edit_customer_address=models.BooleanField(default=False)
    customer_registration=models.BooleanField(default=False)
    allotment_of_unit=models.BooleanField(default=False)
    transaction=models.BooleanField(default=False)
    allotment_form=models.BooleanField(default=False)
    allotment_letter=models.BooleanField(default=False)
    allotment_cancellation=models.BooleanField(default=False)
    allotment_information=models.BooleanField(default=False)
    maintenance_agreement=models.BooleanField(default=False)
    rera_agreement=models.BooleanField(default=False)
    allotment_agreement_status=models.BooleanField(default=False)
    allotment_cancel_report=models.BooleanField(default=False)
    receipt_process=models.BooleanField(default=False)
    receipt_generation=models.BooleanField(default=False)
    receipt_print=models.BooleanField(default=False)
    journal_entry=models.BooleanField(default=False)
    debit_credit_refund=models.BooleanField(default=False)
    journal_report=models.BooleanField(default=False)
    jv_dr_cr_refund_reversal=models.BooleanField(default=False)
    edit_receipt=models.BooleanField(default=False)
    edit_head_wise_receipt=models.BooleanField(default=False)
    reset_receipt=models.BooleanField(default=False)
    cancel_receipt=models.BooleanField(default=False)
    assign_re_challan=models.BooleanField(default=False)
    cancel_receipt_report=models.BooleanField(default=False)
    report=models.BooleanField(default=False)
    receipt_register=models.BooleanField(default=False)
    payment_clear_delay=models.BooleanField(default=False)
    cumulative_receipt_booking=models.BooleanField(default=False)
    tds_challan_report=models.BooleanField(default=False)
    demand_raise=models.BooleanField(default=False)
    stage_wise=models.BooleanField(default=False)
    tower_wise=models.BooleanField(default=False)
    customer_wise=models.BooleanField(default=False)
    installment_wise=models.BooleanField(default=False)
    unit_stage_wise=models.BooleanField(default=False)
    demand_unraise=models.BooleanField(default=False)
    construction_update_for_demand=models.BooleanField(default=False)
    demand_help=models.BooleanField(default=False)
    gst_invoicing=models.BooleanField(default=False)
    gst_setup=models.BooleanField(default=False)
    set_customer_opening=models.BooleanField(default=False)
    assigned_itc_for_customer=models.BooleanField(default=False)
    gst_transaction=models.BooleanField(default=False)
    invoice_generation=models.BooleanField(default=False)
    manual_invoice_generation=models.BooleanField(default=False)
    inoice_reversal=models.BooleanField(default=False)
    invoice_against_advance=models.BooleanField(default=False)
    debit_credit_against_invoice=models.BooleanField(default=False)
    pending_invoice=models.BooleanField(default=False)
    gst_report=models.BooleanField(default=False)
    invoice_details=models.BooleanField(default=False)
    opening_balance=models.BooleanField(default=False)
    invoice_receipts=models.BooleanField(default=False)
    month_wise_invoice_details=models.BooleanField(default=False)
    hsn_charge_wise_report=models.BooleanField(default=False)
    gst_help=models.BooleanField(default=False)
    printing_of_documents=models.BooleanField(default=False)
    printing_welcome=models.BooleanField(default=False)
    demand_printing=models.BooleanField(default=False)
    print_demand=models.BooleanField(default=False)
    installment_wise_demand_status=models.BooleanField(default=False)
    print_demand_manual=models.BooleanField(default=False)
    email_notification=models.BooleanField(default=False)
    agreement=models.BooleanField(default=False)
    tpa=models.BooleanField(default=False)
    user_define_letter=models.BooleanField(default=False)
    aplicant_ledger=models.BooleanField(default=False)
    address_label=models.BooleanField(default=False)
    banking=models.BooleanField(default=False)
    cheque_deposit=models.BooleanField(default=False)
    verify_cheque_status=models.BooleanField(default=False)
    change_cheque_status=models.BooleanField(default=False)
    cheque_status_report=models.BooleanField(default=False)
    cheque_represent=models.BooleanField(default=False)
    change_clearing_date=models.BooleanField(default=False)
    intrest_calculator=models.BooleanField(default=False)
    intrest_schedular=models.BooleanField(default=False)
    project_wise=models.BooleanField(default=False)
    interest_master=models.BooleanField(default=False)
    installment_wise_interest=models.BooleanField(default=False)
    customer_wise_interest=models.BooleanField(default=False)
    delete_interest=models.BooleanField(default=False)
    customer_installment_wise_interest=models.BooleanField(default=False)
    manual_interest=models.BooleanField(default=False)
    interest_waiver=models.BooleanField(default=False)
    interest_wavie_off_letter=models.BooleanField(default=False)
    customer_waiver_report=models.BooleanField(default=False)
    interest_waive_off=models.BooleanField(default=False)
    grace_period=models.BooleanField(default=False)
    project_wise_grace_period=models.BooleanField(default=False)
    installment_wise_grace_period=models.BooleanField(default=False)
    addon_charge=models.BooleanField(default=False)
    documents_pending=models.BooleanField(default=False)
    pending_documents=models.BooleanField(default=False)
    uploaded_documents=models.BooleanField(default=False)
    dispatch=models.BooleanField(default=False)
    document_dispatch_register=models.BooleanField(default=False)
    dispatch_report=models.BooleanField(default=False)
    customer_document_dispatch=models.BooleanField(default=False)
    printed_document=models.BooleanField(default=False)
    pending_kyc_booking=models.BooleanField(default=False)
    loan_process=models.BooleanField(default=False)
    finance_details=models.BooleanField(default=False)
    loan_dispersal_report=models.BooleanField(default=False)
    mortgage=models.BooleanField(default=False)
    transfer=models.BooleanField(default=False)
    setup_transerfer=models.BooleanField(default=False)
    transfer_fee=models.BooleanField(default=False)
    service_tax_master=models.BooleanField(default=False)
    application_transfer=models.BooleanField(default=False)
    transfer_report=models.BooleanField(default=False)
    surrender=models.BooleanField(default=False)
    surrender_application=models.BooleanField(default=False)
    surrender_report=models.BooleanField(default=False)
    surrender_restore=models.BooleanField(default=False)
    surrender_summary=models.BooleanField(default=False)
    reports=models.BooleanField(default=False)
    email_setup=models.BooleanField(default=False)
    def __str__(self):
        return self.role_name
class employee_info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.DecimalField(max_digits=12,decimal_places=0)
    user_role=models.ForeignKey(role,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
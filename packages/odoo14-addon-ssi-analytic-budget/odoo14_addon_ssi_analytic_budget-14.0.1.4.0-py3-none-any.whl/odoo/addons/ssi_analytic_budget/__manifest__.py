# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

{
    "name": "Analytic Budget",
    "version": "14.0.1.4.0",
    "category": "Accounting",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_financial_accounting",
        "ssi_cost_accounting",
        "ssi_master_data_mixin",
        "ssi_product_line_price_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_terminate_mixin",
        "ssi_company_currency_mixin",
        "account_fiscal_month",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/approval_template_data.xml",
        "data/policy_template_data.xml",
        "menu.xml",
        "views/analytic_budget_type_views.xml",
        "views/analytic_budget_budget_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": [
        "demo/analytic_budget_type_demo.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}

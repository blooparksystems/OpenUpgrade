UPDATE ir_model_data as d SET module = 'lr_mail' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_bcc' AND f.model = 'mail.mail';
UPDATE ir_model_data as d SET module = 'lr_mail' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_cc_ids' AND f.model = 'mail.message';
UPDATE ir_model_data as d SET module = 'lr_mail' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_bcc_ids' AND f.model = 'mail.message';
UPDATE ir_model_data as d SET module = 'lr_mail' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_cc_ids' AND f.model = 'mail.compose.message';
UPDATE ir_model_data as d SET module = 'lr_mail' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_bcc_ids' AND f.model = 'mail.compose.message';
UPDATE ir_model_data as d SET module = 'lr_email_template' FROM ir_model_fields f WHERE d.res_id = f.id AND d.model = 'ir.model.fields' AND f.name = 'email_bcc' AND f.model = 'email.template';

UPDATE ir_model_data SET module = 'lr_email_template' WHERE model = 'ir.ui.view' AND name = 'email_template_form_inherit';
UPDATE ir_model_data SET module = 'lr_mail' WHERE model = 'ir.ui.view' AND name = 'view_message_form_inherit';
UPDATE ir_model_data SET module = 'lr_mail' WHERE model = 'ir.ui.view' AND name = 'email_compose_message_wizard_form_inherit';

UPDATE ir_model_data SET module = 'lr_mail' WHERE model = 'ir.model' AND module = 'email_cc_bcc' AND name LIKE 'model_mail_%';
UPDATE ir_model_data SET module = 'lr_email_template' WHERE model = 'ir.model' AND module = 'email_cc_bcc' AND name = 'model_email_template';
UPDATE ir_model_data SET module = 'lr_base' WHERE model = 'ir.model' AND module = 'email_cc_bcc' AND name = 'model_ir_mail_server';
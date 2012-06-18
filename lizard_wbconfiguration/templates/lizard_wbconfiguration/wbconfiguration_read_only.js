{% load history_extras %}
{% load get_grid %}
{% load get_portal_template %}
{
    xtype: 'wb_grid_history',
    config: {
        log_entry_id: {{ view.log_entry_id }}

    },
    log_entry_id: {{ view.log_entry_id }}
}

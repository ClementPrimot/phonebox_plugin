from extras.plugins import PluginMenuItem, PluginMenuButton

menu_items = (
    PluginMenuItem(
        link='plugins:phonebox_plugin:list_view',
        link_text='Numbers',
        buttons=(
            PluginMenuButton(
                link="plugins:phonebox_plugin:add_number",
                title="Add Number",
                icon_class="mdi mdi-plus-thick",
                color="green",
            ),
            PluginMenuButton(
                link="plugins:phonebox_plugin:import_numbers",
                title="Import Number",
                icon_class="mdi mdi-upload",
                color="teal",
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:phonebox_plugin:voice_circuit_list_view',
        link_text='Voice Circuits',
        buttons=()
    ),
)

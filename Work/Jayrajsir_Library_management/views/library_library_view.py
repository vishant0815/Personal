<odoo>
    <record id="view_library_library_list" model="ir.ui.view">
        <field name="name">library.library.list</field>
        <field name="model">library.library</field>
        <field name="arch" type="xml">
            <tree>
                <field name="name"/>
                <field name="location"/>
                <field name="capacity"/>
            </tree>
        </field>
    </record>

    <record id="view_library_library_form" model="ir.ui.view">
        <field name="name">library.library.form</field>
        <field name="model">library.library</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <group>
                        <field name="name"/>
                        <field name="location"/>
                        <field name="capacity"/>
                        <field name="notes"/>
                    </group>
                    <notebook>
                        <page string="Books">
                            <field name="book_ids">
                                <tree editable="bottom">
                                    <field name="name"/>
                                    <field name="author"/>
                                    <field name="isbn"/>
                                    <field name="category_id"/>
                                </tree>
                            </field>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_library_library" model="ir.actions.act_window">
        <field name="name">Libraries</field>
        <field name="res_model">library.library</field>
        <field name="view_mode">tree,form</field>
    </record>
</odoo>

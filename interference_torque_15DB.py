# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='Interference fitting', kernelModule='interference_torque', kernelFunction='createInterferentionwithTorque', includeApplyBtn=False, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgTabBook(name='TabBook_1', p='DialogBox', layout='0')
RsgTabItem(name='TabItem_1', p='TabBook_1', text='Geometry')
RsgSeparator(p='TabItem_1')
RsgTabBook(name='TabBook_4', p='TabItem_1', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y')
RsgTabItem(name='TabItem_8', p='TabBook_4', text='Shaft')
RsgHorizontalFrame(name='HFrame_1', p='TabItem_8', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_1', fieldType='Float', ncols=6, labelText='Outside', keyword='dso', default='')
RsgLabel(p='HFrame_1', text='mm', useBoldFont=False)
RsgComboBox(name='ComboBox_2', p='HFrame_1', text='Tolerance', keyword='toleranceOUT', default='', comboType='STANDARD', repository='', rootText='', rootKeyword='None', layout='')
RsgListItem(p='ComboBox_2', text='none')
RsgListItem(p='ComboBox_2', text='p6')
RsgListItem(p='ComboBox_2', text='p7')
RsgListItem(p='ComboBox_2', text='p8')
RsgListItem(p='ComboBox_2', text='r6')
RsgListItem(p='ComboBox_2', text='r7')
RsgListItem(p='ComboBox_2', text='r8')
RsgListItem(p='ComboBox_2', text='s6')
RsgListItem(p='ComboBox_2', text='s7')
RsgListItem(p='ComboBox_2', text='s8')
RsgListItem(p='ComboBox_2', text='t6')
RsgListItem(p='ComboBox_2', text='t7')
RsgListItem(p='ComboBox_2', text='t8')
RsgListItem(p='ComboBox_2', text='u6')
RsgListItem(p='ComboBox_2', text='u7')
RsgListItem(p='ComboBox_2', text='u8')
RsgListItem(p='ComboBox_2', text='x6')
RsgListItem(p='ComboBox_2', text='x7')
RsgListItem(p='ComboBox_2', text='x8')
RsgListItem(p='ComboBox_2', text='z6')
RsgListItem(p='ComboBox_2', text='z7')
RsgListItem(p='ComboBox_2', text='z8')
RsgTabItem(name='TabItem_9', p='TabBook_4', text='Wheel')
RsgHorizontalFrame(name='HFrame_2', p='TabItem_9', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_2', fieldType='Float', ncols=6, labelText='Inside   ', keyword='dwi', default='')
RsgLabel(p='HFrame_2', text='mm', useBoldFont=False)
RsgComboBox(name='ComboBox_3', p='HFrame_2', text='Tolerance', keyword='toleranceIN', default='', comboType='STANDARD', repository='', rootText='', rootKeyword='None', layout='')
RsgListItem(p='ComboBox_3', text='none')
RsgListItem(p='ComboBox_3', text='H6')
RsgListItem(p='ComboBox_3', text='H7')
RsgListItem(p='ComboBox_3', text='H8')
RsgSeparator(p='TabItem_9')
RsgHorizontalFrame(name='HFrame_3', p='TabItem_9', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_3', fieldType='Float', ncols=6, labelText='Outside', keyword='dwo', default='')
RsgLabel(p='HFrame_3', text='mm', useBoldFont=False)
RsgSeparator(p='TabItem_9')
RsgHorizontalFrame(name='HFrame_9', p='TabItem_9', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_9', fieldType='Float', ncols=6, labelText='Length ', keyword='l', default='')
RsgLabel(p='HFrame_9', text='mm', useBoldFont=False)
RsgTabItem(name='TabItem_10', p='TabBook_1', text='Material properties')
RsgTextField(p='TabItem_10', fieldType='Float', ncols=12, labelText='Friction ', keyword='fr', default='')
RsgComboBox(name='ComboBox_1', p='TabItem_10', text='Material', keyword='wybor', default='', comboType='STANDARD', repository='', rootText='', rootKeyword='None', layout='')
RsgListItem(p='ComboBox_1', text='Steel')
RsgListItem(p='ComboBox_1', text='Aluminium')
RsgListItem(p='ComboBox_1', text='Titanium')
RsgListItem(p='ComboBox_1', text='Copper')
RsgListItem(p='ComboBox_1', text='User define')
RsgSeparator(p='TabItem_10')
RsgHorizontalFrame(name='HFrame_5', p='TabItem_10', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_5', fieldType='Float', ncols=12, labelText='Young module', keyword='Younguser', default='0')
RsgLabel(p='HFrame_5', text='MPa', useBoldFont=False)
RsgTextField(p='TabItem_10', fieldType='Float', ncols=12, labelText='Poisson ratio    ', keyword='Poissonuser', default='0')
RsgCheckButton(p='TabItem_10', text='User define', keyword='check', default=False)
RsgTabItem(name='TabItem_12', p='TabBook_1', text='Loads')
RsgHorizontalFrame(name='HFrame_6', p='TabItem_12', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_6', fieldType='Float', ncols=12, labelText='Torque', keyword='tq', default='')
RsgLabel(p='HFrame_6', text='Nmm', useBoldFont=False)
RsgTabItem(name='TabItem_13', p='TabBook_1', text='Mesh')
RsgTabBook(name='TabBook_5', p='TabItem_13', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y')
RsgTabItem(name='TabItem_14', p='TabBook_5', text='Shaft')
RsgHorizontalFrame(name='HFrame_8', p='TabItem_14', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_4', p='HFrame_8', text='Define by size', layout='0')
RsgTextField(p='GroupBox_4', fieldType='Float', ncols=8, labelText='Global', keyword='s1', default='')
RsgTextField(p='GroupBox_4', fieldType='Float', ncols=8, labelText='Local  ', keyword='s11', default='')
RsgTextField(p='HFrame_8', fieldType='Float', ncols=8, labelText='Thickness', keyword='ts', default='')
RsgTabItem(name='TabItem_15', p='TabBook_5', text='Wheel')
RsgHorizontalFrame(name='HFrame_7', p='TabItem_15', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_5', p='HFrame_7', text='Define by size', layout='0')
RsgTextField(p='GroupBox_5', fieldType='Float', ncols=8, labelText='Global', keyword='s2', default='')
RsgTextField(p='GroupBox_5', fieldType='Float', ncols=8, labelText='Local  ', keyword='s22', default='')
RsgTextField(p='HFrame_7', fieldType='Float', ncols=8, labelText='Thickness', keyword='tw', default='')
dialogBox.show()
import intrepyd as ip
import intrepyd.scr
import intrepyd.circuit
import collections

class SimulinkCircuit(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_naked_circuit_impl(self, inputs):
        input_keys = list(inputs)
        # presentPositionEntered -> n1
        n1 = inputs[input_keys[0]]
        # ACAIRB -> n2
        n2 = inputs[input_keys[1]]
        # IMSAUTOC -> n3
        n3 = inputs[input_keys[2]]
        # Desig -> n4
        n4 = inputs[input_keys[3]]
        # Data23=Sea -> n5
        n5 = inputs[input_keys[4]]
        # CAstageComplete -> n6
        n6 = inputs[input_keys[5]]
        # CLstageComplete -> n7
        n7 = inputs[input_keys[6]]
        # NDstageComplete -> n8
        n8 = inputs[input_keys[7]]
        # HSstageComplete -> n9
        n9 = inputs[input_keys[8]]
        # PNLTEST=TEST -> n10
        n10 = inputs[input_keys[9]]
        # IMSup -> n11
        n11 = inputs[input_keys[10]]
        # latitude -> n12
        n12 = inputs[input_keys[11]]
        # DopplerUp -> n13
        n13 = inputs[input_keys[12]]
        # DopplerCoupled -> n14
        n14 = inputs[input_keys[13]]
        # IMSMODE -> n15
        n15 = inputs[input_keys[14]]
        # AirVelocityTestPassed -> n16
        n16 = inputs[input_keys[15]]
        # PitchSmall AND RollSmall -> n17
        n17 = inputs[input_keys[16]]
        # SINSup -> n18
        n18 = inputs[input_keys[17]]
        # SINSvelocityTestPassed -> n19
        n19 = inputs[input_keys[18]]
        # LandVelocityTestPassed -> n20
        n20 = inputs[input_keys[19]]
        # NonInterveningTakeoff -> n21
        n21 = inputs[input_keys[20]]
        # GroundTestFinished -> n22
        n22 = inputs[input_keys[21]]
        # UPDATTW -> n23
        n23 = inputs[input_keys[22]]
        # MODEROT -> n24
        n24 = inputs[input_keys[23]]
        # PRESPOS -> n25
        n25 = inputs[input_keys[24]]
        # GUNNSEL -> n26
        n26 = inputs[input_keys[25]]
        # MSFW -> n27
        n27 = inputs[input_keys[26]]
        # NonZeroDigitEntered -> n28
        n28 = inputs[input_keys[27]]
        # ENTERSW -> n29
        n29 = inputs[input_keys[28]]
        # FLYTOchanged -> n30
        n30 = inputs[input_keys[29]]
        # HUDREL -> n31
        n31 = inputs[input_keys[30]]
        # AnyDestEntered -> n32
        n32 = inputs[input_keys[31]]
        # HighDrag -> n33
        n33 = inputs[input_keys[32]]
        # LowDrag -> n34
        n34 = inputs[input_keys[33]]
        # OverflownExit -> n35
        n35 = inputs[input_keys[34]]
        # Overflown>42 -> n36
        n36 = inputs[input_keys[35]]
        # FLYTOTOG=Dest -> n37
        n37 = inputs[input_keys[36]]
        # FLYTOTW -> n38
        n38 = inputs[input_keys[37]]
        # WEAPTYPE -> n39
        n39 = inputs[input_keys[38]]
        # Station_Selected -> n40
        n40 = inputs[input_keys[39]]
        # TD -> n41
        n41 = inputs[input_keys[40]]
        # NU=AflyUpd -> n42
        n42 = inputs[input_keys[41]]
        # A7E_requirements/Constant
        n43 = self.context.mk_number('70.0', self.context.mk_real_type())
        self.nets['A7E_requirements/Constant'] = n43
        # A7E_requirements/Relational Operator -> n44
        n44 = self.context.mk_gt(n12, n43)
        self.nets['A7E_requirements/Relational Operator'] = n44
        # A7E_requirements/Constant1
        n45 = self.context.mk_number('80.0', self.context.mk_real_type())
        self.nets['A7E_requirements/Constant1'] = n45
        # A7E_requirements/Relational Operator1 -> n46
        n46 = self.context.mk_gt(n12, n45)
        self.nets['A7E_requirements/Relational Operator1'] = n46
        # A7E_requirements/Gndal
        n47 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/Gndal'] = n47
        # A7E_requirements/ro -> n48
        n48 = self.context.mk_eq(n15, n47)
        self.nets['A7E_requirements/ro'] = n48
        # A7E_requirements/Norm
        n49 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/Norm'] = n49
        # A7E_requirements/ro1 -> n50
        n50 = self.context.mk_eq(n15, n49)
        self.nets['A7E_requirements/ro1'] = n50
        # A7E_requirements/Iner
        n51 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/Iner'] = n51
        # A7E_requirements/ro2 -> n52
        n52 = self.context.mk_eq(n15, n51)
        self.nets['A7E_requirements/ro2'] = n52
        # A7E_requirements/MagSl
        n53 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/MagSl'] = n53
        # A7E_requirements/ro3 -> n54
        n54 = self.context.mk_eq(n15, n53)
        self.nets['A7E_requirements/ro3'] = n54
        # A7E_requirements/Grid
        n55 = self.context.mk_number('4', self.context.mk_int8_type())
        self.nets['A7E_requirements/Grid'] = n55
        # A7E_requirements/ro4 -> n56
        n56 = self.context.mk_eq(n15, n55)
        self.nets['A7E_requirements/ro4'] = n56
        n57_1 = self.ANT(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n44, n46, n13, n14, n48, n50, n52, n54, n56, n16, n17, n18, n19, n20, n21, n22)
        # A7E_requirements/FLYOVER
        n59 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/FLYOVER'] = n59
        # A7E_requirements/ro5 -> n60
        n60 = self.context.mk_eq(n23, n59)
        self.nets['A7E_requirements/ro5'] = n60
        # A7E_requirements/HUD
        n61 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/HUD'] = n61
        # A7E_requirements/ro6 -> n62
        n62 = self.context.mk_eq(n23, n61)
        self.nets['A7E_requirements/ro6'] = n62
        # A7E_requirements/RADAR
        n63 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/RADAR'] = n63
        # A7E_requirements/ro7 -> n64
        n64 = self.context.mk_eq(n23, n63)
        self.nets['A7E_requirements/ro7'] = n64
        # A7E_requirements/TACLL
        n65 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/TACLL'] = n65
        # A7E_requirements/ro8 -> n66
        n66 = self.context.mk_eq(n23, n65)
        self.nets['A7E_requirements/ro8'] = n66
        # A7E_requirements/Other
        n67 = self.context.mk_number('4', self.context.mk_int8_type())
        self.nets['A7E_requirements/Other'] = n67
        # A7E_requirements/ro9 -> n68
        n68 = self.context.mk_eq(n23, n67)
        self.nets['A7E_requirements/ro9'] = n68
        # A7E_requirements/BOC_
        n69 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/BOC_'] = n69
        # A7E_requirements/ro12 -> n70
        n70 = self.context.mk_eq(n27, n69)
        self.nets['A7E_requirements/ro12'] = n70
        # A7E_requirements/BOCOFF
        n71 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/BOCOFF'] = n71
        # A7E_requirements/ro13 -> n72
        n72 = self.context.mk_eq(n27, n71)
        self.nets['A7E_requirements/ro13'] = n72
        # A7E_requirements/CCIP
        n73 = self.context.mk_number('4', self.context.mk_int8_type())
        self.nets['A7E_requirements/CCIP'] = n73
        # A7E_requirements/ro14 -> n74
        n74 = self.context.mk_eq(n27, n73)
        self.nets['A7E_requirements/ro14'] = n74
        # A7E_requirements/NATT
        n75 = self.context.mk_number('5', self.context.mk_int8_type())
        self.nets['A7E_requirements/NATT'] = n75
        # A7E_requirements/ro15 -> n76
        n76 = self.context.mk_eq(n27, n75)
        self.nets['A7E_requirements/ro15'] = n76
        # A7E_requirements/NATOFF
        n77 = self.context.mk_number('6', self.context.mk_int8_type())
        self.nets['A7E_requirements/NATOFF'] = n77
        # A7E_requirements/ro16 -> n78
        n78 = self.context.mk_eq(n27, n77)
        self.nets['A7E_requirements/ro16'] = n78
        # A7E_requirements/WDMFS -> n79
        tn2 = self.context.mk_or(n76, n78)
        tn1 = self.context.mk_or(n74, tn2)
        tn0 = self.context.mk_or(n72, tn1)
        n79 = self.context.mk_or(n70, tn0)
        self.nets['A7E_requirements/WDMFS'] = n79
        # A7E_requirements/BOC
        n80 = self.context.mk_number('30', self.context.mk_int8_type())
        self.nets['A7E_requirements/BOC'] = n80
        # A7E_requirements/00
        n81 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/00'] = n81
        # A7E_requirements/ro20 -> n82
        n82 = self.context.mk_eq(n81, n39)
        self.nets['A7E_requirements/ro20'] = n82
        # A7E_requirements/not2 -> n83
        n83 = self.context.mk_not(n82)
        self.nets['A7E_requirements/not2'] = n83
        # A7E_requirements/UN
        n84 = self.context.mk_number('12', self.context.mk_int8_type())
        self.nets['A7E_requirements/UN'] = n84
        # A7E_requirements/GN
        n85 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/GN'] = n85
        # A7E_requirements/RK
        n86 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/RK'] = n86
        # A7E_requirements/WL
        n87 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/WL'] = n87
        # A7E_requirements/SK
        n88 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/SK'] = n88
        # A7E_requirements/MF
        n89 = self.context.mk_number('4', self.context.mk_int8_type())
        self.nets['A7E_requirements/MF'] = n89
        # A7E_requirements/SOD
        n90 = self.context.mk_number('5', self.context.mk_int8_type())
        self.nets['A7E_requirements/SOD'] = n90
        # A7E_requirements/SSH
        n91 = self.context.mk_number('6', self.context.mk_int8_type())
        self.nets['A7E_requirements/SSH'] = n91
        # A7E_requirements/SL
        n92 = self.context.mk_number('7', self.context.mk_int8_type())
        self.nets['A7E_requirements/SL'] = n92
        # A7E_requirements/MD
        n93 = self.context.mk_number('8', self.context.mk_int8_type())
        self.nets['A7E_requirements/MD'] = n93
        # A7E_requirements/OD
        n94 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['A7E_requirements/OD'] = n94
        # A7E_requirements/SM
        n95 = self.context.mk_number('10', self.context.mk_int8_type())
        self.nets['A7E_requirements/SM'] = n95
        # A7E_requirements/OR
        n96 = self.context.mk_number('11', self.context.mk_int8_type())
        self.nets['A7E_requirements/OR'] = n96
        n97_1 = self.weapon_class(n39, n84, n85, n86, n87, n88, n89, n90, n91, n92, n93, n94, n95, n96)
        # A7E_requirements/diff -> n98
        n98 = self.context.mk_neq(n84, n97_1)
        self.nets['A7E_requirements/diff'] = n98
        # A7E_requirements/Ready_Station -> n99
        tn3 = self.context.mk_and(n83, n98)
        n99 = self.context.mk_and(n40, tn3)
        self.nets['A7E_requirements/Ready_Station'] = n99
        # A7E_requirements/eq1 -> n100
        n100 = self.context.mk_eq(n90, n97_1)
        self.nets['A7E_requirements/eq1'] = n100
        # A7E_requirements/eq2 -> n101
        n101 = self.context.mk_eq(n91, n97_1)
        self.nets['A7E_requirements/eq2'] = n101
        # A7E_requirements/Special -> n102
        n102 = self.context.mk_or(n100, n101)
        self.nets['A7E_requirements/Special'] = n102
        # A7E_requirements/Walleye -> n103
        n103 = self.context.mk_eq(n97_1, n87)
        self.nets['A7E_requirements/Walleye'] = n103
        # A7E_requirements/Guns -> n104
        n104 = self.context.mk_eq(n97_1, n85)
        self.nets['A7E_requirements/Guns'] = n104
        # A7E_requirements/Rockets -> n105
        n105 = self.context.mk_eq(n97_1, n86)
        self.nets['A7E_requirements/Rockets'] = n105
        # A7E_requirements/Reserved_Weapon -> n106
        tn5 = self.context.mk_or(n104, n105)
        tn4 = self.context.mk_or(n103, tn5)
        n106 = self.context.mk_or(n102, tn4)
        self.nets['A7E_requirements/Reserved_Weapon'] = n106
        # A7E_requirements/Shrike -> n107
        n107 = self.context.mk_eq(n97_1, n88)
        self.nets['A7E_requirements/Shrike'] = n107
        # A7E_requirements/not3 -> n108
        n108 = self.context.mk_not(n107)
        self.nets['A7E_requirements/not3'] = n108
        # A7E_requirements/not4 -> n109
        n109 = self.context.mk_not(n106)
        self.nets['A7E_requirements/not4'] = n109
        # A7E_requirements/Other_Weapon -> n110
        tn6 = self.context.mk_and(n108, n109)
        n110 = self.context.mk_and(n99, tn6)
        self.nets['A7E_requirements/Other_Weapon'] = n110
        # A7E_requirements/not1 -> n111
        n111 = self.context.mk_not(n26)
        self.nets['A7E_requirements/not1'] = n111
        # A7E_requirements/zero
        n112 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/zero'] = n112
        # A7E_requirements/ro17 -> n113
        n113 = self.context.mk_eq(n38, n112)
        self.nets['A7E_requirements/ro17'] = n113
        # A7E_requirements/reset
        n114 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/reset'] = n114
        # A7E_requirements/ro18 -> n115
        n115 = self.context.mk_eq(n38, n114)
        self.nets['A7E_requirements/ro18'] = n115
        # A7E_requirements/or2 -> n116
        n116 = self.context.mk_or(n28, n41)
        self.nets['A7E_requirements/or2'] = n116
        # A7E_requirements/Redesignate -> n117
        n117 = self.context.mk_and(n42, n116)
        self.nets['A7E_requirements/Redesignate'] = n117
        n118_1 = self.WD(n99, n31, n106, n102, n105, n104, n103, n107, n110, n111, n113, n115, n37, n79, n70, n72, n74, n76, n78, n4, n117, n32, n33, n34, n35, n36, n2)
        # A7E_requirements/ro19 -> n119
        n119 = self.context.mk_eq(n80, n118_1)
        self.nets['A7E_requirements/ro19'] = n119
        # A7E_requirements/None
        n120 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/None'] = n120
        # A7E_requirements/ro10 -> n121
        n121 = self.context.mk_eq(n27, n120)
        self.nets['A7E_requirements/ro10'] = n121
        # A7E_requirements/TF
        n122 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/TF'] = n122
        # A7E_requirements/ro11 -> n123
        n123 = self.context.mk_eq(n27, n122)
        self.nets['A7E_requirements/ro11'] = n123
        n124_1 = self.NU(n40, n2, n24, n25, n60, n62, n64, n66, n68, n26, n79, n5, n119, n121, n123, n28, n29, n30)
        # A7E_requirements/or1 -> n127
        n127 = self.context.mk_or(n40, n82)
        self.nets['A7E_requirements/or1'] = n127
        # A7E_requirements/Assumption
        self.context.mk_assumption(n127)
        # A7E_requirements/Enum1 -> n129
        tn11 = self.context.mk_or(n76, n78)
        tn10 = self.context.mk_or(n74, tn11)
        tn9 = self.context.mk_or(n72, tn10)
        tn8 = self.context.mk_or(n70, tn9)
        tn7 = self.context.mk_or(n123, tn8)
        n129 = self.context.mk_or(n121, tn7)
        self.nets['A7E_requirements/Enum1'] = n129
        # A7E_requirements/Assumption1
        self.context.mk_assumption(n129)
        # A7E_requirements/Enum2 -> n131
        tn14 = self.context.mk_or(n66, n68)
        tn13 = self.context.mk_or(n64, tn14)
        tn12 = self.context.mk_or(n62, tn13)
        n131 = self.context.mk_or(n60, tn12)
        self.nets['A7E_requirements/Enum2'] = n131
        # A7E_requirements/Assumption2
        self.context.mk_assumption(n131)
        # A7E_requirements/AflyUpd
        n133 = self.context.mk_number('22', self.context.mk_int8_type())
        self.nets['A7E_requirements/AflyUpd'] = n133
        # A7E_requirements/ro21 -> n134
        n134 = self.context.mk_eq(n124_1, n133)
        self.nets['A7E_requirements/ro21'] = n134
        # A7E_requirements/and2 -> n135
        n135 = self.context.mk_and(n134, n42)
        self.nets['A7E_requirements/and2'] = n135
        # A7E_requirements/Assumption3
        self.context.mk_assumption(n135)
        # n57 -> ANT_MODE
        # n124 -> NU_MODE
        # n118 -> WD_MODE
        outputs = collections.OrderedDict()
        outputs['A7E_requirements/ANT_MODE'] = n57_1
        self.nets['A7E_requirements/ANT_MODE'] = n57_1
        outputs['A7E_requirements/NU_MODE'] = n124_1
        self.nets['A7E_requirements/NU_MODE'] = n124_1
        outputs['A7E_requirements/WD_MODE'] = n118_1
        self.nets['A7E_requirements/WD_MODE'] = n118_1
        return outputs

    def _mk_inputs(self):
        # A7E_requirements/presentPositionEntered -> n1
        n1 = self.context.mk_input('presentPositionEntered', self.context.mk_boolean_type())
        self.inputs['presentPositionEntered'] = n1
        # A7E_requirements/ACAIRB -> n2
        n2 = self.context.mk_input('ACAIRB', self.context.mk_boolean_type())
        self.inputs['ACAIRB'] = n2
        # A7E_requirements/IMSAUTOC -> n3
        n3 = self.context.mk_input('IMSAUTOC', self.context.mk_boolean_type())
        self.inputs['IMSAUTOC'] = n3
        # A7E_requirements/Desig -> n4
        n4 = self.context.mk_input('Desig', self.context.mk_boolean_type())
        self.inputs['Desig'] = n4
        # A7E_requirements/Data23=Sea -> n5
        n5 = self.context.mk_input('Data23=Sea', self.context.mk_boolean_type())
        self.inputs['Data23=Sea'] = n5
        # A7E_requirements/CAstageComplete -> n6
        n6 = self.context.mk_input('CAstageComplete', self.context.mk_boolean_type())
        self.inputs['CAstageComplete'] = n6
        # A7E_requirements/CLstageComplete -> n7
        n7 = self.context.mk_input('CLstageComplete', self.context.mk_boolean_type())
        self.inputs['CLstageComplete'] = n7
        # A7E_requirements/NDstageComplete -> n8
        n8 = self.context.mk_input('NDstageComplete', self.context.mk_boolean_type())
        self.inputs['NDstageComplete'] = n8
        # A7E_requirements/HSstageComplete -> n9
        n9 = self.context.mk_input('HSstageComplete', self.context.mk_boolean_type())
        self.inputs['HSstageComplete'] = n9
        # A7E_requirements/PNLTEST=TEST -> n10
        n10 = self.context.mk_input('PNLTEST=TEST', self.context.mk_boolean_type())
        self.inputs['PNLTEST=TEST'] = n10
        # A7E_requirements/IMSup -> n11
        n11 = self.context.mk_input('IMSup', self.context.mk_boolean_type())
        self.inputs['IMSup'] = n11
        # A7E_requirements/latitude -> n12
        n12 = self.context.mk_input('latitude', self.context.mk_real_type())
        self.inputs['latitude'] = n12
        # A7E_requirements/DopplerUp -> n13
        n13 = self.context.mk_input('DopplerUp', self.context.mk_boolean_type())
        self.inputs['DopplerUp'] = n13
        # A7E_requirements/DopplerCoupled -> n14
        n14 = self.context.mk_input('DopplerCoupled', self.context.mk_boolean_type())
        self.inputs['DopplerCoupled'] = n14
        # A7E_requirements/IMSMODE -> n15
        n15 = self.context.mk_input('IMSMODE', self.context.mk_int8_type())
        self.inputs['IMSMODE'] = n15
        # A7E_requirements/AirVelocityTestPassed -> n16
        n16 = self.context.mk_input('AirVelocityTestPassed', self.context.mk_boolean_type())
        self.inputs['AirVelocityTestPassed'] = n16
        # A7E_requirements/PitchSmall AND RollSmall -> n17
        n17 = self.context.mk_input('PitchSmall AND RollSmall', self.context.mk_boolean_type())
        self.inputs['PitchSmall AND RollSmall'] = n17
        # A7E_requirements/SINSup -> n18
        n18 = self.context.mk_input('SINSup', self.context.mk_boolean_type())
        self.inputs['SINSup'] = n18
        # A7E_requirements/SINSvelocityTestPassed -> n19
        n19 = self.context.mk_input('SINSvelocityTestPassed', self.context.mk_boolean_type())
        self.inputs['SINSvelocityTestPassed'] = n19
        # A7E_requirements/LandVelocityTestPassed -> n20
        n20 = self.context.mk_input('LandVelocityTestPassed', self.context.mk_boolean_type())
        self.inputs['LandVelocityTestPassed'] = n20
        # A7E_requirements/NonInterveningTakeoff -> n21
        n21 = self.context.mk_input('NonInterveningTakeoff', self.context.mk_boolean_type())
        self.inputs['NonInterveningTakeoff'] = n21
        # A7E_requirements/GroundTestFinished -> n22
        n22 = self.context.mk_input('GroundTestFinished', self.context.mk_boolean_type())
        self.inputs['GroundTestFinished'] = n22
        # A7E_requirements/UPDATTW -> n23
        n23 = self.context.mk_input('UPDATTW', self.context.mk_int8_type())
        self.inputs['UPDATTW'] = n23
        # A7E_requirements/MODEROT -> n24
        n24 = self.context.mk_input('MODEROT', self.context.mk_boolean_type())
        self.inputs['MODEROT'] = n24
        # A7E_requirements/PRESPOS -> n25
        n25 = self.context.mk_input('PRESPOS', self.context.mk_boolean_type())
        self.inputs['PRESPOS'] = n25
        # A7E_requirements/GUNNSEL -> n26
        n26 = self.context.mk_input('GUNNSEL', self.context.mk_boolean_type())
        self.inputs['GUNNSEL'] = n26
        # A7E_requirements/MSFW -> n27
        n27 = self.context.mk_input('MSFW', self.context.mk_int8_type())
        self.inputs['MSFW'] = n27
        # A7E_requirements/NonZeroDigitEntered -> n28
        n28 = self.context.mk_input('NonZeroDigitEntered', self.context.mk_boolean_type())
        self.inputs['NonZeroDigitEntered'] = n28
        # A7E_requirements/ENTERSW -> n29
        n29 = self.context.mk_input('ENTERSW', self.context.mk_boolean_type())
        self.inputs['ENTERSW'] = n29
        # A7E_requirements/FLYTOchanged -> n30
        n30 = self.context.mk_input('FLYTOchanged', self.context.mk_boolean_type())
        self.inputs['FLYTOchanged'] = n30
        # A7E_requirements/HUDREL -> n31
        n31 = self.context.mk_input('HUDREL', self.context.mk_boolean_type())
        self.inputs['HUDREL'] = n31
        # A7E_requirements/AnyDestEntered -> n32
        n32 = self.context.mk_input('AnyDestEntered', self.context.mk_boolean_type())
        self.inputs['AnyDestEntered'] = n32
        # A7E_requirements/HighDrag -> n33
        n33 = self.context.mk_input('HighDrag', self.context.mk_boolean_type())
        self.inputs['HighDrag'] = n33
        # A7E_requirements/LowDrag -> n34
        n34 = self.context.mk_input('LowDrag', self.context.mk_boolean_type())
        self.inputs['LowDrag'] = n34
        # A7E_requirements/OverflownExit -> n35
        n35 = self.context.mk_input('OverflownExit', self.context.mk_boolean_type())
        self.inputs['OverflownExit'] = n35
        # A7E_requirements/Overflown>42 -> n36
        n36 = self.context.mk_input('Overflown>42', self.context.mk_boolean_type())
        self.inputs['Overflown>42'] = n36
        # A7E_requirements/FLYTOTOG=Dest -> n37
        n37 = self.context.mk_input('FLYTOTOG=Dest', self.context.mk_boolean_type())
        self.inputs['FLYTOTOG=Dest'] = n37
        # A7E_requirements/FLYTOTW -> n38
        n38 = self.context.mk_input('FLYTOTW', self.context.mk_int8_type())
        self.inputs['FLYTOTW'] = n38
        # A7E_requirements/WEAPTYPE -> n39
        n39 = self.context.mk_input('WEAPTYPE', self.context.mk_int8_type())
        self.inputs['WEAPTYPE'] = n39
        # A7E_requirements/Station_Selected -> n40
        n40 = self.context.mk_input('Station_Selected', self.context.mk_boolean_type())
        self.inputs['Station_Selected'] = n40
        # A7E_requirements/TD -> n41
        n41 = self.context.mk_input('TD', self.context.mk_boolean_type())
        self.inputs['TD'] = n41
        # A7E_requirements/NU=AflyUpd -> n42
        n42 = self.context.mk_input('NU=AflyUpd', self.context.mk_boolean_type())
        self.inputs['NU=AflyUpd'] = n42

    def weapon_class(self, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150):
        # WEAPTYPE -> n137
        # UN_ -> n138
        # GN_ -> n139
        # RK_ -> n140
        # WL_ -> n141
        # SK_ -> n142
        # MF_ -> n143
        # SOD_ -> n144
        # SSH_ -> n145
        # SL_ -> n146
        # MD_ -> n147
        # OD_ -> n148
        # SM_ -> n149
        # OR_ -> n150
        # A7E_requirements/weapon_class/v54
        n151 = self.context.mk_number('94', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v54'] = n151
        # A7E_requirements/weapon_class/eq52 -> n152
        n152 = self.context.mk_eq(n137, n151)
        self.nets['A7E_requirements/weapon_class/eq52'] = n152
        # A7E_requirements/weapon_class/v53
        n153 = self.context.mk_number('99', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v53'] = n153
        # A7E_requirements/weapon_class/eq53 -> n154
        n154 = self.context.mk_eq(n137, n153)
        self.nets['A7E_requirements/weapon_class/eq53'] = n154
        # A7E_requirements/weapon_class/Logical Operator9 -> n155
        n155 = self.context.mk_or(n152, n154)
        self.nets['A7E_requirements/weapon_class/Logical Operator9'] = n155
        # A7E_requirements/weapon_class/v52
        n156 = self.context.mk_number('59', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v52'] = n156
        # A7E_requirements/weapon_class/eq50 -> n157
        n157 = self.context.mk_eq(n137, n156)
        self.nets['A7E_requirements/weapon_class/eq50'] = n157
        # A7E_requirements/weapon_class/v51
        n158 = self.context.mk_number('75', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v51'] = n158
        # A7E_requirements/weapon_class/eq51 -> n159
        n159 = self.context.mk_eq(n137, n158)
        self.nets['A7E_requirements/weapon_class/eq51'] = n159
        # A7E_requirements/weapon_class/Logical Operator8 -> n160
        n160 = self.context.mk_or(n157, n159)
        self.nets['A7E_requirements/weapon_class/Logical Operator8'] = n160
        # A7E_requirements/weapon_class/v50
        n161 = self.context.mk_number('63', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v50'] = n161
        # A7E_requirements/weapon_class/eq48 -> n162
        n162 = self.context.mk_eq(n137, n161)
        self.nets['A7E_requirements/weapon_class/eq48'] = n162
        # A7E_requirements/weapon_class/v49
        n163 = self.context.mk_number('67', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v49'] = n163
        # A7E_requirements/weapon_class/eq49 -> n164
        n164 = self.context.mk_eq(n137, n163)
        self.nets['A7E_requirements/weapon_class/eq49'] = n164
        # A7E_requirements/weapon_class/Logical Operator7 -> n165
        n165 = self.context.mk_or(n162, n164)
        self.nets['A7E_requirements/weapon_class/Logical Operator7'] = n165
        # A7E_requirements/weapon_class/v46
        n166 = self.context.mk_number('56', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v46'] = n166
        # A7E_requirements/weapon_class/eq44 -> n167
        n167 = self.context.mk_eq(n137, n166)
        self.nets['A7E_requirements/weapon_class/eq44'] = n167
        # A7E_requirements/weapon_class/v45
        n168 = self.context.mk_number('62', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v45'] = n168
        # A7E_requirements/weapon_class/eq43 -> n169
        n169 = self.context.mk_eq(n137, n168)
        self.nets['A7E_requirements/weapon_class/eq43'] = n169
        # A7E_requirements/weapon_class/v44
        n170 = self.context.mk_number('66', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v44'] = n170
        # A7E_requirements/weapon_class/eq42 -> n171
        n171 = self.context.mk_eq(n137, n170)
        self.nets['A7E_requirements/weapon_class/eq42'] = n171
        # A7E_requirements/weapon_class/v43
        n172 = self.context.mk_number('90', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v43'] = n172
        # A7E_requirements/weapon_class/eq41 -> n173
        n173 = self.context.mk_eq(n137, n172)
        self.nets['A7E_requirements/weapon_class/eq41'] = n173
        # A7E_requirements/weapon_class/v42
        n174 = self.context.mk_number('91', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v42'] = n174
        # A7E_requirements/weapon_class/eq40 -> n175
        n175 = self.context.mk_eq(n137, n174)
        self.nets['A7E_requirements/weapon_class/eq40'] = n175
        # A7E_requirements/weapon_class/v41
        n176 = self.context.mk_number('93', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v41'] = n176
        # A7E_requirements/weapon_class/eq45 -> n177
        n177 = self.context.mk_eq(n137, n176)
        self.nets['A7E_requirements/weapon_class/eq45'] = n177
        # A7E_requirements/weapon_class/v47
        n178 = self.context.mk_number('97', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v47'] = n178
        # A7E_requirements/weapon_class/eq46 -> n179
        n179 = self.context.mk_eq(n137, n178)
        self.nets['A7E_requirements/weapon_class/eq46'] = n179
        # A7E_requirements/weapon_class/v48
        n180 = self.context.mk_number('98', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v48'] = n180
        # A7E_requirements/weapon_class/eq47 -> n181
        n181 = self.context.mk_eq(n137, n180)
        self.nets['A7E_requirements/weapon_class/eq47'] = n181
        # A7E_requirements/weapon_class/Logical Operator6 -> n182
        tn20 = self.context.mk_or(n179, n181)
        tn19 = self.context.mk_or(n177, tn20)
        tn18 = self.context.mk_or(n175, tn19)
        tn17 = self.context.mk_or(n173, tn18)
        tn16 = self.context.mk_or(n171, tn17)
        tn15 = self.context.mk_or(n169, tn16)
        n182 = self.context.mk_or(n167, tn15)
        self.nets['A7E_requirements/weapon_class/Logical Operator6'] = n182
        # A7E_requirements/weapon_class/v30
        n183 = self.context.mk_number('50', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v30'] = n183
        # A7E_requirements/weapon_class/eq28 -> n184
        n184 = self.context.mk_eq(n137, n183)
        self.nets['A7E_requirements/weapon_class/eq28'] = n184
        # A7E_requirements/weapon_class/v29
        n185 = self.context.mk_number('53', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v29'] = n185
        # A7E_requirements/weapon_class/eq27 -> n186
        n186 = self.context.mk_eq(n137, n185)
        self.nets['A7E_requirements/weapon_class/eq27'] = n186
        # A7E_requirements/weapon_class/v28
        n187 = self.context.mk_number('60', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v28'] = n187
        # A7E_requirements/weapon_class/eq26 -> n188
        n188 = self.context.mk_eq(n137, n187)
        self.nets['A7E_requirements/weapon_class/eq26'] = n188
        # A7E_requirements/weapon_class/v27
        n189 = self.context.mk_number('61', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v27'] = n189
        # A7E_requirements/weapon_class/eq25 -> n190
        n190 = self.context.mk_eq(n137, n189)
        self.nets['A7E_requirements/weapon_class/eq25'] = n190
        # A7E_requirements/weapon_class/v26
        n191 = self.context.mk_number('64', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v26'] = n191
        # A7E_requirements/weapon_class/eq24 -> n192
        n192 = self.context.mk_eq(n137, n191)
        self.nets['A7E_requirements/weapon_class/eq24'] = n192
        # A7E_requirements/weapon_class/v25
        n193 = self.context.mk_number('65', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v25'] = n193
        # A7E_requirements/weapon_class/eq29 -> n194
        n194 = self.context.mk_eq(n137, n193)
        self.nets['A7E_requirements/weapon_class/eq29'] = n194
        # A7E_requirements/weapon_class/v31
        n195 = self.context.mk_number('68', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v31'] = n195
        # A7E_requirements/weapon_class/eq30 -> n196
        n196 = self.context.mk_eq(n137, n195)
        self.nets['A7E_requirements/weapon_class/eq30'] = n196
        # A7E_requirements/weapon_class/v32
        n197 = self.context.mk_number('69', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v32'] = n197
        # A7E_requirements/weapon_class/eq31 -> n198
        n198 = self.context.mk_eq(n137, n197)
        self.nets['A7E_requirements/weapon_class/eq31'] = n198
        # A7E_requirements/weapon_class/v33
        n199 = self.context.mk_number('70', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v33'] = n199
        # A7E_requirements/weapon_class/eq32 -> n200
        n200 = self.context.mk_eq(n137, n199)
        self.nets['A7E_requirements/weapon_class/eq32'] = n200
        # A7E_requirements/weapon_class/v34
        n201 = self.context.mk_number('72', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v34'] = n201
        # A7E_requirements/weapon_class/eq33 -> n202
        n202 = self.context.mk_eq(n137, n201)
        self.nets['A7E_requirements/weapon_class/eq33'] = n202
        # A7E_requirements/weapon_class/v35
        n203 = self.context.mk_number('73', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v35'] = n203
        # A7E_requirements/weapon_class/eq34 -> n204
        n204 = self.context.mk_eq(n137, n203)
        self.nets['A7E_requirements/weapon_class/eq34'] = n204
        # A7E_requirements/weapon_class/v36
        n205 = self.context.mk_number('74', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v36'] = n205
        # A7E_requirements/weapon_class/eq35 -> n206
        n206 = self.context.mk_eq(n137, n205)
        self.nets['A7E_requirements/weapon_class/eq35'] = n206
        # A7E_requirements/weapon_class/v37
        n207 = self.context.mk_number('77', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v37'] = n207
        # A7E_requirements/weapon_class/eq36 -> n208
        n208 = self.context.mk_eq(n137, n207)
        self.nets['A7E_requirements/weapon_class/eq36'] = n208
        # A7E_requirements/weapon_class/v38
        n209 = self.context.mk_number('78', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v38'] = n209
        # A7E_requirements/weapon_class/eq37 -> n210
        n210 = self.context.mk_eq(n137, n209)
        self.nets['A7E_requirements/weapon_class/eq37'] = n210
        # A7E_requirements/weapon_class/v39
        n211 = self.context.mk_number('79', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v39'] = n211
        # A7E_requirements/weapon_class/eq38 -> n212
        n212 = self.context.mk_eq(n137, n211)
        self.nets['A7E_requirements/weapon_class/eq38'] = n212
        # A7E_requirements/weapon_class/v40
        n213 = self.context.mk_number('95', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v40'] = n213
        # A7E_requirements/weapon_class/eq39 -> n214
        n214 = self.context.mk_eq(n137, n213)
        self.nets['A7E_requirements/weapon_class/eq39'] = n214
        # A7E_requirements/weapon_class/Logical Operator5 -> n215
        tn34 = self.context.mk_or(n212, n214)
        tn33 = self.context.mk_or(n210, tn34)
        tn32 = self.context.mk_or(n208, tn33)
        tn31 = self.context.mk_or(n206, tn32)
        tn30 = self.context.mk_or(n204, tn31)
        tn29 = self.context.mk_or(n202, tn30)
        tn28 = self.context.mk_or(n200, tn29)
        tn27 = self.context.mk_or(n198, tn28)
        tn26 = self.context.mk_or(n196, tn27)
        tn25 = self.context.mk_or(n194, tn26)
        tn24 = self.context.mk_or(n192, tn25)
        tn23 = self.context.mk_or(n190, tn24)
        tn22 = self.context.mk_or(n188, tn23)
        tn21 = self.context.mk_or(n186, tn22)
        n215 = self.context.mk_or(n184, tn21)
        self.nets['A7E_requirements/weapon_class/Logical Operator5'] = n215
        # A7E_requirements/weapon_class/v23
        n216 = self.context.mk_number('43', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v23'] = n216
        # A7E_requirements/weapon_class/eq22 -> n217
        n217 = self.context.mk_eq(n137, n216)
        self.nets['A7E_requirements/weapon_class/eq22'] = n217
        # A7E_requirements/weapon_class/v22
        n218 = self.context.mk_number('45', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v22'] = n218
        # A7E_requirements/weapon_class/eq23 -> n219
        n219 = self.context.mk_eq(n137, n218)
        self.nets['A7E_requirements/weapon_class/eq23'] = n219
        # A7E_requirements/weapon_class/Logical Operator4 -> n220
        n220 = self.context.mk_or(n217, n219)
        self.nets['A7E_requirements/weapon_class/Logical Operator4'] = n220
        # A7E_requirements/weapon_class/v21
        n221 = self.context.mk_number('41', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v21'] = n221
        # A7E_requirements/weapon_class/eq19 -> n222
        n222 = self.context.mk_eq(n137, n221)
        self.nets['A7E_requirements/weapon_class/eq19'] = n222
        # A7E_requirements/weapon_class/v20
        n223 = self.context.mk_number('42', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v20'] = n223
        # A7E_requirements/weapon_class/eq18 -> n224
        n224 = self.context.mk_eq(n137, n223)
        self.nets['A7E_requirements/weapon_class/eq18'] = n224
        # A7E_requirements/weapon_class/v19
        n225 = self.context.mk_number('44', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v19'] = n225
        # A7E_requirements/weapon_class/eq17 -> n226
        n226 = self.context.mk_eq(n137, n225)
        self.nets['A7E_requirements/weapon_class/eq17'] = n226
        # A7E_requirements/weapon_class/v18
        n227 = self.context.mk_number('46', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v18'] = n227
        # A7E_requirements/weapon_class/eq16 -> n228
        n228 = self.context.mk_eq(n137, n227)
        self.nets['A7E_requirements/weapon_class/eq16'] = n228
        # A7E_requirements/weapon_class/v17
        n229 = self.context.mk_number('47', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v17'] = n229
        # A7E_requirements/weapon_class/eq15 -> n230
        n230 = self.context.mk_eq(n137, n229)
        self.nets['A7E_requirements/weapon_class/eq15'] = n230
        # A7E_requirements/weapon_class/v16
        n231 = self.context.mk_number('48', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v16'] = n231
        # A7E_requirements/weapon_class/eq20 -> n232
        n232 = self.context.mk_eq(n137, n231)
        self.nets['A7E_requirements/weapon_class/eq20'] = n232
        # A7E_requirements/weapon_class/v24
        n233 = self.context.mk_number('55', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v24'] = n233
        # A7E_requirements/weapon_class/eq21 -> n234
        n234 = self.context.mk_eq(n137, n233)
        self.nets['A7E_requirements/weapon_class/eq21'] = n234
        # A7E_requirements/weapon_class/Logical Operator3 -> n235
        tn39 = self.context.mk_or(n232, n234)
        tn38 = self.context.mk_or(n230, tn39)
        tn37 = self.context.mk_or(n228, tn38)
        tn36 = self.context.mk_or(n226, tn37)
        tn35 = self.context.mk_or(n224, tn36)
        n235 = self.context.mk_or(n222, tn35)
        self.nets['A7E_requirements/weapon_class/Logical Operator3'] = n235
        # A7E_requirements/weapon_class/v15
        n236 = self.context.mk_number('58', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v15'] = n236
        # A7E_requirements/weapon_class/eq14 -> n237
        n237 = self.context.mk_eq(n137, n236)
        self.nets['A7E_requirements/weapon_class/eq14'] = n237
        # A7E_requirements/weapon_class/v14
        n238 = self.context.mk_number('57', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v14'] = n238
        # A7E_requirements/weapon_class/eq13 -> n239
        n239 = self.context.mk_eq(n137, n238)
        self.nets['A7E_requirements/weapon_class/eq13'] = n239
        # A7E_requirements/weapon_class/v13
        n240 = self.context.mk_number('33', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v13'] = n240
        # A7E_requirements/weapon_class/eq12 -> n241
        n241 = self.context.mk_eq(n137, n240)
        self.nets['A7E_requirements/weapon_class/eq12'] = n241
        # A7E_requirements/weapon_class/v12
        n242 = self.context.mk_number('32', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v12'] = n242
        # A7E_requirements/weapon_class/eq11 -> n243
        n243 = self.context.mk_eq(n137, n242)
        self.nets['A7E_requirements/weapon_class/eq11'] = n243
        # A7E_requirements/weapon_class/v11
        n244 = self.context.mk_number('31', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v11'] = n244
        # A7E_requirements/weapon_class/eq10 -> n245
        n245 = self.context.mk_eq(n137, n244)
        self.nets['A7E_requirements/weapon_class/eq10'] = n245
        # A7E_requirements/weapon_class/v10
        n246 = self.context.mk_number('30', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v10'] = n246
        # A7E_requirements/weapon_class/eq6 -> n247
        n247 = self.context.mk_eq(n137, n246)
        self.nets['A7E_requirements/weapon_class/eq6'] = n247
        # A7E_requirements/weapon_class/v9
        n248 = self.context.mk_number('24', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v9'] = n248
        # A7E_requirements/weapon_class/eq7 -> n249
        n249 = self.context.mk_eq(n137, n248)
        self.nets['A7E_requirements/weapon_class/eq7'] = n249
        # A7E_requirements/weapon_class/v8
        n250 = self.context.mk_number('22', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v8'] = n250
        # A7E_requirements/weapon_class/eq8 -> n251
        n251 = self.context.mk_eq(n137, n250)
        self.nets['A7E_requirements/weapon_class/eq8'] = n251
        # A7E_requirements/weapon_class/v7
        n252 = self.context.mk_number('21', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v7'] = n252
        # A7E_requirements/weapon_class/eq9 -> n253
        n253 = self.context.mk_eq(n137, n252)
        self.nets['A7E_requirements/weapon_class/eq9'] = n253
        # A7E_requirements/weapon_class/Logical Operator2 -> n254
        tn46 = self.context.mk_or(n251, n253)
        tn45 = self.context.mk_or(n249, tn46)
        tn44 = self.context.mk_or(n247, tn45)
        tn43 = self.context.mk_or(n245, tn44)
        tn42 = self.context.mk_or(n243, tn43)
        tn41 = self.context.mk_or(n241, tn42)
        tn40 = self.context.mk_or(n239, tn41)
        n254 = self.context.mk_or(n237, tn40)
        self.nets['A7E_requirements/weapon_class/Logical Operator2'] = n254
        # A7E_requirements/weapon_class/v6
        n255 = self.context.mk_number('17', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v6'] = n255
        # A7E_requirements/weapon_class/eq5 -> n256
        n256 = self.context.mk_eq(n137, n255)
        self.nets['A7E_requirements/weapon_class/eq5'] = n256
        # A7E_requirements/weapon_class/v5
        n257 = self.context.mk_number('10', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v5'] = n257
        # A7E_requirements/weapon_class/eq4 -> n258
        n258 = self.context.mk_eq(n137, n257)
        self.nets['A7E_requirements/weapon_class/eq4'] = n258
        # A7E_requirements/weapon_class/v4
        n259 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v4'] = n259
        # A7E_requirements/weapon_class/eq2 -> n260
        n260 = self.context.mk_eq(n137, n259)
        self.nets['A7E_requirements/weapon_class/eq2'] = n260
        # A7E_requirements/weapon_class/v3
        n261 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v3'] = n261
        # A7E_requirements/weapon_class/eq3 -> n262
        n262 = self.context.mk_eq(n137, n261)
        self.nets['A7E_requirements/weapon_class/eq3'] = n262
        # A7E_requirements/weapon_class/Logical Operator1 -> n263
        n263 = self.context.mk_or(n260, n262)
        self.nets['A7E_requirements/weapon_class/Logical Operator1'] = n263
        # A7E_requirements/weapon_class/v1
        n264 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v1'] = n264
        # A7E_requirements/weapon_class/eq -> n265
        n265 = self.context.mk_eq(n137, n264)
        self.nets['A7E_requirements/weapon_class/eq'] = n265
        # A7E_requirements/weapon_class/v2
        n266 = self.context.mk_number('13', self.context.mk_int8_type())
        self.nets['A7E_requirements/weapon_class/v2'] = n266
        # A7E_requirements/weapon_class/eq1 -> n267
        n267 = self.context.mk_eq(n137, n266)
        self.nets['A7E_requirements/weapon_class/eq1'] = n267
        # A7E_requirements/weapon_class/Logical Operator -> n268
        n268 = self.context.mk_or(n265, n267)
        self.nets['A7E_requirements/weapon_class/Logical Operator'] = n268
        # A7E_requirements/weapon_class/Switch
        n269 = self.context.mk_ite(n268, n139, n138)
        self.nets['A7E_requirements/weapon_class/Switch'] = n269
        # A7E_requirements/weapon_class/Switch1
        n270 = self.context.mk_ite(n263, n140, n269)
        self.nets['A7E_requirements/weapon_class/Switch1'] = n270
        # A7E_requirements/weapon_class/Switch2
        n271 = self.context.mk_ite(n258, n141, n270)
        self.nets['A7E_requirements/weapon_class/Switch2'] = n271
        # A7E_requirements/weapon_class/Switch3
        n272 = self.context.mk_ite(n256, n142, n271)
        self.nets['A7E_requirements/weapon_class/Switch3'] = n272
        # A7E_requirements/weapon_class/Switch4
        n273 = self.context.mk_ite(n254, n143, n272)
        self.nets['A7E_requirements/weapon_class/Switch4'] = n273
        # A7E_requirements/weapon_class/Switch5
        n274 = self.context.mk_ite(n235, n144, n273)
        self.nets['A7E_requirements/weapon_class/Switch5'] = n274
        # A7E_requirements/weapon_class/Switch6
        n275 = self.context.mk_ite(n220, n145, n274)
        self.nets['A7E_requirements/weapon_class/Switch6'] = n275
        # A7E_requirements/weapon_class/Switch7
        n276 = self.context.mk_ite(n215, n146, n275)
        self.nets['A7E_requirements/weapon_class/Switch7'] = n276
        # A7E_requirements/weapon_class/Switch8
        n277 = self.context.mk_ite(n182, n147, n276)
        self.nets['A7E_requirements/weapon_class/Switch8'] = n277
        # A7E_requirements/weapon_class/Switch9
        n278 = self.context.mk_ite(n165, n148, n277)
        self.nets['A7E_requirements/weapon_class/Switch9'] = n278
        # A7E_requirements/weapon_class/Switch10
        n279 = self.context.mk_ite(n160, n149, n278)
        self.nets['A7E_requirements/weapon_class/Switch10'] = n279
        # A7E_requirements/weapon_class/Switch11
        n280 = self.context.mk_ite(n155, n150, n279)
        self.nets['A7E_requirements/weapon_class/Switch11'] = n280
        # n280 -> weapon_class
        return n280

    def InitialState(self, n282, n283, n284, n285, n286, n287, n288, n289, n290, n291, n292, n293):
        # IMSup -> n282
        # IMSMODE=Gndal -> n283
        # IMSMODE=Iner -> n284
        # IMSMODE=Norm -> n285
        # IMSMODE=MagSl -> n286
        # IMSMODE=Grid -> n287
        # Data23=Sea -> n288
        # Landaln -> n289
        # OLB -> n290
        # MagSl -> n291
        # Grid -> n292
        # IMSfail -> n293
        # A7E_requirements/ANT/InitialState/not2 -> n294
        n294 = self.context.mk_not(n282)
        self.nets['A7E_requirements/ANT/InitialState/not2'] = n294
        # A7E_requirements/ANT/InitialState/and5 -> n295
        n295 = self.context.mk_and(n282, n287)
        self.nets['A7E_requirements/ANT/InitialState/and5'] = n295
        # A7E_requirements/ANT/InitialState/and4 -> n296
        n296 = self.context.mk_and(n282, n286)
        self.nets['A7E_requirements/ANT/InitialState/and4'] = n296
        # A7E_requirements/ANT/InitialState/and3 -> n297
        n297 = self.context.mk_and(n283, n288)
        self.nets['A7E_requirements/ANT/InitialState/and3'] = n297
        # A7E_requirements/ANT/InitialState/or1 -> n298
        tn47 = self.context.mk_or(n285, n297)
        n298 = self.context.mk_or(n284, tn47)
        self.nets['A7E_requirements/ANT/InitialState/or1'] = n298
        # A7E_requirements/ANT/InitialState/and2 -> n299
        n299 = self.context.mk_and(n282, n298)
        self.nets['A7E_requirements/ANT/InitialState/and2'] = n299
        # A7E_requirements/ANT/InitialState/not1 -> n300
        n300 = self.context.mk_not(n288)
        self.nets['A7E_requirements/ANT/InitialState/not1'] = n300
        # A7E_requirements/ANT/InitialState/and1 -> n301
        tn48 = self.context.mk_and(n283, n300)
        n301 = self.context.mk_and(n282, tn48)
        self.nets['A7E_requirements/ANT/InitialState/and1'] = n301
        # A7E_requirements/ANT/InitialState/Error
        n302 = self.context.mk_number('255', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/InitialState/Error'] = n302
        # A7E_requirements/ANT/InitialState/Switch
        n303 = self.context.mk_ite(n301, n289, n302)
        self.nets['A7E_requirements/ANT/InitialState/Switch'] = n303
        # A7E_requirements/ANT/InitialState/Switch1
        n304 = self.context.mk_ite(n299, n290, n303)
        self.nets['A7E_requirements/ANT/InitialState/Switch1'] = n304
        # A7E_requirements/ANT/InitialState/Switch2
        n305 = self.context.mk_ite(n296, n291, n304)
        self.nets['A7E_requirements/ANT/InitialState/Switch2'] = n305
        # A7E_requirements/ANT/InitialState/Switch3
        n306 = self.context.mk_ite(n295, n292, n305)
        self.nets['A7E_requirements/ANT/InitialState/Switch3'] = n306
        # A7E_requirements/ANT/InitialState/Switch4
        n307 = self.context.mk_ite(n294, n293, n306)
        self.nets['A7E_requirements/ANT/InitialState/Switch4'] = n307
        # n307 -> InitialState
        return n307

    def ANT(self, n309, n310, n311, n312, n313, n314, n315, n316, n317, n318, n319, n320, n321, n322, n323, n324, n325, n326, n327, n328, n329, n330, n331, n332, n333, n334, n335):
        # presentPositionEntered -> n309
        # ACAIRB=Yes -> n310
        # IMSAUTOC=On -> n311
        # Desig -> n312
        # Data23=Sea -> n313
        # CAstageComplete -> n314
        # CLstageComplete -> n315
        # NDstageComplete -> n316
        # HSstageComplete -> n317
        # PNLTEST=TEST -> n318
        # IMSup -> n319
        # latitude>70 -> n320
        # latitude>80 -> n321
        # DopplerUp -> n322
        # DopplerCoupled -> n323
        # IMSMODE=Gndal -> n324
        # IMSMODE=Norm -> n325
        # IMSMODE=Iner -> n326
        # IMSMODE=MagSl -> n327
        # IMSMODE=Grid -> n328
        # AirVelocityTestPassed -> n329
        # PitchSmall AND RollSmall -> n330
        # SINSup -> n331
        # SINSvelocityTestPassed -> n332
        # LandVelocityTestPassed -> n333
        # NoInterveningTakeoff -> n334
        # GroundTestFinished -> n335
        n336 = self.context.mk_latch('A7E_requirements/ANT/Init', self.context.mk_boolean_type())
        n337 = self.context.mk_latch('A7E_requirements/ANT/Past', self.context.mk_boolean_type())
        n338 = self.context.mk_latch('A7E_requirements/ANT/Past1', self.context.mk_boolean_type())
        n339 = self.context.mk_latch('A7E_requirements/ANT/Past10', self.context.mk_boolean_type())
        n340 = self.context.mk_latch('A7E_requirements/ANT/Past11', self.context.mk_boolean_type())
        n341 = self.context.mk_latch('A7E_requirements/ANT/Past12', self.context.mk_boolean_type())
        n342 = self.context.mk_latch('A7E_requirements/ANT/Past13', self.context.mk_boolean_type())
        n343 = self.context.mk_latch('A7E_requirements/ANT/Past14', self.context.mk_boolean_type())
        n344 = self.context.mk_latch('A7E_requirements/ANT/Past15', self.context.mk_boolean_type())
        n345 = self.context.mk_latch('A7E_requirements/ANT/Past16', self.context.mk_boolean_type())
        n346 = self.context.mk_latch('A7E_requirements/ANT/Past17', self.context.mk_boolean_type())
        n347 = self.context.mk_latch('A7E_requirements/ANT/Past18', self.context.mk_boolean_type())
        n348 = self.context.mk_latch('A7E_requirements/ANT/Past19', self.context.mk_boolean_type())
        n349 = self.context.mk_latch('A7E_requirements/ANT/Past7', self.context.mk_boolean_type())
        n350 = self.context.mk_latch('A7E_requirements/ANT/Past6', self.context.mk_boolean_type())
        n351 = self.context.mk_latch('A7E_requirements/ANT/Past9', self.context.mk_boolean_type())
        n352 = self.context.mk_latch('A7E_requirements/ANT/Past8', self.context.mk_boolean_type())
        n353 = self.context.mk_latch('A7E_requirements/ANT/Past3', self.context.mk_boolean_type())
        n354 = self.context.mk_latch('A7E_requirements/ANT/Past2', self.context.mk_boolean_type())
        n355 = self.context.mk_latch('A7E_requirements/ANT/Past5', self.context.mk_boolean_type())
        n356 = self.context.mk_latch('A7E_requirements/ANT/Past4', self.context.mk_boolean_type())
        n357 = self.context.mk_latch('A7E_requirements/ANT/Past(Mode)', self.context.mk_int8_type())
        n358 = self.context.mk_latch('A7E_requirements/ANT/Past20', self.context.mk_boolean_type())
        n359 = self.context.mk_latch('A7E_requirements/ANT/Past21', self.context.mk_boolean_type())
        n360 = self.context.mk_latch('A7E_requirements/ANT/Past22', self.context.mk_boolean_type())
        n361 = self.context.mk_latch('A7E_requirements/ANT/Past23', self.context.mk_boolean_type())
        n362 = self.context.mk_latch('A7E_requirements/ANT/Past24', self.context.mk_boolean_type())
        n363 = self.context.mk_latch('A7E_requirements/ANT/Past25', self.context.mk_boolean_type())
        n364 = self.context.mk_latch('A7E_requirements/ANT/Past26', self.context.mk_boolean_type())
        # A7E_requirements/ANT/false
        n365 = self.context.mk_false()
        self.nets['A7E_requirements/ANT/false'] = n365
        # A7E_requirements/ANT/Landaln
        n366 = self.context.mk_number('2', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Landaln'] = n366
        # A7E_requirements/ANT/OLB
        n367 = self.context.mk_number('11', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/OLB'] = n367
        # A7E_requirements/ANT/MagSl
        n368 = self.context.mk_number('12', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/MagSl'] = n368
        # A7E_requirements/ANT/Grid
        n369 = self.context.mk_number('13', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Grid'] = n369
        # A7E_requirements/ANT/IMSfail
        n370 = self.context.mk_number('14', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/IMSfail'] = n370
        n371_1 = self.InitialState(n319, n324, n326, n325, n327, n328, n313, n366, n367, n368, n369, n370)
        # Bus Creator
        n372 = [n309, n310, n311, n312, n313, n314, n315, n316, n317, n318, n319, n320, n321, n322, n323, n324, n325, n326, n327, n328, n329, n330, n331, n332, n333, n334, n335]
        # Bus Creator1
        n373 = [n337, n338, n354, n353, n356, n355, n350, n349, n352, n351, n339, n340, n341, n342, n343, n344, n345, n346, n347, n348, n358, n359, n360, n361, n362, n363, n364]
        # A7E_requirements/ANT/Lautocal
        n374 = self.context.mk_number('0', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Lautocal'] = n374
        # A7E_requirements/ANT/Sautocal
        n375 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Sautocal'] = n375
        # A7E_requirements/ANT/SINSaln
        n376 = self.context.mk_number('3', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/SINSaln'] = n376
        # A7E_requirements/ANT/01Update
        n377 = self.context.mk_number('4', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/01Update'] = n377
        # A7E_requirements/ANT/HUDaln
        n378 = self.context.mk_number('5', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/HUDaln'] = n378
        # A7E_requirements/ANT/Airaln
        n379 = self.context.mk_number('6', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Airaln'] = n379
        # A7E_requirements/ANT/DIG
        n380 = self.context.mk_number('7', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/DIG'] = n380
        # A7E_requirements/ANT/DI
        n381 = self.context.mk_number('8', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/DI'] = n381
        # A7E_requirements/ANT/I
        n382 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/I'] = n382
        # A7E_requirements/ANT/UDI
        n383 = self.context.mk_number('10', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/UDI'] = n383
        # A7E_requirements/ANT/PolarDI
        n384 = self.context.mk_number('15', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/PolarDI'] = n384
        # A7E_requirements/ANT/PolarI
        n385 = self.context.mk_number('16', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/PolarI'] = n385
        # A7E_requirements/ANT/Grtest
        n386 = self.context.mk_number('17', self.context.mk_int8_type())
        self.nets['A7E_requirements/ANT/Grtest'] = n386
        # Bus Creator2
        n387 = [n374, n375, n366, n376, n377, n378, n379, n380, n381, n382, n383, n367, n368, n369, n370, n384, n385, n386]
        # A7E_requirements/ANT/Mode1
        n388 = self.context.mk_ite(n336, n371_1, n357)
        self.nets['A7E_requirements/ANT/Mode1'] = n388
        n389_1 = ip.scr.mk_scr(self.context, 'tests/ANT', n372, n373, n387, n388)
        # A7E_requirements/ANT/Mode
        n390 = self.context.mk_ite(n336, n371_1, n389_1)
        self.nets['A7E_requirements/ANT/Mode'] = n390
        in336 = self.context.mk_true()
        self.context.set_latch_init_next(n336, in336, n365)
        in337 = self.context.mk_true()
        self.context.set_latch_init_next(n337, in337, n309)
        in338 = self.context.mk_true()
        self.context.set_latch_init_next(n338, in338, n310)
        in339 = self.context.mk_true()
        self.context.set_latch_init_next(n339, in339, n319)
        in340 = self.context.mk_true()
        self.context.set_latch_init_next(n340, in340, n320)
        in341 = self.context.mk_true()
        self.context.set_latch_init_next(n341, in341, n321)
        in342 = self.context.mk_true()
        self.context.set_latch_init_next(n342, in342, n322)
        in343 = self.context.mk_true()
        self.context.set_latch_init_next(n343, in343, n323)
        in344 = self.context.mk_true()
        self.context.set_latch_init_next(n344, in344, n324)
        in345 = self.context.mk_true()
        self.context.set_latch_init_next(n345, in345, n325)
        in346 = self.context.mk_true()
        self.context.set_latch_init_next(n346, in346, n326)
        in347 = self.context.mk_true()
        self.context.set_latch_init_next(n347, in347, n327)
        in348 = self.context.mk_true()
        self.context.set_latch_init_next(n348, in348, n328)
        in349 = self.context.mk_true()
        self.context.set_latch_init_next(n349, in349, n316)
        in350 = self.context.mk_true()
        self.context.set_latch_init_next(n350, in350, n315)
        in351 = self.context.mk_true()
        self.context.set_latch_init_next(n351, in351, n318)
        in352 = self.context.mk_true()
        self.context.set_latch_init_next(n352, in352, n317)
        in353 = self.context.mk_true()
        self.context.set_latch_init_next(n353, in353, n312)
        in354 = self.context.mk_true()
        self.context.set_latch_init_next(n354, in354, n311)
        in355 = self.context.mk_true()
        self.context.set_latch_init_next(n355, in355, n314)
        in356 = self.context.mk_true()
        self.context.set_latch_init_next(n356, in356, n313)
        in357 = self.context.mk_number('1', self.context.mk_int8_type())
        self.context.set_latch_init_next(n357, in357, n390)
        in358 = self.context.mk_true()
        self.context.set_latch_init_next(n358, in358, n329)
        in359 = self.context.mk_true()
        self.context.set_latch_init_next(n359, in359, n330)
        in360 = self.context.mk_true()
        self.context.set_latch_init_next(n360, in360, n331)
        in361 = self.context.mk_true()
        self.context.set_latch_init_next(n361, in361, n332)
        in362 = self.context.mk_true()
        self.context.set_latch_init_next(n362, in362, n333)
        in363 = self.context.mk_true()
        self.context.set_latch_init_next(n363, in363, n334)
        in364 = self.context.mk_true()
        self.context.set_latch_init_next(n364, in364, n335)
        # n390 -> ANT
        return n390

    def NU(self, n392, n393, n394, n395, n396, n397, n398, n399, n400, n401, n402, n403, n404, n405, n406, n407, n408, n409):
        # StationSelected -> n392
        # ACAIRB=Yes -> n393
        # MODEROT=PRESPOS -> n394
        # PRESPOS=UPDATE -> n395
        # UPDATTW=FLYOVER -> n396
        # UPDATTW=HUD -> n397
        # UPDATTW=RADAR -> n398
        # UPDATTW=TACLL -> n399
        # UPDATTW=Other -> n400
        # GUNNSEL=Yes -> n401
        # WDMFS -> n402
        # Data23=Sea -> n403
        # WeaponMode=BOC -> n404
        # MSFW=None -> n405
        # MSFW=TF -> n406
        # NonZeroDigitEntered -> n407
        # ENTERSW=On -> n408
        # FLYTOchanged -> n409
        n410 = self.context.mk_latch('A7E_requirements/NU/Init', self.context.mk_boolean_type())
        n411 = self.context.mk_latch('A7E_requirements/NU/Past', self.context.mk_boolean_type())
        n412 = self.context.mk_latch('A7E_requirements/NU/Past1', self.context.mk_boolean_type())
        n413 = self.context.mk_latch('A7E_requirements/NU/Past10', self.context.mk_boolean_type())
        n414 = self.context.mk_latch('A7E_requirements/NU/Past11', self.context.mk_boolean_type())
        n415 = self.context.mk_latch('A7E_requirements/NU/Past12', self.context.mk_boolean_type())
        n416 = self.context.mk_latch('A7E_requirements/NU/Past13', self.context.mk_boolean_type())
        n417 = self.context.mk_latch('A7E_requirements/NU/Past14', self.context.mk_boolean_type())
        n418 = self.context.mk_latch('A7E_requirements/NU/Past15', self.context.mk_boolean_type())
        n419 = self.context.mk_latch('A7E_requirements/NU/Past16', self.context.mk_boolean_type())
        n420 = self.context.mk_latch('A7E_requirements/NU/Past17', self.context.mk_boolean_type())
        n421 = self.context.mk_latch('A7E_requirements/NU/Past7', self.context.mk_boolean_type())
        n422 = self.context.mk_latch('A7E_requirements/NU/Past6', self.context.mk_boolean_type())
        n423 = self.context.mk_latch('A7E_requirements/NU/Past9', self.context.mk_boolean_type())
        n424 = self.context.mk_latch('A7E_requirements/NU/Past8', self.context.mk_boolean_type())
        n425 = self.context.mk_latch('A7E_requirements/NU/Past3', self.context.mk_boolean_type())
        n426 = self.context.mk_latch('A7E_requirements/NU/Past2', self.context.mk_boolean_type())
        n427 = self.context.mk_latch('A7E_requirements/NU/Past5', self.context.mk_boolean_type())
        n428 = self.context.mk_latch('A7E_requirements/NU/Past4', self.context.mk_boolean_type())
        n429 = self.context.mk_latch('A7E_requirements/NU/Past(Mode)', self.context.mk_int8_type())
        # A7E_requirements/NU/false
        n430 = self.context.mk_false()
        self.nets['A7E_requirements/NU/false'] = n430
        # A7E_requirements/NU/UNone
        n431 = self.context.mk_number('18', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/UNone'] = n431
        # Bus Creator
        n432 = [n392, n393, n394, n395, n396, n397, n398, n399, n400, n401, n402, n403, n404, n405, n406, n407, n408, n409]
        # Bus Creator1
        n433 = [n411, n412, n426, n425, n428, n427, n422, n421, n424, n423, n413, n414, n415, n416, n417, n418, n419, n420]
        # A7E_requirements/NU/HUDUpd
        n434 = self.context.mk_number('19', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/HUDUpd'] = n434
        # A7E_requirements/NU/RadarUpd
        n435 = self.context.mk_number('20', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/RadarUpd'] = n435
        # A7E_requirements/NU/FlyUpd
        n436 = self.context.mk_number('21', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/FlyUpd'] = n436
        # A7E_requirements/NU/AflyUpd
        n437 = self.context.mk_number('22', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/AflyUpd'] = n437
        # A7E_requirements/NU/MapUpd
        n438 = self.context.mk_number('23', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/MapUpd'] = n438
        # A7E_requirements/NU/TacUpd
        n439 = self.context.mk_number('24', self.context.mk_int8_type())
        self.nets['A7E_requirements/NU/TacUpd'] = n439
        # Bus Creator2
        n440 = [n431, n434, n435, n436, n437, n438, n439]
        # A7E_requirements/NU/Mode1
        n441 = self.context.mk_ite(n410, n431, n429)
        self.nets['A7E_requirements/NU/Mode1'] = n441
        n442_1 = ip.scr.mk_scr(self.context, 'tests/NU', n432, n433, n440, n441)
        # A7E_requirements/NU/Mode
        n443 = self.context.mk_ite(n410, n431, n442_1)
        self.nets['A7E_requirements/NU/Mode'] = n443
        in410 = self.context.mk_true()
        self.context.set_latch_init_next(n410, in410, n430)
        in411 = self.context.mk_true()
        self.context.set_latch_init_next(n411, in411, n392)
        in412 = self.context.mk_true()
        self.context.set_latch_init_next(n412, in412, n393)
        in413 = self.context.mk_true()
        self.context.set_latch_init_next(n413, in413, n402)
        in414 = self.context.mk_true()
        self.context.set_latch_init_next(n414, in414, n403)
        in415 = self.context.mk_true()
        self.context.set_latch_init_next(n415, in415, n404)
        in416 = self.context.mk_true()
        self.context.set_latch_init_next(n416, in416, n405)
        in417 = self.context.mk_true()
        self.context.set_latch_init_next(n417, in417, n406)
        in418 = self.context.mk_true()
        self.context.set_latch_init_next(n418, in418, n407)
        in419 = self.context.mk_true()
        self.context.set_latch_init_next(n419, in419, n408)
        in420 = self.context.mk_true()
        self.context.set_latch_init_next(n420, in420, n409)
        in421 = self.context.mk_true()
        self.context.set_latch_init_next(n421, in421, n399)
        in422 = self.context.mk_true()
        self.context.set_latch_init_next(n422, in422, n398)
        in423 = self.context.mk_true()
        self.context.set_latch_init_next(n423, in423, n401)
        in424 = self.context.mk_true()
        self.context.set_latch_init_next(n424, in424, n400)
        in425 = self.context.mk_true()
        self.context.set_latch_init_next(n425, in425, n395)
        in426 = self.context.mk_true()
        self.context.set_latch_init_next(n426, in426, n394)
        in427 = self.context.mk_true()
        self.context.set_latch_init_next(n427, in427, n397)
        in428 = self.context.mk_true()
        self.context.set_latch_init_next(n428, in428, n396)
        in429 = self.context.mk_number('1', self.context.mk_int8_type())
        self.context.set_latch_init_next(n429, in429, n443)
        # n443 -> NU
        return n443

    def WD(self, n445, n446, n447, n448, n449, n450, n451, n452, n453, n454, n455, n456, n457, n458, n459, n460, n461, n462, n463, n464, n465, n466, n467, n468, n469, n470, n471):
        # ReadyStation -> n445
        # HUDREL=Yes -> n446
        # ReservedWeapon -> n447
        # Special -> n448
        # Rockets -> n449
        # Guns -> n450
        # OnWalleye -> n451
        # Shrike -> n452
        # OtherWeapon -> n453
        # GUNSSEL=No -> n454
        # FLYTOTW=0 -> n455
        # FLYTOTW=reset -> n456
        # FLYTOTOG=Dest -> n457
        # WDMFS -> n458
        # MFSW=BOC -> n459
        # MFSW=BOCOFF -> n460
        # MFSW=CCIP -> n461
        # MFSW=NATT -> n462
        # MFSW=NATOFF -> n463
        # Desig -> n464
        # Redesignate -> n465
        # AnyDestEntered -> n466
        # HighDrag -> n467
        # LowDrag -> n468
        # OverflownExit -> n469
        # Overflown>42 -> n470
        # ACAIRB=Yes -> n471
        n472 = self.context.mk_latch('A7E_requirements/WD/Init', self.context.mk_boolean_type())
        n473 = self.context.mk_latch('A7E_requirements/WD/Past', self.context.mk_boolean_type())
        n474 = self.context.mk_latch('A7E_requirements/WD/Past1', self.context.mk_boolean_type())
        n475 = self.context.mk_latch('A7E_requirements/WD/Past10', self.context.mk_boolean_type())
        n476 = self.context.mk_latch('A7E_requirements/WD/Past11', self.context.mk_boolean_type())
        n477 = self.context.mk_latch('A7E_requirements/WD/Past12', self.context.mk_boolean_type())
        n478 = self.context.mk_latch('A7E_requirements/WD/Past13', self.context.mk_boolean_type())
        n479 = self.context.mk_latch('A7E_requirements/WD/Past14', self.context.mk_boolean_type())
        n480 = self.context.mk_latch('A7E_requirements/WD/Past15', self.context.mk_boolean_type())
        n481 = self.context.mk_latch('A7E_requirements/WD/Past16', self.context.mk_boolean_type())
        n482 = self.context.mk_latch('A7E_requirements/WD/Past17', self.context.mk_boolean_type())
        n483 = self.context.mk_latch('A7E_requirements/WD/Past18', self.context.mk_boolean_type())
        n484 = self.context.mk_latch('A7E_requirements/WD/Past19', self.context.mk_boolean_type())
        n485 = self.context.mk_latch('A7E_requirements/WD/Past7', self.context.mk_boolean_type())
        n486 = self.context.mk_latch('A7E_requirements/WD/Past6', self.context.mk_boolean_type())
        n487 = self.context.mk_latch('A7E_requirements/WD/Past9', self.context.mk_boolean_type())
        n488 = self.context.mk_latch('A7E_requirements/WD/Past8', self.context.mk_boolean_type())
        n489 = self.context.mk_latch('A7E_requirements/WD/Past3', self.context.mk_boolean_type())
        n490 = self.context.mk_latch('A7E_requirements/WD/Past2', self.context.mk_boolean_type())
        n491 = self.context.mk_latch('A7E_requirements/WD/Past5', self.context.mk_boolean_type())
        n492 = self.context.mk_latch('A7E_requirements/WD/Past4', self.context.mk_boolean_type())
        n493 = self.context.mk_latch('A7E_requirements/WD/Past(Mode)', self.context.mk_int8_type())
        n494 = self.context.mk_latch('A7E_requirements/WD/Past20', self.context.mk_boolean_type())
        n495 = self.context.mk_latch('A7E_requirements/WD/Past21', self.context.mk_boolean_type())
        n496 = self.context.mk_latch('A7E_requirements/WD/Past22', self.context.mk_boolean_type())
        n497 = self.context.mk_latch('A7E_requirements/WD/Past23', self.context.mk_boolean_type())
        n498 = self.context.mk_latch('A7E_requirements/WD/Past24', self.context.mk_boolean_type())
        n499 = self.context.mk_latch('A7E_requirements/WD/Past25', self.context.mk_boolean_type())
        n500 = self.context.mk_latch('A7E_requirements/WD/Past26', self.context.mk_boolean_type())
        n501 = self.context.mk_latch('A7E_requirements/WD/Past27', self.context.mk_boolean_type())
        n502 = self.context.mk_latch('A7E_requirements/WD/Past28', self.context.mk_boolean_type())
        # A7E_requirements/WD/false
        n503 = self.context.mk_false()
        self.nets['A7E_requirements/WD/false'] = n503
        # A7E_requirements/WD/WNone
        n504 = self.context.mk_number('25', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/WNone'] = n504
        # A7E_requirements/WD/Mode1
        n505 = self.context.mk_ite(n472, n504, n493)
        self.nets['A7E_requirements/WD/Mode1'] = n505
        # A7E_requirements/WD/OFF_MFS
        n506 = self.context.mk_number('26', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/OFF_MFS'] = n506
        # A7E_requirements/WD/Past(In OFF_MFSW) -> n507
        n507 = self.context.mk_eq(n505, n506)
        self.nets['A7E_requirements/WD/Past(In OFF_MFSW)'] = n507
        # A7E_requirements/WD/WD_MFS
        n508 = self.context.mk_number('27', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/WD_MFS'] = n508
        # A7E_requirements/WD/Past(In WD_MFSW) -> n509
        n509 = self.context.mk_eq(n505, n508)
        self.nets['A7E_requirements/WD/Past(In WD_MFSW)'] = n509
        # Bus Creator
        n510 = [n445, n446, n447, n448, n449, n450, n451, n452, n453, n454, n455, n456, n457, n458, n459, n460, n461, n462, n463, n464, n465, n466, n467, n468, n469, n470, n471, n507, n509]
        # Bus Creator1
        n511 = [n473, n474, n490, n489, n492, n491, n486, n485, n488, n487, n475, n476, n477, n478, n479, n480, n481, n482, n483, n484, n494, n495, n496, n497, n498, n499, n500, n501, n502]
        # A7E_requirements/WD/Nattack
        n512 = self.context.mk_number('28', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Nattack'] = n512
        # A7E_requirements/WD/Noffset
        n513 = self.context.mk_number('29', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Noffset'] = n513
        # A7E_requirements/WD/BOC
        n514 = self.context.mk_number('30', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/BOC'] = n514
        # A7E_requirements/WD/BOCFlyto0
        n515 = self.context.mk_number('31', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/BOCFlyto0'] = n515
        # A7E_requirements/WD/BOCoffset
        n516 = self.context.mk_number('32', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/BOCoffset'] = n516
        # A7E_requirements/WD/CCIP
        n517 = self.context.mk_number('33', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/CCIP'] = n517
        # A7E_requirements/WD/HUDdown1
        n518 = self.context.mk_number('34', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/HUDdown1'] = n518
        # A7E_requirements/WD/HUDdown2
        n519 = self.context.mk_number('35', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/HUDdown2'] = n519
        # A7E_requirements/WD/AG_Guns
        n520 = self.context.mk_number('36', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/AG_Guns'] = n520
        # A7E_requirements/WD/AA_Guns
        n521 = self.context.mk_number('37', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/AA_Guns'] = n521
        # A7E_requirements/WD/Manrip
        n522 = self.context.mk_number('38', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Manrip'] = n522
        # A7E_requirements/WD/AA_Manrip
        n523 = self.context.mk_number('39', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/AA_Manrip'] = n523
        # A7E_requirements/WD/Snattack
        n524 = self.context.mk_number('40', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Snattack'] = n524
        # A7E_requirements/WD/Snoffset
        n525 = self.context.mk_number('41', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Snoffset'] = n525
        # A7E_requirements/WD/SBOC
        n526 = self.context.mk_number('42', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/SBOC'] = n526
        # A7E_requirements/WD/SBOCFlyto0
        n527 = self.context.mk_number('43', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/SBOCFlyto0'] = n527
        # A7E_requirements/WD/SBOCoffset
        n528 = self.context.mk_number('44', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/SBOCoffset'] = n528
        # A7E_requirements/WD/Walleye
        n529 = self.context.mk_number('45', self.context.mk_int8_type())
        self.nets['A7E_requirements/WD/Walleye'] = n529
        # Bus Creator2
        n530 = [n504, n506, n508, n512, n513, n514, n515, n516, n517, n518, n519, n520, n521, n522, n523, n524, n525, n526, n527, n528, n529]
        n531_1 = ip.scr.mk_scr(self.context, 'tests/WD', n510, n511, n530, n505)
        # A7E_requirements/WD/Mode
        n532 = self.context.mk_ite(n472, n504, n531_1)
        self.nets['A7E_requirements/WD/Mode'] = n532
        in472 = self.context.mk_true()
        self.context.set_latch_init_next(n472, in472, n503)
        in473 = self.context.mk_true()
        self.context.set_latch_init_next(n473, in473, n445)
        in474 = self.context.mk_true()
        self.context.set_latch_init_next(n474, in474, n446)
        in475 = self.context.mk_true()
        self.context.set_latch_init_next(n475, in475, n455)
        in476 = self.context.mk_true()
        self.context.set_latch_init_next(n476, in476, n456)
        in477 = self.context.mk_true()
        self.context.set_latch_init_next(n477, in477, n457)
        in478 = self.context.mk_true()
        self.context.set_latch_init_next(n478, in478, n458)
        in479 = self.context.mk_true()
        self.context.set_latch_init_next(n479, in479, n459)
        in480 = self.context.mk_true()
        self.context.set_latch_init_next(n480, in480, n460)
        in481 = self.context.mk_true()
        self.context.set_latch_init_next(n481, in481, n461)
        in482 = self.context.mk_true()
        self.context.set_latch_init_next(n482, in482, n462)
        in483 = self.context.mk_true()
        self.context.set_latch_init_next(n483, in483, n463)
        in484 = self.context.mk_true()
        self.context.set_latch_init_next(n484, in484, n464)
        in485 = self.context.mk_true()
        self.context.set_latch_init_next(n485, in485, n452)
        in486 = self.context.mk_true()
        self.context.set_latch_init_next(n486, in486, n451)
        in487 = self.context.mk_true()
        self.context.set_latch_init_next(n487, in487, n454)
        in488 = self.context.mk_true()
        self.context.set_latch_init_next(n488, in488, n453)
        in489 = self.context.mk_true()
        self.context.set_latch_init_next(n489, in489, n448)
        in490 = self.context.mk_true()
        self.context.set_latch_init_next(n490, in490, n447)
        in491 = self.context.mk_true()
        self.context.set_latch_init_next(n491, in491, n450)
        in492 = self.context.mk_true()
        self.context.set_latch_init_next(n492, in492, n449)
        in493 = self.context.mk_number('1', self.context.mk_int8_type())
        self.context.set_latch_init_next(n493, in493, n532)
        in494 = self.context.mk_true()
        self.context.set_latch_init_next(n494, in494, n465)
        in495 = self.context.mk_true()
        self.context.set_latch_init_next(n495, in495, n466)
        in496 = self.context.mk_true()
        self.context.set_latch_init_next(n496, in496, n467)
        in497 = self.context.mk_true()
        self.context.set_latch_init_next(n497, in497, n468)
        in498 = self.context.mk_true()
        self.context.set_latch_init_next(n498, in498, n469)
        in499 = self.context.mk_true()
        self.context.set_latch_init_next(n499, in499, n470)
        in500 = self.context.mk_true()
        self.context.set_latch_init_next(n500, in500, n471)
        in501 = self.context.mk_true()
        self.context.set_latch_init_next(n501, in501, n507)
        in502 = self.context.mk_true()
        self.context.set_latch_init_next(n502, in502, n509)
        # n532 -> WD
        return n532


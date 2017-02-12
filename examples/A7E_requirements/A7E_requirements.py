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
        n43 = ip.mk_number(self.ctx, '70.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant'] = n43
        # A7E_requirements/Relational Operator -> n44
        n44 = ip.mk_gt(self.ctx, n12, n43)
        self.nets['A7E_requirements/Relational Operator'] = n44
        # A7E_requirements/Constant1
        n45 = ip.mk_number(self.ctx, '80.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant1'] = n45
        # A7E_requirements/Relational Operator1 -> n46
        n46 = ip.mk_gt(self.ctx, n12, n45)
        self.nets['A7E_requirements/Relational Operator1'] = n46
        # A7E_requirements/Gndal
        n47 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Gndal'] = n47
        # A7E_requirements/ro -> n48
        n48 = ip.mk_eq(self.ctx, n15, n47)
        self.nets['A7E_requirements/ro'] = n48
        # A7E_requirements/Norm
        n49 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Norm'] = n49
        # A7E_requirements/ro1 -> n50
        n50 = ip.mk_eq(self.ctx, n15, n49)
        self.nets['A7E_requirements/ro1'] = n50
        # A7E_requirements/Iner
        n51 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Iner'] = n51
        # A7E_requirements/ro2 -> n52
        n52 = ip.mk_eq(self.ctx, n15, n51)
        self.nets['A7E_requirements/ro2'] = n52
        # A7E_requirements/MagSl
        n53 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/MagSl'] = n53
        # A7E_requirements/ro3 -> n54
        n54 = ip.mk_eq(self.ctx, n15, n53)
        self.nets['A7E_requirements/ro3'] = n54
        # A7E_requirements/Grid
        n55 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Grid'] = n55
        # A7E_requirements/ro4 -> n56
        n56 = ip.mk_eq(self.ctx, n15, n55)
        self.nets['A7E_requirements/ro4'] = n56
        n57_1 = self.ANT(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n44, n46, n13, n14, n48, n50, n52, n54, n56, n16, n17, n18, n19, n20, n21, n22)
        # A7E_requirements/FLYOVER
        n59 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/FLYOVER'] = n59
        # A7E_requirements/ro5 -> n60
        n60 = ip.mk_eq(self.ctx, n23, n59)
        self.nets['A7E_requirements/ro5'] = n60
        # A7E_requirements/HUD
        n61 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/HUD'] = n61
        # A7E_requirements/ro6 -> n62
        n62 = ip.mk_eq(self.ctx, n23, n61)
        self.nets['A7E_requirements/ro6'] = n62
        # A7E_requirements/RADAR
        n63 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/RADAR'] = n63
        # A7E_requirements/ro7 -> n64
        n64 = ip.mk_eq(self.ctx, n23, n63)
        self.nets['A7E_requirements/ro7'] = n64
        # A7E_requirements/TACLL
        n65 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TACLL'] = n65
        # A7E_requirements/ro8 -> n66
        n66 = ip.mk_eq(self.ctx, n23, n65)
        self.nets['A7E_requirements/ro8'] = n66
        # A7E_requirements/Other
        n67 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Other'] = n67
        # A7E_requirements/ro9 -> n68
        n68 = ip.mk_eq(self.ctx, n23, n67)
        self.nets['A7E_requirements/ro9'] = n68
        # A7E_requirements/BOC_
        n69 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC_'] = n69
        # A7E_requirements/ro12 -> n70
        n70 = ip.mk_eq(self.ctx, n27, n69)
        self.nets['A7E_requirements/ro12'] = n70
        # A7E_requirements/BOCOFF
        n71 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOCOFF'] = n71
        # A7E_requirements/ro13 -> n72
        n72 = ip.mk_eq(self.ctx, n27, n71)
        self.nets['A7E_requirements/ro13'] = n72
        # A7E_requirements/CCIP
        n73 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/CCIP'] = n73
        # A7E_requirements/ro14 -> n74
        n74 = ip.mk_eq(self.ctx, n27, n73)
        self.nets['A7E_requirements/ro14'] = n74
        # A7E_requirements/NATT
        n75 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATT'] = n75
        # A7E_requirements/ro15 -> n76
        n76 = ip.mk_eq(self.ctx, n27, n75)
        self.nets['A7E_requirements/ro15'] = n76
        # A7E_requirements/NATOFF
        n77 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATOFF'] = n77
        # A7E_requirements/ro16 -> n78
        n78 = ip.mk_eq(self.ctx, n27, n77)
        self.nets['A7E_requirements/ro16'] = n78
        # A7E_requirements/WDMFS -> n79
        tn2 = ip.mk_or(self.ctx, n76, n78)
        tn1 = ip.mk_or(self.ctx, n74, tn2)
        tn0 = ip.mk_or(self.ctx, n72, tn1)
        n79 = ip.mk_or(self.ctx, n70, tn0)
        self.nets['A7E_requirements/WDMFS'] = n79
        # A7E_requirements/BOC
        n80 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC'] = n80
        # A7E_requirements/00
        n81 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/00'] = n81
        # A7E_requirements/ro20 -> n82
        n82 = ip.mk_eq(self.ctx, n81, n39)
        self.nets['A7E_requirements/ro20'] = n82
        # A7E_requirements/not2 -> n83
        n83 = ip.mk_not(self.ctx, n82)
        self.nets['A7E_requirements/not2'] = n83
        # A7E_requirements/UN
        n84 = ip.mk_number(self.ctx, '12', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/UN'] = n84
        # A7E_requirements/GN
        n85 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/GN'] = n85
        # A7E_requirements/RK
        n86 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/RK'] = n86
        # A7E_requirements/WL
        n87 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WL'] = n87
        # A7E_requirements/SK
        n88 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/SK'] = n88
        # A7E_requirements/MF
        n89 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/MF'] = n89
        # A7E_requirements/SOD
        n90 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/SOD'] = n90
        # A7E_requirements/SSH
        n91 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/SSH'] = n91
        # A7E_requirements/SL
        n92 = ip.mk_number(self.ctx, '7', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/SL'] = n92
        # A7E_requirements/MD
        n93 = ip.mk_number(self.ctx, '8', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/MD'] = n93
        # A7E_requirements/OD
        n94 = ip.mk_number(self.ctx, '9', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/OD'] = n94
        # A7E_requirements/SM
        n95 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/SM'] = n95
        # A7E_requirements/OR
        n96 = ip.mk_number(self.ctx, '11', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/OR'] = n96
        n97_1 = self.weapon_class(n39, n84, n85, n86, n87, n88, n89, n90, n91, n92, n93, n94, n95, n96)
        # A7E_requirements/diff -> n98
        n98 = ip.mk_neq(self.ctx, n84, n97_1)
        self.nets['A7E_requirements/diff'] = n98
        # A7E_requirements/Ready_Station -> n99
        tn3 = ip.mk_and(self.ctx, n83, n98)
        n99 = ip.mk_and(self.ctx, n40, tn3)
        self.nets['A7E_requirements/Ready_Station'] = n99
        # A7E_requirements/eq1 -> n100
        n100 = ip.mk_eq(self.ctx, n90, n97_1)
        self.nets['A7E_requirements/eq1'] = n100
        # A7E_requirements/eq2 -> n101
        n101 = ip.mk_eq(self.ctx, n91, n97_1)
        self.nets['A7E_requirements/eq2'] = n101
        # A7E_requirements/Special -> n102
        n102 = ip.mk_or(self.ctx, n100, n101)
        self.nets['A7E_requirements/Special'] = n102
        # A7E_requirements/Walleye -> n103
        n103 = ip.mk_eq(self.ctx, n97_1, n87)
        self.nets['A7E_requirements/Walleye'] = n103
        # A7E_requirements/Guns -> n104
        n104 = ip.mk_eq(self.ctx, n97_1, n85)
        self.nets['A7E_requirements/Guns'] = n104
        # A7E_requirements/Rockets -> n105
        n105 = ip.mk_eq(self.ctx, n97_1, n86)
        self.nets['A7E_requirements/Rockets'] = n105
        # A7E_requirements/Reserved_Weapon -> n106
        tn5 = ip.mk_or(self.ctx, n104, n105)
        tn4 = ip.mk_or(self.ctx, n103, tn5)
        n106 = ip.mk_or(self.ctx, n102, tn4)
        self.nets['A7E_requirements/Reserved_Weapon'] = n106
        # A7E_requirements/Shrike -> n107
        n107 = ip.mk_eq(self.ctx, n97_1, n88)
        self.nets['A7E_requirements/Shrike'] = n107
        # A7E_requirements/not3 -> n108
        n108 = ip.mk_not(self.ctx, n107)
        self.nets['A7E_requirements/not3'] = n108
        # A7E_requirements/not4 -> n109
        n109 = ip.mk_not(self.ctx, n106)
        self.nets['A7E_requirements/not4'] = n109
        # A7E_requirements/Other_Weapon -> n110
        tn6 = ip.mk_and(self.ctx, n108, n109)
        n110 = ip.mk_and(self.ctx, n99, tn6)
        self.nets['A7E_requirements/Other_Weapon'] = n110
        # A7E_requirements/not1 -> n111
        n111 = ip.mk_not(self.ctx, n26)
        self.nets['A7E_requirements/not1'] = n111
        # A7E_requirements/zero
        n112 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/zero'] = n112
        # A7E_requirements/ro17 -> n113
        n113 = ip.mk_eq(self.ctx, n38, n112)
        self.nets['A7E_requirements/ro17'] = n113
        # A7E_requirements/reset
        n114 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/reset'] = n114
        # A7E_requirements/ro18 -> n115
        n115 = ip.mk_eq(self.ctx, n38, n114)
        self.nets['A7E_requirements/ro18'] = n115
        # A7E_requirements/or2 -> n116
        n116 = ip.mk_or(self.ctx, n28, n41)
        self.nets['A7E_requirements/or2'] = n116
        # A7E_requirements/Redesignate -> n117
        n117 = ip.mk_and(self.ctx, n42, n116)
        self.nets['A7E_requirements/Redesignate'] = n117
        n118_1 = self.WD(n99, n31, n106, n102, n105, n104, n103, n107, n110, n111, n113, n115, n37, n79, n70, n72, n74, n76, n78, n4, n117, n32, n33, n34, n35, n36, n2)
        # A7E_requirements/ro19 -> n119
        n119 = ip.mk_eq(self.ctx, n80, n118_1)
        self.nets['A7E_requirements/ro19'] = n119
        # A7E_requirements/None
        n120 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/None'] = n120
        # A7E_requirements/ro10 -> n121
        n121 = ip.mk_eq(self.ctx, n27, n120)
        self.nets['A7E_requirements/ro10'] = n121
        # A7E_requirements/TF
        n122 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TF'] = n122
        # A7E_requirements/ro11 -> n123
        n123 = ip.mk_eq(self.ctx, n27, n122)
        self.nets['A7E_requirements/ro11'] = n123
        n124_1 = self.NU(n40, n2, n24, n25, n60, n62, n64, n66, n68, n26, n79, n5, n119, n121, n123, n28, n29, n30)
        # A7E_requirements/or1 -> n127
        n127 = ip.mk_or(self.ctx, n40, n82)
        self.nets['A7E_requirements/or1'] = n127
        # A7E_requirements/Assumption
        ip.mk_assumption(self.ctx, n127)
        # A7E_requirements/Enum1 -> n129
        tn11 = ip.mk_or(self.ctx, n76, n78)
        tn10 = ip.mk_or(self.ctx, n74, tn11)
        tn9 = ip.mk_or(self.ctx, n72, tn10)
        tn8 = ip.mk_or(self.ctx, n70, tn9)
        tn7 = ip.mk_or(self.ctx, n123, tn8)
        n129 = ip.mk_or(self.ctx, n121, tn7)
        self.nets['A7E_requirements/Enum1'] = n129
        # A7E_requirements/Assumption1
        ip.mk_assumption(self.ctx, n129)
        # A7E_requirements/Enum2 -> n131
        tn14 = ip.mk_or(self.ctx, n66, n68)
        tn13 = ip.mk_or(self.ctx, n64, tn14)
        tn12 = ip.mk_or(self.ctx, n62, tn13)
        n131 = ip.mk_or(self.ctx, n60, tn12)
        self.nets['A7E_requirements/Enum2'] = n131
        # A7E_requirements/Assumption2
        ip.mk_assumption(self.ctx, n131)
        # A7E_requirements/AflyUpd
        n133 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/AflyUpd'] = n133
        # A7E_requirements/ro21 -> n134
        n134 = ip.mk_eq(self.ctx, n124_1, n133)
        self.nets['A7E_requirements/ro21'] = n134
        # A7E_requirements/and2 -> n135
        n135 = ip.mk_and(self.ctx, n134, n42)
        self.nets['A7E_requirements/and2'] = n135
        # A7E_requirements/Assumption3
        ip.mk_assumption(self.ctx, n135)
        # n57 -> ANT_MODE
        # n124 -> NU_MODE
        # n118 -> WD_MODE
        outputs = collections.OrderedDict()
        outputs['A7E_requirements/ANT_MODE'] = n57_1
        outputs['A7E_requirements/NU_MODE'] = n124_1
        outputs['A7E_requirements/WD_MODE'] = n118_1
        return outputs

    def _mk_inputs(self):
        # A7E_requirements/presentPositionEntered -> n1
        n1 = ip.mk_input(self.ctx, 'presentPositionEntered', ip.mk_boolean_type(self.ctx))
        self.inputs['presentPositionEntered'] = n1
        # A7E_requirements/ACAIRB -> n2
        n2 = ip.mk_input(self.ctx, 'ACAIRB', ip.mk_boolean_type(self.ctx))
        self.inputs['ACAIRB'] = n2
        # A7E_requirements/IMSAUTOC -> n3
        n3 = ip.mk_input(self.ctx, 'IMSAUTOC', ip.mk_boolean_type(self.ctx))
        self.inputs['IMSAUTOC'] = n3
        # A7E_requirements/Desig -> n4
        n4 = ip.mk_input(self.ctx, 'Desig', ip.mk_boolean_type(self.ctx))
        self.inputs['Desig'] = n4
        # A7E_requirements/Data23=Sea -> n5
        n5 = ip.mk_input(self.ctx, 'Data23=Sea', ip.mk_boolean_type(self.ctx))
        self.inputs['Data23=Sea'] = n5
        # A7E_requirements/CAstageComplete -> n6
        n6 = ip.mk_input(self.ctx, 'CAstageComplete', ip.mk_boolean_type(self.ctx))
        self.inputs['CAstageComplete'] = n6
        # A7E_requirements/CLstageComplete -> n7
        n7 = ip.mk_input(self.ctx, 'CLstageComplete', ip.mk_boolean_type(self.ctx))
        self.inputs['CLstageComplete'] = n7
        # A7E_requirements/NDstageComplete -> n8
        n8 = ip.mk_input(self.ctx, 'NDstageComplete', ip.mk_boolean_type(self.ctx))
        self.inputs['NDstageComplete'] = n8
        # A7E_requirements/HSstageComplete -> n9
        n9 = ip.mk_input(self.ctx, 'HSstageComplete', ip.mk_boolean_type(self.ctx))
        self.inputs['HSstageComplete'] = n9
        # A7E_requirements/PNLTEST=TEST -> n10
        n10 = ip.mk_input(self.ctx, 'PNLTEST=TEST', ip.mk_boolean_type(self.ctx))
        self.inputs['PNLTEST=TEST'] = n10
        # A7E_requirements/IMSup -> n11
        n11 = ip.mk_input(self.ctx, 'IMSup', ip.mk_boolean_type(self.ctx))
        self.inputs['IMSup'] = n11
        # A7E_requirements/latitude -> n12
        n12 = ip.mk_input(self.ctx, 'latitude', ip.mk_real_type(self.ctx))
        self.inputs['latitude'] = n12
        # A7E_requirements/DopplerUp -> n13
        n13 = ip.mk_input(self.ctx, 'DopplerUp', ip.mk_boolean_type(self.ctx))
        self.inputs['DopplerUp'] = n13
        # A7E_requirements/DopplerCoupled -> n14
        n14 = ip.mk_input(self.ctx, 'DopplerCoupled', ip.mk_boolean_type(self.ctx))
        self.inputs['DopplerCoupled'] = n14
        # A7E_requirements/IMSMODE -> n15
        n15 = ip.mk_input(self.ctx, 'IMSMODE', ip.mk_int8_type(self.ctx))
        self.inputs['IMSMODE'] = n15
        # A7E_requirements/AirVelocityTestPassed -> n16
        n16 = ip.mk_input(self.ctx, 'AirVelocityTestPassed', ip.mk_boolean_type(self.ctx))
        self.inputs['AirVelocityTestPassed'] = n16
        # A7E_requirements/PitchSmall AND RollSmall -> n17
        n17 = ip.mk_input(self.ctx, 'PitchSmall AND RollSmall', ip.mk_boolean_type(self.ctx))
        self.inputs['PitchSmall AND RollSmall'] = n17
        # A7E_requirements/SINSup -> n18
        n18 = ip.mk_input(self.ctx, 'SINSup', ip.mk_boolean_type(self.ctx))
        self.inputs['SINSup'] = n18
        # A7E_requirements/SINSvelocityTestPassed -> n19
        n19 = ip.mk_input(self.ctx, 'SINSvelocityTestPassed', ip.mk_boolean_type(self.ctx))
        self.inputs['SINSvelocityTestPassed'] = n19
        # A7E_requirements/LandVelocityTestPassed -> n20
        n20 = ip.mk_input(self.ctx, 'LandVelocityTestPassed', ip.mk_boolean_type(self.ctx))
        self.inputs['LandVelocityTestPassed'] = n20
        # A7E_requirements/NonInterveningTakeoff -> n21
        n21 = ip.mk_input(self.ctx, 'NonInterveningTakeoff', ip.mk_boolean_type(self.ctx))
        self.inputs['NonInterveningTakeoff'] = n21
        # A7E_requirements/GroundTestFinished -> n22
        n22 = ip.mk_input(self.ctx, 'GroundTestFinished', ip.mk_boolean_type(self.ctx))
        self.inputs['GroundTestFinished'] = n22
        # A7E_requirements/UPDATTW -> n23
        n23 = ip.mk_input(self.ctx, 'UPDATTW', ip.mk_int8_type(self.ctx))
        self.inputs['UPDATTW'] = n23
        # A7E_requirements/MODEROT -> n24
        n24 = ip.mk_input(self.ctx, 'MODEROT', ip.mk_boolean_type(self.ctx))
        self.inputs['MODEROT'] = n24
        # A7E_requirements/PRESPOS -> n25
        n25 = ip.mk_input(self.ctx, 'PRESPOS', ip.mk_boolean_type(self.ctx))
        self.inputs['PRESPOS'] = n25
        # A7E_requirements/GUNNSEL -> n26
        n26 = ip.mk_input(self.ctx, 'GUNNSEL', ip.mk_boolean_type(self.ctx))
        self.inputs['GUNNSEL'] = n26
        # A7E_requirements/MSFW -> n27
        n27 = ip.mk_input(self.ctx, 'MSFW', ip.mk_int8_type(self.ctx))
        self.inputs['MSFW'] = n27
        # A7E_requirements/NonZeroDigitEntered -> n28
        n28 = ip.mk_input(self.ctx, 'NonZeroDigitEntered', ip.mk_boolean_type(self.ctx))
        self.inputs['NonZeroDigitEntered'] = n28
        # A7E_requirements/ENTERSW -> n29
        n29 = ip.mk_input(self.ctx, 'ENTERSW', ip.mk_boolean_type(self.ctx))
        self.inputs['ENTERSW'] = n29
        # A7E_requirements/FLYTOchanged -> n30
        n30 = ip.mk_input(self.ctx, 'FLYTOchanged', ip.mk_boolean_type(self.ctx))
        self.inputs['FLYTOchanged'] = n30
        # A7E_requirements/HUDREL -> n31
        n31 = ip.mk_input(self.ctx, 'HUDREL', ip.mk_boolean_type(self.ctx))
        self.inputs['HUDREL'] = n31
        # A7E_requirements/AnyDestEntered -> n32
        n32 = ip.mk_input(self.ctx, 'AnyDestEntered', ip.mk_boolean_type(self.ctx))
        self.inputs['AnyDestEntered'] = n32
        # A7E_requirements/HighDrag -> n33
        n33 = ip.mk_input(self.ctx, 'HighDrag', ip.mk_boolean_type(self.ctx))
        self.inputs['HighDrag'] = n33
        # A7E_requirements/LowDrag -> n34
        n34 = ip.mk_input(self.ctx, 'LowDrag', ip.mk_boolean_type(self.ctx))
        self.inputs['LowDrag'] = n34
        # A7E_requirements/OverflownExit -> n35
        n35 = ip.mk_input(self.ctx, 'OverflownExit', ip.mk_boolean_type(self.ctx))
        self.inputs['OverflownExit'] = n35
        # A7E_requirements/Overflown>42 -> n36
        n36 = ip.mk_input(self.ctx, 'Overflown>42', ip.mk_boolean_type(self.ctx))
        self.inputs['Overflown>42'] = n36
        # A7E_requirements/FLYTOTOG=Dest -> n37
        n37 = ip.mk_input(self.ctx, 'FLYTOTOG=Dest', ip.mk_boolean_type(self.ctx))
        self.inputs['FLYTOTOG=Dest'] = n37
        # A7E_requirements/FLYTOTW -> n38
        n38 = ip.mk_input(self.ctx, 'FLYTOTW', ip.mk_int8_type(self.ctx))
        self.inputs['FLYTOTW'] = n38
        # A7E_requirements/WEAPTYPE -> n39
        n39 = ip.mk_input(self.ctx, 'WEAPTYPE', ip.mk_int8_type(self.ctx))
        self.inputs['WEAPTYPE'] = n39
        # A7E_requirements/Station_Selected -> n40
        n40 = ip.mk_input(self.ctx, 'Station_Selected', ip.mk_boolean_type(self.ctx))
        self.inputs['Station_Selected'] = n40
        # A7E_requirements/TD -> n41
        n41 = ip.mk_input(self.ctx, 'TD', ip.mk_boolean_type(self.ctx))
        self.inputs['TD'] = n41
        # A7E_requirements/NU=AflyUpd -> n42
        n42 = ip.mk_input(self.ctx, 'NU=AflyUpd', ip.mk_boolean_type(self.ctx))
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
        n151 = ip.mk_number(self.ctx, '94', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v54'] = n151
        # A7E_requirements/weapon_class/eq52 -> n152
        n152 = ip.mk_eq(self.ctx, n137, n151)
        self.nets['A7E_requirements/weapon_class/eq52'] = n152
        # A7E_requirements/weapon_class/v53
        n153 = ip.mk_number(self.ctx, '99', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v53'] = n153
        # A7E_requirements/weapon_class/eq53 -> n154
        n154 = ip.mk_eq(self.ctx, n137, n153)
        self.nets['A7E_requirements/weapon_class/eq53'] = n154
        # A7E_requirements/weapon_class/Logical Operator9 -> n155
        n155 = ip.mk_or(self.ctx, n152, n154)
        self.nets['A7E_requirements/weapon_class/Logical Operator9'] = n155
        # A7E_requirements/weapon_class/v52
        n156 = ip.mk_number(self.ctx, '59', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v52'] = n156
        # A7E_requirements/weapon_class/eq50 -> n157
        n157 = ip.mk_eq(self.ctx, n137, n156)
        self.nets['A7E_requirements/weapon_class/eq50'] = n157
        # A7E_requirements/weapon_class/v51
        n158 = ip.mk_number(self.ctx, '75', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v51'] = n158
        # A7E_requirements/weapon_class/eq51 -> n159
        n159 = ip.mk_eq(self.ctx, n137, n158)
        self.nets['A7E_requirements/weapon_class/eq51'] = n159
        # A7E_requirements/weapon_class/Logical Operator8 -> n160
        n160 = ip.mk_or(self.ctx, n157, n159)
        self.nets['A7E_requirements/weapon_class/Logical Operator8'] = n160
        # A7E_requirements/weapon_class/v50
        n161 = ip.mk_number(self.ctx, '63', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v50'] = n161
        # A7E_requirements/weapon_class/eq48 -> n162
        n162 = ip.mk_eq(self.ctx, n137, n161)
        self.nets['A7E_requirements/weapon_class/eq48'] = n162
        # A7E_requirements/weapon_class/v49
        n163 = ip.mk_number(self.ctx, '67', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v49'] = n163
        # A7E_requirements/weapon_class/eq49 -> n164
        n164 = ip.mk_eq(self.ctx, n137, n163)
        self.nets['A7E_requirements/weapon_class/eq49'] = n164
        # A7E_requirements/weapon_class/Logical Operator7 -> n165
        n165 = ip.mk_or(self.ctx, n162, n164)
        self.nets['A7E_requirements/weapon_class/Logical Operator7'] = n165
        # A7E_requirements/weapon_class/v46
        n166 = ip.mk_number(self.ctx, '56', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v46'] = n166
        # A7E_requirements/weapon_class/eq44 -> n167
        n167 = ip.mk_eq(self.ctx, n137, n166)
        self.nets['A7E_requirements/weapon_class/eq44'] = n167
        # A7E_requirements/weapon_class/v45
        n168 = ip.mk_number(self.ctx, '62', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v45'] = n168
        # A7E_requirements/weapon_class/eq43 -> n169
        n169 = ip.mk_eq(self.ctx, n137, n168)
        self.nets['A7E_requirements/weapon_class/eq43'] = n169
        # A7E_requirements/weapon_class/v44
        n170 = ip.mk_number(self.ctx, '66', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v44'] = n170
        # A7E_requirements/weapon_class/eq42 -> n171
        n171 = ip.mk_eq(self.ctx, n137, n170)
        self.nets['A7E_requirements/weapon_class/eq42'] = n171
        # A7E_requirements/weapon_class/v43
        n172 = ip.mk_number(self.ctx, '90', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v43'] = n172
        # A7E_requirements/weapon_class/eq41 -> n173
        n173 = ip.mk_eq(self.ctx, n137, n172)
        self.nets['A7E_requirements/weapon_class/eq41'] = n173
        # A7E_requirements/weapon_class/v42
        n174 = ip.mk_number(self.ctx, '91', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v42'] = n174
        # A7E_requirements/weapon_class/eq40 -> n175
        n175 = ip.mk_eq(self.ctx, n137, n174)
        self.nets['A7E_requirements/weapon_class/eq40'] = n175
        # A7E_requirements/weapon_class/v41
        n176 = ip.mk_number(self.ctx, '93', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v41'] = n176
        # A7E_requirements/weapon_class/eq45 -> n177
        n177 = ip.mk_eq(self.ctx, n137, n176)
        self.nets['A7E_requirements/weapon_class/eq45'] = n177
        # A7E_requirements/weapon_class/v47
        n178 = ip.mk_number(self.ctx, '97', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v47'] = n178
        # A7E_requirements/weapon_class/eq46 -> n179
        n179 = ip.mk_eq(self.ctx, n137, n178)
        self.nets['A7E_requirements/weapon_class/eq46'] = n179
        # A7E_requirements/weapon_class/v48
        n180 = ip.mk_number(self.ctx, '98', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v48'] = n180
        # A7E_requirements/weapon_class/eq47 -> n181
        n181 = ip.mk_eq(self.ctx, n137, n180)
        self.nets['A7E_requirements/weapon_class/eq47'] = n181
        # A7E_requirements/weapon_class/Logical Operator6 -> n182
        tn20 = ip.mk_or(self.ctx, n179, n181)
        tn19 = ip.mk_or(self.ctx, n177, tn20)
        tn18 = ip.mk_or(self.ctx, n175, tn19)
        tn17 = ip.mk_or(self.ctx, n173, tn18)
        tn16 = ip.mk_or(self.ctx, n171, tn17)
        tn15 = ip.mk_or(self.ctx, n169, tn16)
        n182 = ip.mk_or(self.ctx, n167, tn15)
        self.nets['A7E_requirements/weapon_class/Logical Operator6'] = n182
        # A7E_requirements/weapon_class/v30
        n183 = ip.mk_number(self.ctx, '50', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v30'] = n183
        # A7E_requirements/weapon_class/eq28 -> n184
        n184 = ip.mk_eq(self.ctx, n137, n183)
        self.nets['A7E_requirements/weapon_class/eq28'] = n184
        # A7E_requirements/weapon_class/v29
        n185 = ip.mk_number(self.ctx, '53', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v29'] = n185
        # A7E_requirements/weapon_class/eq27 -> n186
        n186 = ip.mk_eq(self.ctx, n137, n185)
        self.nets['A7E_requirements/weapon_class/eq27'] = n186
        # A7E_requirements/weapon_class/v28
        n187 = ip.mk_number(self.ctx, '60', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v28'] = n187
        # A7E_requirements/weapon_class/eq26 -> n188
        n188 = ip.mk_eq(self.ctx, n137, n187)
        self.nets['A7E_requirements/weapon_class/eq26'] = n188
        # A7E_requirements/weapon_class/v27
        n189 = ip.mk_number(self.ctx, '61', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v27'] = n189
        # A7E_requirements/weapon_class/eq25 -> n190
        n190 = ip.mk_eq(self.ctx, n137, n189)
        self.nets['A7E_requirements/weapon_class/eq25'] = n190
        # A7E_requirements/weapon_class/v26
        n191 = ip.mk_number(self.ctx, '64', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v26'] = n191
        # A7E_requirements/weapon_class/eq24 -> n192
        n192 = ip.mk_eq(self.ctx, n137, n191)
        self.nets['A7E_requirements/weapon_class/eq24'] = n192
        # A7E_requirements/weapon_class/v25
        n193 = ip.mk_number(self.ctx, '65', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v25'] = n193
        # A7E_requirements/weapon_class/eq29 -> n194
        n194 = ip.mk_eq(self.ctx, n137, n193)
        self.nets['A7E_requirements/weapon_class/eq29'] = n194
        # A7E_requirements/weapon_class/v31
        n195 = ip.mk_number(self.ctx, '68', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v31'] = n195
        # A7E_requirements/weapon_class/eq30 -> n196
        n196 = ip.mk_eq(self.ctx, n137, n195)
        self.nets['A7E_requirements/weapon_class/eq30'] = n196
        # A7E_requirements/weapon_class/v32
        n197 = ip.mk_number(self.ctx, '69', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v32'] = n197
        # A7E_requirements/weapon_class/eq31 -> n198
        n198 = ip.mk_eq(self.ctx, n137, n197)
        self.nets['A7E_requirements/weapon_class/eq31'] = n198
        # A7E_requirements/weapon_class/v33
        n199 = ip.mk_number(self.ctx, '70', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v33'] = n199
        # A7E_requirements/weapon_class/eq32 -> n200
        n200 = ip.mk_eq(self.ctx, n137, n199)
        self.nets['A7E_requirements/weapon_class/eq32'] = n200
        # A7E_requirements/weapon_class/v34
        n201 = ip.mk_number(self.ctx, '72', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v34'] = n201
        # A7E_requirements/weapon_class/eq33 -> n202
        n202 = ip.mk_eq(self.ctx, n137, n201)
        self.nets['A7E_requirements/weapon_class/eq33'] = n202
        # A7E_requirements/weapon_class/v35
        n203 = ip.mk_number(self.ctx, '73', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v35'] = n203
        # A7E_requirements/weapon_class/eq34 -> n204
        n204 = ip.mk_eq(self.ctx, n137, n203)
        self.nets['A7E_requirements/weapon_class/eq34'] = n204
        # A7E_requirements/weapon_class/v36
        n205 = ip.mk_number(self.ctx, '74', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v36'] = n205
        # A7E_requirements/weapon_class/eq35 -> n206
        n206 = ip.mk_eq(self.ctx, n137, n205)
        self.nets['A7E_requirements/weapon_class/eq35'] = n206
        # A7E_requirements/weapon_class/v37
        n207 = ip.mk_number(self.ctx, '77', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v37'] = n207
        # A7E_requirements/weapon_class/eq36 -> n208
        n208 = ip.mk_eq(self.ctx, n137, n207)
        self.nets['A7E_requirements/weapon_class/eq36'] = n208
        # A7E_requirements/weapon_class/v38
        n209 = ip.mk_number(self.ctx, '78', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v38'] = n209
        # A7E_requirements/weapon_class/eq37 -> n210
        n210 = ip.mk_eq(self.ctx, n137, n209)
        self.nets['A7E_requirements/weapon_class/eq37'] = n210
        # A7E_requirements/weapon_class/v39
        n211 = ip.mk_number(self.ctx, '79', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v39'] = n211
        # A7E_requirements/weapon_class/eq38 -> n212
        n212 = ip.mk_eq(self.ctx, n137, n211)
        self.nets['A7E_requirements/weapon_class/eq38'] = n212
        # A7E_requirements/weapon_class/v40
        n213 = ip.mk_number(self.ctx, '95', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v40'] = n213
        # A7E_requirements/weapon_class/eq39 -> n214
        n214 = ip.mk_eq(self.ctx, n137, n213)
        self.nets['A7E_requirements/weapon_class/eq39'] = n214
        # A7E_requirements/weapon_class/Logical Operator5 -> n215
        tn34 = ip.mk_or(self.ctx, n212, n214)
        tn33 = ip.mk_or(self.ctx, n210, tn34)
        tn32 = ip.mk_or(self.ctx, n208, tn33)
        tn31 = ip.mk_or(self.ctx, n206, tn32)
        tn30 = ip.mk_or(self.ctx, n204, tn31)
        tn29 = ip.mk_or(self.ctx, n202, tn30)
        tn28 = ip.mk_or(self.ctx, n200, tn29)
        tn27 = ip.mk_or(self.ctx, n198, tn28)
        tn26 = ip.mk_or(self.ctx, n196, tn27)
        tn25 = ip.mk_or(self.ctx, n194, tn26)
        tn24 = ip.mk_or(self.ctx, n192, tn25)
        tn23 = ip.mk_or(self.ctx, n190, tn24)
        tn22 = ip.mk_or(self.ctx, n188, tn23)
        tn21 = ip.mk_or(self.ctx, n186, tn22)
        n215 = ip.mk_or(self.ctx, n184, tn21)
        self.nets['A7E_requirements/weapon_class/Logical Operator5'] = n215
        # A7E_requirements/weapon_class/v23
        n216 = ip.mk_number(self.ctx, '43', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v23'] = n216
        # A7E_requirements/weapon_class/eq22 -> n217
        n217 = ip.mk_eq(self.ctx, n137, n216)
        self.nets['A7E_requirements/weapon_class/eq22'] = n217
        # A7E_requirements/weapon_class/v22
        n218 = ip.mk_number(self.ctx, '45', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v22'] = n218
        # A7E_requirements/weapon_class/eq23 -> n219
        n219 = ip.mk_eq(self.ctx, n137, n218)
        self.nets['A7E_requirements/weapon_class/eq23'] = n219
        # A7E_requirements/weapon_class/Logical Operator4 -> n220
        n220 = ip.mk_or(self.ctx, n217, n219)
        self.nets['A7E_requirements/weapon_class/Logical Operator4'] = n220
        # A7E_requirements/weapon_class/v21
        n221 = ip.mk_number(self.ctx, '41', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v21'] = n221
        # A7E_requirements/weapon_class/eq19 -> n222
        n222 = ip.mk_eq(self.ctx, n137, n221)
        self.nets['A7E_requirements/weapon_class/eq19'] = n222
        # A7E_requirements/weapon_class/v20
        n223 = ip.mk_number(self.ctx, '42', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v20'] = n223
        # A7E_requirements/weapon_class/eq18 -> n224
        n224 = ip.mk_eq(self.ctx, n137, n223)
        self.nets['A7E_requirements/weapon_class/eq18'] = n224
        # A7E_requirements/weapon_class/v19
        n225 = ip.mk_number(self.ctx, '44', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v19'] = n225
        # A7E_requirements/weapon_class/eq17 -> n226
        n226 = ip.mk_eq(self.ctx, n137, n225)
        self.nets['A7E_requirements/weapon_class/eq17'] = n226
        # A7E_requirements/weapon_class/v18
        n227 = ip.mk_number(self.ctx, '46', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v18'] = n227
        # A7E_requirements/weapon_class/eq16 -> n228
        n228 = ip.mk_eq(self.ctx, n137, n227)
        self.nets['A7E_requirements/weapon_class/eq16'] = n228
        # A7E_requirements/weapon_class/v17
        n229 = ip.mk_number(self.ctx, '47', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v17'] = n229
        # A7E_requirements/weapon_class/eq15 -> n230
        n230 = ip.mk_eq(self.ctx, n137, n229)
        self.nets['A7E_requirements/weapon_class/eq15'] = n230
        # A7E_requirements/weapon_class/v16
        n231 = ip.mk_number(self.ctx, '48', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v16'] = n231
        # A7E_requirements/weapon_class/eq20 -> n232
        n232 = ip.mk_eq(self.ctx, n137, n231)
        self.nets['A7E_requirements/weapon_class/eq20'] = n232
        # A7E_requirements/weapon_class/v24
        n233 = ip.mk_number(self.ctx, '55', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v24'] = n233
        # A7E_requirements/weapon_class/eq21 -> n234
        n234 = ip.mk_eq(self.ctx, n137, n233)
        self.nets['A7E_requirements/weapon_class/eq21'] = n234
        # A7E_requirements/weapon_class/Logical Operator3 -> n235
        tn39 = ip.mk_or(self.ctx, n232, n234)
        tn38 = ip.mk_or(self.ctx, n230, tn39)
        tn37 = ip.mk_or(self.ctx, n228, tn38)
        tn36 = ip.mk_or(self.ctx, n226, tn37)
        tn35 = ip.mk_or(self.ctx, n224, tn36)
        n235 = ip.mk_or(self.ctx, n222, tn35)
        self.nets['A7E_requirements/weapon_class/Logical Operator3'] = n235
        # A7E_requirements/weapon_class/v15
        n236 = ip.mk_number(self.ctx, '58', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v15'] = n236
        # A7E_requirements/weapon_class/eq14 -> n237
        n237 = ip.mk_eq(self.ctx, n137, n236)
        self.nets['A7E_requirements/weapon_class/eq14'] = n237
        # A7E_requirements/weapon_class/v14
        n238 = ip.mk_number(self.ctx, '57', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v14'] = n238
        # A7E_requirements/weapon_class/eq13 -> n239
        n239 = ip.mk_eq(self.ctx, n137, n238)
        self.nets['A7E_requirements/weapon_class/eq13'] = n239
        # A7E_requirements/weapon_class/v13
        n240 = ip.mk_number(self.ctx, '33', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v13'] = n240
        # A7E_requirements/weapon_class/eq12 -> n241
        n241 = ip.mk_eq(self.ctx, n137, n240)
        self.nets['A7E_requirements/weapon_class/eq12'] = n241
        # A7E_requirements/weapon_class/v12
        n242 = ip.mk_number(self.ctx, '32', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v12'] = n242
        # A7E_requirements/weapon_class/eq11 -> n243
        n243 = ip.mk_eq(self.ctx, n137, n242)
        self.nets['A7E_requirements/weapon_class/eq11'] = n243
        # A7E_requirements/weapon_class/v11
        n244 = ip.mk_number(self.ctx, '31', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v11'] = n244
        # A7E_requirements/weapon_class/eq10 -> n245
        n245 = ip.mk_eq(self.ctx, n137, n244)
        self.nets['A7E_requirements/weapon_class/eq10'] = n245
        # A7E_requirements/weapon_class/v10
        n246 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v10'] = n246
        # A7E_requirements/weapon_class/eq6 -> n247
        n247 = ip.mk_eq(self.ctx, n137, n246)
        self.nets['A7E_requirements/weapon_class/eq6'] = n247
        # A7E_requirements/weapon_class/v9
        n248 = ip.mk_number(self.ctx, '24', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v9'] = n248
        # A7E_requirements/weapon_class/eq7 -> n249
        n249 = ip.mk_eq(self.ctx, n137, n248)
        self.nets['A7E_requirements/weapon_class/eq7'] = n249
        # A7E_requirements/weapon_class/v8
        n250 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v8'] = n250
        # A7E_requirements/weapon_class/eq8 -> n251
        n251 = ip.mk_eq(self.ctx, n137, n250)
        self.nets['A7E_requirements/weapon_class/eq8'] = n251
        # A7E_requirements/weapon_class/v7
        n252 = ip.mk_number(self.ctx, '21', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v7'] = n252
        # A7E_requirements/weapon_class/eq9 -> n253
        n253 = ip.mk_eq(self.ctx, n137, n252)
        self.nets['A7E_requirements/weapon_class/eq9'] = n253
        # A7E_requirements/weapon_class/Logical Operator2 -> n254
        tn46 = ip.mk_or(self.ctx, n251, n253)
        tn45 = ip.mk_or(self.ctx, n249, tn46)
        tn44 = ip.mk_or(self.ctx, n247, tn45)
        tn43 = ip.mk_or(self.ctx, n245, tn44)
        tn42 = ip.mk_or(self.ctx, n243, tn43)
        tn41 = ip.mk_or(self.ctx, n241, tn42)
        tn40 = ip.mk_or(self.ctx, n239, tn41)
        n254 = ip.mk_or(self.ctx, n237, tn40)
        self.nets['A7E_requirements/weapon_class/Logical Operator2'] = n254
        # A7E_requirements/weapon_class/v6
        n255 = ip.mk_number(self.ctx, '17', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v6'] = n255
        # A7E_requirements/weapon_class/eq5 -> n256
        n256 = ip.mk_eq(self.ctx, n137, n255)
        self.nets['A7E_requirements/weapon_class/eq5'] = n256
        # A7E_requirements/weapon_class/v5
        n257 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v5'] = n257
        # A7E_requirements/weapon_class/eq4 -> n258
        n258 = ip.mk_eq(self.ctx, n137, n257)
        self.nets['A7E_requirements/weapon_class/eq4'] = n258
        # A7E_requirements/weapon_class/v4
        n259 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v4'] = n259
        # A7E_requirements/weapon_class/eq2 -> n260
        n260 = ip.mk_eq(self.ctx, n137, n259)
        self.nets['A7E_requirements/weapon_class/eq2'] = n260
        # A7E_requirements/weapon_class/v3
        n261 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v3'] = n261
        # A7E_requirements/weapon_class/eq3 -> n262
        n262 = ip.mk_eq(self.ctx, n137, n261)
        self.nets['A7E_requirements/weapon_class/eq3'] = n262
        # A7E_requirements/weapon_class/Logical Operator1 -> n263
        n263 = ip.mk_or(self.ctx, n260, n262)
        self.nets['A7E_requirements/weapon_class/Logical Operator1'] = n263
        # A7E_requirements/weapon_class/v1
        n264 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v1'] = n264
        # A7E_requirements/weapon_class/eq -> n265
        n265 = ip.mk_eq(self.ctx, n137, n264)
        self.nets['A7E_requirements/weapon_class/eq'] = n265
        # A7E_requirements/weapon_class/v2
        n266 = ip.mk_number(self.ctx, '13', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v2'] = n266
        # A7E_requirements/weapon_class/eq1 -> n267
        n267 = ip.mk_eq(self.ctx, n137, n266)
        self.nets['A7E_requirements/weapon_class/eq1'] = n267
        # A7E_requirements/weapon_class/Logical Operator -> n268
        n268 = ip.mk_or(self.ctx, n265, n267)
        self.nets['A7E_requirements/weapon_class/Logical Operator'] = n268
        # A7E_requirements/weapon_class/Switch
        n269 = ip.mk_ite(self.ctx, n268, n139, n138)
        self.nets['A7E_requirements/weapon_class/Switch'] = n269
        # A7E_requirements/weapon_class/Switch1
        n270 = ip.mk_ite(self.ctx, n263, n140, n269)
        self.nets['A7E_requirements/weapon_class/Switch1'] = n270
        # A7E_requirements/weapon_class/Switch2
        n271 = ip.mk_ite(self.ctx, n258, n141, n270)
        self.nets['A7E_requirements/weapon_class/Switch2'] = n271
        # A7E_requirements/weapon_class/Switch3
        n272 = ip.mk_ite(self.ctx, n256, n142, n271)
        self.nets['A7E_requirements/weapon_class/Switch3'] = n272
        # A7E_requirements/weapon_class/Switch4
        n273 = ip.mk_ite(self.ctx, n254, n143, n272)
        self.nets['A7E_requirements/weapon_class/Switch4'] = n273
        # A7E_requirements/weapon_class/Switch5
        n274 = ip.mk_ite(self.ctx, n235, n144, n273)
        self.nets['A7E_requirements/weapon_class/Switch5'] = n274
        # A7E_requirements/weapon_class/Switch6
        n275 = ip.mk_ite(self.ctx, n220, n145, n274)
        self.nets['A7E_requirements/weapon_class/Switch6'] = n275
        # A7E_requirements/weapon_class/Switch7
        n276 = ip.mk_ite(self.ctx, n215, n146, n275)
        self.nets['A7E_requirements/weapon_class/Switch7'] = n276
        # A7E_requirements/weapon_class/Switch8
        n277 = ip.mk_ite(self.ctx, n182, n147, n276)
        self.nets['A7E_requirements/weapon_class/Switch8'] = n277
        # A7E_requirements/weapon_class/Switch9
        n278 = ip.mk_ite(self.ctx, n165, n148, n277)
        self.nets['A7E_requirements/weapon_class/Switch9'] = n278
        # A7E_requirements/weapon_class/Switch10
        n279 = ip.mk_ite(self.ctx, n160, n149, n278)
        self.nets['A7E_requirements/weapon_class/Switch10'] = n279
        # A7E_requirements/weapon_class/Switch11
        n280 = ip.mk_ite(self.ctx, n155, n150, n279)
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
        n294 = ip.mk_not(self.ctx, n282)
        self.nets['A7E_requirements/ANT/InitialState/not2'] = n294
        # A7E_requirements/ANT/InitialState/and5 -> n295
        n295 = ip.mk_and(self.ctx, n282, n287)
        self.nets['A7E_requirements/ANT/InitialState/and5'] = n295
        # A7E_requirements/ANT/InitialState/and4 -> n296
        n296 = ip.mk_and(self.ctx, n282, n286)
        self.nets['A7E_requirements/ANT/InitialState/and4'] = n296
        # A7E_requirements/ANT/InitialState/and3 -> n297
        n297 = ip.mk_and(self.ctx, n283, n288)
        self.nets['A7E_requirements/ANT/InitialState/and3'] = n297
        # A7E_requirements/ANT/InitialState/or1 -> n298
        tn47 = ip.mk_or(self.ctx, n285, n297)
        n298 = ip.mk_or(self.ctx, n284, tn47)
        self.nets['A7E_requirements/ANT/InitialState/or1'] = n298
        # A7E_requirements/ANT/InitialState/and2 -> n299
        n299 = ip.mk_and(self.ctx, n282, n298)
        self.nets['A7E_requirements/ANT/InitialState/and2'] = n299
        # A7E_requirements/ANT/InitialState/not1 -> n300
        n300 = ip.mk_not(self.ctx, n288)
        self.nets['A7E_requirements/ANT/InitialState/not1'] = n300
        # A7E_requirements/ANT/InitialState/and1 -> n301
        tn48 = ip.mk_and(self.ctx, n283, n300)
        n301 = ip.mk_and(self.ctx, n282, tn48)
        self.nets['A7E_requirements/ANT/InitialState/and1'] = n301
        # A7E_requirements/ANT/InitialState/Error
        n302 = ip.mk_number(self.ctx, '255', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/InitialState/Error'] = n302
        # A7E_requirements/ANT/InitialState/Switch
        n303 = ip.mk_ite(self.ctx, n301, n289, n302)
        self.nets['A7E_requirements/ANT/InitialState/Switch'] = n303
        # A7E_requirements/ANT/InitialState/Switch1
        n304 = ip.mk_ite(self.ctx, n299, n290, n303)
        self.nets['A7E_requirements/ANT/InitialState/Switch1'] = n304
        # A7E_requirements/ANT/InitialState/Switch2
        n305 = ip.mk_ite(self.ctx, n296, n291, n304)
        self.nets['A7E_requirements/ANT/InitialState/Switch2'] = n305
        # A7E_requirements/ANT/InitialState/Switch3
        n306 = ip.mk_ite(self.ctx, n295, n292, n305)
        self.nets['A7E_requirements/ANT/InitialState/Switch3'] = n306
        # A7E_requirements/ANT/InitialState/Switch4
        n307 = ip.mk_ite(self.ctx, n294, n293, n306)
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
        n336 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Init', ip.mk_boolean_type(self.ctx))
        n337 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past', ip.mk_boolean_type(self.ctx))
        n338 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past1', ip.mk_boolean_type(self.ctx))
        n339 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past10', ip.mk_boolean_type(self.ctx))
        n340 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past11', ip.mk_boolean_type(self.ctx))
        n341 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past12', ip.mk_boolean_type(self.ctx))
        n342 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past13', ip.mk_boolean_type(self.ctx))
        n343 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past14', ip.mk_boolean_type(self.ctx))
        n344 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past15', ip.mk_boolean_type(self.ctx))
        n345 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past16', ip.mk_boolean_type(self.ctx))
        n346 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past17', ip.mk_boolean_type(self.ctx))
        n347 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past18', ip.mk_boolean_type(self.ctx))
        n348 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past19', ip.mk_boolean_type(self.ctx))
        n349 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past7', ip.mk_boolean_type(self.ctx))
        n350 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past6', ip.mk_boolean_type(self.ctx))
        n351 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past9', ip.mk_boolean_type(self.ctx))
        n352 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past8', ip.mk_boolean_type(self.ctx))
        n353 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past3', ip.mk_boolean_type(self.ctx))
        n354 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past2', ip.mk_boolean_type(self.ctx))
        n355 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past5', ip.mk_boolean_type(self.ctx))
        n356 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past4', ip.mk_boolean_type(self.ctx))
        n357 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past(Mode)', ip.mk_int8_type(self.ctx))
        n358 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past20', ip.mk_boolean_type(self.ctx))
        n359 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past21', ip.mk_boolean_type(self.ctx))
        n360 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past22', ip.mk_boolean_type(self.ctx))
        n361 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past23', ip.mk_boolean_type(self.ctx))
        n362 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past24', ip.mk_boolean_type(self.ctx))
        n363 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past25', ip.mk_boolean_type(self.ctx))
        n364 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past26', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/ANT/false
        n365 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/ANT/false'] = n365
        # A7E_requirements/ANT/Landaln
        n366 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Landaln'] = n366
        # A7E_requirements/ANT/OLB
        n367 = ip.mk_number(self.ctx, '11', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/OLB'] = n367
        # A7E_requirements/ANT/MagSl
        n368 = ip.mk_number(self.ctx, '12', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/MagSl'] = n368
        # A7E_requirements/ANT/Grid
        n369 = ip.mk_number(self.ctx, '13', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grid'] = n369
        # A7E_requirements/ANT/IMSfail
        n370 = ip.mk_number(self.ctx, '14', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/IMSfail'] = n370
        n371_1 = self.InitialState(n319, n324, n326, n325, n327, n328, n313, n366, n367, n368, n369, n370)
        # Bus Creator
        n372 = [n309, n310, n311, n312, n313, n314, n315, n316, n317, n318, n319, n320, n321, n322, n323, n324, n325, n326, n327, n328, n329, n330, n331, n332, n333, n334, n335]
        # Bus Creator1
        n373 = [n337, n338, n354, n353, n356, n355, n350, n349, n352, n351, n339, n340, n341, n342, n343, n344, n345, n346, n347, n348, n358, n359, n360, n361, n362, n363, n364]
        # A7E_requirements/ANT/Lautocal
        n374 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Lautocal'] = n374
        # A7E_requirements/ANT/Sautocal
        n375 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Sautocal'] = n375
        # A7E_requirements/ANT/SINSaln
        n376 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/SINSaln'] = n376
        # A7E_requirements/ANT/01Update
        n377 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/01Update'] = n377
        # A7E_requirements/ANT/HUDaln
        n378 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/HUDaln'] = n378
        # A7E_requirements/ANT/Airaln
        n379 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Airaln'] = n379
        # A7E_requirements/ANT/DIG
        n380 = ip.mk_number(self.ctx, '7', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DIG'] = n380
        # A7E_requirements/ANT/DI
        n381 = ip.mk_number(self.ctx, '8', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DI'] = n381
        # A7E_requirements/ANT/I
        n382 = ip.mk_number(self.ctx, '9', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/I'] = n382
        # A7E_requirements/ANT/UDI
        n383 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/UDI'] = n383
        # A7E_requirements/ANT/PolarDI
        n384 = ip.mk_number(self.ctx, '15', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarDI'] = n384
        # A7E_requirements/ANT/PolarI
        n385 = ip.mk_number(self.ctx, '16', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarI'] = n385
        # A7E_requirements/ANT/Grtest
        n386 = ip.mk_number(self.ctx, '17', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grtest'] = n386
        # Bus Creator2
        n387 = [n374, n375, n366, n376, n377, n378, n379, n380, n381, n382, n383, n367, n368, n369, n370, n384, n385, n386]
        # A7E_requirements/ANT/Mode1
        n388 = ip.mk_ite(self.ctx, n336, n371_1, n357)
        self.nets['A7E_requirements/ANT/Mode1'] = n388
        n389_1 = ip.scr.mk_scr(self.ctx, 'ANT', n372, n373, n387, n388)
        # A7E_requirements/ANT/Mode
        n390 = ip.mk_ite(self.ctx, n336, n371_1, n389_1)
        self.nets['A7E_requirements/ANT/Mode'] = n390
        in336 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n336, in336, n365)
        in337 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n337, in337, n309)
        in338 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n338, in338, n310)
        in339 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n339, in339, n319)
        in340 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n340, in340, n320)
        in341 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n341, in341, n321)
        in342 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n342, in342, n322)
        in343 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n343, in343, n323)
        in344 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n344, in344, n324)
        in345 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n345, in345, n325)
        in346 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n346, in346, n326)
        in347 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n347, in347, n327)
        in348 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n348, in348, n328)
        in349 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n349, in349, n316)
        in350 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n350, in350, n315)
        in351 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n351, in351, n318)
        in352 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n352, in352, n317)
        in353 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n353, in353, n312)
        in354 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n354, in354, n311)
        in355 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n355, in355, n314)
        in356 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n356, in356, n313)
        in357 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n357, in357, n390)
        in358 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n358, in358, n329)
        in359 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n359, in359, n330)
        in360 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n360, in360, n331)
        in361 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n361, in361, n332)
        in362 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n362, in362, n333)
        in363 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n363, in363, n334)
        in364 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n364, in364, n335)
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
        n410 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Init', ip.mk_boolean_type(self.ctx))
        n411 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past', ip.mk_boolean_type(self.ctx))
        n412 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past1', ip.mk_boolean_type(self.ctx))
        n413 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past10', ip.mk_boolean_type(self.ctx))
        n414 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past11', ip.mk_boolean_type(self.ctx))
        n415 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past12', ip.mk_boolean_type(self.ctx))
        n416 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past13', ip.mk_boolean_type(self.ctx))
        n417 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past14', ip.mk_boolean_type(self.ctx))
        n418 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past15', ip.mk_boolean_type(self.ctx))
        n419 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past16', ip.mk_boolean_type(self.ctx))
        n420 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past17', ip.mk_boolean_type(self.ctx))
        n421 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past7', ip.mk_boolean_type(self.ctx))
        n422 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past6', ip.mk_boolean_type(self.ctx))
        n423 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past9', ip.mk_boolean_type(self.ctx))
        n424 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past8', ip.mk_boolean_type(self.ctx))
        n425 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past3', ip.mk_boolean_type(self.ctx))
        n426 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past2', ip.mk_boolean_type(self.ctx))
        n427 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past5', ip.mk_boolean_type(self.ctx))
        n428 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past4', ip.mk_boolean_type(self.ctx))
        n429 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past(Mode)', ip.mk_int8_type(self.ctx))
        # A7E_requirements/NU/false
        n430 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/NU/false'] = n430
        # A7E_requirements/NU/UNone
        n431 = ip.mk_number(self.ctx, '18', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/UNone'] = n431
        # Bus Creator
        n432 = [n392, n393, n394, n395, n396, n397, n398, n399, n400, n401, n402, n403, n404, n405, n406, n407, n408, n409]
        # Bus Creator1
        n433 = [n411, n412, n426, n425, n428, n427, n422, n421, n424, n423, n413, n414, n415, n416, n417, n418, n419, n420]
        # A7E_requirements/NU/HUDUpd
        n434 = ip.mk_number(self.ctx, '19', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/HUDUpd'] = n434
        # A7E_requirements/NU/RadarUpd
        n435 = ip.mk_number(self.ctx, '20', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/RadarUpd'] = n435
        # A7E_requirements/NU/FlyUpd
        n436 = ip.mk_number(self.ctx, '21', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/FlyUpd'] = n436
        # A7E_requirements/NU/AflyUpd
        n437 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/AflyUpd'] = n437
        # A7E_requirements/NU/MapUpd
        n438 = ip.mk_number(self.ctx, '23', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/MapUpd'] = n438
        # A7E_requirements/NU/TacUpd
        n439 = ip.mk_number(self.ctx, '24', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/TacUpd'] = n439
        # Bus Creator2
        n440 = [n431, n434, n435, n436, n437, n438, n439]
        # A7E_requirements/NU/Mode1
        n441 = ip.mk_ite(self.ctx, n410, n431, n429)
        self.nets['A7E_requirements/NU/Mode1'] = n441
        n442_1 = ip.scr.mk_scr(self.ctx, 'NU', n432, n433, n440, n441)
        # A7E_requirements/NU/Mode
        n443 = ip.mk_ite(self.ctx, n410, n431, n442_1)
        self.nets['A7E_requirements/NU/Mode'] = n443
        in410 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n410, in410, n430)
        in411 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n411, in411, n392)
        in412 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n412, in412, n393)
        in413 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n413, in413, n402)
        in414 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n414, in414, n403)
        in415 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n415, in415, n404)
        in416 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n416, in416, n405)
        in417 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n417, in417, n406)
        in418 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n418, in418, n407)
        in419 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n419, in419, n408)
        in420 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n420, in420, n409)
        in421 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n421, in421, n399)
        in422 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n422, in422, n398)
        in423 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n423, in423, n401)
        in424 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n424, in424, n400)
        in425 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n425, in425, n395)
        in426 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n426, in426, n394)
        in427 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n427, in427, n397)
        in428 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n428, in428, n396)
        in429 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n429, in429, n443)
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
        n472 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Init', ip.mk_boolean_type(self.ctx))
        n473 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past', ip.mk_boolean_type(self.ctx))
        n474 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past1', ip.mk_boolean_type(self.ctx))
        n475 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past10', ip.mk_boolean_type(self.ctx))
        n476 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past11', ip.mk_boolean_type(self.ctx))
        n477 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past12', ip.mk_boolean_type(self.ctx))
        n478 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past13', ip.mk_boolean_type(self.ctx))
        n479 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past14', ip.mk_boolean_type(self.ctx))
        n480 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past15', ip.mk_boolean_type(self.ctx))
        n481 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past16', ip.mk_boolean_type(self.ctx))
        n482 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past17', ip.mk_boolean_type(self.ctx))
        n483 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past18', ip.mk_boolean_type(self.ctx))
        n484 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past19', ip.mk_boolean_type(self.ctx))
        n485 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past7', ip.mk_boolean_type(self.ctx))
        n486 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past6', ip.mk_boolean_type(self.ctx))
        n487 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past9', ip.mk_boolean_type(self.ctx))
        n488 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past8', ip.mk_boolean_type(self.ctx))
        n489 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past3', ip.mk_boolean_type(self.ctx))
        n490 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past2', ip.mk_boolean_type(self.ctx))
        n491 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past5', ip.mk_boolean_type(self.ctx))
        n492 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past4', ip.mk_boolean_type(self.ctx))
        n493 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past(Mode)', ip.mk_int8_type(self.ctx))
        n494 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past20', ip.mk_boolean_type(self.ctx))
        n495 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past21', ip.mk_boolean_type(self.ctx))
        n496 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past22', ip.mk_boolean_type(self.ctx))
        n497 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past23', ip.mk_boolean_type(self.ctx))
        n498 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past24', ip.mk_boolean_type(self.ctx))
        n499 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past25', ip.mk_boolean_type(self.ctx))
        n500 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past26', ip.mk_boolean_type(self.ctx))
        n501 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past27', ip.mk_boolean_type(self.ctx))
        n502 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past28', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/WD/false
        n503 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/WD/false'] = n503
        # A7E_requirements/WD/WNone
        n504 = ip.mk_number(self.ctx, '25', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WNone'] = n504
        # A7E_requirements/WD/Mode1
        n505 = ip.mk_ite(self.ctx, n472, n504, n493)
        self.nets['A7E_requirements/WD/Mode1'] = n505
        # A7E_requirements/WD/OFF_MFS
        n506 = ip.mk_number(self.ctx, '26', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/OFF_MFS'] = n506
        # A7E_requirements/WD/Past(In OFF_MFSW) -> n507
        n507 = ip.mk_eq(self.ctx, n505, n506)
        self.nets['A7E_requirements/WD/Past(In OFF_MFSW)'] = n507
        # A7E_requirements/WD/WD_MFS
        n508 = ip.mk_number(self.ctx, '27', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WD_MFS'] = n508
        # A7E_requirements/WD/Past(In WD_MFSW) -> n509
        n509 = ip.mk_eq(self.ctx, n505, n508)
        self.nets['A7E_requirements/WD/Past(In WD_MFSW)'] = n509
        # Bus Creator
        n510 = [n445, n446, n447, n448, n449, n450, n451, n452, n453, n454, n455, n456, n457, n458, n459, n460, n461, n462, n463, n464, n465, n466, n467, n468, n469, n470, n471, n507, n509]
        # Bus Creator1
        n511 = [n473, n474, n490, n489, n492, n491, n486, n485, n488, n487, n475, n476, n477, n478, n479, n480, n481, n482, n483, n484, n494, n495, n496, n497, n498, n499, n500, n501, n502]
        # A7E_requirements/WD/Nattack
        n512 = ip.mk_number(self.ctx, '28', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Nattack'] = n512
        # A7E_requirements/WD/Noffset
        n513 = ip.mk_number(self.ctx, '29', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Noffset'] = n513
        # A7E_requirements/WD/BOC
        n514 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOC'] = n514
        # A7E_requirements/WD/BOCFlyto0
        n515 = ip.mk_number(self.ctx, '31', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCFlyto0'] = n515
        # A7E_requirements/WD/BOCoffset
        n516 = ip.mk_number(self.ctx, '32', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCoffset'] = n516
        # A7E_requirements/WD/CCIP
        n517 = ip.mk_number(self.ctx, '33', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/CCIP'] = n517
        # A7E_requirements/WD/HUDdown1
        n518 = ip.mk_number(self.ctx, '34', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown1'] = n518
        # A7E_requirements/WD/HUDdown2
        n519 = ip.mk_number(self.ctx, '35', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown2'] = n519
        # A7E_requirements/WD/AG_Guns
        n520 = ip.mk_number(self.ctx, '36', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AG_Guns'] = n520
        # A7E_requirements/WD/AA_Guns
        n521 = ip.mk_number(self.ctx, '37', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Guns'] = n521
        # A7E_requirements/WD/Manrip
        n522 = ip.mk_number(self.ctx, '38', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Manrip'] = n522
        # A7E_requirements/WD/AA_Manrip
        n523 = ip.mk_number(self.ctx, '39', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Manrip'] = n523
        # A7E_requirements/WD/Snattack
        n524 = ip.mk_number(self.ctx, '40', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snattack'] = n524
        # A7E_requirements/WD/Snoffset
        n525 = ip.mk_number(self.ctx, '41', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snoffset'] = n525
        # A7E_requirements/WD/SBOC
        n526 = ip.mk_number(self.ctx, '42', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOC'] = n526
        # A7E_requirements/WD/SBOCFlyto0
        n527 = ip.mk_number(self.ctx, '43', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCFlyto0'] = n527
        # A7E_requirements/WD/SBOCoffset
        n528 = ip.mk_number(self.ctx, '44', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCoffset'] = n528
        # A7E_requirements/WD/Walleye
        n529 = ip.mk_number(self.ctx, '45', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Walleye'] = n529
        # Bus Creator2
        n530 = [n504, n506, n508, n512, n513, n514, n515, n516, n517, n518, n519, n520, n521, n522, n523, n524, n525, n526, n527, n528, n529]
        n531_1 = ip.scr.mk_scr(self.ctx, 'WD', n510, n511, n530, n505)
        # A7E_requirements/WD/Mode
        n532 = ip.mk_ite(self.ctx, n472, n504, n531_1)
        self.nets['A7E_requirements/WD/Mode'] = n532
        in472 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n472, in472, n503)
        in473 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n473, in473, n445)
        in474 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n474, in474, n446)
        in475 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n475, in475, n455)
        in476 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n476, in476, n456)
        in477 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n477, in477, n457)
        in478 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n478, in478, n458)
        in479 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n479, in479, n459)
        in480 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n480, in480, n460)
        in481 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n481, in481, n461)
        in482 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n482, in482, n462)
        in483 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n483, in483, n463)
        in484 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n484, in484, n464)
        in485 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n485, in485, n452)
        in486 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n486, in486, n451)
        in487 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n487, in487, n454)
        in488 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n488, in488, n453)
        in489 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n489, in489, n448)
        in490 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n490, in490, n447)
        in491 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n491, in491, n450)
        in492 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n492, in492, n449)
        in493 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n493, in493, n532)
        in494 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n494, in494, n465)
        in495 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n495, in495, n466)
        in496 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n496, in496, n467)
        in497 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n497, in497, n468)
        in498 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n498, in498, n469)
        in499 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n499, in499, n470)
        in500 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n500, in500, n471)
        in501 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n501, in501, n507)
        in502 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n502, in502, n509)
        # n532 -> WD
        return n532


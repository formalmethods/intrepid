import intrepid as ip
import intrepid.scr
import intrepid.circuit
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
        # StationSelected -> n23
        n23 = inputs[input_keys[22]]
        # UPDATTW -> n24
        n24 = inputs[input_keys[23]]
        # MODEROT -> n25
        n25 = inputs[input_keys[24]]
        # PRESPOS -> n26
        n26 = inputs[input_keys[25]]
        # GUNNSEL -> n27
        n27 = inputs[input_keys[26]]
        # WDNFS -> n28
        n28 = inputs[input_keys[27]]
        # MSFW -> n29
        n29 = inputs[input_keys[28]]
        # NonZeroDigitEntered -> n30
        n30 = inputs[input_keys[29]]
        # ENTERSW -> n31
        n31 = inputs[input_keys[30]]
        # FLYTOchanged -> n32
        n32 = inputs[input_keys[31]]
        # ReadyStation -> n33
        n33 = inputs[input_keys[32]]
        # HUREL -> n34
        n34 = inputs[input_keys[33]]
        # ReservedWeapon -> n35
        n35 = inputs[input_keys[34]]
        # Special -> n36
        n36 = inputs[input_keys[35]]
        # Rockets -> n37
        n37 = inputs[input_keys[36]]
        # Guns -> n38
        n38 = inputs[input_keys[37]]
        # OnWalleye -> n39
        n39 = inputs[input_keys[38]]
        # Shrike -> n40
        n40 = inputs[input_keys[39]]
        # OtherWeapon -> n41
        n41 = inputs[input_keys[40]]
        # Redesignate -> n42
        n42 = inputs[input_keys[41]]
        # AnyDestEntered -> n43
        n43 = inputs[input_keys[42]]
        # HighDrag -> n44
        n44 = inputs[input_keys[43]]
        # LowDrag -> n45
        n45 = inputs[input_keys[44]]
        # OverflownExit -> n46
        n46 = inputs[input_keys[45]]
        # Overflown>42 -> n47
        n47 = inputs[input_keys[46]]
        # FLYTOTOG=Dest -> n48
        n48 = inputs[input_keys[47]]
        # FLYTOTW -> n49
        n49 = inputs[input_keys[48]]
        # A7E_requirements/Constant
        n50 = ip.mk_number(self.ctx, '70.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant'] = n50
        # A7E_requirements/Relational Operator -> n51
        n51 = ip.mk_gt(self.ctx, n12, n50)
        self.nets['A7E_requirements/Relational Operator'] = n51
        # A7E_requirements/Constant1
        n52 = ip.mk_number(self.ctx, '80.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant1'] = n52
        # A7E_requirements/Relational Operator1 -> n53
        n53 = ip.mk_gt(self.ctx, n12, n52)
        self.nets['A7E_requirements/Relational Operator1'] = n53
        # A7E_requirements/Gndal
        n54 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Gndal'] = n54
        # A7E_requirements/ro -> n55
        n55 = ip.mk_eq(self.ctx, n15, n54)
        self.nets['A7E_requirements/ro'] = n55
        # A7E_requirements/Norm
        n56 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Norm'] = n56
        # A7E_requirements/ro1 -> n57
        n57 = ip.mk_eq(self.ctx, n15, n56)
        self.nets['A7E_requirements/ro1'] = n57
        # A7E_requirements/Iner
        n58 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Iner'] = n58
        # A7E_requirements/ro2 -> n59
        n59 = ip.mk_eq(self.ctx, n15, n58)
        self.nets['A7E_requirements/ro2'] = n59
        # A7E_requirements/MagSl
        n60 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/MagSl'] = n60
        # A7E_requirements/ro3 -> n61
        n61 = ip.mk_eq(self.ctx, n15, n60)
        self.nets['A7E_requirements/ro3'] = n61
        # A7E_requirements/Grid
        n62 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Grid'] = n62
        # A7E_requirements/ro4 -> n63
        n63 = ip.mk_eq(self.ctx, n15, n62)
        self.nets['A7E_requirements/ro4'] = n63
        n64_1 = self.ANT(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n51, n53, n13, n14, n55, n57, n59, n61, n63, n16, n17, n18, n19, n20, n21, n22)
        # A7E_requirements/FLYOVER
        n66 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/FLYOVER'] = n66
        # A7E_requirements/ro5 -> n67
        n67 = ip.mk_eq(self.ctx, n24, n66)
        self.nets['A7E_requirements/ro5'] = n67
        # A7E_requirements/HUD
        n68 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/HUD'] = n68
        # A7E_requirements/ro6 -> n69
        n69 = ip.mk_eq(self.ctx, n24, n68)
        self.nets['A7E_requirements/ro6'] = n69
        # A7E_requirements/RADAR
        n70 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/RADAR'] = n70
        # A7E_requirements/ro7 -> n71
        n71 = ip.mk_eq(self.ctx, n24, n70)
        self.nets['A7E_requirements/ro7'] = n71
        # A7E_requirements/TACLL
        n72 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TACLL'] = n72
        # A7E_requirements/ro8 -> n73
        n73 = ip.mk_eq(self.ctx, n24, n72)
        self.nets['A7E_requirements/ro8'] = n73
        # A7E_requirements/Other
        n74 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Other'] = n74
        # A7E_requirements/ro9 -> n75
        n75 = ip.mk_eq(self.ctx, n24, n74)
        self.nets['A7E_requirements/ro9'] = n75
        # A7E_requirements/BOC
        n76 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC'] = n76
        # A7E_requirements/not1 -> n77
        n77 = ip.mk_not(self.ctx, n27)
        self.nets['A7E_requirements/not1'] = n77
        # A7E_requirements/zero
        n78 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/zero'] = n78
        # A7E_requirements/ro17 -> n79
        n79 = ip.mk_eq(self.ctx, n49, n78)
        self.nets['A7E_requirements/ro17'] = n79
        # A7E_requirements/reset
        n80 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/reset'] = n80
        # A7E_requirements/ro18 -> n81
        n81 = ip.mk_eq(self.ctx, n49, n80)
        self.nets['A7E_requirements/ro18'] = n81
        # A7E_requirements/BOC_
        n82 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC_'] = n82
        # A7E_requirements/ro12 -> n83
        n83 = ip.mk_eq(self.ctx, n29, n82)
        self.nets['A7E_requirements/ro12'] = n83
        # A7E_requirements/BOCOFF
        n84 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOCOFF'] = n84
        # A7E_requirements/ro13 -> n85
        n85 = ip.mk_eq(self.ctx, n29, n84)
        self.nets['A7E_requirements/ro13'] = n85
        # A7E_requirements/CCIP
        n86 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/CCIP'] = n86
        # A7E_requirements/ro14 -> n87
        n87 = ip.mk_eq(self.ctx, n29, n86)
        self.nets['A7E_requirements/ro14'] = n87
        # A7E_requirements/NATT
        n88 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATT'] = n88
        # A7E_requirements/ro15 -> n89
        n89 = ip.mk_eq(self.ctx, n29, n88)
        self.nets['A7E_requirements/ro15'] = n89
        # A7E_requirements/NATOFF
        n90 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATOFF'] = n90
        # A7E_requirements/ro16 -> n91
        n91 = ip.mk_eq(self.ctx, n29, n90)
        self.nets['A7E_requirements/ro16'] = n91
        n92_1 = self.WD(n33, n34, n35, n36, n37, n38, n39, n40, n41, n77, n79, n81, n48, n28, n83, n85, n87, n89, n91, n4, n42, n43, n44, n45, n46, n47, n2)
        # A7E_requirements/ro19 -> n93
        n93 = ip.mk_eq(self.ctx, n76, n92_1)
        self.nets['A7E_requirements/ro19'] = n93
        # A7E_requirements/None
        n94 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/None'] = n94
        # A7E_requirements/ro10 -> n95
        n95 = ip.mk_eq(self.ctx, n29, n94)
        self.nets['A7E_requirements/ro10'] = n95
        # A7E_requirements/TF
        n96 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TF'] = n96
        # A7E_requirements/ro11 -> n97
        n97 = ip.mk_eq(self.ctx, n29, n96)
        self.nets['A7E_requirements/ro11'] = n97
        n98_1 = self.NU(n23, n2, n25, n26, n67, n69, n71, n73, n75, n27, n28, n5, n93, n95, n97, n30, n31, n32)
        # n64 -> ANT_MODE
        # n98 -> NU_MODE
        # n92 -> WD_MODE
        outputs = collections.OrderedDict()
        outputs['A7E_requirements/ANT_MODE'] = n64_1
        outputs['A7E_requirements/NU_MODE'] = n98_1
        outputs['A7E_requirements/WD_MODE'] = n92_1
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
        # A7E_requirements/StationSelected -> n23
        n23 = ip.mk_input(self.ctx, 'StationSelected', ip.mk_boolean_type(self.ctx))
        self.inputs['StationSelected'] = n23
        # A7E_requirements/UPDATTW -> n24
        n24 = ip.mk_input(self.ctx, 'UPDATTW', ip.mk_int8_type(self.ctx))
        self.inputs['UPDATTW'] = n24
        # A7E_requirements/MODEROT -> n25
        n25 = ip.mk_input(self.ctx, 'MODEROT', ip.mk_boolean_type(self.ctx))
        self.inputs['MODEROT'] = n25
        # A7E_requirements/PRESPOS -> n26
        n26 = ip.mk_input(self.ctx, 'PRESPOS', ip.mk_boolean_type(self.ctx))
        self.inputs['PRESPOS'] = n26
        # A7E_requirements/GUNNSEL -> n27
        n27 = ip.mk_input(self.ctx, 'GUNNSEL', ip.mk_boolean_type(self.ctx))
        self.inputs['GUNNSEL'] = n27
        # A7E_requirements/WDNFS -> n28
        n28 = ip.mk_input(self.ctx, 'WDNFS', ip.mk_boolean_type(self.ctx))
        self.inputs['WDNFS'] = n28
        # A7E_requirements/MSFW -> n29
        n29 = ip.mk_input(self.ctx, 'MSFW', ip.mk_int8_type(self.ctx))
        self.inputs['MSFW'] = n29
        # A7E_requirements/NonZeroDigitEntered -> n30
        n30 = ip.mk_input(self.ctx, 'NonZeroDigitEntered', ip.mk_boolean_type(self.ctx))
        self.inputs['NonZeroDigitEntered'] = n30
        # A7E_requirements/ENTERSW -> n31
        n31 = ip.mk_input(self.ctx, 'ENTERSW', ip.mk_boolean_type(self.ctx))
        self.inputs['ENTERSW'] = n31
        # A7E_requirements/FLYTOchanged -> n32
        n32 = ip.mk_input(self.ctx, 'FLYTOchanged', ip.mk_boolean_type(self.ctx))
        self.inputs['FLYTOchanged'] = n32
        # A7E_requirements/ReadyStation -> n33
        n33 = ip.mk_input(self.ctx, 'ReadyStation', ip.mk_boolean_type(self.ctx))
        self.inputs['ReadyStation'] = n33
        # A7E_requirements/HUREL -> n34
        n34 = ip.mk_input(self.ctx, 'HUREL', ip.mk_boolean_type(self.ctx))
        self.inputs['HUREL'] = n34
        # A7E_requirements/ReservedWeapon -> n35
        n35 = ip.mk_input(self.ctx, 'ReservedWeapon', ip.mk_boolean_type(self.ctx))
        self.inputs['ReservedWeapon'] = n35
        # A7E_requirements/Special -> n36
        n36 = ip.mk_input(self.ctx, 'Special', ip.mk_boolean_type(self.ctx))
        self.inputs['Special'] = n36
        # A7E_requirements/Rockets -> n37
        n37 = ip.mk_input(self.ctx, 'Rockets', ip.mk_boolean_type(self.ctx))
        self.inputs['Rockets'] = n37
        # A7E_requirements/Guns -> n38
        n38 = ip.mk_input(self.ctx, 'Guns', ip.mk_boolean_type(self.ctx))
        self.inputs['Guns'] = n38
        # A7E_requirements/OnWalleye -> n39
        n39 = ip.mk_input(self.ctx, 'OnWalleye', ip.mk_boolean_type(self.ctx))
        self.inputs['OnWalleye'] = n39
        # A7E_requirements/Shrike -> n40
        n40 = ip.mk_input(self.ctx, 'Shrike', ip.mk_boolean_type(self.ctx))
        self.inputs['Shrike'] = n40
        # A7E_requirements/OtherWeapon -> n41
        n41 = ip.mk_input(self.ctx, 'OtherWeapon', ip.mk_boolean_type(self.ctx))
        self.inputs['OtherWeapon'] = n41
        # A7E_requirements/Redesignate -> n42
        n42 = ip.mk_input(self.ctx, 'Redesignate', ip.mk_boolean_type(self.ctx))
        self.inputs['Redesignate'] = n42
        # A7E_requirements/AnyDestEntered -> n43
        n43 = ip.mk_input(self.ctx, 'AnyDestEntered', ip.mk_boolean_type(self.ctx))
        self.inputs['AnyDestEntered'] = n43
        # A7E_requirements/HighDrag -> n44
        n44 = ip.mk_input(self.ctx, 'HighDrag', ip.mk_boolean_type(self.ctx))
        self.inputs['HighDrag'] = n44
        # A7E_requirements/LowDrag -> n45
        n45 = ip.mk_input(self.ctx, 'LowDrag', ip.mk_boolean_type(self.ctx))
        self.inputs['LowDrag'] = n45
        # A7E_requirements/OverflownExit -> n46
        n46 = ip.mk_input(self.ctx, 'OverflownExit', ip.mk_boolean_type(self.ctx))
        self.inputs['OverflownExit'] = n46
        # A7E_requirements/Overflown>42 -> n47
        n47 = ip.mk_input(self.ctx, 'Overflown>42', ip.mk_boolean_type(self.ctx))
        self.inputs['Overflown>42'] = n47
        # A7E_requirements/FLYTOTOG=Dest -> n48
        n48 = ip.mk_input(self.ctx, 'FLYTOTOG=Dest', ip.mk_boolean_type(self.ctx))
        self.inputs['FLYTOTOG=Dest'] = n48
        # A7E_requirements/FLYTOTW -> n49
        n49 = ip.mk_input(self.ctx, 'FLYTOTW', ip.mk_int8_type(self.ctx))
        self.inputs['FLYTOTW'] = n49

    def InitialState(self, n101, n102, n103, n104, n105, n106, n107, n108, n109, n110, n111, n112):
        # IMSup -> n101
        # IMSMODE=Gndal -> n102
        # IMSMODE=Iner -> n103
        # IMSMODE=Norm -> n104
        # IMSMODE=MagSl -> n105
        # IMSMODE=Grid -> n106
        # Data23=Sea -> n107
        # Landaln -> n108
        # OLB -> n109
        # MagSl -> n110
        # Grid -> n111
        # IMSfail -> n112
        # A7E_requirements/ANT/InitialState/not2 -> n113
        n113 = ip.mk_not(self.ctx, n101)
        self.nets['A7E_requirements/ANT/InitialState/not2'] = n113
        # A7E_requirements/ANT/InitialState/and5 -> n114
        n114 = ip.mk_and(self.ctx, n101, n106)
        self.nets['A7E_requirements/ANT/InitialState/and5'] = n114
        # A7E_requirements/ANT/InitialState/and4 -> n115
        n115 = ip.mk_and(self.ctx, n101, n105)
        self.nets['A7E_requirements/ANT/InitialState/and4'] = n115
        # A7E_requirements/ANT/InitialState/and3 -> n116
        n116 = ip.mk_and(self.ctx, n102, n107)
        self.nets['A7E_requirements/ANT/InitialState/and3'] = n116
        # A7E_requirements/ANT/InitialState/or1 -> n117
        tn0 = ip.mk_or(self.ctx, n104, n116)
        n117 = ip.mk_or(self.ctx, n103, tn0)
        self.nets['A7E_requirements/ANT/InitialState/or1'] = n117
        # A7E_requirements/ANT/InitialState/and2 -> n118
        n118 = ip.mk_and(self.ctx, n101, n117)
        self.nets['A7E_requirements/ANT/InitialState/and2'] = n118
        # A7E_requirements/ANT/InitialState/not1 -> n119
        n119 = ip.mk_not(self.ctx, n107)
        self.nets['A7E_requirements/ANT/InitialState/not1'] = n119
        # A7E_requirements/ANT/InitialState/and1 -> n120
        tn1 = ip.mk_and(self.ctx, n102, n119)
        n120 = ip.mk_and(self.ctx, n101, tn1)
        self.nets['A7E_requirements/ANT/InitialState/and1'] = n120
        # A7E_requirements/ANT/InitialState/Error
        n121 = ip.mk_number(self.ctx, '255', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/InitialState/Error'] = n121
        # A7E_requirements/ANT/InitialState/Switch
        n122 = ip.mk_ite(self.ctx, n120, n108, n121)
        self.nets['A7E_requirements/ANT/InitialState/Switch'] = n122
        # A7E_requirements/ANT/InitialState/Switch1
        n123 = ip.mk_ite(self.ctx, n118, n109, n122)
        self.nets['A7E_requirements/ANT/InitialState/Switch1'] = n123
        # A7E_requirements/ANT/InitialState/Switch2
        n124 = ip.mk_ite(self.ctx, n115, n110, n123)
        self.nets['A7E_requirements/ANT/InitialState/Switch2'] = n124
        # A7E_requirements/ANT/InitialState/Switch3
        n125 = ip.mk_ite(self.ctx, n114, n111, n124)
        self.nets['A7E_requirements/ANT/InitialState/Switch3'] = n125
        # A7E_requirements/ANT/InitialState/Switch4
        n126 = ip.mk_ite(self.ctx, n113, n112, n125)
        self.nets['A7E_requirements/ANT/InitialState/Switch4'] = n126
        # n126 -> InitialState
        return n126

    def ANT(self, n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150, n151, n152, n153, n154):
        # presentPositionEntered -> n128
        # ACAIRB=Yes -> n129
        # IMSAUTOC=On -> n130
        # Desig -> n131
        # Data23=Sea -> n132
        # CAstageComplete -> n133
        # CLstageComplete -> n134
        # NDstageComplete -> n135
        # HSstageComplete -> n136
        # PNLTEST=TEST -> n137
        # IMSup -> n138
        # latitude>70 -> n139
        # latitude>80 -> n140
        # DopplerUp -> n141
        # DopplerCoupled -> n142
        # IMSMODE=Gndal -> n143
        # IMSMODE=Norm -> n144
        # IMSMODE=Iner -> n145
        # IMSMODE=MagSl -> n146
        # IMSMODE=Grid -> n147
        # AirVelocityTestPassed -> n148
        # PitchSmall AND RollSmall -> n149
        # SINSup -> n150
        # SINSvelocityTestPassed -> n151
        # LandVelocityTestPassed -> n152
        # NoInterveningTakeoff -> n153
        # GroundTestFinished -> n154
        n155 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Init', ip.mk_boolean_type(self.ctx))
        n156 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past', ip.mk_boolean_type(self.ctx))
        n157 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past1', ip.mk_boolean_type(self.ctx))
        n158 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past10', ip.mk_boolean_type(self.ctx))
        n159 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past11', ip.mk_boolean_type(self.ctx))
        n160 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past12', ip.mk_boolean_type(self.ctx))
        n161 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past13', ip.mk_boolean_type(self.ctx))
        n162 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past14', ip.mk_boolean_type(self.ctx))
        n163 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past15', ip.mk_boolean_type(self.ctx))
        n164 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past16', ip.mk_boolean_type(self.ctx))
        n165 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past17', ip.mk_boolean_type(self.ctx))
        n166 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past18', ip.mk_boolean_type(self.ctx))
        n167 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past19', ip.mk_boolean_type(self.ctx))
        n168 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past7', ip.mk_boolean_type(self.ctx))
        n169 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past6', ip.mk_boolean_type(self.ctx))
        n170 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past9', ip.mk_boolean_type(self.ctx))
        n171 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past8', ip.mk_boolean_type(self.ctx))
        n172 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past3', ip.mk_boolean_type(self.ctx))
        n173 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past2', ip.mk_boolean_type(self.ctx))
        n174 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past5', ip.mk_boolean_type(self.ctx))
        n175 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past4', ip.mk_boolean_type(self.ctx))
        n176 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past(Mode)', ip.mk_int8_type(self.ctx))
        n177 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past20', ip.mk_boolean_type(self.ctx))
        n178 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past21', ip.mk_boolean_type(self.ctx))
        n179 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past22', ip.mk_boolean_type(self.ctx))
        n180 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past23', ip.mk_boolean_type(self.ctx))
        n181 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past24', ip.mk_boolean_type(self.ctx))
        n182 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past25', ip.mk_boolean_type(self.ctx))
        n183 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past26', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/ANT/false
        n184 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/ANT/false'] = n184
        # A7E_requirements/ANT/Landaln
        n185 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Landaln'] = n185
        # A7E_requirements/ANT/OLB
        n186 = ip.mk_number(self.ctx, '11', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/OLB'] = n186
        # A7E_requirements/ANT/MagSl
        n187 = ip.mk_number(self.ctx, '12', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/MagSl'] = n187
        # A7E_requirements/ANT/Grid
        n188 = ip.mk_number(self.ctx, '13', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grid'] = n188
        # A7E_requirements/ANT/IMSfail
        n189 = ip.mk_number(self.ctx, '14', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/IMSfail'] = n189
        n190_1 = self.InitialState(n138, n143, n145, n144, n146, n147, n132, n185, n186, n187, n188, n189)
        # Bus Creator
        n191 = [n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150, n151, n152, n153, n154]
        # Bus Creator1
        n192 = [n156, n157, n173, n172, n175, n174, n169, n168, n171, n170, n158, n159, n160, n161, n162, n163, n164, n165, n166, n167, n177, n178, n179, n180, n181, n182, n183]
        # A7E_requirements/ANT/Lautocal
        n193 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Lautocal'] = n193
        # A7E_requirements/ANT/Sautocal
        n194 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Sautocal'] = n194
        # A7E_requirements/ANT/SINSaln
        n195 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/SINSaln'] = n195
        # A7E_requirements/ANT/01Update
        n196 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/01Update'] = n196
        # A7E_requirements/ANT/HUDaln
        n197 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/HUDaln'] = n197
        # A7E_requirements/ANT/Airaln
        n198 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Airaln'] = n198
        # A7E_requirements/ANT/DIG
        n199 = ip.mk_number(self.ctx, '7', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DIG'] = n199
        # A7E_requirements/ANT/DI
        n200 = ip.mk_number(self.ctx, '8', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DI'] = n200
        # A7E_requirements/ANT/I
        n201 = ip.mk_number(self.ctx, '9', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/I'] = n201
        # A7E_requirements/ANT/UDI
        n202 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/UDI'] = n202
        # A7E_requirements/ANT/PolarDI
        n203 = ip.mk_number(self.ctx, '15', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarDI'] = n203
        # A7E_requirements/ANT/PolarI
        n204 = ip.mk_number(self.ctx, '16', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarI'] = n204
        # A7E_requirements/ANT/Grtest
        n205 = ip.mk_number(self.ctx, '17', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grtest'] = n205
        # Bus Creator2
        n206 = [n193, n194, n185, n195, n196, n197, n198, n199, n200, n201, n202, n186, n187, n188, n189, n203, n204, n205]
        # A7E_requirements/ANT/Mode1
        n207 = ip.mk_ite(self.ctx, n155, n190_1, n176)
        self.nets['A7E_requirements/ANT/Mode1'] = n207
        n208_1 = ip.scr.mk_scr(self.ctx, 'ANT', n191, n192, n206, n207)
        # A7E_requirements/ANT/Mode
        n209 = ip.mk_ite(self.ctx, n155, n190_1, n208_1)
        self.nets['A7E_requirements/ANT/Mode'] = n209
        in155 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n155, in155, n184)
        in156 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n156, in156, n128)
        in157 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n157, in157, n129)
        in158 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n158, in158, n138)
        in159 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n159, in159, n139)
        in160 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n160, in160, n140)
        in161 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n161, in161, n141)
        in162 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n162, in162, n142)
        in163 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n163, in163, n143)
        in164 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n164, in164, n144)
        in165 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n165, in165, n145)
        in166 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n166, in166, n146)
        in167 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n167, in167, n147)
        in168 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n168, in168, n135)
        in169 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n169, in169, n134)
        in170 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n170, in170, n137)
        in171 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n171, in171, n136)
        in172 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n172, in172, n131)
        in173 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n173, in173, n130)
        in174 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n174, in174, n133)
        in175 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n175, in175, n132)
        in176 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n176, in176, n209)
        in177 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n177, in177, n148)
        in178 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n178, in178, n149)
        in179 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n179, in179, n150)
        in180 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n180, in180, n151)
        in181 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n181, in181, n152)
        in182 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n182, in182, n153)
        in183 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n183, in183, n154)
        # n209 -> ANT
        return n209

    def NU(self, n211, n212, n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223, n224, n225, n226, n227, n228):
        # StationSelected -> n211
        # ACAIRB=Yes -> n212
        # MODEROT=PRESPOS -> n213
        # PRESPOS=UPDATE -> n214
        # UPDATTW=FLYOVER -> n215
        # UPDATTW=HUD -> n216
        # UPDATTW=RADAR -> n217
        # UPDATTW=TACLL -> n218
        # UPDATTW=Other -> n219
        # GUNNSEL=Yes -> n220
        # WDMFS -> n221
        # Data23=Sea -> n222
        # WeaponMode=BOC -> n223
        # MSFW=None -> n224
        # MSFW=TF -> n225
        # NonZeroDigitEntered -> n226
        # ENTERSW=On -> n227
        # FLYTOchanged -> n228
        n229 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Init', ip.mk_boolean_type(self.ctx))
        n230 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past', ip.mk_boolean_type(self.ctx))
        n231 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past1', ip.mk_boolean_type(self.ctx))
        n232 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past10', ip.mk_boolean_type(self.ctx))
        n233 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past11', ip.mk_boolean_type(self.ctx))
        n234 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past12', ip.mk_boolean_type(self.ctx))
        n235 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past13', ip.mk_boolean_type(self.ctx))
        n236 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past14', ip.mk_boolean_type(self.ctx))
        n237 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past15', ip.mk_boolean_type(self.ctx))
        n238 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past16', ip.mk_boolean_type(self.ctx))
        n239 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past17', ip.mk_boolean_type(self.ctx))
        n240 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past7', ip.mk_boolean_type(self.ctx))
        n241 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past6', ip.mk_boolean_type(self.ctx))
        n242 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past9', ip.mk_boolean_type(self.ctx))
        n243 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past8', ip.mk_boolean_type(self.ctx))
        n244 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past3', ip.mk_boolean_type(self.ctx))
        n245 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past2', ip.mk_boolean_type(self.ctx))
        n246 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past5', ip.mk_boolean_type(self.ctx))
        n247 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past4', ip.mk_boolean_type(self.ctx))
        n248 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past(Mode)', ip.mk_int8_type(self.ctx))
        # A7E_requirements/NU/false
        n249 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/NU/false'] = n249
        # A7E_requirements/NU/UNone
        n250 = ip.mk_number(self.ctx, '18', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/UNone'] = n250
        # Bus Creator
        n251 = [n211, n212, n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223, n224, n225, n226, n227, n228]
        # Bus Creator1
        n252 = [n230, n231, n245, n244, n247, n246, n241, n240, n243, n242, n232, n233, n234, n235, n236, n237, n238, n239]
        # A7E_requirements/NU/HUDUpd
        n253 = ip.mk_number(self.ctx, '19', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/HUDUpd'] = n253
        # A7E_requirements/NU/RadarUpd
        n254 = ip.mk_number(self.ctx, '20', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/RadarUpd'] = n254
        # A7E_requirements/NU/FlyUpd
        n255 = ip.mk_number(self.ctx, '21', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/FlyUpd'] = n255
        # A7E_requirements/NU/AflyUpd
        n256 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/AflyUpd'] = n256
        # A7E_requirements/NU/MapUpd
        n257 = ip.mk_number(self.ctx, '23', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/MapUpd'] = n257
        # A7E_requirements/NU/TacUpd
        n258 = ip.mk_number(self.ctx, '24', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/TacUpd'] = n258
        # Bus Creator2
        n259 = [n250, n253, n254, n255, n256, n257, n258]
        # A7E_requirements/NU/Mode1
        n260 = ip.mk_ite(self.ctx, n229, n250, n248)
        self.nets['A7E_requirements/NU/Mode1'] = n260
        n261_1 = ip.scr.mk_scr(self.ctx, 'NU', n251, n252, n259, n260)
        # A7E_requirements/NU/Mode
        n262 = ip.mk_ite(self.ctx, n229, n250, n261_1)
        self.nets['A7E_requirements/NU/Mode'] = n262
        in229 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n229, in229, n249)
        in230 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n230, in230, n211)
        in231 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n231, in231, n212)
        in232 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n232, in232, n221)
        in233 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n233, in233, n222)
        in234 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n234, in234, n223)
        in235 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n235, in235, n224)
        in236 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n236, in236, n225)
        in237 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n237, in237, n226)
        in238 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n238, in238, n227)
        in239 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n239, in239, n228)
        in240 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n240, in240, n218)
        in241 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n241, in241, n217)
        in242 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n242, in242, n220)
        in243 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n243, in243, n219)
        in244 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n244, in244, n214)
        in245 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n245, in245, n213)
        in246 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n246, in246, n216)
        in247 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n247, in247, n215)
        in248 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n248, in248, n262)
        # n262 -> NU
        return n262

    def WD(self, n264, n265, n266, n267, n268, n269, n270, n271, n272, n273, n274, n275, n276, n277, n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289, n290):
        # ReadyStation -> n264
        # HUREL=Yes -> n265
        # ReservedWeapon -> n266
        # Special -> n267
        # Rockets -> n268
        # Guns -> n269
        # OnWalleye -> n270
        # Shrike -> n271
        # OtherWeapon -> n272
        # GUNSSEL=No -> n273
        # FLYTOTW=0 -> n274
        # FLYTOTW=reset -> n275
        # FLYTOTOG=Dest -> n276
        # WDMFS -> n277
        # MFSW=BOC -> n278
        # MFSW=BOCOFF -> n279
        # MFSW=CCIP -> n280
        # MFSW=NATT -> n281
        # MFSW=NATOFF -> n282
        # Desig -> n283
        # Redesignate -> n284
        # AnyDestEntered -> n285
        # HighDrag -> n286
        # LowDrag -> n287
        # OverflownExit -> n288
        # Overflown>42 -> n289
        # ACAIRB=Yes -> n290
        n291 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Init', ip.mk_boolean_type(self.ctx))
        n292 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past', ip.mk_boolean_type(self.ctx))
        n293 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past1', ip.mk_boolean_type(self.ctx))
        n294 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past10', ip.mk_boolean_type(self.ctx))
        n295 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past11', ip.mk_boolean_type(self.ctx))
        n296 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past12', ip.mk_boolean_type(self.ctx))
        n297 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past13', ip.mk_boolean_type(self.ctx))
        n298 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past14', ip.mk_boolean_type(self.ctx))
        n299 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past15', ip.mk_boolean_type(self.ctx))
        n300 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past16', ip.mk_boolean_type(self.ctx))
        n301 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past17', ip.mk_boolean_type(self.ctx))
        n302 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past18', ip.mk_boolean_type(self.ctx))
        n303 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past19', ip.mk_boolean_type(self.ctx))
        n304 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past7', ip.mk_boolean_type(self.ctx))
        n305 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past6', ip.mk_boolean_type(self.ctx))
        n306 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past9', ip.mk_boolean_type(self.ctx))
        n307 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past8', ip.mk_boolean_type(self.ctx))
        n308 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past3', ip.mk_boolean_type(self.ctx))
        n309 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past2', ip.mk_boolean_type(self.ctx))
        n310 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past5', ip.mk_boolean_type(self.ctx))
        n311 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past4', ip.mk_boolean_type(self.ctx))
        n312 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past(Mode)', ip.mk_int8_type(self.ctx))
        n313 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past20', ip.mk_boolean_type(self.ctx))
        n314 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past21', ip.mk_boolean_type(self.ctx))
        n315 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past22', ip.mk_boolean_type(self.ctx))
        n316 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past23', ip.mk_boolean_type(self.ctx))
        n317 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past24', ip.mk_boolean_type(self.ctx))
        n318 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past25', ip.mk_boolean_type(self.ctx))
        n319 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past26', ip.mk_boolean_type(self.ctx))
        n320 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past27', ip.mk_boolean_type(self.ctx))
        n321 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past28', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/WD/false
        n322 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/WD/false'] = n322
        # A7E_requirements/WD/WNone
        n323 = ip.mk_number(self.ctx, '25', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WNone'] = n323
        # A7E_requirements/WD/Mode1
        n324 = ip.mk_ite(self.ctx, n291, n323, n312)
        self.nets['A7E_requirements/WD/Mode1'] = n324
        # A7E_requirements/WD/OFF_MFS
        n325 = ip.mk_number(self.ctx, '26', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/OFF_MFS'] = n325
        # A7E_requirements/WD/Past(In OFF_MFSW) -> n326
        n326 = ip.mk_eq(self.ctx, n324, n325)
        self.nets['A7E_requirements/WD/Past(In OFF_MFSW)'] = n326
        # A7E_requirements/WD/WD_MFS
        n327 = ip.mk_number(self.ctx, '27', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WD_MFS'] = n327
        # A7E_requirements/WD/Past(In WD_MFSW) -> n328
        n328 = ip.mk_eq(self.ctx, n324, n327)
        self.nets['A7E_requirements/WD/Past(In WD_MFSW)'] = n328
        # Bus Creator
        n329 = [n264, n265, n266, n267, n268, n269, n270, n271, n272, n273, n274, n275, n276, n277, n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289, n290, n326, n328]
        # Bus Creator1
        n330 = [n292, n293, n309, n308, n311, n310, n305, n304, n307, n306, n294, n295, n296, n297, n298, n299, n300, n301, n302, n303, n313, n314, n315, n316, n317, n318, n319, n320, n321]
        # A7E_requirements/WD/Nattack
        n331 = ip.mk_number(self.ctx, '28', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Nattack'] = n331
        # A7E_requirements/WD/Noffset
        n332 = ip.mk_number(self.ctx, '29', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Noffset'] = n332
        # A7E_requirements/WD/BOC
        n333 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOC'] = n333
        # A7E_requirements/WD/BOCFlyto0
        n334 = ip.mk_number(self.ctx, '31', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCFlyto0'] = n334
        # A7E_requirements/WD/BOCoffset
        n335 = ip.mk_number(self.ctx, '32', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCoffset'] = n335
        # A7E_requirements/WD/CCIP
        n336 = ip.mk_number(self.ctx, '33', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/CCIP'] = n336
        # A7E_requirements/WD/HUDdown1
        n337 = ip.mk_number(self.ctx, '34', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown1'] = n337
        # A7E_requirements/WD/HUDdown2
        n338 = ip.mk_number(self.ctx, '35', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown2'] = n338
        # A7E_requirements/WD/AG_Guns
        n339 = ip.mk_number(self.ctx, '36', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AG_Guns'] = n339
        # A7E_requirements/WD/AA_Guns
        n340 = ip.mk_number(self.ctx, '37', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Guns'] = n340
        # A7E_requirements/WD/Manrip
        n341 = ip.mk_number(self.ctx, '38', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Manrip'] = n341
        # A7E_requirements/WD/AA_Manrip
        n342 = ip.mk_number(self.ctx, '39', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Manrip'] = n342
        # A7E_requirements/WD/Snattack
        n343 = ip.mk_number(self.ctx, '40', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snattack'] = n343
        # A7E_requirements/WD/Snoffset
        n344 = ip.mk_number(self.ctx, '41', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snoffset'] = n344
        # A7E_requirements/WD/SBOC
        n345 = ip.mk_number(self.ctx, '42', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOC'] = n345
        # A7E_requirements/WD/SBOCFlyto0
        n346 = ip.mk_number(self.ctx, '43', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCFlyto0'] = n346
        # A7E_requirements/WD/SBOCoffset
        n347 = ip.mk_number(self.ctx, '44', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCoffset'] = n347
        # A7E_requirements/WD/Walleye
        n348 = ip.mk_number(self.ctx, '45', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Walleye'] = n348
        # Bus Creator2
        n349 = [n323, n325, n327, n331, n332, n333, n334, n335, n336, n337, n338, n339, n340, n341, n342, n343, n344, n345, n346, n347, n348]
        n350_1 = ip.scr.mk_scr(self.ctx, 'WD', n329, n330, n349, n324)
        # A7E_requirements/WD/Mode
        n351 = ip.mk_ite(self.ctx, n291, n323, n350_1)
        self.nets['A7E_requirements/WD/Mode'] = n351
        in291 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n291, in291, n322)
        in292 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n292, in292, n264)
        in293 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n293, in293, n265)
        in294 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n294, in294, n274)
        in295 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n295, in295, n275)
        in296 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n296, in296, n276)
        in297 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n297, in297, n277)
        in298 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n298, in298, n278)
        in299 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n299, in299, n279)
        in300 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n300, in300, n280)
        in301 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n301, in301, n281)
        in302 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n302, in302, n282)
        in303 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n303, in303, n283)
        in304 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n304, in304, n271)
        in305 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n305, in305, n270)
        in306 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n306, in306, n273)
        in307 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n307, in307, n272)
        in308 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n308, in308, n267)
        in309 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n309, in309, n266)
        in310 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n310, in310, n269)
        in311 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n311, in311, n268)
        in312 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n312, in312, n351)
        in313 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n313, in313, n284)
        in314 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n314, in314, n285)
        in315 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n315, in315, n286)
        in316 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n316, in316, n287)
        in317 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n317, in317, n288)
        in318 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n318, in318, n289)
        in319 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n319, in319, n290)
        in320 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n320, in320, n326)
        in321 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n321, in321, n328)
        # n351 -> WD
        return n351


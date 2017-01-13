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
        # WEAPTYPE -> n50
        n50 = inputs[input_keys[49]]
        # A7E_requirements/Constant
        n51 = ip.mk_number(self.ctx, '70.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant'] = n51
        # A7E_requirements/Relational Operator -> n52
        n52 = ip.mk_gt(self.ctx, n12, n51)
        self.nets['A7E_requirements/Relational Operator'] = n52
        # A7E_requirements/Constant1
        n53 = ip.mk_number(self.ctx, '80.0', ip.mk_real_type(self.ctx))
        self.nets['A7E_requirements/Constant1'] = n53
        # A7E_requirements/Relational Operator1 -> n54
        n54 = ip.mk_gt(self.ctx, n12, n53)
        self.nets['A7E_requirements/Relational Operator1'] = n54
        # A7E_requirements/Gndal
        n55 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Gndal'] = n55
        # A7E_requirements/ro -> n56
        n56 = ip.mk_eq(self.ctx, n15, n55)
        self.nets['A7E_requirements/ro'] = n56
        # A7E_requirements/Norm
        n57 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Norm'] = n57
        # A7E_requirements/ro1 -> n58
        n58 = ip.mk_eq(self.ctx, n15, n57)
        self.nets['A7E_requirements/ro1'] = n58
        # A7E_requirements/Iner
        n59 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Iner'] = n59
        # A7E_requirements/ro2 -> n60
        n60 = ip.mk_eq(self.ctx, n15, n59)
        self.nets['A7E_requirements/ro2'] = n60
        # A7E_requirements/MagSl
        n61 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/MagSl'] = n61
        # A7E_requirements/ro3 -> n62
        n62 = ip.mk_eq(self.ctx, n15, n61)
        self.nets['A7E_requirements/ro3'] = n62
        # A7E_requirements/Grid
        n63 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Grid'] = n63
        # A7E_requirements/ro4 -> n64
        n64 = ip.mk_eq(self.ctx, n15, n63)
        self.nets['A7E_requirements/ro4'] = n64
        n65_1 = self.ANT(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n52, n54, n13, n14, n56, n58, n60, n62, n64, n16, n17, n18, n19, n20, n21, n22)
        # A7E_requirements/FLYOVER
        n67 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/FLYOVER'] = n67
        # A7E_requirements/ro5 -> n68
        n68 = ip.mk_eq(self.ctx, n24, n67)
        self.nets['A7E_requirements/ro5'] = n68
        # A7E_requirements/HUD
        n69 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/HUD'] = n69
        # A7E_requirements/ro6 -> n70
        n70 = ip.mk_eq(self.ctx, n24, n69)
        self.nets['A7E_requirements/ro6'] = n70
        # A7E_requirements/RADAR
        n71 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/RADAR'] = n71
        # A7E_requirements/ro7 -> n72
        n72 = ip.mk_eq(self.ctx, n24, n71)
        self.nets['A7E_requirements/ro7'] = n72
        # A7E_requirements/TACLL
        n73 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TACLL'] = n73
        # A7E_requirements/ro8 -> n74
        n74 = ip.mk_eq(self.ctx, n24, n73)
        self.nets['A7E_requirements/ro8'] = n74
        # A7E_requirements/Other
        n75 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/Other'] = n75
        # A7E_requirements/ro9 -> n76
        n76 = ip.mk_eq(self.ctx, n24, n75)
        self.nets['A7E_requirements/ro9'] = n76
        # A7E_requirements/BOC
        n77 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC'] = n77
        # A7E_requirements/not1 -> n78
        n78 = ip.mk_not(self.ctx, n27)
        self.nets['A7E_requirements/not1'] = n78
        # A7E_requirements/zero
        n79 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/zero'] = n79
        # A7E_requirements/ro17 -> n80
        n80 = ip.mk_eq(self.ctx, n49, n79)
        self.nets['A7E_requirements/ro17'] = n80
        # A7E_requirements/reset
        n81 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/reset'] = n81
        # A7E_requirements/ro18 -> n82
        n82 = ip.mk_eq(self.ctx, n49, n81)
        self.nets['A7E_requirements/ro18'] = n82
        # A7E_requirements/BOC_
        n83 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOC_'] = n83
        # A7E_requirements/ro12 -> n84
        n84 = ip.mk_eq(self.ctx, n29, n83)
        self.nets['A7E_requirements/ro12'] = n84
        # A7E_requirements/BOCOFF
        n85 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/BOCOFF'] = n85
        # A7E_requirements/ro13 -> n86
        n86 = ip.mk_eq(self.ctx, n29, n85)
        self.nets['A7E_requirements/ro13'] = n86
        # A7E_requirements/CCIP
        n87 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/CCIP'] = n87
        # A7E_requirements/ro14 -> n88
        n88 = ip.mk_eq(self.ctx, n29, n87)
        self.nets['A7E_requirements/ro14'] = n88
        # A7E_requirements/NATT
        n89 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATT'] = n89
        # A7E_requirements/ro15 -> n90
        n90 = ip.mk_eq(self.ctx, n29, n89)
        self.nets['A7E_requirements/ro15'] = n90
        # A7E_requirements/NATOFF
        n91 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NATOFF'] = n91
        # A7E_requirements/ro16 -> n92
        n92 = ip.mk_eq(self.ctx, n29, n91)
        self.nets['A7E_requirements/ro16'] = n92
        n93_1 = self.WD(n33, n34, n35, n36, n37, n38, n39, n40, n41, n78, n80, n82, n48, n28, n84, n86, n88, n90, n92, n4, n42, n43, n44, n45, n46, n47, n2)
        # A7E_requirements/ro19 -> n94
        n94 = ip.mk_eq(self.ctx, n77, n93_1)
        self.nets['A7E_requirements/ro19'] = n94
        # A7E_requirements/None
        n95 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/None'] = n95
        # A7E_requirements/ro10 -> n96
        n96 = ip.mk_eq(self.ctx, n29, n95)
        self.nets['A7E_requirements/ro10'] = n96
        # A7E_requirements/TF
        n97 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/TF'] = n97
        # A7E_requirements/ro11 -> n98
        n98 = ip.mk_eq(self.ctx, n29, n97)
        self.nets['A7E_requirements/ro11'] = n98
        n99_1 = self.NU(n23, n2, n25, n26, n68, n70, n72, n74, n76, n27, n28, n5, n94, n96, n98, n30, n31, n32)
        # n65 -> ANT_MODE
        # n99 -> NU_MODE
        # n93 -> WD_MODE
        outputs = collections.OrderedDict()
        outputs['A7E_requirements/ANT_MODE'] = n65_1
        outputs['A7E_requirements/NU_MODE'] = n99_1
        outputs['A7E_requirements/WD_MODE'] = n93_1
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
        # A7E_requirements/WEAPTYPE -> n50
        n50 = ip.mk_input(self.ctx, 'WEAPTYPE', ip.mk_int8_type(self.ctx))
        self.inputs['WEAPTYPE'] = n50

    def weapon_class(self, n102):
        # WEAPTYPE -> n102
        # A7E_requirements/weapon_class/OR
        n103 = ip.mk_number(self.ctx, '11', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/OR'] = n103
        # A7E_requirements/weapon_class/v54
        n104 = ip.mk_number(self.ctx, '94', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v54'] = n104
        # A7E_requirements/weapon_class/eq52 -> n105
        n105 = ip.mk_eq(self.ctx, n102, n104)
        self.nets['A7E_requirements/weapon_class/eq52'] = n105
        # A7E_requirements/weapon_class/v53
        n106 = ip.mk_number(self.ctx, '99', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v53'] = n106
        # A7E_requirements/weapon_class/eq53 -> n107
        n107 = ip.mk_eq(self.ctx, n102, n106)
        self.nets['A7E_requirements/weapon_class/eq53'] = n107
        # A7E_requirements/weapon_class/Logical Operator9 -> n108
        n108 = ip.mk_or(self.ctx, n105, n107)
        self.nets['A7E_requirements/weapon_class/Logical Operator9'] = n108
        # A7E_requirements/weapon_class/SM
        n109 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/SM'] = n109
        # A7E_requirements/weapon_class/v52
        n110 = ip.mk_number(self.ctx, '59', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v52'] = n110
        # A7E_requirements/weapon_class/eq50 -> n111
        n111 = ip.mk_eq(self.ctx, n102, n110)
        self.nets['A7E_requirements/weapon_class/eq50'] = n111
        # A7E_requirements/weapon_class/v51
        n112 = ip.mk_number(self.ctx, '75', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v51'] = n112
        # A7E_requirements/weapon_class/eq51 -> n113
        n113 = ip.mk_eq(self.ctx, n102, n112)
        self.nets['A7E_requirements/weapon_class/eq51'] = n113
        # A7E_requirements/weapon_class/Logical Operator8 -> n114
        n114 = ip.mk_or(self.ctx, n111, n113)
        self.nets['A7E_requirements/weapon_class/Logical Operator8'] = n114
        # A7E_requirements/weapon_class/OD
        n115 = ip.mk_number(self.ctx, '9', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/OD'] = n115
        # A7E_requirements/weapon_class/v50
        n116 = ip.mk_number(self.ctx, '63', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v50'] = n116
        # A7E_requirements/weapon_class/eq48 -> n117
        n117 = ip.mk_eq(self.ctx, n102, n116)
        self.nets['A7E_requirements/weapon_class/eq48'] = n117
        # A7E_requirements/weapon_class/v49
        n118 = ip.mk_number(self.ctx, '67', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v49'] = n118
        # A7E_requirements/weapon_class/eq49 -> n119
        n119 = ip.mk_eq(self.ctx, n102, n118)
        self.nets['A7E_requirements/weapon_class/eq49'] = n119
        # A7E_requirements/weapon_class/Logical Operator7 -> n120
        n120 = ip.mk_or(self.ctx, n117, n119)
        self.nets['A7E_requirements/weapon_class/Logical Operator7'] = n120
        # A7E_requirements/weapon_class/MD
        n121 = ip.mk_number(self.ctx, '8', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/MD'] = n121
        # A7E_requirements/weapon_class/v46
        n122 = ip.mk_number(self.ctx, '56', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v46'] = n122
        # A7E_requirements/weapon_class/eq44 -> n123
        n123 = ip.mk_eq(self.ctx, n102, n122)
        self.nets['A7E_requirements/weapon_class/eq44'] = n123
        # A7E_requirements/weapon_class/v45
        n124 = ip.mk_number(self.ctx, '62', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v45'] = n124
        # A7E_requirements/weapon_class/eq43 -> n125
        n125 = ip.mk_eq(self.ctx, n102, n124)
        self.nets['A7E_requirements/weapon_class/eq43'] = n125
        # A7E_requirements/weapon_class/v44
        n126 = ip.mk_number(self.ctx, '66', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v44'] = n126
        # A7E_requirements/weapon_class/eq42 -> n127
        n127 = ip.mk_eq(self.ctx, n102, n126)
        self.nets['A7E_requirements/weapon_class/eq42'] = n127
        # A7E_requirements/weapon_class/v43
        n128 = ip.mk_number(self.ctx, '90', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v43'] = n128
        # A7E_requirements/weapon_class/eq41 -> n129
        n129 = ip.mk_eq(self.ctx, n102, n128)
        self.nets['A7E_requirements/weapon_class/eq41'] = n129
        # A7E_requirements/weapon_class/v42
        n130 = ip.mk_number(self.ctx, '91', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v42'] = n130
        # A7E_requirements/weapon_class/eq40 -> n131
        n131 = ip.mk_eq(self.ctx, n102, n130)
        self.nets['A7E_requirements/weapon_class/eq40'] = n131
        # A7E_requirements/weapon_class/v41
        n132 = ip.mk_number(self.ctx, '93', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v41'] = n132
        # A7E_requirements/weapon_class/eq45 -> n133
        n133 = ip.mk_eq(self.ctx, n102, n132)
        self.nets['A7E_requirements/weapon_class/eq45'] = n133
        # A7E_requirements/weapon_class/v47
        n134 = ip.mk_number(self.ctx, '97', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v47'] = n134
        # A7E_requirements/weapon_class/eq46 -> n135
        n135 = ip.mk_eq(self.ctx, n102, n134)
        self.nets['A7E_requirements/weapon_class/eq46'] = n135
        # A7E_requirements/weapon_class/v48
        n136 = ip.mk_number(self.ctx, '98', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v48'] = n136
        # A7E_requirements/weapon_class/eq47 -> n137
        n137 = ip.mk_eq(self.ctx, n102, n136)
        self.nets['A7E_requirements/weapon_class/eq47'] = n137
        # A7E_requirements/weapon_class/Logical Operator6 -> n138
        tn5 = ip.mk_or(self.ctx, n135, n137)
        tn4 = ip.mk_or(self.ctx, n133, tn5)
        tn3 = ip.mk_or(self.ctx, n131, tn4)
        tn2 = ip.mk_or(self.ctx, n129, tn3)
        tn1 = ip.mk_or(self.ctx, n127, tn2)
        tn0 = ip.mk_or(self.ctx, n125, tn1)
        n138 = ip.mk_or(self.ctx, n123, tn0)
        self.nets['A7E_requirements/weapon_class/Logical Operator6'] = n138
        # A7E_requirements/weapon_class/SL
        n139 = ip.mk_number(self.ctx, '7', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/SL'] = n139
        # A7E_requirements/weapon_class/v30
        n140 = ip.mk_number(self.ctx, '50', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v30'] = n140
        # A7E_requirements/weapon_class/eq28 -> n141
        n141 = ip.mk_eq(self.ctx, n102, n140)
        self.nets['A7E_requirements/weapon_class/eq28'] = n141
        # A7E_requirements/weapon_class/v29
        n142 = ip.mk_number(self.ctx, '53', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v29'] = n142
        # A7E_requirements/weapon_class/eq27 -> n143
        n143 = ip.mk_eq(self.ctx, n102, n142)
        self.nets['A7E_requirements/weapon_class/eq27'] = n143
        # A7E_requirements/weapon_class/v28
        n144 = ip.mk_number(self.ctx, '60', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v28'] = n144
        # A7E_requirements/weapon_class/eq26 -> n145
        n145 = ip.mk_eq(self.ctx, n102, n144)
        self.nets['A7E_requirements/weapon_class/eq26'] = n145
        # A7E_requirements/weapon_class/v27
        n146 = ip.mk_number(self.ctx, '61', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v27'] = n146
        # A7E_requirements/weapon_class/eq25 -> n147
        n147 = ip.mk_eq(self.ctx, n102, n146)
        self.nets['A7E_requirements/weapon_class/eq25'] = n147
        # A7E_requirements/weapon_class/v26
        n148 = ip.mk_number(self.ctx, '64', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v26'] = n148
        # A7E_requirements/weapon_class/eq24 -> n149
        n149 = ip.mk_eq(self.ctx, n102, n148)
        self.nets['A7E_requirements/weapon_class/eq24'] = n149
        # A7E_requirements/weapon_class/v25
        n150 = ip.mk_number(self.ctx, '65', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v25'] = n150
        # A7E_requirements/weapon_class/eq29 -> n151
        n151 = ip.mk_eq(self.ctx, n102, n150)
        self.nets['A7E_requirements/weapon_class/eq29'] = n151
        # A7E_requirements/weapon_class/v31
        n152 = ip.mk_number(self.ctx, '68', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v31'] = n152
        # A7E_requirements/weapon_class/eq30 -> n153
        n153 = ip.mk_eq(self.ctx, n102, n152)
        self.nets['A7E_requirements/weapon_class/eq30'] = n153
        # A7E_requirements/weapon_class/v32
        n154 = ip.mk_number(self.ctx, '69', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v32'] = n154
        # A7E_requirements/weapon_class/eq31 -> n155
        n155 = ip.mk_eq(self.ctx, n102, n154)
        self.nets['A7E_requirements/weapon_class/eq31'] = n155
        # A7E_requirements/weapon_class/v33
        n156 = ip.mk_number(self.ctx, '70', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v33'] = n156
        # A7E_requirements/weapon_class/eq32 -> n157
        n157 = ip.mk_eq(self.ctx, n102, n156)
        self.nets['A7E_requirements/weapon_class/eq32'] = n157
        # A7E_requirements/weapon_class/v34
        n158 = ip.mk_number(self.ctx, '72', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v34'] = n158
        # A7E_requirements/weapon_class/eq33 -> n159
        n159 = ip.mk_eq(self.ctx, n102, n158)
        self.nets['A7E_requirements/weapon_class/eq33'] = n159
        # A7E_requirements/weapon_class/v35
        n160 = ip.mk_number(self.ctx, '73', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v35'] = n160
        # A7E_requirements/weapon_class/eq34 -> n161
        n161 = ip.mk_eq(self.ctx, n102, n160)
        self.nets['A7E_requirements/weapon_class/eq34'] = n161
        # A7E_requirements/weapon_class/v36
        n162 = ip.mk_number(self.ctx, '74', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v36'] = n162
        # A7E_requirements/weapon_class/eq35 -> n163
        n163 = ip.mk_eq(self.ctx, n102, n162)
        self.nets['A7E_requirements/weapon_class/eq35'] = n163
        # A7E_requirements/weapon_class/v37
        n164 = ip.mk_number(self.ctx, '77', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v37'] = n164
        # A7E_requirements/weapon_class/eq36 -> n165
        n165 = ip.mk_eq(self.ctx, n102, n164)
        self.nets['A7E_requirements/weapon_class/eq36'] = n165
        # A7E_requirements/weapon_class/v38
        n166 = ip.mk_number(self.ctx, '78', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v38'] = n166
        # A7E_requirements/weapon_class/eq37 -> n167
        n167 = ip.mk_eq(self.ctx, n102, n166)
        self.nets['A7E_requirements/weapon_class/eq37'] = n167
        # A7E_requirements/weapon_class/v39
        n168 = ip.mk_number(self.ctx, '79', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v39'] = n168
        # A7E_requirements/weapon_class/eq38 -> n169
        n169 = ip.mk_eq(self.ctx, n102, n168)
        self.nets['A7E_requirements/weapon_class/eq38'] = n169
        # A7E_requirements/weapon_class/v40
        n170 = ip.mk_number(self.ctx, '95', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v40'] = n170
        # A7E_requirements/weapon_class/eq39 -> n171
        n171 = ip.mk_eq(self.ctx, n102, n170)
        self.nets['A7E_requirements/weapon_class/eq39'] = n171
        # A7E_requirements/weapon_class/Logical Operator5 -> n172
        tn19 = ip.mk_or(self.ctx, n169, n171)
        tn18 = ip.mk_or(self.ctx, n167, tn19)
        tn17 = ip.mk_or(self.ctx, n165, tn18)
        tn16 = ip.mk_or(self.ctx, n163, tn17)
        tn15 = ip.mk_or(self.ctx, n161, tn16)
        tn14 = ip.mk_or(self.ctx, n159, tn15)
        tn13 = ip.mk_or(self.ctx, n157, tn14)
        tn12 = ip.mk_or(self.ctx, n155, tn13)
        tn11 = ip.mk_or(self.ctx, n153, tn12)
        tn10 = ip.mk_or(self.ctx, n151, tn11)
        tn9 = ip.mk_or(self.ctx, n149, tn10)
        tn8 = ip.mk_or(self.ctx, n147, tn9)
        tn7 = ip.mk_or(self.ctx, n145, tn8)
        tn6 = ip.mk_or(self.ctx, n143, tn7)
        n172 = ip.mk_or(self.ctx, n141, tn6)
        self.nets['A7E_requirements/weapon_class/Logical Operator5'] = n172
        # A7E_requirements/weapon_class/SSH
        n173 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/SSH'] = n173
        # A7E_requirements/weapon_class/v23
        n174 = ip.mk_number(self.ctx, '43', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v23'] = n174
        # A7E_requirements/weapon_class/eq22 -> n175
        n175 = ip.mk_eq(self.ctx, n102, n174)
        self.nets['A7E_requirements/weapon_class/eq22'] = n175
        # A7E_requirements/weapon_class/v22
        n176 = ip.mk_number(self.ctx, '45', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v22'] = n176
        # A7E_requirements/weapon_class/eq23 -> n177
        n177 = ip.mk_eq(self.ctx, n102, n176)
        self.nets['A7E_requirements/weapon_class/eq23'] = n177
        # A7E_requirements/weapon_class/Logical Operator4 -> n178
        n178 = ip.mk_or(self.ctx, n175, n177)
        self.nets['A7E_requirements/weapon_class/Logical Operator4'] = n178
        # A7E_requirements/weapon_class/SOD
        n179 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/SOD'] = n179
        # A7E_requirements/weapon_class/v21
        n180 = ip.mk_number(self.ctx, '41', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v21'] = n180
        # A7E_requirements/weapon_class/eq19 -> n181
        n181 = ip.mk_eq(self.ctx, n102, n180)
        self.nets['A7E_requirements/weapon_class/eq19'] = n181
        # A7E_requirements/weapon_class/v20
        n182 = ip.mk_number(self.ctx, '42', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v20'] = n182
        # A7E_requirements/weapon_class/eq18 -> n183
        n183 = ip.mk_eq(self.ctx, n102, n182)
        self.nets['A7E_requirements/weapon_class/eq18'] = n183
        # A7E_requirements/weapon_class/v19
        n184 = ip.mk_number(self.ctx, '44', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v19'] = n184
        # A7E_requirements/weapon_class/eq17 -> n185
        n185 = ip.mk_eq(self.ctx, n102, n184)
        self.nets['A7E_requirements/weapon_class/eq17'] = n185
        # A7E_requirements/weapon_class/v18
        n186 = ip.mk_number(self.ctx, '46', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v18'] = n186
        # A7E_requirements/weapon_class/eq16 -> n187
        n187 = ip.mk_eq(self.ctx, n102, n186)
        self.nets['A7E_requirements/weapon_class/eq16'] = n187
        # A7E_requirements/weapon_class/v17
        n188 = ip.mk_number(self.ctx, '47', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v17'] = n188
        # A7E_requirements/weapon_class/eq15 -> n189
        n189 = ip.mk_eq(self.ctx, n102, n188)
        self.nets['A7E_requirements/weapon_class/eq15'] = n189
        # A7E_requirements/weapon_class/v16
        n190 = ip.mk_number(self.ctx, '48', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v16'] = n190
        # A7E_requirements/weapon_class/eq20 -> n191
        n191 = ip.mk_eq(self.ctx, n102, n190)
        self.nets['A7E_requirements/weapon_class/eq20'] = n191
        # A7E_requirements/weapon_class/v24
        n192 = ip.mk_number(self.ctx, '55', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v24'] = n192
        # A7E_requirements/weapon_class/eq21 -> n193
        n193 = ip.mk_eq(self.ctx, n102, n192)
        self.nets['A7E_requirements/weapon_class/eq21'] = n193
        # A7E_requirements/weapon_class/Logical Operator3 -> n194
        tn24 = ip.mk_or(self.ctx, n191, n193)
        tn23 = ip.mk_or(self.ctx, n189, tn24)
        tn22 = ip.mk_or(self.ctx, n187, tn23)
        tn21 = ip.mk_or(self.ctx, n185, tn22)
        tn20 = ip.mk_or(self.ctx, n183, tn21)
        n194 = ip.mk_or(self.ctx, n181, tn20)
        self.nets['A7E_requirements/weapon_class/Logical Operator3'] = n194
        # A7E_requirements/weapon_class/MF
        n195 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/MF'] = n195
        # A7E_requirements/weapon_class/v15
        n196 = ip.mk_number(self.ctx, '58', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v15'] = n196
        # A7E_requirements/weapon_class/eq14 -> n197
        n197 = ip.mk_eq(self.ctx, n102, n196)
        self.nets['A7E_requirements/weapon_class/eq14'] = n197
        # A7E_requirements/weapon_class/v14
        n198 = ip.mk_number(self.ctx, '57', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v14'] = n198
        # A7E_requirements/weapon_class/eq13 -> n199
        n199 = ip.mk_eq(self.ctx, n102, n198)
        self.nets['A7E_requirements/weapon_class/eq13'] = n199
        # A7E_requirements/weapon_class/v13
        n200 = ip.mk_number(self.ctx, '33', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v13'] = n200
        # A7E_requirements/weapon_class/eq12 -> n201
        n201 = ip.mk_eq(self.ctx, n102, n200)
        self.nets['A7E_requirements/weapon_class/eq12'] = n201
        # A7E_requirements/weapon_class/v12
        n202 = ip.mk_number(self.ctx, '32', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v12'] = n202
        # A7E_requirements/weapon_class/eq11 -> n203
        n203 = ip.mk_eq(self.ctx, n102, n202)
        self.nets['A7E_requirements/weapon_class/eq11'] = n203
        # A7E_requirements/weapon_class/v11
        n204 = ip.mk_number(self.ctx, '31', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v11'] = n204
        # A7E_requirements/weapon_class/eq10 -> n205
        n205 = ip.mk_eq(self.ctx, n102, n204)
        self.nets['A7E_requirements/weapon_class/eq10'] = n205
        # A7E_requirements/weapon_class/v10
        n206 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v10'] = n206
        # A7E_requirements/weapon_class/eq6 -> n207
        n207 = ip.mk_eq(self.ctx, n102, n206)
        self.nets['A7E_requirements/weapon_class/eq6'] = n207
        # A7E_requirements/weapon_class/v9
        n208 = ip.mk_number(self.ctx, '24', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v9'] = n208
        # A7E_requirements/weapon_class/eq7 -> n209
        n209 = ip.mk_eq(self.ctx, n102, n208)
        self.nets['A7E_requirements/weapon_class/eq7'] = n209
        # A7E_requirements/weapon_class/v8
        n210 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v8'] = n210
        # A7E_requirements/weapon_class/eq8 -> n211
        n211 = ip.mk_eq(self.ctx, n102, n210)
        self.nets['A7E_requirements/weapon_class/eq8'] = n211
        # A7E_requirements/weapon_class/v7
        n212 = ip.mk_number(self.ctx, '21', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v7'] = n212
        # A7E_requirements/weapon_class/eq9 -> n213
        n213 = ip.mk_eq(self.ctx, n102, n212)
        self.nets['A7E_requirements/weapon_class/eq9'] = n213
        # A7E_requirements/weapon_class/Logical Operator2 -> n214
        tn31 = ip.mk_or(self.ctx, n211, n213)
        tn30 = ip.mk_or(self.ctx, n209, tn31)
        tn29 = ip.mk_or(self.ctx, n207, tn30)
        tn28 = ip.mk_or(self.ctx, n205, tn29)
        tn27 = ip.mk_or(self.ctx, n203, tn28)
        tn26 = ip.mk_or(self.ctx, n201, tn27)
        tn25 = ip.mk_or(self.ctx, n199, tn26)
        n214 = ip.mk_or(self.ctx, n197, tn25)
        self.nets['A7E_requirements/weapon_class/Logical Operator2'] = n214
        # A7E_requirements/weapon_class/SK
        n215 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/SK'] = n215
        # A7E_requirements/weapon_class/v6
        n216 = ip.mk_number(self.ctx, '17', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v6'] = n216
        # A7E_requirements/weapon_class/eq5 -> n217
        n217 = ip.mk_eq(self.ctx, n102, n216)
        self.nets['A7E_requirements/weapon_class/eq5'] = n217
        # A7E_requirements/weapon_class/WL
        n218 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/WL'] = n218
        # A7E_requirements/weapon_class/v5
        n219 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v5'] = n219
        # A7E_requirements/weapon_class/eq4 -> n220
        n220 = ip.mk_eq(self.ctx, n102, n219)
        self.nets['A7E_requirements/weapon_class/eq4'] = n220
        # A7E_requirements/weapon_class/RK
        n221 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/RK'] = n221
        # A7E_requirements/weapon_class/v4
        n222 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v4'] = n222
        # A7E_requirements/weapon_class/eq2 -> n223
        n223 = ip.mk_eq(self.ctx, n102, n222)
        self.nets['A7E_requirements/weapon_class/eq2'] = n223
        # A7E_requirements/weapon_class/v3
        n224 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v3'] = n224
        # A7E_requirements/weapon_class/eq3 -> n225
        n225 = ip.mk_eq(self.ctx, n102, n224)
        self.nets['A7E_requirements/weapon_class/eq3'] = n225
        # A7E_requirements/weapon_class/Logical Operator1 -> n226
        n226 = ip.mk_or(self.ctx, n223, n225)
        self.nets['A7E_requirements/weapon_class/Logical Operator1'] = n226
        # A7E_requirements/weapon_class/GN
        n227 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/GN'] = n227
        # A7E_requirements/weapon_class/v1
        n228 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v1'] = n228
        # A7E_requirements/weapon_class/eq -> n229
        n229 = ip.mk_eq(self.ctx, n102, n228)
        self.nets['A7E_requirements/weapon_class/eq'] = n229
        # A7E_requirements/weapon_class/v2
        n230 = ip.mk_number(self.ctx, '13', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/v2'] = n230
        # A7E_requirements/weapon_class/eq1 -> n231
        n231 = ip.mk_eq(self.ctx, n102, n230)
        self.nets['A7E_requirements/weapon_class/eq1'] = n231
        # A7E_requirements/weapon_class/Logical Operator -> n232
        n232 = ip.mk_or(self.ctx, n229, n231)
        self.nets['A7E_requirements/weapon_class/Logical Operator'] = n232
        # A7E_requirements/weapon_class/UN
        n233 = ip.mk_number(self.ctx, '12', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/weapon_class/UN'] = n233
        # A7E_requirements/weapon_class/Switch
        n234 = ip.mk_ite(self.ctx, n232, n227, n233)
        self.nets['A7E_requirements/weapon_class/Switch'] = n234
        # A7E_requirements/weapon_class/Switch1
        n235 = ip.mk_ite(self.ctx, n226, n221, n234)
        self.nets['A7E_requirements/weapon_class/Switch1'] = n235
        # A7E_requirements/weapon_class/Switch2
        n236 = ip.mk_ite(self.ctx, n220, n218, n235)
        self.nets['A7E_requirements/weapon_class/Switch2'] = n236
        # A7E_requirements/weapon_class/Switch3
        n237 = ip.mk_ite(self.ctx, n217, n215, n236)
        self.nets['A7E_requirements/weapon_class/Switch3'] = n237
        # A7E_requirements/weapon_class/Switch4
        n238 = ip.mk_ite(self.ctx, n214, n195, n237)
        self.nets['A7E_requirements/weapon_class/Switch4'] = n238
        # A7E_requirements/weapon_class/Switch5
        n239 = ip.mk_ite(self.ctx, n194, n179, n238)
        self.nets['A7E_requirements/weapon_class/Switch5'] = n239
        # A7E_requirements/weapon_class/Switch6
        n240 = ip.mk_ite(self.ctx, n178, n173, n239)
        self.nets['A7E_requirements/weapon_class/Switch6'] = n240
        # A7E_requirements/weapon_class/Switch7
        n241 = ip.mk_ite(self.ctx, n172, n139, n240)
        self.nets['A7E_requirements/weapon_class/Switch7'] = n241
        # A7E_requirements/weapon_class/Switch8
        n242 = ip.mk_ite(self.ctx, n138, n121, n241)
        self.nets['A7E_requirements/weapon_class/Switch8'] = n242
        # A7E_requirements/weapon_class/Switch9
        n243 = ip.mk_ite(self.ctx, n120, n115, n242)
        self.nets['A7E_requirements/weapon_class/Switch9'] = n243
        # A7E_requirements/weapon_class/Switch10
        n244 = ip.mk_ite(self.ctx, n114, n109, n243)
        self.nets['A7E_requirements/weapon_class/Switch10'] = n244
        # A7E_requirements/weapon_class/Switch11
        n245 = ip.mk_ite(self.ctx, n108, n103, n244)
        self.nets['A7E_requirements/weapon_class/Switch11'] = n245
        # n245 -> weapon_class
        return n245

    def InitialState(self, n247, n248, n249, n250, n251, n252, n253, n254, n255, n256, n257, n258):
        # IMSup -> n247
        # IMSMODE=Gndal -> n248
        # IMSMODE=Iner -> n249
        # IMSMODE=Norm -> n250
        # IMSMODE=MagSl -> n251
        # IMSMODE=Grid -> n252
        # Data23=Sea -> n253
        # Landaln -> n254
        # OLB -> n255
        # MagSl -> n256
        # Grid -> n257
        # IMSfail -> n258
        # A7E_requirements/ANT/InitialState/not2 -> n259
        n259 = ip.mk_not(self.ctx, n247)
        self.nets['A7E_requirements/ANT/InitialState/not2'] = n259
        # A7E_requirements/ANT/InitialState/and5 -> n260
        n260 = ip.mk_and(self.ctx, n247, n252)
        self.nets['A7E_requirements/ANT/InitialState/and5'] = n260
        # A7E_requirements/ANT/InitialState/and4 -> n261
        n261 = ip.mk_and(self.ctx, n247, n251)
        self.nets['A7E_requirements/ANT/InitialState/and4'] = n261
        # A7E_requirements/ANT/InitialState/and3 -> n262
        n262 = ip.mk_and(self.ctx, n248, n253)
        self.nets['A7E_requirements/ANT/InitialState/and3'] = n262
        # A7E_requirements/ANT/InitialState/or1 -> n263
        tn32 = ip.mk_or(self.ctx, n250, n262)
        n263 = ip.mk_or(self.ctx, n249, tn32)
        self.nets['A7E_requirements/ANT/InitialState/or1'] = n263
        # A7E_requirements/ANT/InitialState/and2 -> n264
        n264 = ip.mk_and(self.ctx, n247, n263)
        self.nets['A7E_requirements/ANT/InitialState/and2'] = n264
        # A7E_requirements/ANT/InitialState/not1 -> n265
        n265 = ip.mk_not(self.ctx, n253)
        self.nets['A7E_requirements/ANT/InitialState/not1'] = n265
        # A7E_requirements/ANT/InitialState/and1 -> n266
        tn33 = ip.mk_and(self.ctx, n248, n265)
        n266 = ip.mk_and(self.ctx, n247, tn33)
        self.nets['A7E_requirements/ANT/InitialState/and1'] = n266
        # A7E_requirements/ANT/InitialState/Error
        n267 = ip.mk_number(self.ctx, '255', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/InitialState/Error'] = n267
        # A7E_requirements/ANT/InitialState/Switch
        n268 = ip.mk_ite(self.ctx, n266, n254, n267)
        self.nets['A7E_requirements/ANT/InitialState/Switch'] = n268
        # A7E_requirements/ANT/InitialState/Switch1
        n269 = ip.mk_ite(self.ctx, n264, n255, n268)
        self.nets['A7E_requirements/ANT/InitialState/Switch1'] = n269
        # A7E_requirements/ANT/InitialState/Switch2
        n270 = ip.mk_ite(self.ctx, n261, n256, n269)
        self.nets['A7E_requirements/ANT/InitialState/Switch2'] = n270
        # A7E_requirements/ANT/InitialState/Switch3
        n271 = ip.mk_ite(self.ctx, n260, n257, n270)
        self.nets['A7E_requirements/ANT/InitialState/Switch3'] = n271
        # A7E_requirements/ANT/InitialState/Switch4
        n272 = ip.mk_ite(self.ctx, n259, n258, n271)
        self.nets['A7E_requirements/ANT/InitialState/Switch4'] = n272
        # n272 -> InitialState
        return n272

    def ANT(self, n274, n275, n276, n277, n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289, n290, n291, n292, n293, n294, n295, n296, n297, n298, n299, n300):
        # presentPositionEntered -> n274
        # ACAIRB=Yes -> n275
        # IMSAUTOC=On -> n276
        # Desig -> n277
        # Data23=Sea -> n278
        # CAstageComplete -> n279
        # CLstageComplete -> n280
        # NDstageComplete -> n281
        # HSstageComplete -> n282
        # PNLTEST=TEST -> n283
        # IMSup -> n284
        # latitude>70 -> n285
        # latitude>80 -> n286
        # DopplerUp -> n287
        # DopplerCoupled -> n288
        # IMSMODE=Gndal -> n289
        # IMSMODE=Norm -> n290
        # IMSMODE=Iner -> n291
        # IMSMODE=MagSl -> n292
        # IMSMODE=Grid -> n293
        # AirVelocityTestPassed -> n294
        # PitchSmall AND RollSmall -> n295
        # SINSup -> n296
        # SINSvelocityTestPassed -> n297
        # LandVelocityTestPassed -> n298
        # NoInterveningTakeoff -> n299
        # GroundTestFinished -> n300
        n301 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Init', ip.mk_boolean_type(self.ctx))
        n302 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past', ip.mk_boolean_type(self.ctx))
        n303 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past1', ip.mk_boolean_type(self.ctx))
        n304 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past10', ip.mk_boolean_type(self.ctx))
        n305 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past11', ip.mk_boolean_type(self.ctx))
        n306 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past12', ip.mk_boolean_type(self.ctx))
        n307 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past13', ip.mk_boolean_type(self.ctx))
        n308 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past14', ip.mk_boolean_type(self.ctx))
        n309 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past15', ip.mk_boolean_type(self.ctx))
        n310 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past16', ip.mk_boolean_type(self.ctx))
        n311 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past17', ip.mk_boolean_type(self.ctx))
        n312 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past18', ip.mk_boolean_type(self.ctx))
        n313 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past19', ip.mk_boolean_type(self.ctx))
        n314 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past7', ip.mk_boolean_type(self.ctx))
        n315 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past6', ip.mk_boolean_type(self.ctx))
        n316 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past9', ip.mk_boolean_type(self.ctx))
        n317 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past8', ip.mk_boolean_type(self.ctx))
        n318 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past3', ip.mk_boolean_type(self.ctx))
        n319 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past2', ip.mk_boolean_type(self.ctx))
        n320 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past5', ip.mk_boolean_type(self.ctx))
        n321 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past4', ip.mk_boolean_type(self.ctx))
        n322 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past(Mode)', ip.mk_int8_type(self.ctx))
        n323 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past20', ip.mk_boolean_type(self.ctx))
        n324 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past21', ip.mk_boolean_type(self.ctx))
        n325 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past22', ip.mk_boolean_type(self.ctx))
        n326 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past23', ip.mk_boolean_type(self.ctx))
        n327 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past24', ip.mk_boolean_type(self.ctx))
        n328 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past25', ip.mk_boolean_type(self.ctx))
        n329 = ip.mk_latch(self.ctx, 'A7E_requirements/ANT/Past26', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/ANT/false
        n330 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/ANT/false'] = n330
        # A7E_requirements/ANT/Landaln
        n331 = ip.mk_number(self.ctx, '2', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Landaln'] = n331
        # A7E_requirements/ANT/OLB
        n332 = ip.mk_number(self.ctx, '11', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/OLB'] = n332
        # A7E_requirements/ANT/MagSl
        n333 = ip.mk_number(self.ctx, '12', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/MagSl'] = n333
        # A7E_requirements/ANT/Grid
        n334 = ip.mk_number(self.ctx, '13', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grid'] = n334
        # A7E_requirements/ANT/IMSfail
        n335 = ip.mk_number(self.ctx, '14', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/IMSfail'] = n335
        n336_1 = self.InitialState(n284, n289, n291, n290, n292, n293, n278, n331, n332, n333, n334, n335)
        # Bus Creator
        n337 = [n274, n275, n276, n277, n278, n279, n280, n281, n282, n283, n284, n285, n286, n287, n288, n289, n290, n291, n292, n293, n294, n295, n296, n297, n298, n299, n300]
        # Bus Creator1
        n338 = [n302, n303, n319, n318, n321, n320, n315, n314, n317, n316, n304, n305, n306, n307, n308, n309, n310, n311, n312, n313, n323, n324, n325, n326, n327, n328, n329]
        # A7E_requirements/ANT/Lautocal
        n339 = ip.mk_number(self.ctx, '0', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Lautocal'] = n339
        # A7E_requirements/ANT/Sautocal
        n340 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Sautocal'] = n340
        # A7E_requirements/ANT/SINSaln
        n341 = ip.mk_number(self.ctx, '3', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/SINSaln'] = n341
        # A7E_requirements/ANT/01Update
        n342 = ip.mk_number(self.ctx, '4', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/01Update'] = n342
        # A7E_requirements/ANT/HUDaln
        n343 = ip.mk_number(self.ctx, '5', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/HUDaln'] = n343
        # A7E_requirements/ANT/Airaln
        n344 = ip.mk_number(self.ctx, '6', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Airaln'] = n344
        # A7E_requirements/ANT/DIG
        n345 = ip.mk_number(self.ctx, '7', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DIG'] = n345
        # A7E_requirements/ANT/DI
        n346 = ip.mk_number(self.ctx, '8', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/DI'] = n346
        # A7E_requirements/ANT/I
        n347 = ip.mk_number(self.ctx, '9', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/I'] = n347
        # A7E_requirements/ANT/UDI
        n348 = ip.mk_number(self.ctx, '10', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/UDI'] = n348
        # A7E_requirements/ANT/PolarDI
        n349 = ip.mk_number(self.ctx, '15', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarDI'] = n349
        # A7E_requirements/ANT/PolarI
        n350 = ip.mk_number(self.ctx, '16', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/PolarI'] = n350
        # A7E_requirements/ANT/Grtest
        n351 = ip.mk_number(self.ctx, '17', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/ANT/Grtest'] = n351
        # Bus Creator2
        n352 = [n339, n340, n331, n341, n342, n343, n344, n345, n346, n347, n348, n332, n333, n334, n335, n349, n350, n351]
        # A7E_requirements/ANT/Mode1
        n353 = ip.mk_ite(self.ctx, n301, n336_1, n322)
        self.nets['A7E_requirements/ANT/Mode1'] = n353
        n354_1 = ip.scr.mk_scr(self.ctx, 'ANT', n337, n338, n352, n353)
        # A7E_requirements/ANT/Mode
        n355 = ip.mk_ite(self.ctx, n301, n336_1, n354_1)
        self.nets['A7E_requirements/ANT/Mode'] = n355
        in301 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n301, in301, n330)
        in302 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n302, in302, n274)
        in303 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n303, in303, n275)
        in304 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n304, in304, n284)
        in305 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n305, in305, n285)
        in306 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n306, in306, n286)
        in307 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n307, in307, n287)
        in308 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n308, in308, n288)
        in309 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n309, in309, n289)
        in310 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n310, in310, n290)
        in311 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n311, in311, n291)
        in312 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n312, in312, n292)
        in313 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n313, in313, n293)
        in314 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n314, in314, n281)
        in315 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n315, in315, n280)
        in316 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n316, in316, n283)
        in317 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n317, in317, n282)
        in318 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n318, in318, n277)
        in319 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n319, in319, n276)
        in320 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n320, in320, n279)
        in321 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n321, in321, n278)
        in322 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n322, in322, n355)
        in323 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n323, in323, n294)
        in324 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n324, in324, n295)
        in325 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n325, in325, n296)
        in326 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n326, in326, n297)
        in327 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n327, in327, n298)
        in328 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n328, in328, n299)
        in329 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n329, in329, n300)
        # n355 -> ANT
        return n355

    def NU(self, n357, n358, n359, n360, n361, n362, n363, n364, n365, n366, n367, n368, n369, n370, n371, n372, n373, n374):
        # StationSelected -> n357
        # ACAIRB=Yes -> n358
        # MODEROT=PRESPOS -> n359
        # PRESPOS=UPDATE -> n360
        # UPDATTW=FLYOVER -> n361
        # UPDATTW=HUD -> n362
        # UPDATTW=RADAR -> n363
        # UPDATTW=TACLL -> n364
        # UPDATTW=Other -> n365
        # GUNNSEL=Yes -> n366
        # WDMFS -> n367
        # Data23=Sea -> n368
        # WeaponMode=BOC -> n369
        # MSFW=None -> n370
        # MSFW=TF -> n371
        # NonZeroDigitEntered -> n372
        # ENTERSW=On -> n373
        # FLYTOchanged -> n374
        n375 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Init', ip.mk_boolean_type(self.ctx))
        n376 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past', ip.mk_boolean_type(self.ctx))
        n377 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past1', ip.mk_boolean_type(self.ctx))
        n378 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past10', ip.mk_boolean_type(self.ctx))
        n379 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past11', ip.mk_boolean_type(self.ctx))
        n380 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past12', ip.mk_boolean_type(self.ctx))
        n381 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past13', ip.mk_boolean_type(self.ctx))
        n382 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past14', ip.mk_boolean_type(self.ctx))
        n383 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past15', ip.mk_boolean_type(self.ctx))
        n384 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past16', ip.mk_boolean_type(self.ctx))
        n385 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past17', ip.mk_boolean_type(self.ctx))
        n386 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past7', ip.mk_boolean_type(self.ctx))
        n387 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past6', ip.mk_boolean_type(self.ctx))
        n388 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past9', ip.mk_boolean_type(self.ctx))
        n389 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past8', ip.mk_boolean_type(self.ctx))
        n390 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past3', ip.mk_boolean_type(self.ctx))
        n391 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past2', ip.mk_boolean_type(self.ctx))
        n392 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past5', ip.mk_boolean_type(self.ctx))
        n393 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past4', ip.mk_boolean_type(self.ctx))
        n394 = ip.mk_latch(self.ctx, 'A7E_requirements/NU/Past(Mode)', ip.mk_int8_type(self.ctx))
        # A7E_requirements/NU/false
        n395 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/NU/false'] = n395
        # A7E_requirements/NU/UNone
        n396 = ip.mk_number(self.ctx, '18', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/UNone'] = n396
        # Bus Creator
        n397 = [n357, n358, n359, n360, n361, n362, n363, n364, n365, n366, n367, n368, n369, n370, n371, n372, n373, n374]
        # Bus Creator1
        n398 = [n376, n377, n391, n390, n393, n392, n387, n386, n389, n388, n378, n379, n380, n381, n382, n383, n384, n385]
        # A7E_requirements/NU/HUDUpd
        n399 = ip.mk_number(self.ctx, '19', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/HUDUpd'] = n399
        # A7E_requirements/NU/RadarUpd
        n400 = ip.mk_number(self.ctx, '20', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/RadarUpd'] = n400
        # A7E_requirements/NU/FlyUpd
        n401 = ip.mk_number(self.ctx, '21', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/FlyUpd'] = n401
        # A7E_requirements/NU/AflyUpd
        n402 = ip.mk_number(self.ctx, '22', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/AflyUpd'] = n402
        # A7E_requirements/NU/MapUpd
        n403 = ip.mk_number(self.ctx, '23', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/MapUpd'] = n403
        # A7E_requirements/NU/TacUpd
        n404 = ip.mk_number(self.ctx, '24', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/NU/TacUpd'] = n404
        # Bus Creator2
        n405 = [n396, n399, n400, n401, n402, n403, n404]
        # A7E_requirements/NU/Mode1
        n406 = ip.mk_ite(self.ctx, n375, n396, n394)
        self.nets['A7E_requirements/NU/Mode1'] = n406
        n407_1 = ip.scr.mk_scr(self.ctx, 'NU', n397, n398, n405, n406)
        # A7E_requirements/NU/Mode
        n408 = ip.mk_ite(self.ctx, n375, n396, n407_1)
        self.nets['A7E_requirements/NU/Mode'] = n408
        in375 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n375, in375, n395)
        in376 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n376, in376, n357)
        in377 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n377, in377, n358)
        in378 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n378, in378, n367)
        in379 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n379, in379, n368)
        in380 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n380, in380, n369)
        in381 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n381, in381, n370)
        in382 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n382, in382, n371)
        in383 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n383, in383, n372)
        in384 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n384, in384, n373)
        in385 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n385, in385, n374)
        in386 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n386, in386, n364)
        in387 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n387, in387, n363)
        in388 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n388, in388, n366)
        in389 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n389, in389, n365)
        in390 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n390, in390, n360)
        in391 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n391, in391, n359)
        in392 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n392, in392, n362)
        in393 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n393, in393, n361)
        in394 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n394, in394, n408)
        # n408 -> NU
        return n408

    def WD(self, n410, n411, n412, n413, n414, n415, n416, n417, n418, n419, n420, n421, n422, n423, n424, n425, n426, n427, n428, n429, n430, n431, n432, n433, n434, n435, n436):
        # ReadyStation -> n410
        # HUREL=Yes -> n411
        # ReservedWeapon -> n412
        # Special -> n413
        # Rockets -> n414
        # Guns -> n415
        # OnWalleye -> n416
        # Shrike -> n417
        # OtherWeapon -> n418
        # GUNSSEL=No -> n419
        # FLYTOTW=0 -> n420
        # FLYTOTW=reset -> n421
        # FLYTOTOG=Dest -> n422
        # WDMFS -> n423
        # MFSW=BOC -> n424
        # MFSW=BOCOFF -> n425
        # MFSW=CCIP -> n426
        # MFSW=NATT -> n427
        # MFSW=NATOFF -> n428
        # Desig -> n429
        # Redesignate -> n430
        # AnyDestEntered -> n431
        # HighDrag -> n432
        # LowDrag -> n433
        # OverflownExit -> n434
        # Overflown>42 -> n435
        # ACAIRB=Yes -> n436
        n437 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Init', ip.mk_boolean_type(self.ctx))
        n438 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past', ip.mk_boolean_type(self.ctx))
        n439 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past1', ip.mk_boolean_type(self.ctx))
        n440 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past10', ip.mk_boolean_type(self.ctx))
        n441 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past11', ip.mk_boolean_type(self.ctx))
        n442 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past12', ip.mk_boolean_type(self.ctx))
        n443 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past13', ip.mk_boolean_type(self.ctx))
        n444 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past14', ip.mk_boolean_type(self.ctx))
        n445 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past15', ip.mk_boolean_type(self.ctx))
        n446 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past16', ip.mk_boolean_type(self.ctx))
        n447 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past17', ip.mk_boolean_type(self.ctx))
        n448 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past18', ip.mk_boolean_type(self.ctx))
        n449 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past19', ip.mk_boolean_type(self.ctx))
        n450 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past7', ip.mk_boolean_type(self.ctx))
        n451 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past6', ip.mk_boolean_type(self.ctx))
        n452 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past9', ip.mk_boolean_type(self.ctx))
        n453 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past8', ip.mk_boolean_type(self.ctx))
        n454 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past3', ip.mk_boolean_type(self.ctx))
        n455 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past2', ip.mk_boolean_type(self.ctx))
        n456 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past5', ip.mk_boolean_type(self.ctx))
        n457 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past4', ip.mk_boolean_type(self.ctx))
        n458 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past(Mode)', ip.mk_int8_type(self.ctx))
        n459 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past20', ip.mk_boolean_type(self.ctx))
        n460 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past21', ip.mk_boolean_type(self.ctx))
        n461 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past22', ip.mk_boolean_type(self.ctx))
        n462 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past23', ip.mk_boolean_type(self.ctx))
        n463 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past24', ip.mk_boolean_type(self.ctx))
        n464 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past25', ip.mk_boolean_type(self.ctx))
        n465 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past26', ip.mk_boolean_type(self.ctx))
        n466 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past27', ip.mk_boolean_type(self.ctx))
        n467 = ip.mk_latch(self.ctx, 'A7E_requirements/WD/Past28', ip.mk_boolean_type(self.ctx))
        # A7E_requirements/WD/false
        n468 = ip.mk_false(self.ctx)
        self.nets['A7E_requirements/WD/false'] = n468
        # A7E_requirements/WD/WNone
        n469 = ip.mk_number(self.ctx, '25', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WNone'] = n469
        # A7E_requirements/WD/Mode1
        n470 = ip.mk_ite(self.ctx, n437, n469, n458)
        self.nets['A7E_requirements/WD/Mode1'] = n470
        # A7E_requirements/WD/OFF_MFS
        n471 = ip.mk_number(self.ctx, '26', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/OFF_MFS'] = n471
        # A7E_requirements/WD/Past(In OFF_MFSW) -> n472
        n472 = ip.mk_eq(self.ctx, n470, n471)
        self.nets['A7E_requirements/WD/Past(In OFF_MFSW)'] = n472
        # A7E_requirements/WD/WD_MFS
        n473 = ip.mk_number(self.ctx, '27', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/WD_MFS'] = n473
        # A7E_requirements/WD/Past(In WD_MFSW) -> n474
        n474 = ip.mk_eq(self.ctx, n470, n473)
        self.nets['A7E_requirements/WD/Past(In WD_MFSW)'] = n474
        # Bus Creator
        n475 = [n410, n411, n412, n413, n414, n415, n416, n417, n418, n419, n420, n421, n422, n423, n424, n425, n426, n427, n428, n429, n430, n431, n432, n433, n434, n435, n436, n472, n474]
        # Bus Creator1
        n476 = [n438, n439, n455, n454, n457, n456, n451, n450, n453, n452, n440, n441, n442, n443, n444, n445, n446, n447, n448, n449, n459, n460, n461, n462, n463, n464, n465, n466, n467]
        # A7E_requirements/WD/Nattack
        n477 = ip.mk_number(self.ctx, '28', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Nattack'] = n477
        # A7E_requirements/WD/Noffset
        n478 = ip.mk_number(self.ctx, '29', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Noffset'] = n478
        # A7E_requirements/WD/BOC
        n479 = ip.mk_number(self.ctx, '30', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOC'] = n479
        # A7E_requirements/WD/BOCFlyto0
        n480 = ip.mk_number(self.ctx, '31', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCFlyto0'] = n480
        # A7E_requirements/WD/BOCoffset
        n481 = ip.mk_number(self.ctx, '32', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/BOCoffset'] = n481
        # A7E_requirements/WD/CCIP
        n482 = ip.mk_number(self.ctx, '33', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/CCIP'] = n482
        # A7E_requirements/WD/HUDdown1
        n483 = ip.mk_number(self.ctx, '34', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown1'] = n483
        # A7E_requirements/WD/HUDdown2
        n484 = ip.mk_number(self.ctx, '35', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/HUDdown2'] = n484
        # A7E_requirements/WD/AG_Guns
        n485 = ip.mk_number(self.ctx, '36', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AG_Guns'] = n485
        # A7E_requirements/WD/AA_Guns
        n486 = ip.mk_number(self.ctx, '37', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Guns'] = n486
        # A7E_requirements/WD/Manrip
        n487 = ip.mk_number(self.ctx, '38', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Manrip'] = n487
        # A7E_requirements/WD/AA_Manrip
        n488 = ip.mk_number(self.ctx, '39', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/AA_Manrip'] = n488
        # A7E_requirements/WD/Snattack
        n489 = ip.mk_number(self.ctx, '40', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snattack'] = n489
        # A7E_requirements/WD/Snoffset
        n490 = ip.mk_number(self.ctx, '41', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Snoffset'] = n490
        # A7E_requirements/WD/SBOC
        n491 = ip.mk_number(self.ctx, '42', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOC'] = n491
        # A7E_requirements/WD/SBOCFlyto0
        n492 = ip.mk_number(self.ctx, '43', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCFlyto0'] = n492
        # A7E_requirements/WD/SBOCoffset
        n493 = ip.mk_number(self.ctx, '44', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/SBOCoffset'] = n493
        # A7E_requirements/WD/Walleye
        n494 = ip.mk_number(self.ctx, '45', ip.mk_int8_type(self.ctx))
        self.nets['A7E_requirements/WD/Walleye'] = n494
        # Bus Creator2
        n495 = [n469, n471, n473, n477, n478, n479, n480, n481, n482, n483, n484, n485, n486, n487, n488, n489, n490, n491, n492, n493, n494]
        n496_1 = ip.scr.mk_scr(self.ctx, 'WD', n475, n476, n495, n470)
        # A7E_requirements/WD/Mode
        n497 = ip.mk_ite(self.ctx, n437, n469, n496_1)
        self.nets['A7E_requirements/WD/Mode'] = n497
        in437 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n437, in437, n468)
        in438 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n438, in438, n410)
        in439 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n439, in439, n411)
        in440 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n440, in440, n420)
        in441 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n441, in441, n421)
        in442 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n442, in442, n422)
        in443 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n443, in443, n423)
        in444 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n444, in444, n424)
        in445 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n445, in445, n425)
        in446 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n446, in446, n426)
        in447 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n447, in447, n427)
        in448 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n448, in448, n428)
        in449 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n449, in449, n429)
        in450 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n450, in450, n417)
        in451 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n451, in451, n416)
        in452 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n452, in452, n419)
        in453 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n453, in453, n418)
        in454 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n454, in454, n413)
        in455 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n455, in455, n412)
        in456 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n456, in456, n415)
        in457 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n457, in457, n414)
        in458 = ip.mk_number(self.ctx, '1', ip.mk_int8_type(self.ctx))
        ip.set_latch_init_next(self.ctx, n458, in458, n497)
        in459 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n459, in459, n430)
        in460 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n460, in460, n431)
        in461 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n461, in461, n432)
        in462 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n462, in462, n433)
        in463 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n463, in463, n434)
        in464 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n464, in464, n435)
        in465 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n465, in465, n436)
        in466 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n466, in466, n472)
        in467 = ip.mk_true(self.ctx)
        ip.set_latch_init_next(self.ctx, n467, in467, n474)
        # n497 -> WD
        return n497


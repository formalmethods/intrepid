import intrepyd as ip
import intrepyd.scr
import intrepyd.circuit
import collections

class SimulinkCircuit(ip.circuit.Circuit):
    def __init__(self, ctx, name):
        ip.circuit.Circuit.__init__(self, ctx, name)

    def _mk_naked_circuit_impl(self, inputs):
        input_keys = list(inputs)
        # In1 -> n1
        n1 = inputs[input_keys[0]]
        # In2 -> n2
        n2 = inputs[input_keys[1]]
        # In3 -> n3
        n3 = inputs[input_keys[2]]
        # In4 -> n4
        n4 = inputs[input_keys[3]]
        # In5 -> n5
        n5 = inputs[input_keys[4]]
        # In6 -> n6
        n6 = inputs[input_keys[5]]
        # In7 -> n7
        n7 = inputs[input_keys[6]]
        # In8 -> n8
        n8 = inputs[input_keys[7]]
        # In9 -> n9
        n9 = inputs[input_keys[8]]
        # In10 -> n10
        n10 = inputs[input_keys[9]]
        # In11 -> n11
        n11 = inputs[input_keys[10]]
        # In12 -> n12
        n12 = inputs[input_keys[11]]
        # In13 -> n13
        n13 = inputs[input_keys[12]]
        # In14 -> n14
        n14 = inputs[input_keys[13]]
        # In15 -> n15
        n15 = inputs[input_keys[14]]
        # In16 -> n16
        n16 = inputs[input_keys[15]]
        # In17 -> n17
        n17 = inputs[input_keys[16]]
        # In18 -> n18
        n18 = inputs[input_keys[17]]
        # In19 -> n19
        n19 = inputs[input_keys[18]]
        # In20 -> n20
        n20 = inputs[input_keys[19]]
        # In21 -> n21
        n21 = inputs[input_keys[20]]
        # In22 -> n22
        n22 = inputs[input_keys[21]]
        # In23 -> n23
        n23 = inputs[input_keys[22]]
        # In24 -> n24
        n24 = inputs[input_keys[23]]
        # In25 -> n25
        n25 = inputs[input_keys[24]]
        # In26 -> n26
        n26 = inputs[input_keys[25]]
        # In27 -> n27
        n27 = inputs[input_keys[26]]
        # In28 -> n28
        n28 = inputs[input_keys[27]]
        # In29 -> n29
        n29 = inputs[input_keys[28]]
        # In30 -> n30
        n30 = inputs[input_keys[29]]
        # In31 -> n31
        n31 = inputs[input_keys[30]]
        # In32 -> n32
        n32 = inputs[input_keys[31]]
        # In33 -> n33
        n33 = inputs[input_keys[32]]
        # In34 -> n34
        n34 = inputs[input_keys[33]]
        # In35 -> n35
        n35 = inputs[input_keys[34]]
        # In36 -> n36
        n36 = inputs[input_keys[35]]
        # In37 -> n37
        n37 = inputs[input_keys[36]]
        # In38 -> n38
        n38 = inputs[input_keys[37]]
        # In39 -> n39
        n39 = inputs[input_keys[38]]
        # In40 -> n40
        n40 = inputs[input_keys[39]]
        # In41 -> n41
        n41 = inputs[input_keys[40]]
        # In42 -> n42
        n42 = inputs[input_keys[41]]
        # In43 -> n43
        n43 = inputs[input_keys[42]]
        # In44 -> n44
        n44 = inputs[input_keys[43]]
        # In45 -> n45
        n45 = inputs[input_keys[44]]
        # In46 -> n46
        n46 = inputs[input_keys[45]]
        # In47 -> n47
        n47 = inputs[input_keys[46]]
        # In48 -> n48
        n48 = inputs[input_keys[47]]
        # In49 -> n49
        n49 = inputs[input_keys[48]]
        # In50 -> n50
        n50 = inputs[input_keys[49]]
        # In51 -> n51
        n51 = inputs[input_keys[50]]
        # In52 -> n52
        n52 = inputs[input_keys[51]]
        # In53 -> n53
        n53 = inputs[input_keys[52]]
        # In54 -> n54
        n54 = inputs[input_keys[53]]
        # In55 -> n55
        n55 = inputs[input_keys[54]]
        # In56 -> n56
        n56 = inputs[input_keys[55]]
        # In57 -> n57
        n57 = inputs[input_keys[56]]
        # In58 -> n58
        n58 = inputs[input_keys[57]]
        # In59 -> n59
        n59 = inputs[input_keys[58]]
        # In60 -> n60
        n60 = inputs[input_keys[59]]
        # In61 -> n61
        n61 = inputs[input_keys[60]]
        # In62 -> n62
        n62 = inputs[input_keys[61]]
        # In63 -> n63
        n63 = inputs[input_keys[62]]
        # In64 -> n64
        n64 = inputs[input_keys[63]]
        # In65 -> n65
        n65 = inputs[input_keys[64]]
        # In66 -> n66
        n66 = inputs[input_keys[65]]
        # In67 -> n67
        n67 = inputs[input_keys[66]]
        # In68 -> n68
        n68 = inputs[input_keys[67]]
        # In69 -> n69
        n69 = inputs[input_keys[68]]
        # In70 -> n70
        n70 = inputs[input_keys[69]]
        # In71 -> n71
        n71 = inputs[input_keys[70]]
        # In72 -> n72
        n72 = inputs[input_keys[71]]
        # In73 -> n73
        n73 = inputs[input_keys[72]]
        # In74 -> n74
        n74 = inputs[input_keys[73]]
        # In75 -> n75
        n75 = inputs[input_keys[74]]
        # In76 -> n76
        n76 = inputs[input_keys[75]]
        # In77 -> n77
        n77 = inputs[input_keys[76]]
        # In78 -> n78
        n78 = inputs[input_keys[77]]
        # In79 -> n79
        n79 = inputs[input_keys[78]]
        # In80 -> n80
        n80 = inputs[input_keys[79]]
        # In81 -> n81
        n81 = inputs[input_keys[80]]
        n82_1 = self.Rows(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81)
        n83_1, n83_2, n83_3, n83_4, n83_5, n83_6, n83_7, n83_8, n83_9, n83_10, n83_11, n83_12, n83_13, n83_14, n83_15, n83_16, n83_17, n83_18, n83_19, n83_20, n83_21, n83_22, n83_23, n83_24, n83_25, n83_26, n83_27, n83_28, n83_29, n83_30, n83_31, n83_32, n83_33, n83_34, n83_35, n83_36, n83_37, n83_38, n83_39, n83_40, n83_41, n83_42, n83_43, n83_44, n83_45, n83_46, n83_47, n83_48, n83_49, n83_50, n83_51, n83_52, n83_53, n83_54, n83_55, n83_56, n83_57, n83_58, n83_59, n83_60, n83_61, n83_62, n83_63, n83_64, n83_65, n83_66, n83_67, n83_68, n83_69, n83_70, n83_71, n83_72, n83_73, n83_74, n83_75, n83_76, n83_77, n83_78, n83_79, n83_80, n83_81 = self.ColRewire(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81)
        n84_1 = self.columns(n83_1, n83_2, n83_3, n83_4, n83_5, n83_6, n83_7, n83_8, n83_9, n83_10, n83_11, n83_12, n83_13, n83_14, n83_15, n83_16, n83_17, n83_18, n83_19, n83_20, n83_21, n83_22, n83_23, n83_24, n83_25, n83_26, n83_27, n83_28, n83_29, n83_30, n83_31, n83_32, n83_33, n83_34, n83_35, n83_36, n83_37, n83_38, n83_39, n83_40, n83_41, n83_42, n83_43, n83_44, n83_45, n83_46, n83_47, n83_48, n83_49, n83_50, n83_51, n83_52, n83_53, n83_54, n83_55, n83_56, n83_57, n83_58, n83_59, n83_60, n83_61, n83_62, n83_63, n83_64, n83_65, n83_66, n83_67, n83_68, n83_69, n83_70, n83_71, n83_72, n83_73, n83_74, n83_75, n83_76, n83_77, n83_78, n83_79, n83_80, n83_81)
        n85_1, n85_2, n85_3, n85_4, n85_5, n85_6, n85_7, n85_8, n85_9, n85_10, n85_11, n85_12, n85_13, n85_14, n85_15, n85_16, n85_17, n85_18, n85_19, n85_20, n85_21, n85_22, n85_23, n85_24, n85_25, n85_26, n85_27, n85_28, n85_29, n85_30, n85_31, n85_32, n85_33, n85_34, n85_35, n85_36, n85_37, n85_38, n85_39, n85_40, n85_41, n85_42, n85_43, n85_44, n85_45, n85_46, n85_47, n85_48, n85_49, n85_50, n85_51, n85_52, n85_53, n85_54, n85_55, n85_56, n85_57, n85_58, n85_59, n85_60, n85_61, n85_62, n85_63, n85_64, n85_65, n85_66, n85_67, n85_68, n85_69, n85_70, n85_71, n85_72, n85_73, n85_74, n85_75, n85_76, n85_77, n85_78, n85_79, n85_80, n85_81 = self.BlockRewire(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81)
        n86_1 = self.blocks(n85_1, n85_2, n85_3, n85_4, n85_5, n85_6, n85_7, n85_8, n85_9, n85_10, n85_11, n85_12, n85_13, n85_14, n85_15, n85_16, n85_17, n85_18, n85_19, n85_20, n85_21, n85_22, n85_23, n85_24, n85_25, n85_26, n85_27, n85_28, n85_29, n85_30, n85_31, n85_32, n85_33, n85_34, n85_35, n85_36, n85_37, n85_38, n85_39, n85_40, n85_41, n85_42, n85_43, n85_44, n85_45, n85_46, n85_47, n85_48, n85_49, n85_50, n85_51, n85_52, n85_53, n85_54, n85_55, n85_56, n85_57, n85_58, n85_59, n85_60, n85_61, n85_62, n85_63, n85_64, n85_65, n85_66, n85_67, n85_68, n85_69, n85_70, n85_71, n85_72, n85_73, n85_74, n85_75, n85_76, n85_77, n85_78, n85_79, n85_80, n85_81)
        # sudoku/Logical Operator -> n87
        tn0 = self.context.mk_and(n84_1, n86_1)
        n87 = self.context.mk_and(n82_1, tn0)
        self.nets['sudoku/Logical Operator'] = n87
        self.targets['sudoku/Proof Objective'] = n87
        self.bounds5(n6)
        self.bounds49(n48)
        self.bounds6(n7)
        self.bounds48(n47)
        self.bounds7(n8)
        self.bounds47(n46)
        self.bounds8(n9)
        self.bounds9(n10)
        self.bounds42(n41)
        self.bounds41(n81)
        self.bounds40(n41)
        self.bounds46(n45)
        self.bounds45(n44)
        self.bounds44(n43)
        self.bounds43(n42)
        self.bounds1(n2)
        self.bounds2(n3)
        self.bounds3(n4)
        self.bounds4(n5)
        self.bounds39(n40)
        self.bounds38(n39)
        self.bounds37(n38)
        self.bounds36(n37)
        self.bounds(n1)
        self.bounds31(n32)
        self.bounds30(n31)
        self.bounds35(n36)
        self.bounds34(n35)
        self.bounds33(n34)
        self.bounds32(n33)
        self.bounds28(n29)
        self.bounds27(n28)
        self.bounds26(n27)
        self.bounds25(n26)
        self.bounds29(n30)
        self.bounds20(n21)
        self.bounds24(n25)
        self.bounds23(n24)
        self.bounds22(n23)
        self.bounds21(n22)
        self.bounds17(n18)
        self.bounds16(n17)
        self.bounds15(n16)
        self.bounds14(n15)
        self.bounds19(n20)
        self.bounds18(n19)
        self.bounds13(n14)
        self.bounds12(n13)
        self.bounds11(n12)
        self.bounds10(n11)
        self.bounds81(n80)
        self.bounds80(n79)
        self.bounds71(n70)
        self.bounds70(n69)
        self.bounds75(n74)
        self.bounds74(n73)
        self.bounds73(n72)
        self.bounds72(n71)
        self.bounds79(n78)
        self.bounds78(n77)
        self.bounds77(n76)
        self.bounds76(n75)
        self.bounds60(n59)
        self.bounds69(n68)
        self.bounds64(n63)
        self.bounds63(n62)
        self.bounds62(n61)
        self.bounds61(n60)
        self.bounds68(n67)
        self.bounds67(n66)
        self.bounds66(n65)
        self.bounds65(n64)
        self.bounds59(n58)
        self.bounds58(n57)
        self.bounds53(n52)
        self.bounds52(n51)
        self.bounds51(n50)
        self.bounds50(n49)
        self.bounds57(n56)
        self.bounds56(n55)
        self.bounds55(n54)
        self.bounds54(n53)
        # n87 -> Out1
        outputs = collections.OrderedDict()
        outputs['sudoku/Out1'] = n87
        return outputs

    def _mk_inputs(self):
        # sudoku/In1 -> n1
        n1 = self.context.mk_input('In1', self.context.mk_int8_type())
        self.inputs['In1'] = n1
        # sudoku/In2 -> n2
        n2 = self.context.mk_input('In2', self.context.mk_int8_type())
        self.inputs['In2'] = n2
        # sudoku/In3 -> n3
        n3 = self.context.mk_input('In3', self.context.mk_int8_type())
        self.inputs['In3'] = n3
        # sudoku/In4 -> n4
        n4 = self.context.mk_input('In4', self.context.mk_int8_type())
        self.inputs['In4'] = n4
        # sudoku/In5 -> n5
        n5 = self.context.mk_input('In5', self.context.mk_int8_type())
        self.inputs['In5'] = n5
        # sudoku/In6 -> n6
        n6 = self.context.mk_input('In6', self.context.mk_int8_type())
        self.inputs['In6'] = n6
        # sudoku/In7 -> n7
        n7 = self.context.mk_input('In7', self.context.mk_int8_type())
        self.inputs['In7'] = n7
        # sudoku/In8 -> n8
        n8 = self.context.mk_input('In8', self.context.mk_int8_type())
        self.inputs['In8'] = n8
        # sudoku/In9 -> n9
        n9 = self.context.mk_input('In9', self.context.mk_int8_type())
        self.inputs['In9'] = n9
        # sudoku/In10 -> n10
        n10 = self.context.mk_input('In10', self.context.mk_int8_type())
        self.inputs['In10'] = n10
        # sudoku/In11 -> n11
        n11 = self.context.mk_input('In11', self.context.mk_int8_type())
        self.inputs['In11'] = n11
        # sudoku/In12 -> n12
        n12 = self.context.mk_input('In12', self.context.mk_int8_type())
        self.inputs['In12'] = n12
        # sudoku/In13 -> n13
        n13 = self.context.mk_input('In13', self.context.mk_int8_type())
        self.inputs['In13'] = n13
        # sudoku/In14 -> n14
        n14 = self.context.mk_input('In14', self.context.mk_int8_type())
        self.inputs['In14'] = n14
        # sudoku/In15 -> n15
        n15 = self.context.mk_input('In15', self.context.mk_int8_type())
        self.inputs['In15'] = n15
        # sudoku/In16 -> n16
        n16 = self.context.mk_input('In16', self.context.mk_int8_type())
        self.inputs['In16'] = n16
        # sudoku/In17 -> n17
        n17 = self.context.mk_input('In17', self.context.mk_int8_type())
        self.inputs['In17'] = n17
        # sudoku/In18 -> n18
        n18 = self.context.mk_input('In18', self.context.mk_int8_type())
        self.inputs['In18'] = n18
        # sudoku/In19 -> n19
        n19 = self.context.mk_input('In19', self.context.mk_int8_type())
        self.inputs['In19'] = n19
        # sudoku/In20 -> n20
        n20 = self.context.mk_input('In20', self.context.mk_int8_type())
        self.inputs['In20'] = n20
        # sudoku/In21 -> n21
        n21 = self.context.mk_input('In21', self.context.mk_int8_type())
        self.inputs['In21'] = n21
        # sudoku/In22 -> n22
        n22 = self.context.mk_input('In22', self.context.mk_int8_type())
        self.inputs['In22'] = n22
        # sudoku/In23 -> n23
        n23 = self.context.mk_input('In23', self.context.mk_int8_type())
        self.inputs['In23'] = n23
        # sudoku/In24 -> n24
        n24 = self.context.mk_input('In24', self.context.mk_int8_type())
        self.inputs['In24'] = n24
        # sudoku/In25 -> n25
        n25 = self.context.mk_input('In25', self.context.mk_int8_type())
        self.inputs['In25'] = n25
        # sudoku/In26 -> n26
        n26 = self.context.mk_input('In26', self.context.mk_int8_type())
        self.inputs['In26'] = n26
        # sudoku/In27 -> n27
        n27 = self.context.mk_input('In27', self.context.mk_int8_type())
        self.inputs['In27'] = n27
        # sudoku/In28 -> n28
        n28 = self.context.mk_input('In28', self.context.mk_int8_type())
        self.inputs['In28'] = n28
        # sudoku/In29 -> n29
        n29 = self.context.mk_input('In29', self.context.mk_int8_type())
        self.inputs['In29'] = n29
        # sudoku/In30 -> n30
        n30 = self.context.mk_input('In30', self.context.mk_int8_type())
        self.inputs['In30'] = n30
        # sudoku/In31 -> n31
        n31 = self.context.mk_input('In31', self.context.mk_int8_type())
        self.inputs['In31'] = n31
        # sudoku/In32 -> n32
        n32 = self.context.mk_input('In32', self.context.mk_int8_type())
        self.inputs['In32'] = n32
        # sudoku/In33 -> n33
        n33 = self.context.mk_input('In33', self.context.mk_int8_type())
        self.inputs['In33'] = n33
        # sudoku/In34 -> n34
        n34 = self.context.mk_input('In34', self.context.mk_int8_type())
        self.inputs['In34'] = n34
        # sudoku/In35 -> n35
        n35 = self.context.mk_input('In35', self.context.mk_int8_type())
        self.inputs['In35'] = n35
        # sudoku/In36 -> n36
        n36 = self.context.mk_input('In36', self.context.mk_int8_type())
        self.inputs['In36'] = n36
        # sudoku/In37 -> n37
        n37 = self.context.mk_input('In37', self.context.mk_int8_type())
        self.inputs['In37'] = n37
        # sudoku/In38 -> n38
        n38 = self.context.mk_input('In38', self.context.mk_int8_type())
        self.inputs['In38'] = n38
        # sudoku/In39 -> n39
        n39 = self.context.mk_input('In39', self.context.mk_int8_type())
        self.inputs['In39'] = n39
        # sudoku/In40 -> n40
        n40 = self.context.mk_input('In40', self.context.mk_int8_type())
        self.inputs['In40'] = n40
        # sudoku/In41 -> n41
        n41 = self.context.mk_input('In41', self.context.mk_int8_type())
        self.inputs['In41'] = n41
        # sudoku/In42 -> n42
        n42 = self.context.mk_input('In42', self.context.mk_int8_type())
        self.inputs['In42'] = n42
        # sudoku/In43 -> n43
        n43 = self.context.mk_input('In43', self.context.mk_int8_type())
        self.inputs['In43'] = n43
        # sudoku/In44 -> n44
        n44 = self.context.mk_input('In44', self.context.mk_int8_type())
        self.inputs['In44'] = n44
        # sudoku/In45 -> n45
        n45 = self.context.mk_input('In45', self.context.mk_int8_type())
        self.inputs['In45'] = n45
        # sudoku/In46 -> n46
        n46 = self.context.mk_input('In46', self.context.mk_int8_type())
        self.inputs['In46'] = n46
        # sudoku/In47 -> n47
        n47 = self.context.mk_input('In47', self.context.mk_int8_type())
        self.inputs['In47'] = n47
        # sudoku/In48 -> n48
        n48 = self.context.mk_input('In48', self.context.mk_int8_type())
        self.inputs['In48'] = n48
        # sudoku/In49 -> n49
        n49 = self.context.mk_input('In49', self.context.mk_int8_type())
        self.inputs['In49'] = n49
        # sudoku/In50 -> n50
        n50 = self.context.mk_input('In50', self.context.mk_int8_type())
        self.inputs['In50'] = n50
        # sudoku/In51 -> n51
        n51 = self.context.mk_input('In51', self.context.mk_int8_type())
        self.inputs['In51'] = n51
        # sudoku/In52 -> n52
        n52 = self.context.mk_input('In52', self.context.mk_int8_type())
        self.inputs['In52'] = n52
        # sudoku/In53 -> n53
        n53 = self.context.mk_input('In53', self.context.mk_int8_type())
        self.inputs['In53'] = n53
        # sudoku/In54 -> n54
        n54 = self.context.mk_input('In54', self.context.mk_int8_type())
        self.inputs['In54'] = n54
        # sudoku/In55 -> n55
        n55 = self.context.mk_input('In55', self.context.mk_int8_type())
        self.inputs['In55'] = n55
        # sudoku/In56 -> n56
        n56 = self.context.mk_input('In56', self.context.mk_int8_type())
        self.inputs['In56'] = n56
        # sudoku/In57 -> n57
        n57 = self.context.mk_input('In57', self.context.mk_int8_type())
        self.inputs['In57'] = n57
        # sudoku/In58 -> n58
        n58 = self.context.mk_input('In58', self.context.mk_int8_type())
        self.inputs['In58'] = n58
        # sudoku/In59 -> n59
        n59 = self.context.mk_input('In59', self.context.mk_int8_type())
        self.inputs['In59'] = n59
        # sudoku/In60 -> n60
        n60 = self.context.mk_input('In60', self.context.mk_int8_type())
        self.inputs['In60'] = n60
        # sudoku/In61 -> n61
        n61 = self.context.mk_input('In61', self.context.mk_int8_type())
        self.inputs['In61'] = n61
        # sudoku/In62 -> n62
        n62 = self.context.mk_input('In62', self.context.mk_int8_type())
        self.inputs['In62'] = n62
        # sudoku/In63 -> n63
        n63 = self.context.mk_input('In63', self.context.mk_int8_type())
        self.inputs['In63'] = n63
        # sudoku/In64 -> n64
        n64 = self.context.mk_input('In64', self.context.mk_int8_type())
        self.inputs['In64'] = n64
        # sudoku/In65 -> n65
        n65 = self.context.mk_input('In65', self.context.mk_int8_type())
        self.inputs['In65'] = n65
        # sudoku/In66 -> n66
        n66 = self.context.mk_input('In66', self.context.mk_int8_type())
        self.inputs['In66'] = n66
        # sudoku/In67 -> n67
        n67 = self.context.mk_input('In67', self.context.mk_int8_type())
        self.inputs['In67'] = n67
        # sudoku/In68 -> n68
        n68 = self.context.mk_input('In68', self.context.mk_int8_type())
        self.inputs['In68'] = n68
        # sudoku/In69 -> n69
        n69 = self.context.mk_input('In69', self.context.mk_int8_type())
        self.inputs['In69'] = n69
        # sudoku/In70 -> n70
        n70 = self.context.mk_input('In70', self.context.mk_int8_type())
        self.inputs['In70'] = n70
        # sudoku/In71 -> n71
        n71 = self.context.mk_input('In71', self.context.mk_int8_type())
        self.inputs['In71'] = n71
        # sudoku/In72 -> n72
        n72 = self.context.mk_input('In72', self.context.mk_int8_type())
        self.inputs['In72'] = n72
        # sudoku/In73 -> n73
        n73 = self.context.mk_input('In73', self.context.mk_int8_type())
        self.inputs['In73'] = n73
        # sudoku/In74 -> n74
        n74 = self.context.mk_input('In74', self.context.mk_int8_type())
        self.inputs['In74'] = n74
        # sudoku/In75 -> n75
        n75 = self.context.mk_input('In75', self.context.mk_int8_type())
        self.inputs['In75'] = n75
        # sudoku/In76 -> n76
        n76 = self.context.mk_input('In76', self.context.mk_int8_type())
        self.inputs['In76'] = n76
        # sudoku/In77 -> n77
        n77 = self.context.mk_input('In77', self.context.mk_int8_type())
        self.inputs['In77'] = n77
        # sudoku/In78 -> n78
        n78 = self.context.mk_input('In78', self.context.mk_int8_type())
        self.inputs['In78'] = n78
        # sudoku/In79 -> n79
        n79 = self.context.mk_input('In79', self.context.mk_int8_type())
        self.inputs['In79'] = n79
        # sudoku/In80 -> n80
        n80 = self.context.mk_input('In80', self.context.mk_int8_type())
        self.inputs['In80'] = n80
        # sudoku/In81 -> n81
        n81 = self.context.mk_input('In81', self.context.mk_int8_type())
        self.inputs['In81'] = n81

    def bounds5(self, n172):
        # In1 -> n172
        # sudoku/bounds5/lb
        n173 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds5/lb'] = n173
        # sudoku/bounds5/leq -> n174
        n174 = self.context.mk_leq(n173, n172)
        self.nets['sudoku/bounds5/leq'] = n174
        # sudoku/bounds5/ub
        n175 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds5/ub'] = n175
        # sudoku/bounds5/geq -> n176
        n176 = self.context.mk_leq(n172, n175)
        self.nets['sudoku/bounds5/geq'] = n176
        # sudoku/bounds5/Logical Operator -> n177
        n177 = self.context.mk_and(n174, n176)
        self.nets['sudoku/bounds5/Logical Operator'] = n177
        # sudoku/bounds5/Assumption
        self.context.mk_assumption(n177)
        return 

    def bounds49(self, n179):
        # In1 -> n179
        # sudoku/bounds49/lb
        n180 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds49/lb'] = n180
        # sudoku/bounds49/leq -> n181
        n181 = self.context.mk_leq(n180, n179)
        self.nets['sudoku/bounds49/leq'] = n181
        # sudoku/bounds49/ub
        n182 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds49/ub'] = n182
        # sudoku/bounds49/geq -> n183
        n183 = self.context.mk_leq(n179, n182)
        self.nets['sudoku/bounds49/geq'] = n183
        # sudoku/bounds49/Logical Operator -> n184
        n184 = self.context.mk_and(n181, n183)
        self.nets['sudoku/bounds49/Logical Operator'] = n184
        # sudoku/bounds49/Assumption
        self.context.mk_assumption(n184)
        return 

    def bounds6(self, n186):
        # In1 -> n186
        # sudoku/bounds6/lb
        n187 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds6/lb'] = n187
        # sudoku/bounds6/leq -> n188
        n188 = self.context.mk_leq(n187, n186)
        self.nets['sudoku/bounds6/leq'] = n188
        # sudoku/bounds6/ub
        n189 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds6/ub'] = n189
        # sudoku/bounds6/geq -> n190
        n190 = self.context.mk_leq(n186, n189)
        self.nets['sudoku/bounds6/geq'] = n190
        # sudoku/bounds6/Logical Operator -> n191
        n191 = self.context.mk_and(n188, n190)
        self.nets['sudoku/bounds6/Logical Operator'] = n191
        # sudoku/bounds6/Assumption
        self.context.mk_assumption(n191)
        return 

    def bounds48(self, n193):
        # In1 -> n193
        # sudoku/bounds48/lb
        n194 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds48/lb'] = n194
        # sudoku/bounds48/leq -> n195
        n195 = self.context.mk_leq(n194, n193)
        self.nets['sudoku/bounds48/leq'] = n195
        # sudoku/bounds48/ub
        n196 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds48/ub'] = n196
        # sudoku/bounds48/geq -> n197
        n197 = self.context.mk_leq(n193, n196)
        self.nets['sudoku/bounds48/geq'] = n197
        # sudoku/bounds48/Logical Operator -> n198
        n198 = self.context.mk_and(n195, n197)
        self.nets['sudoku/bounds48/Logical Operator'] = n198
        # sudoku/bounds48/Assumption
        self.context.mk_assumption(n198)
        return 

    def bounds7(self, n200):
        # In1 -> n200
        # sudoku/bounds7/lb
        n201 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds7/lb'] = n201
        # sudoku/bounds7/leq -> n202
        n202 = self.context.mk_leq(n201, n200)
        self.nets['sudoku/bounds7/leq'] = n202
        # sudoku/bounds7/ub
        n203 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds7/ub'] = n203
        # sudoku/bounds7/geq -> n204
        n204 = self.context.mk_leq(n200, n203)
        self.nets['sudoku/bounds7/geq'] = n204
        # sudoku/bounds7/Logical Operator -> n205
        n205 = self.context.mk_and(n202, n204)
        self.nets['sudoku/bounds7/Logical Operator'] = n205
        # sudoku/bounds7/Assumption
        self.context.mk_assumption(n205)
        return 

    def bounds47(self, n207):
        # In1 -> n207
        # sudoku/bounds47/lb
        n208 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds47/lb'] = n208
        # sudoku/bounds47/leq -> n209
        n209 = self.context.mk_leq(n208, n207)
        self.nets['sudoku/bounds47/leq'] = n209
        # sudoku/bounds47/ub
        n210 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds47/ub'] = n210
        # sudoku/bounds47/geq -> n211
        n211 = self.context.mk_leq(n207, n210)
        self.nets['sudoku/bounds47/geq'] = n211
        # sudoku/bounds47/Logical Operator -> n212
        n212 = self.context.mk_and(n209, n211)
        self.nets['sudoku/bounds47/Logical Operator'] = n212
        # sudoku/bounds47/Assumption
        self.context.mk_assumption(n212)
        return 

    def bounds8(self, n214):
        # In1 -> n214
        # sudoku/bounds8/lb
        n215 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds8/lb'] = n215
        # sudoku/bounds8/leq -> n216
        n216 = self.context.mk_leq(n215, n214)
        self.nets['sudoku/bounds8/leq'] = n216
        # sudoku/bounds8/ub
        n217 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds8/ub'] = n217
        # sudoku/bounds8/geq -> n218
        n218 = self.context.mk_leq(n214, n217)
        self.nets['sudoku/bounds8/geq'] = n218
        # sudoku/bounds8/Logical Operator -> n219
        n219 = self.context.mk_and(n216, n218)
        self.nets['sudoku/bounds8/Logical Operator'] = n219
        # sudoku/bounds8/Assumption
        self.context.mk_assumption(n219)
        return 

    def bounds9(self, n221):
        # In1 -> n221
        # sudoku/bounds9/lb
        n222 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds9/lb'] = n222
        # sudoku/bounds9/leq -> n223
        n223 = self.context.mk_leq(n222, n221)
        self.nets['sudoku/bounds9/leq'] = n223
        # sudoku/bounds9/ub
        n224 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds9/ub'] = n224
        # sudoku/bounds9/geq -> n225
        n225 = self.context.mk_leq(n221, n224)
        self.nets['sudoku/bounds9/geq'] = n225
        # sudoku/bounds9/Logical Operator -> n226
        n226 = self.context.mk_and(n223, n225)
        self.nets['sudoku/bounds9/Logical Operator'] = n226
        # sudoku/bounds9/Assumption
        self.context.mk_assumption(n226)
        return 

    def bounds42(self, n228):
        # In1 -> n228
        # sudoku/bounds42/lb
        n229 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds42/lb'] = n229
        # sudoku/bounds42/leq -> n230
        n230 = self.context.mk_leq(n229, n228)
        self.nets['sudoku/bounds42/leq'] = n230
        # sudoku/bounds42/ub
        n231 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds42/ub'] = n231
        # sudoku/bounds42/geq -> n232
        n232 = self.context.mk_leq(n228, n231)
        self.nets['sudoku/bounds42/geq'] = n232
        # sudoku/bounds42/Logical Operator -> n233
        n233 = self.context.mk_and(n230, n232)
        self.nets['sudoku/bounds42/Logical Operator'] = n233
        # sudoku/bounds42/Assumption
        self.context.mk_assumption(n233)
        return 

    def bounds41(self, n235):
        # In1 -> n235
        # sudoku/bounds41/lb
        n236 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds41/lb'] = n236
        # sudoku/bounds41/leq -> n237
        n237 = self.context.mk_leq(n236, n235)
        self.nets['sudoku/bounds41/leq'] = n237
        # sudoku/bounds41/ub
        n238 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds41/ub'] = n238
        # sudoku/bounds41/geq -> n239
        n239 = self.context.mk_leq(n235, n238)
        self.nets['sudoku/bounds41/geq'] = n239
        # sudoku/bounds41/Logical Operator -> n240
        n240 = self.context.mk_and(n237, n239)
        self.nets['sudoku/bounds41/Logical Operator'] = n240
        # sudoku/bounds41/Assumption
        self.context.mk_assumption(n240)
        return 

    def bounds40(self, n242):
        # In1 -> n242
        # sudoku/bounds40/lb
        n243 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds40/lb'] = n243
        # sudoku/bounds40/leq -> n244
        n244 = self.context.mk_leq(n243, n242)
        self.nets['sudoku/bounds40/leq'] = n244
        # sudoku/bounds40/ub
        n245 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds40/ub'] = n245
        # sudoku/bounds40/geq -> n246
        n246 = self.context.mk_leq(n242, n245)
        self.nets['sudoku/bounds40/geq'] = n246
        # sudoku/bounds40/Logical Operator -> n247
        n247 = self.context.mk_and(n244, n246)
        self.nets['sudoku/bounds40/Logical Operator'] = n247
        # sudoku/bounds40/Assumption
        self.context.mk_assumption(n247)
        return 

    def bounds46(self, n249):
        # In1 -> n249
        # sudoku/bounds46/lb
        n250 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds46/lb'] = n250
        # sudoku/bounds46/leq -> n251
        n251 = self.context.mk_leq(n250, n249)
        self.nets['sudoku/bounds46/leq'] = n251
        # sudoku/bounds46/ub
        n252 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds46/ub'] = n252
        # sudoku/bounds46/geq -> n253
        n253 = self.context.mk_leq(n249, n252)
        self.nets['sudoku/bounds46/geq'] = n253
        # sudoku/bounds46/Logical Operator -> n254
        n254 = self.context.mk_and(n251, n253)
        self.nets['sudoku/bounds46/Logical Operator'] = n254
        # sudoku/bounds46/Assumption
        self.context.mk_assumption(n254)
        return 

    def bounds45(self, n256):
        # In1 -> n256
        # sudoku/bounds45/lb
        n257 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds45/lb'] = n257
        # sudoku/bounds45/leq -> n258
        n258 = self.context.mk_leq(n257, n256)
        self.nets['sudoku/bounds45/leq'] = n258
        # sudoku/bounds45/ub
        n259 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds45/ub'] = n259
        # sudoku/bounds45/geq -> n260
        n260 = self.context.mk_leq(n256, n259)
        self.nets['sudoku/bounds45/geq'] = n260
        # sudoku/bounds45/Logical Operator -> n261
        n261 = self.context.mk_and(n258, n260)
        self.nets['sudoku/bounds45/Logical Operator'] = n261
        # sudoku/bounds45/Assumption
        self.context.mk_assumption(n261)
        return 

    def bounds44(self, n263):
        # In1 -> n263
        # sudoku/bounds44/lb
        n264 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds44/lb'] = n264
        # sudoku/bounds44/leq -> n265
        n265 = self.context.mk_leq(n264, n263)
        self.nets['sudoku/bounds44/leq'] = n265
        # sudoku/bounds44/ub
        n266 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds44/ub'] = n266
        # sudoku/bounds44/geq -> n267
        n267 = self.context.mk_leq(n263, n266)
        self.nets['sudoku/bounds44/geq'] = n267
        # sudoku/bounds44/Logical Operator -> n268
        n268 = self.context.mk_and(n265, n267)
        self.nets['sudoku/bounds44/Logical Operator'] = n268
        # sudoku/bounds44/Assumption
        self.context.mk_assumption(n268)
        return 

    def bounds43(self, n270):
        # In1 -> n270
        # sudoku/bounds43/lb
        n271 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds43/lb'] = n271
        # sudoku/bounds43/leq -> n272
        n272 = self.context.mk_leq(n271, n270)
        self.nets['sudoku/bounds43/leq'] = n272
        # sudoku/bounds43/ub
        n273 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds43/ub'] = n273
        # sudoku/bounds43/geq -> n274
        n274 = self.context.mk_leq(n270, n273)
        self.nets['sudoku/bounds43/geq'] = n274
        # sudoku/bounds43/Logical Operator -> n275
        n275 = self.context.mk_and(n272, n274)
        self.nets['sudoku/bounds43/Logical Operator'] = n275
        # sudoku/bounds43/Assumption
        self.context.mk_assumption(n275)
        return 

    def bounds1(self, n277):
        # In1 -> n277
        # sudoku/bounds1/lb
        n278 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds1/lb'] = n278
        # sudoku/bounds1/leq -> n279
        n279 = self.context.mk_leq(n278, n277)
        self.nets['sudoku/bounds1/leq'] = n279
        # sudoku/bounds1/ub
        n280 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds1/ub'] = n280
        # sudoku/bounds1/geq -> n281
        n281 = self.context.mk_leq(n277, n280)
        self.nets['sudoku/bounds1/geq'] = n281
        # sudoku/bounds1/Logical Operator -> n282
        n282 = self.context.mk_and(n279, n281)
        self.nets['sudoku/bounds1/Logical Operator'] = n282
        # sudoku/bounds1/Assumption
        self.context.mk_assumption(n282)
        return 

    def bounds2(self, n284):
        # In1 -> n284
        # sudoku/bounds2/lb
        n285 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds2/lb'] = n285
        # sudoku/bounds2/leq -> n286
        n286 = self.context.mk_leq(n285, n284)
        self.nets['sudoku/bounds2/leq'] = n286
        # sudoku/bounds2/ub
        n287 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds2/ub'] = n287
        # sudoku/bounds2/geq -> n288
        n288 = self.context.mk_leq(n284, n287)
        self.nets['sudoku/bounds2/geq'] = n288
        # sudoku/bounds2/Logical Operator -> n289
        n289 = self.context.mk_and(n286, n288)
        self.nets['sudoku/bounds2/Logical Operator'] = n289
        # sudoku/bounds2/Assumption
        self.context.mk_assumption(n289)
        return 

    def bounds3(self, n291):
        # In1 -> n291
        # sudoku/bounds3/lb
        n292 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds3/lb'] = n292
        # sudoku/bounds3/leq -> n293
        n293 = self.context.mk_leq(n292, n291)
        self.nets['sudoku/bounds3/leq'] = n293
        # sudoku/bounds3/ub
        n294 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds3/ub'] = n294
        # sudoku/bounds3/geq -> n295
        n295 = self.context.mk_leq(n291, n294)
        self.nets['sudoku/bounds3/geq'] = n295
        # sudoku/bounds3/Logical Operator -> n296
        n296 = self.context.mk_and(n293, n295)
        self.nets['sudoku/bounds3/Logical Operator'] = n296
        # sudoku/bounds3/Assumption
        self.context.mk_assumption(n296)
        return 

    def bounds4(self, n298):
        # In1 -> n298
        # sudoku/bounds4/lb
        n299 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds4/lb'] = n299
        # sudoku/bounds4/leq -> n300
        n300 = self.context.mk_leq(n299, n298)
        self.nets['sudoku/bounds4/leq'] = n300
        # sudoku/bounds4/ub
        n301 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds4/ub'] = n301
        # sudoku/bounds4/geq -> n302
        n302 = self.context.mk_leq(n298, n301)
        self.nets['sudoku/bounds4/geq'] = n302
        # sudoku/bounds4/Logical Operator -> n303
        n303 = self.context.mk_and(n300, n302)
        self.nets['sudoku/bounds4/Logical Operator'] = n303
        # sudoku/bounds4/Assumption
        self.context.mk_assumption(n303)
        return 

    def bounds39(self, n305):
        # In1 -> n305
        # sudoku/bounds39/lb
        n306 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds39/lb'] = n306
        # sudoku/bounds39/leq -> n307
        n307 = self.context.mk_leq(n306, n305)
        self.nets['sudoku/bounds39/leq'] = n307
        # sudoku/bounds39/ub
        n308 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds39/ub'] = n308
        # sudoku/bounds39/geq -> n309
        n309 = self.context.mk_leq(n305, n308)
        self.nets['sudoku/bounds39/geq'] = n309
        # sudoku/bounds39/Logical Operator -> n310
        n310 = self.context.mk_and(n307, n309)
        self.nets['sudoku/bounds39/Logical Operator'] = n310
        # sudoku/bounds39/Assumption
        self.context.mk_assumption(n310)
        return 

    def bounds38(self, n312):
        # In1 -> n312
        # sudoku/bounds38/lb
        n313 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds38/lb'] = n313
        # sudoku/bounds38/leq -> n314
        n314 = self.context.mk_leq(n313, n312)
        self.nets['sudoku/bounds38/leq'] = n314
        # sudoku/bounds38/ub
        n315 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds38/ub'] = n315
        # sudoku/bounds38/geq -> n316
        n316 = self.context.mk_leq(n312, n315)
        self.nets['sudoku/bounds38/geq'] = n316
        # sudoku/bounds38/Logical Operator -> n317
        n317 = self.context.mk_and(n314, n316)
        self.nets['sudoku/bounds38/Logical Operator'] = n317
        # sudoku/bounds38/Assumption
        self.context.mk_assumption(n317)
        return 

    def bounds37(self, n319):
        # In1 -> n319
        # sudoku/bounds37/lb
        n320 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds37/lb'] = n320
        # sudoku/bounds37/leq -> n321
        n321 = self.context.mk_leq(n320, n319)
        self.nets['sudoku/bounds37/leq'] = n321
        # sudoku/bounds37/ub
        n322 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds37/ub'] = n322
        # sudoku/bounds37/geq -> n323
        n323 = self.context.mk_leq(n319, n322)
        self.nets['sudoku/bounds37/geq'] = n323
        # sudoku/bounds37/Logical Operator -> n324
        n324 = self.context.mk_and(n321, n323)
        self.nets['sudoku/bounds37/Logical Operator'] = n324
        # sudoku/bounds37/Assumption
        self.context.mk_assumption(n324)
        return 

    def bounds36(self, n326):
        # In1 -> n326
        # sudoku/bounds36/lb
        n327 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds36/lb'] = n327
        # sudoku/bounds36/leq -> n328
        n328 = self.context.mk_leq(n327, n326)
        self.nets['sudoku/bounds36/leq'] = n328
        # sudoku/bounds36/ub
        n329 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds36/ub'] = n329
        # sudoku/bounds36/geq -> n330
        n330 = self.context.mk_leq(n326, n329)
        self.nets['sudoku/bounds36/geq'] = n330
        # sudoku/bounds36/Logical Operator -> n331
        n331 = self.context.mk_and(n328, n330)
        self.nets['sudoku/bounds36/Logical Operator'] = n331
        # sudoku/bounds36/Assumption
        self.context.mk_assumption(n331)
        return 

    def bounds(self, n333):
        # In1 -> n333
        # sudoku/bounds/lb
        n334 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds/lb'] = n334
        # sudoku/bounds/leq -> n335
        n335 = self.context.mk_leq(n334, n333)
        self.nets['sudoku/bounds/leq'] = n335
        # sudoku/bounds/ub
        n336 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds/ub'] = n336
        # sudoku/bounds/geq -> n337
        n337 = self.context.mk_leq(n333, n336)
        self.nets['sudoku/bounds/geq'] = n337
        # sudoku/bounds/Logical Operator -> n338
        n338 = self.context.mk_and(n335, n337)
        self.nets['sudoku/bounds/Logical Operator'] = n338
        # sudoku/bounds/Assumption
        self.context.mk_assumption(n338)
        return 

    def bounds31(self, n340):
        # In1 -> n340
        # sudoku/bounds31/lb
        n341 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds31/lb'] = n341
        # sudoku/bounds31/leq -> n342
        n342 = self.context.mk_leq(n341, n340)
        self.nets['sudoku/bounds31/leq'] = n342
        # sudoku/bounds31/ub
        n343 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds31/ub'] = n343
        # sudoku/bounds31/geq -> n344
        n344 = self.context.mk_leq(n340, n343)
        self.nets['sudoku/bounds31/geq'] = n344
        # sudoku/bounds31/Logical Operator -> n345
        n345 = self.context.mk_and(n342, n344)
        self.nets['sudoku/bounds31/Logical Operator'] = n345
        # sudoku/bounds31/Assumption
        self.context.mk_assumption(n345)
        return 

    def bounds30(self, n347):
        # In1 -> n347
        # sudoku/bounds30/lb
        n348 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds30/lb'] = n348
        # sudoku/bounds30/leq -> n349
        n349 = self.context.mk_leq(n348, n347)
        self.nets['sudoku/bounds30/leq'] = n349
        # sudoku/bounds30/ub
        n350 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds30/ub'] = n350
        # sudoku/bounds30/geq -> n351
        n351 = self.context.mk_leq(n347, n350)
        self.nets['sudoku/bounds30/geq'] = n351
        # sudoku/bounds30/Logical Operator -> n352
        n352 = self.context.mk_and(n349, n351)
        self.nets['sudoku/bounds30/Logical Operator'] = n352
        # sudoku/bounds30/Assumption
        self.context.mk_assumption(n352)
        return 

    def bounds35(self, n354):
        # In1 -> n354
        # sudoku/bounds35/lb
        n355 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds35/lb'] = n355
        # sudoku/bounds35/leq -> n356
        n356 = self.context.mk_leq(n355, n354)
        self.nets['sudoku/bounds35/leq'] = n356
        # sudoku/bounds35/ub
        n357 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds35/ub'] = n357
        # sudoku/bounds35/geq -> n358
        n358 = self.context.mk_leq(n354, n357)
        self.nets['sudoku/bounds35/geq'] = n358
        # sudoku/bounds35/Logical Operator -> n359
        n359 = self.context.mk_and(n356, n358)
        self.nets['sudoku/bounds35/Logical Operator'] = n359
        # sudoku/bounds35/Assumption
        self.context.mk_assumption(n359)
        return 

    def bounds34(self, n361):
        # In1 -> n361
        # sudoku/bounds34/lb
        n362 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds34/lb'] = n362
        # sudoku/bounds34/leq -> n363
        n363 = self.context.mk_leq(n362, n361)
        self.nets['sudoku/bounds34/leq'] = n363
        # sudoku/bounds34/ub
        n364 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds34/ub'] = n364
        # sudoku/bounds34/geq -> n365
        n365 = self.context.mk_leq(n361, n364)
        self.nets['sudoku/bounds34/geq'] = n365
        # sudoku/bounds34/Logical Operator -> n366
        n366 = self.context.mk_and(n363, n365)
        self.nets['sudoku/bounds34/Logical Operator'] = n366
        # sudoku/bounds34/Assumption
        self.context.mk_assumption(n366)
        return 

    def bounds33(self, n368):
        # In1 -> n368
        # sudoku/bounds33/lb
        n369 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds33/lb'] = n369
        # sudoku/bounds33/leq -> n370
        n370 = self.context.mk_leq(n369, n368)
        self.nets['sudoku/bounds33/leq'] = n370
        # sudoku/bounds33/ub
        n371 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds33/ub'] = n371
        # sudoku/bounds33/geq -> n372
        n372 = self.context.mk_leq(n368, n371)
        self.nets['sudoku/bounds33/geq'] = n372
        # sudoku/bounds33/Logical Operator -> n373
        n373 = self.context.mk_and(n370, n372)
        self.nets['sudoku/bounds33/Logical Operator'] = n373
        # sudoku/bounds33/Assumption
        self.context.mk_assumption(n373)
        return 

    def bounds32(self, n375):
        # In1 -> n375
        # sudoku/bounds32/lb
        n376 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds32/lb'] = n376
        # sudoku/bounds32/leq -> n377
        n377 = self.context.mk_leq(n376, n375)
        self.nets['sudoku/bounds32/leq'] = n377
        # sudoku/bounds32/ub
        n378 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds32/ub'] = n378
        # sudoku/bounds32/geq -> n379
        n379 = self.context.mk_leq(n375, n378)
        self.nets['sudoku/bounds32/geq'] = n379
        # sudoku/bounds32/Logical Operator -> n380
        n380 = self.context.mk_and(n377, n379)
        self.nets['sudoku/bounds32/Logical Operator'] = n380
        # sudoku/bounds32/Assumption
        self.context.mk_assumption(n380)
        return 

    def col_6(self, n382, n383, n384, n385, n386, n387, n388, n389, n390):
        # In1 -> n382
        # In2 -> n383
        # In3 -> n384
        # In4 -> n385
        # In5 -> n386
        # In6 -> n387
        # In7 -> n388
        # In8 -> n389
        # In9 -> n390
        # sudoku/columns/col_6/diff36 -> n391
        n391 = self.context.mk_neq(n389, n390)
        self.nets['sudoku/columns/col_6/diff36'] = n391
        # sudoku/columns/col_6/diff34 -> n392
        n392 = self.context.mk_neq(n388, n389)
        self.nets['sudoku/columns/col_6/diff34'] = n392
        # sudoku/columns/col_6/diff35 -> n393
        n393 = self.context.mk_neq(n388, n390)
        self.nets['sudoku/columns/col_6/diff35'] = n393
        # sudoku/columns/col_6/Logical Operator6 -> n394
        n394 = self.context.mk_and(n392, n393)
        self.nets['sudoku/columns/col_6/Logical Operator6'] = n394
        # sudoku/columns/col_6/diff31 -> n395
        n395 = self.context.mk_neq(n387, n388)
        self.nets['sudoku/columns/col_6/diff31'] = n395
        # sudoku/columns/col_6/diff32 -> n396
        n396 = self.context.mk_neq(n387, n389)
        self.nets['sudoku/columns/col_6/diff32'] = n396
        # sudoku/columns/col_6/diff33 -> n397
        n397 = self.context.mk_neq(n387, n390)
        self.nets['sudoku/columns/col_6/diff33'] = n397
        # sudoku/columns/col_6/Logical Operator5 -> n398
        tn1 = self.context.mk_and(n396, n397)
        n398 = self.context.mk_and(n395, tn1)
        self.nets['sudoku/columns/col_6/Logical Operator5'] = n398
        # sudoku/columns/col_6/diff27 -> n399
        n399 = self.context.mk_neq(n386, n387)
        self.nets['sudoku/columns/col_6/diff27'] = n399
        # sudoku/columns/col_6/diff28 -> n400
        n400 = self.context.mk_neq(n386, n388)
        self.nets['sudoku/columns/col_6/diff28'] = n400
        # sudoku/columns/col_6/diff29 -> n401
        n401 = self.context.mk_neq(n386, n389)
        self.nets['sudoku/columns/col_6/diff29'] = n401
        # sudoku/columns/col_6/diff30 -> n402
        n402 = self.context.mk_neq(n386, n390)
        self.nets['sudoku/columns/col_6/diff30'] = n402
        # sudoku/columns/col_6/Logical Operator4 -> n403
        tn3 = self.context.mk_and(n401, n402)
        tn2 = self.context.mk_and(n400, tn3)
        n403 = self.context.mk_and(n399, tn2)
        self.nets['sudoku/columns/col_6/Logical Operator4'] = n403
        # sudoku/columns/col_6/diff22 -> n404
        n404 = self.context.mk_neq(n385, n386)
        self.nets['sudoku/columns/col_6/diff22'] = n404
        # sudoku/columns/col_6/diff23 -> n405
        n405 = self.context.mk_neq(n385, n387)
        self.nets['sudoku/columns/col_6/diff23'] = n405
        # sudoku/columns/col_6/diff24 -> n406
        n406 = self.context.mk_neq(n385, n388)
        self.nets['sudoku/columns/col_6/diff24'] = n406
        # sudoku/columns/col_6/diff25 -> n407
        n407 = self.context.mk_neq(n385, n389)
        self.nets['sudoku/columns/col_6/diff25'] = n407
        # sudoku/columns/col_6/diff26 -> n408
        n408 = self.context.mk_neq(n385, n390)
        self.nets['sudoku/columns/col_6/diff26'] = n408
        # sudoku/columns/col_6/Logical Operator3 -> n409
        tn6 = self.context.mk_and(n407, n408)
        tn5 = self.context.mk_and(n406, tn6)
        tn4 = self.context.mk_and(n405, tn5)
        n409 = self.context.mk_and(n404, tn4)
        self.nets['sudoku/columns/col_6/Logical Operator3'] = n409
        # sudoku/columns/col_6/diff16 -> n410
        n410 = self.context.mk_neq(n384, n385)
        self.nets['sudoku/columns/col_6/diff16'] = n410
        # sudoku/columns/col_6/diff17 -> n411
        n411 = self.context.mk_neq(n384, n386)
        self.nets['sudoku/columns/col_6/diff17'] = n411
        # sudoku/columns/col_6/diff18 -> n412
        n412 = self.context.mk_neq(n384, n387)
        self.nets['sudoku/columns/col_6/diff18'] = n412
        # sudoku/columns/col_6/diff19 -> n413
        n413 = self.context.mk_neq(n384, n388)
        self.nets['sudoku/columns/col_6/diff19'] = n413
        # sudoku/columns/col_6/diff20 -> n414
        n414 = self.context.mk_neq(n384, n389)
        self.nets['sudoku/columns/col_6/diff20'] = n414
        # sudoku/columns/col_6/diff21 -> n415
        n415 = self.context.mk_neq(n384, n390)
        self.nets['sudoku/columns/col_6/diff21'] = n415
        # sudoku/columns/col_6/Logical Operator2 -> n416
        tn10 = self.context.mk_and(n414, n415)
        tn9 = self.context.mk_and(n413, tn10)
        tn8 = self.context.mk_and(n412, tn9)
        tn7 = self.context.mk_and(n411, tn8)
        n416 = self.context.mk_and(n410, tn7)
        self.nets['sudoku/columns/col_6/Logical Operator2'] = n416
        # sudoku/columns/col_6/diff9 -> n417
        n417 = self.context.mk_neq(n383, n384)
        self.nets['sudoku/columns/col_6/diff9'] = n417
        # sudoku/columns/col_6/diff10 -> n418
        n418 = self.context.mk_neq(n383, n385)
        self.nets['sudoku/columns/col_6/diff10'] = n418
        # sudoku/columns/col_6/diff11 -> n419
        n419 = self.context.mk_neq(n383, n386)
        self.nets['sudoku/columns/col_6/diff11'] = n419
        # sudoku/columns/col_6/diff12 -> n420
        n420 = self.context.mk_neq(n383, n387)
        self.nets['sudoku/columns/col_6/diff12'] = n420
        # sudoku/columns/col_6/diff13 -> n421
        n421 = self.context.mk_neq(n383, n388)
        self.nets['sudoku/columns/col_6/diff13'] = n421
        # sudoku/columns/col_6/diff14 -> n422
        n422 = self.context.mk_neq(n383, n389)
        self.nets['sudoku/columns/col_6/diff14'] = n422
        # sudoku/columns/col_6/diff15 -> n423
        n423 = self.context.mk_neq(n383, n390)
        self.nets['sudoku/columns/col_6/diff15'] = n423
        # sudoku/columns/col_6/Logical Operator1 -> n424
        tn15 = self.context.mk_and(n422, n423)
        tn14 = self.context.mk_and(n421, tn15)
        tn13 = self.context.mk_and(n420, tn14)
        tn12 = self.context.mk_and(n419, tn13)
        tn11 = self.context.mk_and(n418, tn12)
        n424 = self.context.mk_and(n417, tn11)
        self.nets['sudoku/columns/col_6/Logical Operator1'] = n424
        # sudoku/columns/col_6/diff1 -> n425
        n425 = self.context.mk_neq(n382, n383)
        self.nets['sudoku/columns/col_6/diff1'] = n425
        # sudoku/columns/col_6/diff2 -> n426
        n426 = self.context.mk_neq(n382, n384)
        self.nets['sudoku/columns/col_6/diff2'] = n426
        # sudoku/columns/col_6/diff3 -> n427
        n427 = self.context.mk_neq(n382, n385)
        self.nets['sudoku/columns/col_6/diff3'] = n427
        # sudoku/columns/col_6/diff4 -> n428
        n428 = self.context.mk_neq(n382, n386)
        self.nets['sudoku/columns/col_6/diff4'] = n428
        # sudoku/columns/col_6/diff5 -> n429
        n429 = self.context.mk_neq(n382, n387)
        self.nets['sudoku/columns/col_6/diff5'] = n429
        # sudoku/columns/col_6/diff6 -> n430
        n430 = self.context.mk_neq(n382, n388)
        self.nets['sudoku/columns/col_6/diff6'] = n430
        # sudoku/columns/col_6/diff7 -> n431
        n431 = self.context.mk_neq(n382, n389)
        self.nets['sudoku/columns/col_6/diff7'] = n431
        # sudoku/columns/col_6/diff8 -> n432
        n432 = self.context.mk_neq(n382, n390)
        self.nets['sudoku/columns/col_6/diff8'] = n432
        # sudoku/columns/col_6/Logical Operator -> n433
        tn21 = self.context.mk_and(n431, n432)
        tn20 = self.context.mk_and(n430, tn21)
        tn19 = self.context.mk_and(n429, tn20)
        tn18 = self.context.mk_and(n428, tn19)
        tn17 = self.context.mk_and(n427, tn18)
        tn16 = self.context.mk_and(n426, tn17)
        n433 = self.context.mk_and(n425, tn16)
        self.nets['sudoku/columns/col_6/Logical Operator'] = n433
        # sudoku/columns/col_6/Logical Operator7 -> n434
        tn27 = self.context.mk_and(n424, n433)
        tn26 = self.context.mk_and(n416, tn27)
        tn25 = self.context.mk_and(n409, tn26)
        tn24 = self.context.mk_and(n403, tn25)
        tn23 = self.context.mk_and(n398, tn24)
        tn22 = self.context.mk_and(n394, tn23)
        n434 = self.context.mk_and(n391, tn22)
        self.nets['sudoku/columns/col_6/Logical Operator7'] = n434
        # n434 -> Out1
        return n434

    def col_5(self, n436, n437, n438, n439, n440, n441, n442, n443, n444):
        # In1 -> n436
        # In2 -> n437
        # In3 -> n438
        # In4 -> n439
        # In5 -> n440
        # In6 -> n441
        # In7 -> n442
        # In8 -> n443
        # In9 -> n444
        # sudoku/columns/col_5/diff36 -> n445
        n445 = self.context.mk_neq(n443, n444)
        self.nets['sudoku/columns/col_5/diff36'] = n445
        # sudoku/columns/col_5/diff34 -> n446
        n446 = self.context.mk_neq(n442, n443)
        self.nets['sudoku/columns/col_5/diff34'] = n446
        # sudoku/columns/col_5/diff35 -> n447
        n447 = self.context.mk_neq(n442, n444)
        self.nets['sudoku/columns/col_5/diff35'] = n447
        # sudoku/columns/col_5/Logical Operator6 -> n448
        n448 = self.context.mk_and(n446, n447)
        self.nets['sudoku/columns/col_5/Logical Operator6'] = n448
        # sudoku/columns/col_5/diff31 -> n449
        n449 = self.context.mk_neq(n441, n442)
        self.nets['sudoku/columns/col_5/diff31'] = n449
        # sudoku/columns/col_5/diff32 -> n450
        n450 = self.context.mk_neq(n441, n443)
        self.nets['sudoku/columns/col_5/diff32'] = n450
        # sudoku/columns/col_5/diff33 -> n451
        n451 = self.context.mk_neq(n441, n444)
        self.nets['sudoku/columns/col_5/diff33'] = n451
        # sudoku/columns/col_5/Logical Operator5 -> n452
        tn28 = self.context.mk_and(n450, n451)
        n452 = self.context.mk_and(n449, tn28)
        self.nets['sudoku/columns/col_5/Logical Operator5'] = n452
        # sudoku/columns/col_5/diff27 -> n453
        n453 = self.context.mk_neq(n440, n441)
        self.nets['sudoku/columns/col_5/diff27'] = n453
        # sudoku/columns/col_5/diff28 -> n454
        n454 = self.context.mk_neq(n440, n442)
        self.nets['sudoku/columns/col_5/diff28'] = n454
        # sudoku/columns/col_5/diff29 -> n455
        n455 = self.context.mk_neq(n440, n443)
        self.nets['sudoku/columns/col_5/diff29'] = n455
        # sudoku/columns/col_5/diff30 -> n456
        n456 = self.context.mk_neq(n440, n444)
        self.nets['sudoku/columns/col_5/diff30'] = n456
        # sudoku/columns/col_5/Logical Operator4 -> n457
        tn30 = self.context.mk_and(n455, n456)
        tn29 = self.context.mk_and(n454, tn30)
        n457 = self.context.mk_and(n453, tn29)
        self.nets['sudoku/columns/col_5/Logical Operator4'] = n457
        # sudoku/columns/col_5/diff22 -> n458
        n458 = self.context.mk_neq(n439, n440)
        self.nets['sudoku/columns/col_5/diff22'] = n458
        # sudoku/columns/col_5/diff23 -> n459
        n459 = self.context.mk_neq(n439, n441)
        self.nets['sudoku/columns/col_5/diff23'] = n459
        # sudoku/columns/col_5/diff24 -> n460
        n460 = self.context.mk_neq(n439, n442)
        self.nets['sudoku/columns/col_5/diff24'] = n460
        # sudoku/columns/col_5/diff25 -> n461
        n461 = self.context.mk_neq(n439, n443)
        self.nets['sudoku/columns/col_5/diff25'] = n461
        # sudoku/columns/col_5/diff26 -> n462
        n462 = self.context.mk_neq(n439, n444)
        self.nets['sudoku/columns/col_5/diff26'] = n462
        # sudoku/columns/col_5/Logical Operator3 -> n463
        tn33 = self.context.mk_and(n461, n462)
        tn32 = self.context.mk_and(n460, tn33)
        tn31 = self.context.mk_and(n459, tn32)
        n463 = self.context.mk_and(n458, tn31)
        self.nets['sudoku/columns/col_5/Logical Operator3'] = n463
        # sudoku/columns/col_5/diff16 -> n464
        n464 = self.context.mk_neq(n438, n439)
        self.nets['sudoku/columns/col_5/diff16'] = n464
        # sudoku/columns/col_5/diff17 -> n465
        n465 = self.context.mk_neq(n438, n440)
        self.nets['sudoku/columns/col_5/diff17'] = n465
        # sudoku/columns/col_5/diff18 -> n466
        n466 = self.context.mk_neq(n438, n441)
        self.nets['sudoku/columns/col_5/diff18'] = n466
        # sudoku/columns/col_5/diff19 -> n467
        n467 = self.context.mk_neq(n438, n442)
        self.nets['sudoku/columns/col_5/diff19'] = n467
        # sudoku/columns/col_5/diff20 -> n468
        n468 = self.context.mk_neq(n438, n443)
        self.nets['sudoku/columns/col_5/diff20'] = n468
        # sudoku/columns/col_5/diff21 -> n469
        n469 = self.context.mk_neq(n438, n444)
        self.nets['sudoku/columns/col_5/diff21'] = n469
        # sudoku/columns/col_5/Logical Operator2 -> n470
        tn37 = self.context.mk_and(n468, n469)
        tn36 = self.context.mk_and(n467, tn37)
        tn35 = self.context.mk_and(n466, tn36)
        tn34 = self.context.mk_and(n465, tn35)
        n470 = self.context.mk_and(n464, tn34)
        self.nets['sudoku/columns/col_5/Logical Operator2'] = n470
        # sudoku/columns/col_5/diff9 -> n471
        n471 = self.context.mk_neq(n437, n438)
        self.nets['sudoku/columns/col_5/diff9'] = n471
        # sudoku/columns/col_5/diff10 -> n472
        n472 = self.context.mk_neq(n437, n439)
        self.nets['sudoku/columns/col_5/diff10'] = n472
        # sudoku/columns/col_5/diff11 -> n473
        n473 = self.context.mk_neq(n437, n440)
        self.nets['sudoku/columns/col_5/diff11'] = n473
        # sudoku/columns/col_5/diff12 -> n474
        n474 = self.context.mk_neq(n437, n441)
        self.nets['sudoku/columns/col_5/diff12'] = n474
        # sudoku/columns/col_5/diff13 -> n475
        n475 = self.context.mk_neq(n437, n442)
        self.nets['sudoku/columns/col_5/diff13'] = n475
        # sudoku/columns/col_5/diff14 -> n476
        n476 = self.context.mk_neq(n437, n443)
        self.nets['sudoku/columns/col_5/diff14'] = n476
        # sudoku/columns/col_5/diff15 -> n477
        n477 = self.context.mk_neq(n437, n444)
        self.nets['sudoku/columns/col_5/diff15'] = n477
        # sudoku/columns/col_5/Logical Operator1 -> n478
        tn42 = self.context.mk_and(n476, n477)
        tn41 = self.context.mk_and(n475, tn42)
        tn40 = self.context.mk_and(n474, tn41)
        tn39 = self.context.mk_and(n473, tn40)
        tn38 = self.context.mk_and(n472, tn39)
        n478 = self.context.mk_and(n471, tn38)
        self.nets['sudoku/columns/col_5/Logical Operator1'] = n478
        # sudoku/columns/col_5/diff1 -> n479
        n479 = self.context.mk_neq(n436, n437)
        self.nets['sudoku/columns/col_5/diff1'] = n479
        # sudoku/columns/col_5/diff2 -> n480
        n480 = self.context.mk_neq(n436, n438)
        self.nets['sudoku/columns/col_5/diff2'] = n480
        # sudoku/columns/col_5/diff3 -> n481
        n481 = self.context.mk_neq(n436, n439)
        self.nets['sudoku/columns/col_5/diff3'] = n481
        # sudoku/columns/col_5/diff4 -> n482
        n482 = self.context.mk_neq(n436, n440)
        self.nets['sudoku/columns/col_5/diff4'] = n482
        # sudoku/columns/col_5/diff5 -> n483
        n483 = self.context.mk_neq(n436, n441)
        self.nets['sudoku/columns/col_5/diff5'] = n483
        # sudoku/columns/col_5/diff6 -> n484
        n484 = self.context.mk_neq(n436, n442)
        self.nets['sudoku/columns/col_5/diff6'] = n484
        # sudoku/columns/col_5/diff7 -> n485
        n485 = self.context.mk_neq(n436, n443)
        self.nets['sudoku/columns/col_5/diff7'] = n485
        # sudoku/columns/col_5/diff8 -> n486
        n486 = self.context.mk_neq(n436, n444)
        self.nets['sudoku/columns/col_5/diff8'] = n486
        # sudoku/columns/col_5/Logical Operator -> n487
        tn48 = self.context.mk_and(n485, n486)
        tn47 = self.context.mk_and(n484, tn48)
        tn46 = self.context.mk_and(n483, tn47)
        tn45 = self.context.mk_and(n482, tn46)
        tn44 = self.context.mk_and(n481, tn45)
        tn43 = self.context.mk_and(n480, tn44)
        n487 = self.context.mk_and(n479, tn43)
        self.nets['sudoku/columns/col_5/Logical Operator'] = n487
        # sudoku/columns/col_5/Logical Operator7 -> n488
        tn54 = self.context.mk_and(n478, n487)
        tn53 = self.context.mk_and(n470, tn54)
        tn52 = self.context.mk_and(n463, tn53)
        tn51 = self.context.mk_and(n457, tn52)
        tn50 = self.context.mk_and(n452, tn51)
        tn49 = self.context.mk_and(n448, tn50)
        n488 = self.context.mk_and(n445, tn49)
        self.nets['sudoku/columns/col_5/Logical Operator7'] = n488
        # n488 -> Out1
        return n488

    def col_4(self, n490, n491, n492, n493, n494, n495, n496, n497, n498):
        # In1 -> n490
        # In2 -> n491
        # In3 -> n492
        # In4 -> n493
        # In5 -> n494
        # In6 -> n495
        # In7 -> n496
        # In8 -> n497
        # In9 -> n498
        # sudoku/columns/col_4/diff36 -> n499
        n499 = self.context.mk_neq(n497, n498)
        self.nets['sudoku/columns/col_4/diff36'] = n499
        # sudoku/columns/col_4/diff34 -> n500
        n500 = self.context.mk_neq(n496, n497)
        self.nets['sudoku/columns/col_4/diff34'] = n500
        # sudoku/columns/col_4/diff35 -> n501
        n501 = self.context.mk_neq(n496, n498)
        self.nets['sudoku/columns/col_4/diff35'] = n501
        # sudoku/columns/col_4/Logical Operator6 -> n502
        n502 = self.context.mk_and(n500, n501)
        self.nets['sudoku/columns/col_4/Logical Operator6'] = n502
        # sudoku/columns/col_4/diff31 -> n503
        n503 = self.context.mk_neq(n495, n496)
        self.nets['sudoku/columns/col_4/diff31'] = n503
        # sudoku/columns/col_4/diff32 -> n504
        n504 = self.context.mk_neq(n495, n497)
        self.nets['sudoku/columns/col_4/diff32'] = n504
        # sudoku/columns/col_4/diff33 -> n505
        n505 = self.context.mk_neq(n495, n498)
        self.nets['sudoku/columns/col_4/diff33'] = n505
        # sudoku/columns/col_4/Logical Operator5 -> n506
        tn55 = self.context.mk_and(n504, n505)
        n506 = self.context.mk_and(n503, tn55)
        self.nets['sudoku/columns/col_4/Logical Operator5'] = n506
        # sudoku/columns/col_4/diff27 -> n507
        n507 = self.context.mk_neq(n494, n495)
        self.nets['sudoku/columns/col_4/diff27'] = n507
        # sudoku/columns/col_4/diff28 -> n508
        n508 = self.context.mk_neq(n494, n496)
        self.nets['sudoku/columns/col_4/diff28'] = n508
        # sudoku/columns/col_4/diff29 -> n509
        n509 = self.context.mk_neq(n494, n497)
        self.nets['sudoku/columns/col_4/diff29'] = n509
        # sudoku/columns/col_4/diff30 -> n510
        n510 = self.context.mk_neq(n494, n498)
        self.nets['sudoku/columns/col_4/diff30'] = n510
        # sudoku/columns/col_4/Logical Operator4 -> n511
        tn57 = self.context.mk_and(n509, n510)
        tn56 = self.context.mk_and(n508, tn57)
        n511 = self.context.mk_and(n507, tn56)
        self.nets['sudoku/columns/col_4/Logical Operator4'] = n511
        # sudoku/columns/col_4/diff22 -> n512
        n512 = self.context.mk_neq(n493, n494)
        self.nets['sudoku/columns/col_4/diff22'] = n512
        # sudoku/columns/col_4/diff23 -> n513
        n513 = self.context.mk_neq(n493, n495)
        self.nets['sudoku/columns/col_4/diff23'] = n513
        # sudoku/columns/col_4/diff24 -> n514
        n514 = self.context.mk_neq(n493, n496)
        self.nets['sudoku/columns/col_4/diff24'] = n514
        # sudoku/columns/col_4/diff25 -> n515
        n515 = self.context.mk_neq(n493, n497)
        self.nets['sudoku/columns/col_4/diff25'] = n515
        # sudoku/columns/col_4/diff26 -> n516
        n516 = self.context.mk_neq(n493, n498)
        self.nets['sudoku/columns/col_4/diff26'] = n516
        # sudoku/columns/col_4/Logical Operator3 -> n517
        tn60 = self.context.mk_and(n515, n516)
        tn59 = self.context.mk_and(n514, tn60)
        tn58 = self.context.mk_and(n513, tn59)
        n517 = self.context.mk_and(n512, tn58)
        self.nets['sudoku/columns/col_4/Logical Operator3'] = n517
        # sudoku/columns/col_4/diff16 -> n518
        n518 = self.context.mk_neq(n492, n493)
        self.nets['sudoku/columns/col_4/diff16'] = n518
        # sudoku/columns/col_4/diff17 -> n519
        n519 = self.context.mk_neq(n492, n494)
        self.nets['sudoku/columns/col_4/diff17'] = n519
        # sudoku/columns/col_4/diff18 -> n520
        n520 = self.context.mk_neq(n492, n495)
        self.nets['sudoku/columns/col_4/diff18'] = n520
        # sudoku/columns/col_4/diff19 -> n521
        n521 = self.context.mk_neq(n492, n496)
        self.nets['sudoku/columns/col_4/diff19'] = n521
        # sudoku/columns/col_4/diff20 -> n522
        n522 = self.context.mk_neq(n492, n497)
        self.nets['sudoku/columns/col_4/diff20'] = n522
        # sudoku/columns/col_4/diff21 -> n523
        n523 = self.context.mk_neq(n492, n498)
        self.nets['sudoku/columns/col_4/diff21'] = n523
        # sudoku/columns/col_4/Logical Operator2 -> n524
        tn64 = self.context.mk_and(n522, n523)
        tn63 = self.context.mk_and(n521, tn64)
        tn62 = self.context.mk_and(n520, tn63)
        tn61 = self.context.mk_and(n519, tn62)
        n524 = self.context.mk_and(n518, tn61)
        self.nets['sudoku/columns/col_4/Logical Operator2'] = n524
        # sudoku/columns/col_4/diff9 -> n525
        n525 = self.context.mk_neq(n491, n492)
        self.nets['sudoku/columns/col_4/diff9'] = n525
        # sudoku/columns/col_4/diff10 -> n526
        n526 = self.context.mk_neq(n491, n493)
        self.nets['sudoku/columns/col_4/diff10'] = n526
        # sudoku/columns/col_4/diff11 -> n527
        n527 = self.context.mk_neq(n491, n494)
        self.nets['sudoku/columns/col_4/diff11'] = n527
        # sudoku/columns/col_4/diff12 -> n528
        n528 = self.context.mk_neq(n491, n495)
        self.nets['sudoku/columns/col_4/diff12'] = n528
        # sudoku/columns/col_4/diff13 -> n529
        n529 = self.context.mk_neq(n491, n496)
        self.nets['sudoku/columns/col_4/diff13'] = n529
        # sudoku/columns/col_4/diff14 -> n530
        n530 = self.context.mk_neq(n491, n497)
        self.nets['sudoku/columns/col_4/diff14'] = n530
        # sudoku/columns/col_4/diff15 -> n531
        n531 = self.context.mk_neq(n491, n498)
        self.nets['sudoku/columns/col_4/diff15'] = n531
        # sudoku/columns/col_4/Logical Operator1 -> n532
        tn69 = self.context.mk_and(n530, n531)
        tn68 = self.context.mk_and(n529, tn69)
        tn67 = self.context.mk_and(n528, tn68)
        tn66 = self.context.mk_and(n527, tn67)
        tn65 = self.context.mk_and(n526, tn66)
        n532 = self.context.mk_and(n525, tn65)
        self.nets['sudoku/columns/col_4/Logical Operator1'] = n532
        # sudoku/columns/col_4/diff1 -> n533
        n533 = self.context.mk_neq(n490, n491)
        self.nets['sudoku/columns/col_4/diff1'] = n533
        # sudoku/columns/col_4/diff2 -> n534
        n534 = self.context.mk_neq(n490, n492)
        self.nets['sudoku/columns/col_4/diff2'] = n534
        # sudoku/columns/col_4/diff3 -> n535
        n535 = self.context.mk_neq(n490, n493)
        self.nets['sudoku/columns/col_4/diff3'] = n535
        # sudoku/columns/col_4/diff4 -> n536
        n536 = self.context.mk_neq(n490, n494)
        self.nets['sudoku/columns/col_4/diff4'] = n536
        # sudoku/columns/col_4/diff5 -> n537
        n537 = self.context.mk_neq(n490, n495)
        self.nets['sudoku/columns/col_4/diff5'] = n537
        # sudoku/columns/col_4/diff6 -> n538
        n538 = self.context.mk_neq(n490, n496)
        self.nets['sudoku/columns/col_4/diff6'] = n538
        # sudoku/columns/col_4/diff7 -> n539
        n539 = self.context.mk_neq(n490, n497)
        self.nets['sudoku/columns/col_4/diff7'] = n539
        # sudoku/columns/col_4/diff8 -> n540
        n540 = self.context.mk_neq(n490, n498)
        self.nets['sudoku/columns/col_4/diff8'] = n540
        # sudoku/columns/col_4/Logical Operator -> n541
        tn75 = self.context.mk_and(n539, n540)
        tn74 = self.context.mk_and(n538, tn75)
        tn73 = self.context.mk_and(n537, tn74)
        tn72 = self.context.mk_and(n536, tn73)
        tn71 = self.context.mk_and(n535, tn72)
        tn70 = self.context.mk_and(n534, tn71)
        n541 = self.context.mk_and(n533, tn70)
        self.nets['sudoku/columns/col_4/Logical Operator'] = n541
        # sudoku/columns/col_4/Logical Operator7 -> n542
        tn81 = self.context.mk_and(n532, n541)
        tn80 = self.context.mk_and(n524, tn81)
        tn79 = self.context.mk_and(n517, tn80)
        tn78 = self.context.mk_and(n511, tn79)
        tn77 = self.context.mk_and(n506, tn78)
        tn76 = self.context.mk_and(n502, tn77)
        n542 = self.context.mk_and(n499, tn76)
        self.nets['sudoku/columns/col_4/Logical Operator7'] = n542
        # n542 -> Out1
        return n542

    def col_3(self, n544, n545, n546, n547, n548, n549, n550, n551, n552):
        # In1 -> n544
        # In2 -> n545
        # In3 -> n546
        # In4 -> n547
        # In5 -> n548
        # In6 -> n549
        # In7 -> n550
        # In8 -> n551
        # In9 -> n552
        # sudoku/columns/col_3/diff36 -> n553
        n553 = self.context.mk_neq(n551, n552)
        self.nets['sudoku/columns/col_3/diff36'] = n553
        # sudoku/columns/col_3/diff34 -> n554
        n554 = self.context.mk_neq(n550, n551)
        self.nets['sudoku/columns/col_3/diff34'] = n554
        # sudoku/columns/col_3/diff35 -> n555
        n555 = self.context.mk_neq(n550, n552)
        self.nets['sudoku/columns/col_3/diff35'] = n555
        # sudoku/columns/col_3/Logical Operator6 -> n556
        n556 = self.context.mk_and(n554, n555)
        self.nets['sudoku/columns/col_3/Logical Operator6'] = n556
        # sudoku/columns/col_3/diff31 -> n557
        n557 = self.context.mk_neq(n549, n550)
        self.nets['sudoku/columns/col_3/diff31'] = n557
        # sudoku/columns/col_3/diff32 -> n558
        n558 = self.context.mk_neq(n549, n551)
        self.nets['sudoku/columns/col_3/diff32'] = n558
        # sudoku/columns/col_3/diff33 -> n559
        n559 = self.context.mk_neq(n549, n552)
        self.nets['sudoku/columns/col_3/diff33'] = n559
        # sudoku/columns/col_3/Logical Operator5 -> n560
        tn82 = self.context.mk_and(n558, n559)
        n560 = self.context.mk_and(n557, tn82)
        self.nets['sudoku/columns/col_3/Logical Operator5'] = n560
        # sudoku/columns/col_3/diff27 -> n561
        n561 = self.context.mk_neq(n548, n549)
        self.nets['sudoku/columns/col_3/diff27'] = n561
        # sudoku/columns/col_3/diff28 -> n562
        n562 = self.context.mk_neq(n548, n550)
        self.nets['sudoku/columns/col_3/diff28'] = n562
        # sudoku/columns/col_3/diff29 -> n563
        n563 = self.context.mk_neq(n548, n551)
        self.nets['sudoku/columns/col_3/diff29'] = n563
        # sudoku/columns/col_3/diff30 -> n564
        n564 = self.context.mk_neq(n548, n552)
        self.nets['sudoku/columns/col_3/diff30'] = n564
        # sudoku/columns/col_3/Logical Operator4 -> n565
        tn84 = self.context.mk_and(n563, n564)
        tn83 = self.context.mk_and(n562, tn84)
        n565 = self.context.mk_and(n561, tn83)
        self.nets['sudoku/columns/col_3/Logical Operator4'] = n565
        # sudoku/columns/col_3/diff22 -> n566
        n566 = self.context.mk_neq(n547, n548)
        self.nets['sudoku/columns/col_3/diff22'] = n566
        # sudoku/columns/col_3/diff23 -> n567
        n567 = self.context.mk_neq(n547, n549)
        self.nets['sudoku/columns/col_3/diff23'] = n567
        # sudoku/columns/col_3/diff24 -> n568
        n568 = self.context.mk_neq(n547, n550)
        self.nets['sudoku/columns/col_3/diff24'] = n568
        # sudoku/columns/col_3/diff25 -> n569
        n569 = self.context.mk_neq(n547, n551)
        self.nets['sudoku/columns/col_3/diff25'] = n569
        # sudoku/columns/col_3/diff26 -> n570
        n570 = self.context.mk_neq(n547, n552)
        self.nets['sudoku/columns/col_3/diff26'] = n570
        # sudoku/columns/col_3/Logical Operator3 -> n571
        tn87 = self.context.mk_and(n569, n570)
        tn86 = self.context.mk_and(n568, tn87)
        tn85 = self.context.mk_and(n567, tn86)
        n571 = self.context.mk_and(n566, tn85)
        self.nets['sudoku/columns/col_3/Logical Operator3'] = n571
        # sudoku/columns/col_3/diff16 -> n572
        n572 = self.context.mk_neq(n546, n547)
        self.nets['sudoku/columns/col_3/diff16'] = n572
        # sudoku/columns/col_3/diff17 -> n573
        n573 = self.context.mk_neq(n546, n548)
        self.nets['sudoku/columns/col_3/diff17'] = n573
        # sudoku/columns/col_3/diff18 -> n574
        n574 = self.context.mk_neq(n546, n549)
        self.nets['sudoku/columns/col_3/diff18'] = n574
        # sudoku/columns/col_3/diff19 -> n575
        n575 = self.context.mk_neq(n546, n550)
        self.nets['sudoku/columns/col_3/diff19'] = n575
        # sudoku/columns/col_3/diff20 -> n576
        n576 = self.context.mk_neq(n546, n551)
        self.nets['sudoku/columns/col_3/diff20'] = n576
        # sudoku/columns/col_3/diff21 -> n577
        n577 = self.context.mk_neq(n546, n552)
        self.nets['sudoku/columns/col_3/diff21'] = n577
        # sudoku/columns/col_3/Logical Operator2 -> n578
        tn91 = self.context.mk_and(n576, n577)
        tn90 = self.context.mk_and(n575, tn91)
        tn89 = self.context.mk_and(n574, tn90)
        tn88 = self.context.mk_and(n573, tn89)
        n578 = self.context.mk_and(n572, tn88)
        self.nets['sudoku/columns/col_3/Logical Operator2'] = n578
        # sudoku/columns/col_3/diff9 -> n579
        n579 = self.context.mk_neq(n545, n546)
        self.nets['sudoku/columns/col_3/diff9'] = n579
        # sudoku/columns/col_3/diff10 -> n580
        n580 = self.context.mk_neq(n545, n547)
        self.nets['sudoku/columns/col_3/diff10'] = n580
        # sudoku/columns/col_3/diff11 -> n581
        n581 = self.context.mk_neq(n545, n548)
        self.nets['sudoku/columns/col_3/diff11'] = n581
        # sudoku/columns/col_3/diff12 -> n582
        n582 = self.context.mk_neq(n545, n549)
        self.nets['sudoku/columns/col_3/diff12'] = n582
        # sudoku/columns/col_3/diff13 -> n583
        n583 = self.context.mk_neq(n545, n550)
        self.nets['sudoku/columns/col_3/diff13'] = n583
        # sudoku/columns/col_3/diff14 -> n584
        n584 = self.context.mk_neq(n545, n551)
        self.nets['sudoku/columns/col_3/diff14'] = n584
        # sudoku/columns/col_3/diff15 -> n585
        n585 = self.context.mk_neq(n545, n552)
        self.nets['sudoku/columns/col_3/diff15'] = n585
        # sudoku/columns/col_3/Logical Operator1 -> n586
        tn96 = self.context.mk_and(n584, n585)
        tn95 = self.context.mk_and(n583, tn96)
        tn94 = self.context.mk_and(n582, tn95)
        tn93 = self.context.mk_and(n581, tn94)
        tn92 = self.context.mk_and(n580, tn93)
        n586 = self.context.mk_and(n579, tn92)
        self.nets['sudoku/columns/col_3/Logical Operator1'] = n586
        # sudoku/columns/col_3/diff1 -> n587
        n587 = self.context.mk_neq(n544, n545)
        self.nets['sudoku/columns/col_3/diff1'] = n587
        # sudoku/columns/col_3/diff2 -> n588
        n588 = self.context.mk_neq(n544, n546)
        self.nets['sudoku/columns/col_3/diff2'] = n588
        # sudoku/columns/col_3/diff3 -> n589
        n589 = self.context.mk_neq(n544, n547)
        self.nets['sudoku/columns/col_3/diff3'] = n589
        # sudoku/columns/col_3/diff4 -> n590
        n590 = self.context.mk_neq(n544, n548)
        self.nets['sudoku/columns/col_3/diff4'] = n590
        # sudoku/columns/col_3/diff5 -> n591
        n591 = self.context.mk_neq(n544, n549)
        self.nets['sudoku/columns/col_3/diff5'] = n591
        # sudoku/columns/col_3/diff6 -> n592
        n592 = self.context.mk_neq(n544, n550)
        self.nets['sudoku/columns/col_3/diff6'] = n592
        # sudoku/columns/col_3/diff7 -> n593
        n593 = self.context.mk_neq(n544, n551)
        self.nets['sudoku/columns/col_3/diff7'] = n593
        # sudoku/columns/col_3/diff8 -> n594
        n594 = self.context.mk_neq(n544, n552)
        self.nets['sudoku/columns/col_3/diff8'] = n594
        # sudoku/columns/col_3/Logical Operator -> n595
        tn102 = self.context.mk_and(n593, n594)
        tn101 = self.context.mk_and(n592, tn102)
        tn100 = self.context.mk_and(n591, tn101)
        tn99 = self.context.mk_and(n590, tn100)
        tn98 = self.context.mk_and(n589, tn99)
        tn97 = self.context.mk_and(n588, tn98)
        n595 = self.context.mk_and(n587, tn97)
        self.nets['sudoku/columns/col_3/Logical Operator'] = n595
        # sudoku/columns/col_3/Logical Operator7 -> n596
        tn108 = self.context.mk_and(n586, n595)
        tn107 = self.context.mk_and(n578, tn108)
        tn106 = self.context.mk_and(n571, tn107)
        tn105 = self.context.mk_and(n565, tn106)
        tn104 = self.context.mk_and(n560, tn105)
        tn103 = self.context.mk_and(n556, tn104)
        n596 = self.context.mk_and(n553, tn103)
        self.nets['sudoku/columns/col_3/Logical Operator7'] = n596
        # n596 -> Out1
        return n596

    def col_2(self, n598, n599, n600, n601, n602, n603, n604, n605, n606):
        # In1 -> n598
        # In2 -> n599
        # In3 -> n600
        # In4 -> n601
        # In5 -> n602
        # In6 -> n603
        # In7 -> n604
        # In8 -> n605
        # In9 -> n606
        # sudoku/columns/col_2/diff36 -> n607
        n607 = self.context.mk_neq(n605, n606)
        self.nets['sudoku/columns/col_2/diff36'] = n607
        # sudoku/columns/col_2/diff34 -> n608
        n608 = self.context.mk_neq(n604, n605)
        self.nets['sudoku/columns/col_2/diff34'] = n608
        # sudoku/columns/col_2/diff35 -> n609
        n609 = self.context.mk_neq(n604, n606)
        self.nets['sudoku/columns/col_2/diff35'] = n609
        # sudoku/columns/col_2/Logical Operator6 -> n610
        n610 = self.context.mk_and(n608, n609)
        self.nets['sudoku/columns/col_2/Logical Operator6'] = n610
        # sudoku/columns/col_2/diff31 -> n611
        n611 = self.context.mk_neq(n603, n604)
        self.nets['sudoku/columns/col_2/diff31'] = n611
        # sudoku/columns/col_2/diff32 -> n612
        n612 = self.context.mk_neq(n603, n605)
        self.nets['sudoku/columns/col_2/diff32'] = n612
        # sudoku/columns/col_2/diff33 -> n613
        n613 = self.context.mk_neq(n603, n606)
        self.nets['sudoku/columns/col_2/diff33'] = n613
        # sudoku/columns/col_2/Logical Operator5 -> n614
        tn109 = self.context.mk_and(n612, n613)
        n614 = self.context.mk_and(n611, tn109)
        self.nets['sudoku/columns/col_2/Logical Operator5'] = n614
        # sudoku/columns/col_2/diff27 -> n615
        n615 = self.context.mk_neq(n602, n603)
        self.nets['sudoku/columns/col_2/diff27'] = n615
        # sudoku/columns/col_2/diff28 -> n616
        n616 = self.context.mk_neq(n602, n604)
        self.nets['sudoku/columns/col_2/diff28'] = n616
        # sudoku/columns/col_2/diff29 -> n617
        n617 = self.context.mk_neq(n602, n605)
        self.nets['sudoku/columns/col_2/diff29'] = n617
        # sudoku/columns/col_2/diff30 -> n618
        n618 = self.context.mk_neq(n602, n606)
        self.nets['sudoku/columns/col_2/diff30'] = n618
        # sudoku/columns/col_2/Logical Operator4 -> n619
        tn111 = self.context.mk_and(n617, n618)
        tn110 = self.context.mk_and(n616, tn111)
        n619 = self.context.mk_and(n615, tn110)
        self.nets['sudoku/columns/col_2/Logical Operator4'] = n619
        # sudoku/columns/col_2/diff22 -> n620
        n620 = self.context.mk_neq(n601, n602)
        self.nets['sudoku/columns/col_2/diff22'] = n620
        # sudoku/columns/col_2/diff23 -> n621
        n621 = self.context.mk_neq(n601, n603)
        self.nets['sudoku/columns/col_2/diff23'] = n621
        # sudoku/columns/col_2/diff24 -> n622
        n622 = self.context.mk_neq(n601, n604)
        self.nets['sudoku/columns/col_2/diff24'] = n622
        # sudoku/columns/col_2/diff25 -> n623
        n623 = self.context.mk_neq(n601, n605)
        self.nets['sudoku/columns/col_2/diff25'] = n623
        # sudoku/columns/col_2/diff26 -> n624
        n624 = self.context.mk_neq(n601, n606)
        self.nets['sudoku/columns/col_2/diff26'] = n624
        # sudoku/columns/col_2/Logical Operator3 -> n625
        tn114 = self.context.mk_and(n623, n624)
        tn113 = self.context.mk_and(n622, tn114)
        tn112 = self.context.mk_and(n621, tn113)
        n625 = self.context.mk_and(n620, tn112)
        self.nets['sudoku/columns/col_2/Logical Operator3'] = n625
        # sudoku/columns/col_2/diff16 -> n626
        n626 = self.context.mk_neq(n600, n601)
        self.nets['sudoku/columns/col_2/diff16'] = n626
        # sudoku/columns/col_2/diff17 -> n627
        n627 = self.context.mk_neq(n600, n602)
        self.nets['sudoku/columns/col_2/diff17'] = n627
        # sudoku/columns/col_2/diff18 -> n628
        n628 = self.context.mk_neq(n600, n603)
        self.nets['sudoku/columns/col_2/diff18'] = n628
        # sudoku/columns/col_2/diff19 -> n629
        n629 = self.context.mk_neq(n600, n604)
        self.nets['sudoku/columns/col_2/diff19'] = n629
        # sudoku/columns/col_2/diff20 -> n630
        n630 = self.context.mk_neq(n600, n605)
        self.nets['sudoku/columns/col_2/diff20'] = n630
        # sudoku/columns/col_2/diff21 -> n631
        n631 = self.context.mk_neq(n600, n606)
        self.nets['sudoku/columns/col_2/diff21'] = n631
        # sudoku/columns/col_2/Logical Operator2 -> n632
        tn118 = self.context.mk_and(n630, n631)
        tn117 = self.context.mk_and(n629, tn118)
        tn116 = self.context.mk_and(n628, tn117)
        tn115 = self.context.mk_and(n627, tn116)
        n632 = self.context.mk_and(n626, tn115)
        self.nets['sudoku/columns/col_2/Logical Operator2'] = n632
        # sudoku/columns/col_2/diff9 -> n633
        n633 = self.context.mk_neq(n599, n600)
        self.nets['sudoku/columns/col_2/diff9'] = n633
        # sudoku/columns/col_2/diff10 -> n634
        n634 = self.context.mk_neq(n599, n601)
        self.nets['sudoku/columns/col_2/diff10'] = n634
        # sudoku/columns/col_2/diff11 -> n635
        n635 = self.context.mk_neq(n599, n602)
        self.nets['sudoku/columns/col_2/diff11'] = n635
        # sudoku/columns/col_2/diff12 -> n636
        n636 = self.context.mk_neq(n599, n603)
        self.nets['sudoku/columns/col_2/diff12'] = n636
        # sudoku/columns/col_2/diff13 -> n637
        n637 = self.context.mk_neq(n599, n604)
        self.nets['sudoku/columns/col_2/diff13'] = n637
        # sudoku/columns/col_2/diff14 -> n638
        n638 = self.context.mk_neq(n599, n605)
        self.nets['sudoku/columns/col_2/diff14'] = n638
        # sudoku/columns/col_2/diff15 -> n639
        n639 = self.context.mk_neq(n599, n606)
        self.nets['sudoku/columns/col_2/diff15'] = n639
        # sudoku/columns/col_2/Logical Operator1 -> n640
        tn123 = self.context.mk_and(n638, n639)
        tn122 = self.context.mk_and(n637, tn123)
        tn121 = self.context.mk_and(n636, tn122)
        tn120 = self.context.mk_and(n635, tn121)
        tn119 = self.context.mk_and(n634, tn120)
        n640 = self.context.mk_and(n633, tn119)
        self.nets['sudoku/columns/col_2/Logical Operator1'] = n640
        # sudoku/columns/col_2/diff1 -> n641
        n641 = self.context.mk_neq(n598, n599)
        self.nets['sudoku/columns/col_2/diff1'] = n641
        # sudoku/columns/col_2/diff2 -> n642
        n642 = self.context.mk_neq(n598, n600)
        self.nets['sudoku/columns/col_2/diff2'] = n642
        # sudoku/columns/col_2/diff3 -> n643
        n643 = self.context.mk_neq(n598, n601)
        self.nets['sudoku/columns/col_2/diff3'] = n643
        # sudoku/columns/col_2/diff4 -> n644
        n644 = self.context.mk_neq(n598, n602)
        self.nets['sudoku/columns/col_2/diff4'] = n644
        # sudoku/columns/col_2/diff5 -> n645
        n645 = self.context.mk_neq(n598, n603)
        self.nets['sudoku/columns/col_2/diff5'] = n645
        # sudoku/columns/col_2/diff6 -> n646
        n646 = self.context.mk_neq(n598, n604)
        self.nets['sudoku/columns/col_2/diff6'] = n646
        # sudoku/columns/col_2/diff7 -> n647
        n647 = self.context.mk_neq(n598, n605)
        self.nets['sudoku/columns/col_2/diff7'] = n647
        # sudoku/columns/col_2/diff8 -> n648
        n648 = self.context.mk_neq(n598, n606)
        self.nets['sudoku/columns/col_2/diff8'] = n648
        # sudoku/columns/col_2/Logical Operator -> n649
        tn129 = self.context.mk_and(n647, n648)
        tn128 = self.context.mk_and(n646, tn129)
        tn127 = self.context.mk_and(n645, tn128)
        tn126 = self.context.mk_and(n644, tn127)
        tn125 = self.context.mk_and(n643, tn126)
        tn124 = self.context.mk_and(n642, tn125)
        n649 = self.context.mk_and(n641, tn124)
        self.nets['sudoku/columns/col_2/Logical Operator'] = n649
        # sudoku/columns/col_2/Logical Operator7 -> n650
        tn135 = self.context.mk_and(n640, n649)
        tn134 = self.context.mk_and(n632, tn135)
        tn133 = self.context.mk_and(n625, tn134)
        tn132 = self.context.mk_and(n619, tn133)
        tn131 = self.context.mk_and(n614, tn132)
        tn130 = self.context.mk_and(n610, tn131)
        n650 = self.context.mk_and(n607, tn130)
        self.nets['sudoku/columns/col_2/Logical Operator7'] = n650
        # n650 -> Out1
        return n650

    def col_1(self, n652, n653, n654, n655, n656, n657, n658, n659, n660):
        # In1 -> n652
        # In2 -> n653
        # In3 -> n654
        # In4 -> n655
        # In5 -> n656
        # In6 -> n657
        # In7 -> n658
        # In8 -> n659
        # In9 -> n660
        # sudoku/columns/col_1/diff36 -> n661
        n661 = self.context.mk_neq(n659, n660)
        self.nets['sudoku/columns/col_1/diff36'] = n661
        # sudoku/columns/col_1/diff34 -> n662
        n662 = self.context.mk_neq(n658, n659)
        self.nets['sudoku/columns/col_1/diff34'] = n662
        # sudoku/columns/col_1/diff35 -> n663
        n663 = self.context.mk_neq(n658, n660)
        self.nets['sudoku/columns/col_1/diff35'] = n663
        # sudoku/columns/col_1/Logical Operator6 -> n664
        n664 = self.context.mk_and(n662, n663)
        self.nets['sudoku/columns/col_1/Logical Operator6'] = n664
        # sudoku/columns/col_1/diff31 -> n665
        n665 = self.context.mk_neq(n657, n658)
        self.nets['sudoku/columns/col_1/diff31'] = n665
        # sudoku/columns/col_1/diff32 -> n666
        n666 = self.context.mk_neq(n657, n659)
        self.nets['sudoku/columns/col_1/diff32'] = n666
        # sudoku/columns/col_1/diff33 -> n667
        n667 = self.context.mk_neq(n657, n660)
        self.nets['sudoku/columns/col_1/diff33'] = n667
        # sudoku/columns/col_1/Logical Operator5 -> n668
        tn136 = self.context.mk_and(n666, n667)
        n668 = self.context.mk_and(n665, tn136)
        self.nets['sudoku/columns/col_1/Logical Operator5'] = n668
        # sudoku/columns/col_1/diff27 -> n669
        n669 = self.context.mk_neq(n656, n657)
        self.nets['sudoku/columns/col_1/diff27'] = n669
        # sudoku/columns/col_1/diff28 -> n670
        n670 = self.context.mk_neq(n656, n658)
        self.nets['sudoku/columns/col_1/diff28'] = n670
        # sudoku/columns/col_1/diff29 -> n671
        n671 = self.context.mk_neq(n656, n659)
        self.nets['sudoku/columns/col_1/diff29'] = n671
        # sudoku/columns/col_1/diff30 -> n672
        n672 = self.context.mk_neq(n656, n660)
        self.nets['sudoku/columns/col_1/diff30'] = n672
        # sudoku/columns/col_1/Logical Operator4 -> n673
        tn138 = self.context.mk_and(n671, n672)
        tn137 = self.context.mk_and(n670, tn138)
        n673 = self.context.mk_and(n669, tn137)
        self.nets['sudoku/columns/col_1/Logical Operator4'] = n673
        # sudoku/columns/col_1/diff22 -> n674
        n674 = self.context.mk_neq(n655, n656)
        self.nets['sudoku/columns/col_1/diff22'] = n674
        # sudoku/columns/col_1/diff23 -> n675
        n675 = self.context.mk_neq(n655, n657)
        self.nets['sudoku/columns/col_1/diff23'] = n675
        # sudoku/columns/col_1/diff24 -> n676
        n676 = self.context.mk_neq(n655, n658)
        self.nets['sudoku/columns/col_1/diff24'] = n676
        # sudoku/columns/col_1/diff25 -> n677
        n677 = self.context.mk_neq(n655, n659)
        self.nets['sudoku/columns/col_1/diff25'] = n677
        # sudoku/columns/col_1/diff26 -> n678
        n678 = self.context.mk_neq(n655, n660)
        self.nets['sudoku/columns/col_1/diff26'] = n678
        # sudoku/columns/col_1/Logical Operator3 -> n679
        tn141 = self.context.mk_and(n677, n678)
        tn140 = self.context.mk_and(n676, tn141)
        tn139 = self.context.mk_and(n675, tn140)
        n679 = self.context.mk_and(n674, tn139)
        self.nets['sudoku/columns/col_1/Logical Operator3'] = n679
        # sudoku/columns/col_1/diff16 -> n680
        n680 = self.context.mk_neq(n654, n655)
        self.nets['sudoku/columns/col_1/diff16'] = n680
        # sudoku/columns/col_1/diff17 -> n681
        n681 = self.context.mk_neq(n654, n656)
        self.nets['sudoku/columns/col_1/diff17'] = n681
        # sudoku/columns/col_1/diff18 -> n682
        n682 = self.context.mk_neq(n654, n657)
        self.nets['sudoku/columns/col_1/diff18'] = n682
        # sudoku/columns/col_1/diff19 -> n683
        n683 = self.context.mk_neq(n654, n658)
        self.nets['sudoku/columns/col_1/diff19'] = n683
        # sudoku/columns/col_1/diff20 -> n684
        n684 = self.context.mk_neq(n654, n659)
        self.nets['sudoku/columns/col_1/diff20'] = n684
        # sudoku/columns/col_1/diff21 -> n685
        n685 = self.context.mk_neq(n654, n660)
        self.nets['sudoku/columns/col_1/diff21'] = n685
        # sudoku/columns/col_1/Logical Operator2 -> n686
        tn145 = self.context.mk_and(n684, n685)
        tn144 = self.context.mk_and(n683, tn145)
        tn143 = self.context.mk_and(n682, tn144)
        tn142 = self.context.mk_and(n681, tn143)
        n686 = self.context.mk_and(n680, tn142)
        self.nets['sudoku/columns/col_1/Logical Operator2'] = n686
        # sudoku/columns/col_1/diff9 -> n687
        n687 = self.context.mk_neq(n653, n654)
        self.nets['sudoku/columns/col_1/diff9'] = n687
        # sudoku/columns/col_1/diff10 -> n688
        n688 = self.context.mk_neq(n653, n655)
        self.nets['sudoku/columns/col_1/diff10'] = n688
        # sudoku/columns/col_1/diff11 -> n689
        n689 = self.context.mk_neq(n653, n656)
        self.nets['sudoku/columns/col_1/diff11'] = n689
        # sudoku/columns/col_1/diff12 -> n690
        n690 = self.context.mk_neq(n653, n657)
        self.nets['sudoku/columns/col_1/diff12'] = n690
        # sudoku/columns/col_1/diff13 -> n691
        n691 = self.context.mk_neq(n653, n658)
        self.nets['sudoku/columns/col_1/diff13'] = n691
        # sudoku/columns/col_1/diff14 -> n692
        n692 = self.context.mk_neq(n653, n659)
        self.nets['sudoku/columns/col_1/diff14'] = n692
        # sudoku/columns/col_1/diff15 -> n693
        n693 = self.context.mk_neq(n653, n660)
        self.nets['sudoku/columns/col_1/diff15'] = n693
        # sudoku/columns/col_1/Logical Operator1 -> n694
        tn150 = self.context.mk_and(n692, n693)
        tn149 = self.context.mk_and(n691, tn150)
        tn148 = self.context.mk_and(n690, tn149)
        tn147 = self.context.mk_and(n689, tn148)
        tn146 = self.context.mk_and(n688, tn147)
        n694 = self.context.mk_and(n687, tn146)
        self.nets['sudoku/columns/col_1/Logical Operator1'] = n694
        # sudoku/columns/col_1/diff1 -> n695
        n695 = self.context.mk_neq(n652, n653)
        self.nets['sudoku/columns/col_1/diff1'] = n695
        # sudoku/columns/col_1/diff2 -> n696
        n696 = self.context.mk_neq(n652, n654)
        self.nets['sudoku/columns/col_1/diff2'] = n696
        # sudoku/columns/col_1/diff3 -> n697
        n697 = self.context.mk_neq(n652, n655)
        self.nets['sudoku/columns/col_1/diff3'] = n697
        # sudoku/columns/col_1/diff4 -> n698
        n698 = self.context.mk_neq(n652, n656)
        self.nets['sudoku/columns/col_1/diff4'] = n698
        # sudoku/columns/col_1/diff5 -> n699
        n699 = self.context.mk_neq(n652, n657)
        self.nets['sudoku/columns/col_1/diff5'] = n699
        # sudoku/columns/col_1/diff6 -> n700
        n700 = self.context.mk_neq(n652, n658)
        self.nets['sudoku/columns/col_1/diff6'] = n700
        # sudoku/columns/col_1/diff7 -> n701
        n701 = self.context.mk_neq(n652, n659)
        self.nets['sudoku/columns/col_1/diff7'] = n701
        # sudoku/columns/col_1/diff8 -> n702
        n702 = self.context.mk_neq(n652, n660)
        self.nets['sudoku/columns/col_1/diff8'] = n702
        # sudoku/columns/col_1/Logical Operator -> n703
        tn156 = self.context.mk_and(n701, n702)
        tn155 = self.context.mk_and(n700, tn156)
        tn154 = self.context.mk_and(n699, tn155)
        tn153 = self.context.mk_and(n698, tn154)
        tn152 = self.context.mk_and(n697, tn153)
        tn151 = self.context.mk_and(n696, tn152)
        n703 = self.context.mk_and(n695, tn151)
        self.nets['sudoku/columns/col_1/Logical Operator'] = n703
        # sudoku/columns/col_1/Logical Operator7 -> n704
        tn162 = self.context.mk_and(n694, n703)
        tn161 = self.context.mk_and(n686, tn162)
        tn160 = self.context.mk_and(n679, tn161)
        tn159 = self.context.mk_and(n673, tn160)
        tn158 = self.context.mk_and(n668, tn159)
        tn157 = self.context.mk_and(n664, tn158)
        n704 = self.context.mk_and(n661, tn157)
        self.nets['sudoku/columns/col_1/Logical Operator7'] = n704
        # n704 -> Out1
        return n704

    def col_9(self, n706, n707, n708, n709, n710, n711, n712, n713, n714):
        # In1 -> n706
        # In2 -> n707
        # In3 -> n708
        # In4 -> n709
        # In5 -> n710
        # In6 -> n711
        # In7 -> n712
        # In8 -> n713
        # In9 -> n714
        # sudoku/columns/col_9/diff36 -> n715
        n715 = self.context.mk_neq(n713, n714)
        self.nets['sudoku/columns/col_9/diff36'] = n715
        # sudoku/columns/col_9/diff34 -> n716
        n716 = self.context.mk_neq(n712, n713)
        self.nets['sudoku/columns/col_9/diff34'] = n716
        # sudoku/columns/col_9/diff35 -> n717
        n717 = self.context.mk_neq(n712, n714)
        self.nets['sudoku/columns/col_9/diff35'] = n717
        # sudoku/columns/col_9/Logical Operator6 -> n718
        n718 = self.context.mk_and(n716, n717)
        self.nets['sudoku/columns/col_9/Logical Operator6'] = n718
        # sudoku/columns/col_9/diff31 -> n719
        n719 = self.context.mk_neq(n711, n712)
        self.nets['sudoku/columns/col_9/diff31'] = n719
        # sudoku/columns/col_9/diff32 -> n720
        n720 = self.context.mk_neq(n711, n713)
        self.nets['sudoku/columns/col_9/diff32'] = n720
        # sudoku/columns/col_9/diff33 -> n721
        n721 = self.context.mk_neq(n711, n714)
        self.nets['sudoku/columns/col_9/diff33'] = n721
        # sudoku/columns/col_9/Logical Operator5 -> n722
        tn163 = self.context.mk_and(n720, n721)
        n722 = self.context.mk_and(n719, tn163)
        self.nets['sudoku/columns/col_9/Logical Operator5'] = n722
        # sudoku/columns/col_9/diff27 -> n723
        n723 = self.context.mk_neq(n710, n711)
        self.nets['sudoku/columns/col_9/diff27'] = n723
        # sudoku/columns/col_9/diff28 -> n724
        n724 = self.context.mk_neq(n710, n712)
        self.nets['sudoku/columns/col_9/diff28'] = n724
        # sudoku/columns/col_9/diff29 -> n725
        n725 = self.context.mk_neq(n710, n713)
        self.nets['sudoku/columns/col_9/diff29'] = n725
        # sudoku/columns/col_9/diff30 -> n726
        n726 = self.context.mk_neq(n710, n714)
        self.nets['sudoku/columns/col_9/diff30'] = n726
        # sudoku/columns/col_9/Logical Operator4 -> n727
        tn165 = self.context.mk_and(n725, n726)
        tn164 = self.context.mk_and(n724, tn165)
        n727 = self.context.mk_and(n723, tn164)
        self.nets['sudoku/columns/col_9/Logical Operator4'] = n727
        # sudoku/columns/col_9/diff22 -> n728
        n728 = self.context.mk_neq(n709, n710)
        self.nets['sudoku/columns/col_9/diff22'] = n728
        # sudoku/columns/col_9/diff23 -> n729
        n729 = self.context.mk_neq(n709, n711)
        self.nets['sudoku/columns/col_9/diff23'] = n729
        # sudoku/columns/col_9/diff24 -> n730
        n730 = self.context.mk_neq(n709, n712)
        self.nets['sudoku/columns/col_9/diff24'] = n730
        # sudoku/columns/col_9/diff25 -> n731
        n731 = self.context.mk_neq(n709, n713)
        self.nets['sudoku/columns/col_9/diff25'] = n731
        # sudoku/columns/col_9/diff26 -> n732
        n732 = self.context.mk_neq(n709, n714)
        self.nets['sudoku/columns/col_9/diff26'] = n732
        # sudoku/columns/col_9/Logical Operator3 -> n733
        tn168 = self.context.mk_and(n731, n732)
        tn167 = self.context.mk_and(n730, tn168)
        tn166 = self.context.mk_and(n729, tn167)
        n733 = self.context.mk_and(n728, tn166)
        self.nets['sudoku/columns/col_9/Logical Operator3'] = n733
        # sudoku/columns/col_9/diff16 -> n734
        n734 = self.context.mk_neq(n708, n709)
        self.nets['sudoku/columns/col_9/diff16'] = n734
        # sudoku/columns/col_9/diff17 -> n735
        n735 = self.context.mk_neq(n708, n710)
        self.nets['sudoku/columns/col_9/diff17'] = n735
        # sudoku/columns/col_9/diff18 -> n736
        n736 = self.context.mk_neq(n708, n711)
        self.nets['sudoku/columns/col_9/diff18'] = n736
        # sudoku/columns/col_9/diff19 -> n737
        n737 = self.context.mk_neq(n708, n712)
        self.nets['sudoku/columns/col_9/diff19'] = n737
        # sudoku/columns/col_9/diff20 -> n738
        n738 = self.context.mk_neq(n708, n713)
        self.nets['sudoku/columns/col_9/diff20'] = n738
        # sudoku/columns/col_9/diff21 -> n739
        n739 = self.context.mk_neq(n708, n714)
        self.nets['sudoku/columns/col_9/diff21'] = n739
        # sudoku/columns/col_9/Logical Operator2 -> n740
        tn172 = self.context.mk_and(n738, n739)
        tn171 = self.context.mk_and(n737, tn172)
        tn170 = self.context.mk_and(n736, tn171)
        tn169 = self.context.mk_and(n735, tn170)
        n740 = self.context.mk_and(n734, tn169)
        self.nets['sudoku/columns/col_9/Logical Operator2'] = n740
        # sudoku/columns/col_9/diff9 -> n741
        n741 = self.context.mk_neq(n707, n708)
        self.nets['sudoku/columns/col_9/diff9'] = n741
        # sudoku/columns/col_9/diff10 -> n742
        n742 = self.context.mk_neq(n707, n709)
        self.nets['sudoku/columns/col_9/diff10'] = n742
        # sudoku/columns/col_9/diff11 -> n743
        n743 = self.context.mk_neq(n707, n710)
        self.nets['sudoku/columns/col_9/diff11'] = n743
        # sudoku/columns/col_9/diff12 -> n744
        n744 = self.context.mk_neq(n707, n711)
        self.nets['sudoku/columns/col_9/diff12'] = n744
        # sudoku/columns/col_9/diff13 -> n745
        n745 = self.context.mk_neq(n707, n712)
        self.nets['sudoku/columns/col_9/diff13'] = n745
        # sudoku/columns/col_9/diff14 -> n746
        n746 = self.context.mk_neq(n707, n713)
        self.nets['sudoku/columns/col_9/diff14'] = n746
        # sudoku/columns/col_9/diff15 -> n747
        n747 = self.context.mk_neq(n707, n714)
        self.nets['sudoku/columns/col_9/diff15'] = n747
        # sudoku/columns/col_9/Logical Operator1 -> n748
        tn177 = self.context.mk_and(n746, n747)
        tn176 = self.context.mk_and(n745, tn177)
        tn175 = self.context.mk_and(n744, tn176)
        tn174 = self.context.mk_and(n743, tn175)
        tn173 = self.context.mk_and(n742, tn174)
        n748 = self.context.mk_and(n741, tn173)
        self.nets['sudoku/columns/col_9/Logical Operator1'] = n748
        # sudoku/columns/col_9/diff1 -> n749
        n749 = self.context.mk_neq(n706, n707)
        self.nets['sudoku/columns/col_9/diff1'] = n749
        # sudoku/columns/col_9/diff2 -> n750
        n750 = self.context.mk_neq(n706, n708)
        self.nets['sudoku/columns/col_9/diff2'] = n750
        # sudoku/columns/col_9/diff3 -> n751
        n751 = self.context.mk_neq(n706, n709)
        self.nets['sudoku/columns/col_9/diff3'] = n751
        # sudoku/columns/col_9/diff4 -> n752
        n752 = self.context.mk_neq(n706, n710)
        self.nets['sudoku/columns/col_9/diff4'] = n752
        # sudoku/columns/col_9/diff5 -> n753
        n753 = self.context.mk_neq(n706, n711)
        self.nets['sudoku/columns/col_9/diff5'] = n753
        # sudoku/columns/col_9/diff6 -> n754
        n754 = self.context.mk_neq(n706, n712)
        self.nets['sudoku/columns/col_9/diff6'] = n754
        # sudoku/columns/col_9/diff7 -> n755
        n755 = self.context.mk_neq(n706, n713)
        self.nets['sudoku/columns/col_9/diff7'] = n755
        # sudoku/columns/col_9/diff8 -> n756
        n756 = self.context.mk_neq(n706, n714)
        self.nets['sudoku/columns/col_9/diff8'] = n756
        # sudoku/columns/col_9/Logical Operator -> n757
        tn183 = self.context.mk_and(n755, n756)
        tn182 = self.context.mk_and(n754, tn183)
        tn181 = self.context.mk_and(n753, tn182)
        tn180 = self.context.mk_and(n752, tn181)
        tn179 = self.context.mk_and(n751, tn180)
        tn178 = self.context.mk_and(n750, tn179)
        n757 = self.context.mk_and(n749, tn178)
        self.nets['sudoku/columns/col_9/Logical Operator'] = n757
        # sudoku/columns/col_9/Logical Operator7 -> n758
        tn189 = self.context.mk_and(n748, n757)
        tn188 = self.context.mk_and(n740, tn189)
        tn187 = self.context.mk_and(n733, tn188)
        tn186 = self.context.mk_and(n727, tn187)
        tn185 = self.context.mk_and(n722, tn186)
        tn184 = self.context.mk_and(n718, tn185)
        n758 = self.context.mk_and(n715, tn184)
        self.nets['sudoku/columns/col_9/Logical Operator7'] = n758
        # n758 -> Out1
        return n758

    def col_8(self, n760, n761, n762, n763, n764, n765, n766, n767, n768):
        # In1 -> n760
        # In2 -> n761
        # In3 -> n762
        # In4 -> n763
        # In5 -> n764
        # In6 -> n765
        # In7 -> n766
        # In8 -> n767
        # In9 -> n768
        # sudoku/columns/col_8/diff36 -> n769
        n769 = self.context.mk_neq(n767, n768)
        self.nets['sudoku/columns/col_8/diff36'] = n769
        # sudoku/columns/col_8/diff34 -> n770
        n770 = self.context.mk_neq(n766, n767)
        self.nets['sudoku/columns/col_8/diff34'] = n770
        # sudoku/columns/col_8/diff35 -> n771
        n771 = self.context.mk_neq(n766, n768)
        self.nets['sudoku/columns/col_8/diff35'] = n771
        # sudoku/columns/col_8/Logical Operator6 -> n772
        n772 = self.context.mk_and(n770, n771)
        self.nets['sudoku/columns/col_8/Logical Operator6'] = n772
        # sudoku/columns/col_8/diff31 -> n773
        n773 = self.context.mk_neq(n765, n766)
        self.nets['sudoku/columns/col_8/diff31'] = n773
        # sudoku/columns/col_8/diff32 -> n774
        n774 = self.context.mk_neq(n765, n767)
        self.nets['sudoku/columns/col_8/diff32'] = n774
        # sudoku/columns/col_8/diff33 -> n775
        n775 = self.context.mk_neq(n765, n768)
        self.nets['sudoku/columns/col_8/diff33'] = n775
        # sudoku/columns/col_8/Logical Operator5 -> n776
        tn190 = self.context.mk_and(n774, n775)
        n776 = self.context.mk_and(n773, tn190)
        self.nets['sudoku/columns/col_8/Logical Operator5'] = n776
        # sudoku/columns/col_8/diff27 -> n777
        n777 = self.context.mk_neq(n764, n765)
        self.nets['sudoku/columns/col_8/diff27'] = n777
        # sudoku/columns/col_8/diff28 -> n778
        n778 = self.context.mk_neq(n764, n766)
        self.nets['sudoku/columns/col_8/diff28'] = n778
        # sudoku/columns/col_8/diff29 -> n779
        n779 = self.context.mk_neq(n764, n767)
        self.nets['sudoku/columns/col_8/diff29'] = n779
        # sudoku/columns/col_8/diff30 -> n780
        n780 = self.context.mk_neq(n764, n768)
        self.nets['sudoku/columns/col_8/diff30'] = n780
        # sudoku/columns/col_8/Logical Operator4 -> n781
        tn192 = self.context.mk_and(n779, n780)
        tn191 = self.context.mk_and(n778, tn192)
        n781 = self.context.mk_and(n777, tn191)
        self.nets['sudoku/columns/col_8/Logical Operator4'] = n781
        # sudoku/columns/col_8/diff22 -> n782
        n782 = self.context.mk_neq(n763, n764)
        self.nets['sudoku/columns/col_8/diff22'] = n782
        # sudoku/columns/col_8/diff23 -> n783
        n783 = self.context.mk_neq(n763, n765)
        self.nets['sudoku/columns/col_8/diff23'] = n783
        # sudoku/columns/col_8/diff24 -> n784
        n784 = self.context.mk_neq(n763, n766)
        self.nets['sudoku/columns/col_8/diff24'] = n784
        # sudoku/columns/col_8/diff25 -> n785
        n785 = self.context.mk_neq(n763, n767)
        self.nets['sudoku/columns/col_8/diff25'] = n785
        # sudoku/columns/col_8/diff26 -> n786
        n786 = self.context.mk_neq(n763, n768)
        self.nets['sudoku/columns/col_8/diff26'] = n786
        # sudoku/columns/col_8/Logical Operator3 -> n787
        tn195 = self.context.mk_and(n785, n786)
        tn194 = self.context.mk_and(n784, tn195)
        tn193 = self.context.mk_and(n783, tn194)
        n787 = self.context.mk_and(n782, tn193)
        self.nets['sudoku/columns/col_8/Logical Operator3'] = n787
        # sudoku/columns/col_8/diff16 -> n788
        n788 = self.context.mk_neq(n762, n763)
        self.nets['sudoku/columns/col_8/diff16'] = n788
        # sudoku/columns/col_8/diff17 -> n789
        n789 = self.context.mk_neq(n762, n764)
        self.nets['sudoku/columns/col_8/diff17'] = n789
        # sudoku/columns/col_8/diff18 -> n790
        n790 = self.context.mk_neq(n762, n765)
        self.nets['sudoku/columns/col_8/diff18'] = n790
        # sudoku/columns/col_8/diff19 -> n791
        n791 = self.context.mk_neq(n762, n766)
        self.nets['sudoku/columns/col_8/diff19'] = n791
        # sudoku/columns/col_8/diff20 -> n792
        n792 = self.context.mk_neq(n762, n767)
        self.nets['sudoku/columns/col_8/diff20'] = n792
        # sudoku/columns/col_8/diff21 -> n793
        n793 = self.context.mk_neq(n762, n768)
        self.nets['sudoku/columns/col_8/diff21'] = n793
        # sudoku/columns/col_8/Logical Operator2 -> n794
        tn199 = self.context.mk_and(n792, n793)
        tn198 = self.context.mk_and(n791, tn199)
        tn197 = self.context.mk_and(n790, tn198)
        tn196 = self.context.mk_and(n789, tn197)
        n794 = self.context.mk_and(n788, tn196)
        self.nets['sudoku/columns/col_8/Logical Operator2'] = n794
        # sudoku/columns/col_8/diff9 -> n795
        n795 = self.context.mk_neq(n761, n762)
        self.nets['sudoku/columns/col_8/diff9'] = n795
        # sudoku/columns/col_8/diff10 -> n796
        n796 = self.context.mk_neq(n761, n763)
        self.nets['sudoku/columns/col_8/diff10'] = n796
        # sudoku/columns/col_8/diff11 -> n797
        n797 = self.context.mk_neq(n761, n764)
        self.nets['sudoku/columns/col_8/diff11'] = n797
        # sudoku/columns/col_8/diff12 -> n798
        n798 = self.context.mk_neq(n761, n765)
        self.nets['sudoku/columns/col_8/diff12'] = n798
        # sudoku/columns/col_8/diff13 -> n799
        n799 = self.context.mk_neq(n761, n766)
        self.nets['sudoku/columns/col_8/diff13'] = n799
        # sudoku/columns/col_8/diff14 -> n800
        n800 = self.context.mk_neq(n761, n767)
        self.nets['sudoku/columns/col_8/diff14'] = n800
        # sudoku/columns/col_8/diff15 -> n801
        n801 = self.context.mk_neq(n761, n768)
        self.nets['sudoku/columns/col_8/diff15'] = n801
        # sudoku/columns/col_8/Logical Operator1 -> n802
        tn204 = self.context.mk_and(n800, n801)
        tn203 = self.context.mk_and(n799, tn204)
        tn202 = self.context.mk_and(n798, tn203)
        tn201 = self.context.mk_and(n797, tn202)
        tn200 = self.context.mk_and(n796, tn201)
        n802 = self.context.mk_and(n795, tn200)
        self.nets['sudoku/columns/col_8/Logical Operator1'] = n802
        # sudoku/columns/col_8/diff1 -> n803
        n803 = self.context.mk_neq(n760, n761)
        self.nets['sudoku/columns/col_8/diff1'] = n803
        # sudoku/columns/col_8/diff2 -> n804
        n804 = self.context.mk_neq(n760, n762)
        self.nets['sudoku/columns/col_8/diff2'] = n804
        # sudoku/columns/col_8/diff3 -> n805
        n805 = self.context.mk_neq(n760, n763)
        self.nets['sudoku/columns/col_8/diff3'] = n805
        # sudoku/columns/col_8/diff4 -> n806
        n806 = self.context.mk_neq(n760, n764)
        self.nets['sudoku/columns/col_8/diff4'] = n806
        # sudoku/columns/col_8/diff5 -> n807
        n807 = self.context.mk_neq(n760, n765)
        self.nets['sudoku/columns/col_8/diff5'] = n807
        # sudoku/columns/col_8/diff6 -> n808
        n808 = self.context.mk_neq(n760, n766)
        self.nets['sudoku/columns/col_8/diff6'] = n808
        # sudoku/columns/col_8/diff7 -> n809
        n809 = self.context.mk_neq(n760, n767)
        self.nets['sudoku/columns/col_8/diff7'] = n809
        # sudoku/columns/col_8/diff8 -> n810
        n810 = self.context.mk_neq(n760, n768)
        self.nets['sudoku/columns/col_8/diff8'] = n810
        # sudoku/columns/col_8/Logical Operator -> n811
        tn210 = self.context.mk_and(n809, n810)
        tn209 = self.context.mk_and(n808, tn210)
        tn208 = self.context.mk_and(n807, tn209)
        tn207 = self.context.mk_and(n806, tn208)
        tn206 = self.context.mk_and(n805, tn207)
        tn205 = self.context.mk_and(n804, tn206)
        n811 = self.context.mk_and(n803, tn205)
        self.nets['sudoku/columns/col_8/Logical Operator'] = n811
        # sudoku/columns/col_8/Logical Operator7 -> n812
        tn216 = self.context.mk_and(n802, n811)
        tn215 = self.context.mk_and(n794, tn216)
        tn214 = self.context.mk_and(n787, tn215)
        tn213 = self.context.mk_and(n781, tn214)
        tn212 = self.context.mk_and(n776, tn213)
        tn211 = self.context.mk_and(n772, tn212)
        n812 = self.context.mk_and(n769, tn211)
        self.nets['sudoku/columns/col_8/Logical Operator7'] = n812
        # n812 -> Out1
        return n812

    def col_7(self, n814, n815, n816, n817, n818, n819, n820, n821, n822):
        # In1 -> n814
        # In2 -> n815
        # In3 -> n816
        # In4 -> n817
        # In5 -> n818
        # In6 -> n819
        # In7 -> n820
        # In8 -> n821
        # In9 -> n822
        # sudoku/columns/col_7/diff36 -> n823
        n823 = self.context.mk_neq(n821, n822)
        self.nets['sudoku/columns/col_7/diff36'] = n823
        # sudoku/columns/col_7/diff34 -> n824
        n824 = self.context.mk_neq(n820, n821)
        self.nets['sudoku/columns/col_7/diff34'] = n824
        # sudoku/columns/col_7/diff35 -> n825
        n825 = self.context.mk_neq(n820, n822)
        self.nets['sudoku/columns/col_7/diff35'] = n825
        # sudoku/columns/col_7/Logical Operator6 -> n826
        n826 = self.context.mk_and(n824, n825)
        self.nets['sudoku/columns/col_7/Logical Operator6'] = n826
        # sudoku/columns/col_7/diff31 -> n827
        n827 = self.context.mk_neq(n819, n820)
        self.nets['sudoku/columns/col_7/diff31'] = n827
        # sudoku/columns/col_7/diff32 -> n828
        n828 = self.context.mk_neq(n819, n821)
        self.nets['sudoku/columns/col_7/diff32'] = n828
        # sudoku/columns/col_7/diff33 -> n829
        n829 = self.context.mk_neq(n819, n822)
        self.nets['sudoku/columns/col_7/diff33'] = n829
        # sudoku/columns/col_7/Logical Operator5 -> n830
        tn217 = self.context.mk_and(n828, n829)
        n830 = self.context.mk_and(n827, tn217)
        self.nets['sudoku/columns/col_7/Logical Operator5'] = n830
        # sudoku/columns/col_7/diff27 -> n831
        n831 = self.context.mk_neq(n818, n819)
        self.nets['sudoku/columns/col_7/diff27'] = n831
        # sudoku/columns/col_7/diff28 -> n832
        n832 = self.context.mk_neq(n818, n820)
        self.nets['sudoku/columns/col_7/diff28'] = n832
        # sudoku/columns/col_7/diff29 -> n833
        n833 = self.context.mk_neq(n818, n821)
        self.nets['sudoku/columns/col_7/diff29'] = n833
        # sudoku/columns/col_7/diff30 -> n834
        n834 = self.context.mk_neq(n818, n822)
        self.nets['sudoku/columns/col_7/diff30'] = n834
        # sudoku/columns/col_7/Logical Operator4 -> n835
        tn219 = self.context.mk_and(n833, n834)
        tn218 = self.context.mk_and(n832, tn219)
        n835 = self.context.mk_and(n831, tn218)
        self.nets['sudoku/columns/col_7/Logical Operator4'] = n835
        # sudoku/columns/col_7/diff22 -> n836
        n836 = self.context.mk_neq(n817, n818)
        self.nets['sudoku/columns/col_7/diff22'] = n836
        # sudoku/columns/col_7/diff23 -> n837
        n837 = self.context.mk_neq(n817, n819)
        self.nets['sudoku/columns/col_7/diff23'] = n837
        # sudoku/columns/col_7/diff24 -> n838
        n838 = self.context.mk_neq(n817, n820)
        self.nets['sudoku/columns/col_7/diff24'] = n838
        # sudoku/columns/col_7/diff25 -> n839
        n839 = self.context.mk_neq(n817, n821)
        self.nets['sudoku/columns/col_7/diff25'] = n839
        # sudoku/columns/col_7/diff26 -> n840
        n840 = self.context.mk_neq(n817, n822)
        self.nets['sudoku/columns/col_7/diff26'] = n840
        # sudoku/columns/col_7/Logical Operator3 -> n841
        tn222 = self.context.mk_and(n839, n840)
        tn221 = self.context.mk_and(n838, tn222)
        tn220 = self.context.mk_and(n837, tn221)
        n841 = self.context.mk_and(n836, tn220)
        self.nets['sudoku/columns/col_7/Logical Operator3'] = n841
        # sudoku/columns/col_7/diff16 -> n842
        n842 = self.context.mk_neq(n816, n817)
        self.nets['sudoku/columns/col_7/diff16'] = n842
        # sudoku/columns/col_7/diff17 -> n843
        n843 = self.context.mk_neq(n816, n818)
        self.nets['sudoku/columns/col_7/diff17'] = n843
        # sudoku/columns/col_7/diff18 -> n844
        n844 = self.context.mk_neq(n816, n819)
        self.nets['sudoku/columns/col_7/diff18'] = n844
        # sudoku/columns/col_7/diff19 -> n845
        n845 = self.context.mk_neq(n816, n820)
        self.nets['sudoku/columns/col_7/diff19'] = n845
        # sudoku/columns/col_7/diff20 -> n846
        n846 = self.context.mk_neq(n816, n821)
        self.nets['sudoku/columns/col_7/diff20'] = n846
        # sudoku/columns/col_7/diff21 -> n847
        n847 = self.context.mk_neq(n816, n822)
        self.nets['sudoku/columns/col_7/diff21'] = n847
        # sudoku/columns/col_7/Logical Operator2 -> n848
        tn226 = self.context.mk_and(n846, n847)
        tn225 = self.context.mk_and(n845, tn226)
        tn224 = self.context.mk_and(n844, tn225)
        tn223 = self.context.mk_and(n843, tn224)
        n848 = self.context.mk_and(n842, tn223)
        self.nets['sudoku/columns/col_7/Logical Operator2'] = n848
        # sudoku/columns/col_7/diff9 -> n849
        n849 = self.context.mk_neq(n815, n816)
        self.nets['sudoku/columns/col_7/diff9'] = n849
        # sudoku/columns/col_7/diff10 -> n850
        n850 = self.context.mk_neq(n815, n817)
        self.nets['sudoku/columns/col_7/diff10'] = n850
        # sudoku/columns/col_7/diff11 -> n851
        n851 = self.context.mk_neq(n815, n818)
        self.nets['sudoku/columns/col_7/diff11'] = n851
        # sudoku/columns/col_7/diff12 -> n852
        n852 = self.context.mk_neq(n815, n819)
        self.nets['sudoku/columns/col_7/diff12'] = n852
        # sudoku/columns/col_7/diff13 -> n853
        n853 = self.context.mk_neq(n815, n820)
        self.nets['sudoku/columns/col_7/diff13'] = n853
        # sudoku/columns/col_7/diff14 -> n854
        n854 = self.context.mk_neq(n815, n821)
        self.nets['sudoku/columns/col_7/diff14'] = n854
        # sudoku/columns/col_7/diff15 -> n855
        n855 = self.context.mk_neq(n815, n822)
        self.nets['sudoku/columns/col_7/diff15'] = n855
        # sudoku/columns/col_7/Logical Operator1 -> n856
        tn231 = self.context.mk_and(n854, n855)
        tn230 = self.context.mk_and(n853, tn231)
        tn229 = self.context.mk_and(n852, tn230)
        tn228 = self.context.mk_and(n851, tn229)
        tn227 = self.context.mk_and(n850, tn228)
        n856 = self.context.mk_and(n849, tn227)
        self.nets['sudoku/columns/col_7/Logical Operator1'] = n856
        # sudoku/columns/col_7/diff1 -> n857
        n857 = self.context.mk_neq(n814, n815)
        self.nets['sudoku/columns/col_7/diff1'] = n857
        # sudoku/columns/col_7/diff2 -> n858
        n858 = self.context.mk_neq(n814, n816)
        self.nets['sudoku/columns/col_7/diff2'] = n858
        # sudoku/columns/col_7/diff3 -> n859
        n859 = self.context.mk_neq(n814, n817)
        self.nets['sudoku/columns/col_7/diff3'] = n859
        # sudoku/columns/col_7/diff4 -> n860
        n860 = self.context.mk_neq(n814, n818)
        self.nets['sudoku/columns/col_7/diff4'] = n860
        # sudoku/columns/col_7/diff5 -> n861
        n861 = self.context.mk_neq(n814, n819)
        self.nets['sudoku/columns/col_7/diff5'] = n861
        # sudoku/columns/col_7/diff6 -> n862
        n862 = self.context.mk_neq(n814, n820)
        self.nets['sudoku/columns/col_7/diff6'] = n862
        # sudoku/columns/col_7/diff7 -> n863
        n863 = self.context.mk_neq(n814, n821)
        self.nets['sudoku/columns/col_7/diff7'] = n863
        # sudoku/columns/col_7/diff8 -> n864
        n864 = self.context.mk_neq(n814, n822)
        self.nets['sudoku/columns/col_7/diff8'] = n864
        # sudoku/columns/col_7/Logical Operator -> n865
        tn237 = self.context.mk_and(n863, n864)
        tn236 = self.context.mk_and(n862, tn237)
        tn235 = self.context.mk_and(n861, tn236)
        tn234 = self.context.mk_and(n860, tn235)
        tn233 = self.context.mk_and(n859, tn234)
        tn232 = self.context.mk_and(n858, tn233)
        n865 = self.context.mk_and(n857, tn232)
        self.nets['sudoku/columns/col_7/Logical Operator'] = n865
        # sudoku/columns/col_7/Logical Operator7 -> n866
        tn243 = self.context.mk_and(n856, n865)
        tn242 = self.context.mk_and(n848, tn243)
        tn241 = self.context.mk_and(n841, tn242)
        tn240 = self.context.mk_and(n835, tn241)
        tn239 = self.context.mk_and(n830, tn240)
        tn238 = self.context.mk_and(n826, tn239)
        n866 = self.context.mk_and(n823, tn238)
        self.nets['sudoku/columns/col_7/Logical Operator7'] = n866
        # n866 -> Out1
        return n866

    def columns(self, n868, n869, n870, n871, n872, n873, n874, n875, n876, n877, n878, n879, n880, n881, n882, n883, n884, n885, n886, n887, n888, n889, n890, n891, n892, n893, n894, n895, n896, n897, n898, n899, n900, n901, n902, n903, n904, n905, n906, n907, n908, n909, n910, n911, n912, n913, n914, n915, n916, n917, n918, n919, n920, n921, n922, n923, n924, n925, n926, n927, n928, n929, n930, n931, n932, n933, n934, n935, n936, n937, n938, n939, n940, n941, n942, n943, n944, n945, n946, n947, n948):
        # In1 -> n868
        # In2 -> n869
        # In3 -> n870
        # In4 -> n871
        # In5 -> n872
        # In6 -> n873
        # In7 -> n874
        # In8 -> n875
        # In9 -> n876
        # In10 -> n877
        # In11 -> n878
        # In12 -> n879
        # In13 -> n880
        # In14 -> n881
        # In15 -> n882
        # In16 -> n883
        # In17 -> n884
        # In18 -> n885
        # In19 -> n886
        # In20 -> n887
        # In21 -> n888
        # In22 -> n889
        # In23 -> n890
        # In24 -> n891
        # In25 -> n892
        # In26 -> n893
        # In27 -> n894
        # In28 -> n895
        # In29 -> n896
        # In30 -> n897
        # In31 -> n898
        # In32 -> n899
        # In33 -> n900
        # In34 -> n901
        # In35 -> n902
        # In36 -> n903
        # In37 -> n904
        # In38 -> n905
        # In39 -> n906
        # In40 -> n907
        # In41 -> n908
        # In42 -> n909
        # In43 -> n910
        # In44 -> n911
        # In45 -> n912
        # In46 -> n913
        # In47 -> n914
        # In48 -> n915
        # In49 -> n916
        # In50 -> n917
        # In51 -> n918
        # In52 -> n919
        # In53 -> n920
        # In54 -> n921
        # In55 -> n922
        # In56 -> n923
        # In57 -> n924
        # In58 -> n925
        # In59 -> n926
        # In60 -> n927
        # In61 -> n928
        # In62 -> n929
        # In63 -> n930
        # In64 -> n931
        # In65 -> n932
        # In66 -> n933
        # In67 -> n934
        # In68 -> n935
        # In69 -> n936
        # In70 -> n937
        # In71 -> n938
        # In72 -> n939
        # In73 -> n940
        # In74 -> n941
        # In75 -> n942
        # In76 -> n943
        # In77 -> n944
        # In78 -> n945
        # In79 -> n946
        # In80 -> n947
        # In81 -> n948
        n949_1 = self.col_1(n868, n869, n870, n871, n872, n873, n874, n875, n876)
        n950_1 = self.col_2(n877, n878, n879, n880, n881, n882, n883, n884, n885)
        n951_1 = self.col_3(n886, n887, n888, n889, n890, n891, n892, n893, n894)
        n952_1 = self.col_4(n895, n896, n897, n898, n899, n900, n901, n902, n903)
        n953_1 = self.col_5(n904, n905, n906, n907, n908, n909, n910, n911, n912)
        n954_1 = self.col_6(n913, n914, n915, n916, n917, n918, n919, n920, n921)
        n955_1 = self.col_7(n922, n923, n924, n925, n926, n927, n928, n929, n930)
        n956_1 = self.col_8(n931, n932, n933, n934, n935, n936, n937, n938, n939)
        n957_1 = self.col_9(n940, n941, n942, n943, n944, n945, n946, n947, n948)
        # sudoku/columns/Logical Operator -> n958
        tn250 = self.context.mk_and(n956_1, n957_1)
        tn249 = self.context.mk_and(n955_1, tn250)
        tn248 = self.context.mk_and(n954_1, tn249)
        tn247 = self.context.mk_and(n953_1, tn248)
        tn246 = self.context.mk_and(n952_1, tn247)
        tn245 = self.context.mk_and(n951_1, tn246)
        tn244 = self.context.mk_and(n950_1, tn245)
        n958 = self.context.mk_and(n949_1, tn244)
        self.nets['sudoku/columns/Logical Operator'] = n958
        # n958 -> Out1
        return n958

    def bounds28(self, n960):
        # In1 -> n960
        # sudoku/bounds28/lb
        n961 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds28/lb'] = n961
        # sudoku/bounds28/leq -> n962
        n962 = self.context.mk_leq(n961, n960)
        self.nets['sudoku/bounds28/leq'] = n962
        # sudoku/bounds28/ub
        n963 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds28/ub'] = n963
        # sudoku/bounds28/geq -> n964
        n964 = self.context.mk_leq(n960, n963)
        self.nets['sudoku/bounds28/geq'] = n964
        # sudoku/bounds28/Logical Operator -> n965
        n965 = self.context.mk_and(n962, n964)
        self.nets['sudoku/bounds28/Logical Operator'] = n965
        # sudoku/bounds28/Assumption
        self.context.mk_assumption(n965)
        return 

    def bounds27(self, n967):
        # In1 -> n967
        # sudoku/bounds27/lb
        n968 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds27/lb'] = n968
        # sudoku/bounds27/leq -> n969
        n969 = self.context.mk_leq(n968, n967)
        self.nets['sudoku/bounds27/leq'] = n969
        # sudoku/bounds27/ub
        n970 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds27/ub'] = n970
        # sudoku/bounds27/geq -> n971
        n971 = self.context.mk_leq(n967, n970)
        self.nets['sudoku/bounds27/geq'] = n971
        # sudoku/bounds27/Logical Operator -> n972
        n972 = self.context.mk_and(n969, n971)
        self.nets['sudoku/bounds27/Logical Operator'] = n972
        # sudoku/bounds27/Assumption
        self.context.mk_assumption(n972)
        return 

    def bounds26(self, n974):
        # In1 -> n974
        # sudoku/bounds26/lb
        n975 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds26/lb'] = n975
        # sudoku/bounds26/leq -> n976
        n976 = self.context.mk_leq(n975, n974)
        self.nets['sudoku/bounds26/leq'] = n976
        # sudoku/bounds26/ub
        n977 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds26/ub'] = n977
        # sudoku/bounds26/geq -> n978
        n978 = self.context.mk_leq(n974, n977)
        self.nets['sudoku/bounds26/geq'] = n978
        # sudoku/bounds26/Logical Operator -> n979
        n979 = self.context.mk_and(n976, n978)
        self.nets['sudoku/bounds26/Logical Operator'] = n979
        # sudoku/bounds26/Assumption
        self.context.mk_assumption(n979)
        return 

    def bounds25(self, n981):
        # In1 -> n981
        # sudoku/bounds25/lb
        n982 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds25/lb'] = n982
        # sudoku/bounds25/leq -> n983
        n983 = self.context.mk_leq(n982, n981)
        self.nets['sudoku/bounds25/leq'] = n983
        # sudoku/bounds25/ub
        n984 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds25/ub'] = n984
        # sudoku/bounds25/geq -> n985
        n985 = self.context.mk_leq(n981, n984)
        self.nets['sudoku/bounds25/geq'] = n985
        # sudoku/bounds25/Logical Operator -> n986
        n986 = self.context.mk_and(n983, n985)
        self.nets['sudoku/bounds25/Logical Operator'] = n986
        # sudoku/bounds25/Assumption
        self.context.mk_assumption(n986)
        return 

    def bounds29(self, n988):
        # In1 -> n988
        # sudoku/bounds29/lb
        n989 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds29/lb'] = n989
        # sudoku/bounds29/leq -> n990
        n990 = self.context.mk_leq(n989, n988)
        self.nets['sudoku/bounds29/leq'] = n990
        # sudoku/bounds29/ub
        n991 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds29/ub'] = n991
        # sudoku/bounds29/geq -> n992
        n992 = self.context.mk_leq(n988, n991)
        self.nets['sudoku/bounds29/geq'] = n992
        # sudoku/bounds29/Logical Operator -> n993
        n993 = self.context.mk_and(n990, n992)
        self.nets['sudoku/bounds29/Logical Operator'] = n993
        # sudoku/bounds29/Assumption
        self.context.mk_assumption(n993)
        return 

    def bounds20(self, n995):
        # In1 -> n995
        # sudoku/bounds20/lb
        n996 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds20/lb'] = n996
        # sudoku/bounds20/leq -> n997
        n997 = self.context.mk_leq(n996, n995)
        self.nets['sudoku/bounds20/leq'] = n997
        # sudoku/bounds20/ub
        n998 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds20/ub'] = n998
        # sudoku/bounds20/geq -> n999
        n999 = self.context.mk_leq(n995, n998)
        self.nets['sudoku/bounds20/geq'] = n999
        # sudoku/bounds20/Logical Operator -> n1000
        n1000 = self.context.mk_and(n997, n999)
        self.nets['sudoku/bounds20/Logical Operator'] = n1000
        # sudoku/bounds20/Assumption
        self.context.mk_assumption(n1000)
        return 

    def bounds24(self, n1002):
        # In1 -> n1002
        # sudoku/bounds24/lb
        n1003 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds24/lb'] = n1003
        # sudoku/bounds24/leq -> n1004
        n1004 = self.context.mk_leq(n1003, n1002)
        self.nets['sudoku/bounds24/leq'] = n1004
        # sudoku/bounds24/ub
        n1005 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds24/ub'] = n1005
        # sudoku/bounds24/geq -> n1006
        n1006 = self.context.mk_leq(n1002, n1005)
        self.nets['sudoku/bounds24/geq'] = n1006
        # sudoku/bounds24/Logical Operator -> n1007
        n1007 = self.context.mk_and(n1004, n1006)
        self.nets['sudoku/bounds24/Logical Operator'] = n1007
        # sudoku/bounds24/Assumption
        self.context.mk_assumption(n1007)
        return 

    def bounds23(self, n1009):
        # In1 -> n1009
        # sudoku/bounds23/lb
        n1010 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds23/lb'] = n1010
        # sudoku/bounds23/leq -> n1011
        n1011 = self.context.mk_leq(n1010, n1009)
        self.nets['sudoku/bounds23/leq'] = n1011
        # sudoku/bounds23/ub
        n1012 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds23/ub'] = n1012
        # sudoku/bounds23/geq -> n1013
        n1013 = self.context.mk_leq(n1009, n1012)
        self.nets['sudoku/bounds23/geq'] = n1013
        # sudoku/bounds23/Logical Operator -> n1014
        n1014 = self.context.mk_and(n1011, n1013)
        self.nets['sudoku/bounds23/Logical Operator'] = n1014
        # sudoku/bounds23/Assumption
        self.context.mk_assumption(n1014)
        return 

    def bounds22(self, n1016):
        # In1 -> n1016
        # sudoku/bounds22/lb
        n1017 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds22/lb'] = n1017
        # sudoku/bounds22/leq -> n1018
        n1018 = self.context.mk_leq(n1017, n1016)
        self.nets['sudoku/bounds22/leq'] = n1018
        # sudoku/bounds22/ub
        n1019 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds22/ub'] = n1019
        # sudoku/bounds22/geq -> n1020
        n1020 = self.context.mk_leq(n1016, n1019)
        self.nets['sudoku/bounds22/geq'] = n1020
        # sudoku/bounds22/Logical Operator -> n1021
        n1021 = self.context.mk_and(n1018, n1020)
        self.nets['sudoku/bounds22/Logical Operator'] = n1021
        # sudoku/bounds22/Assumption
        self.context.mk_assumption(n1021)
        return 

    def bounds21(self, n1023):
        # In1 -> n1023
        # sudoku/bounds21/lb
        n1024 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds21/lb'] = n1024
        # sudoku/bounds21/leq -> n1025
        n1025 = self.context.mk_leq(n1024, n1023)
        self.nets['sudoku/bounds21/leq'] = n1025
        # sudoku/bounds21/ub
        n1026 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds21/ub'] = n1026
        # sudoku/bounds21/geq -> n1027
        n1027 = self.context.mk_leq(n1023, n1026)
        self.nets['sudoku/bounds21/geq'] = n1027
        # sudoku/bounds21/Logical Operator -> n1028
        n1028 = self.context.mk_and(n1025, n1027)
        self.nets['sudoku/bounds21/Logical Operator'] = n1028
        # sudoku/bounds21/Assumption
        self.context.mk_assumption(n1028)
        return 

    def bounds17(self, n1030):
        # In1 -> n1030
        # sudoku/bounds17/lb
        n1031 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds17/lb'] = n1031
        # sudoku/bounds17/leq -> n1032
        n1032 = self.context.mk_leq(n1031, n1030)
        self.nets['sudoku/bounds17/leq'] = n1032
        # sudoku/bounds17/ub
        n1033 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds17/ub'] = n1033
        # sudoku/bounds17/geq -> n1034
        n1034 = self.context.mk_leq(n1030, n1033)
        self.nets['sudoku/bounds17/geq'] = n1034
        # sudoku/bounds17/Logical Operator -> n1035
        n1035 = self.context.mk_and(n1032, n1034)
        self.nets['sudoku/bounds17/Logical Operator'] = n1035
        # sudoku/bounds17/Assumption
        self.context.mk_assumption(n1035)
        return 

    def bounds16(self, n1037):
        # In1 -> n1037
        # sudoku/bounds16/lb
        n1038 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds16/lb'] = n1038
        # sudoku/bounds16/leq -> n1039
        n1039 = self.context.mk_leq(n1038, n1037)
        self.nets['sudoku/bounds16/leq'] = n1039
        # sudoku/bounds16/ub
        n1040 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds16/ub'] = n1040
        # sudoku/bounds16/geq -> n1041
        n1041 = self.context.mk_leq(n1037, n1040)
        self.nets['sudoku/bounds16/geq'] = n1041
        # sudoku/bounds16/Logical Operator -> n1042
        n1042 = self.context.mk_and(n1039, n1041)
        self.nets['sudoku/bounds16/Logical Operator'] = n1042
        # sudoku/bounds16/Assumption
        self.context.mk_assumption(n1042)
        return 

    def bounds15(self, n1044):
        # In1 -> n1044
        # sudoku/bounds15/lb
        n1045 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds15/lb'] = n1045
        # sudoku/bounds15/leq -> n1046
        n1046 = self.context.mk_leq(n1045, n1044)
        self.nets['sudoku/bounds15/leq'] = n1046
        # sudoku/bounds15/ub
        n1047 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds15/ub'] = n1047
        # sudoku/bounds15/geq -> n1048
        n1048 = self.context.mk_leq(n1044, n1047)
        self.nets['sudoku/bounds15/geq'] = n1048
        # sudoku/bounds15/Logical Operator -> n1049
        n1049 = self.context.mk_and(n1046, n1048)
        self.nets['sudoku/bounds15/Logical Operator'] = n1049
        # sudoku/bounds15/Assumption
        self.context.mk_assumption(n1049)
        return 

    def bounds14(self, n1051):
        # In1 -> n1051
        # sudoku/bounds14/lb
        n1052 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds14/lb'] = n1052
        # sudoku/bounds14/leq -> n1053
        n1053 = self.context.mk_leq(n1052, n1051)
        self.nets['sudoku/bounds14/leq'] = n1053
        # sudoku/bounds14/ub
        n1054 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds14/ub'] = n1054
        # sudoku/bounds14/geq -> n1055
        n1055 = self.context.mk_leq(n1051, n1054)
        self.nets['sudoku/bounds14/geq'] = n1055
        # sudoku/bounds14/Logical Operator -> n1056
        n1056 = self.context.mk_and(n1053, n1055)
        self.nets['sudoku/bounds14/Logical Operator'] = n1056
        # sudoku/bounds14/Assumption
        self.context.mk_assumption(n1056)
        return 

    def bounds19(self, n1058):
        # In1 -> n1058
        # sudoku/bounds19/lb
        n1059 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds19/lb'] = n1059
        # sudoku/bounds19/leq -> n1060
        n1060 = self.context.mk_leq(n1059, n1058)
        self.nets['sudoku/bounds19/leq'] = n1060
        # sudoku/bounds19/ub
        n1061 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds19/ub'] = n1061
        # sudoku/bounds19/geq -> n1062
        n1062 = self.context.mk_leq(n1058, n1061)
        self.nets['sudoku/bounds19/geq'] = n1062
        # sudoku/bounds19/Logical Operator -> n1063
        n1063 = self.context.mk_and(n1060, n1062)
        self.nets['sudoku/bounds19/Logical Operator'] = n1063
        # sudoku/bounds19/Assumption
        self.context.mk_assumption(n1063)
        return 

    def bounds18(self, n1065):
        # In1 -> n1065
        # sudoku/bounds18/lb
        n1066 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds18/lb'] = n1066
        # sudoku/bounds18/leq -> n1067
        n1067 = self.context.mk_leq(n1066, n1065)
        self.nets['sudoku/bounds18/leq'] = n1067
        # sudoku/bounds18/ub
        n1068 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds18/ub'] = n1068
        # sudoku/bounds18/geq -> n1069
        n1069 = self.context.mk_leq(n1065, n1068)
        self.nets['sudoku/bounds18/geq'] = n1069
        # sudoku/bounds18/Logical Operator -> n1070
        n1070 = self.context.mk_and(n1067, n1069)
        self.nets['sudoku/bounds18/Logical Operator'] = n1070
        # sudoku/bounds18/Assumption
        self.context.mk_assumption(n1070)
        return 

    def bounds13(self, n1072):
        # In1 -> n1072
        # sudoku/bounds13/lb
        n1073 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds13/lb'] = n1073
        # sudoku/bounds13/leq -> n1074
        n1074 = self.context.mk_leq(n1073, n1072)
        self.nets['sudoku/bounds13/leq'] = n1074
        # sudoku/bounds13/ub
        n1075 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds13/ub'] = n1075
        # sudoku/bounds13/geq -> n1076
        n1076 = self.context.mk_leq(n1072, n1075)
        self.nets['sudoku/bounds13/geq'] = n1076
        # sudoku/bounds13/Logical Operator -> n1077
        n1077 = self.context.mk_and(n1074, n1076)
        self.nets['sudoku/bounds13/Logical Operator'] = n1077
        # sudoku/bounds13/Assumption
        self.context.mk_assumption(n1077)
        return 

    def bounds12(self, n1079):
        # In1 -> n1079
        # sudoku/bounds12/lb
        n1080 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds12/lb'] = n1080
        # sudoku/bounds12/leq -> n1081
        n1081 = self.context.mk_leq(n1080, n1079)
        self.nets['sudoku/bounds12/leq'] = n1081
        # sudoku/bounds12/ub
        n1082 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds12/ub'] = n1082
        # sudoku/bounds12/geq -> n1083
        n1083 = self.context.mk_leq(n1079, n1082)
        self.nets['sudoku/bounds12/geq'] = n1083
        # sudoku/bounds12/Logical Operator -> n1084
        n1084 = self.context.mk_and(n1081, n1083)
        self.nets['sudoku/bounds12/Logical Operator'] = n1084
        # sudoku/bounds12/Assumption
        self.context.mk_assumption(n1084)
        return 

    def bounds11(self, n1086):
        # In1 -> n1086
        # sudoku/bounds11/lb
        n1087 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds11/lb'] = n1087
        # sudoku/bounds11/leq -> n1088
        n1088 = self.context.mk_leq(n1087, n1086)
        self.nets['sudoku/bounds11/leq'] = n1088
        # sudoku/bounds11/ub
        n1089 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds11/ub'] = n1089
        # sudoku/bounds11/geq -> n1090
        n1090 = self.context.mk_leq(n1086, n1089)
        self.nets['sudoku/bounds11/geq'] = n1090
        # sudoku/bounds11/Logical Operator -> n1091
        n1091 = self.context.mk_and(n1088, n1090)
        self.nets['sudoku/bounds11/Logical Operator'] = n1091
        # sudoku/bounds11/Assumption
        self.context.mk_assumption(n1091)
        return 

    def bounds10(self, n1093):
        # In1 -> n1093
        # sudoku/bounds10/lb
        n1094 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds10/lb'] = n1094
        # sudoku/bounds10/leq -> n1095
        n1095 = self.context.mk_leq(n1094, n1093)
        self.nets['sudoku/bounds10/leq'] = n1095
        # sudoku/bounds10/ub
        n1096 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds10/ub'] = n1096
        # sudoku/bounds10/geq -> n1097
        n1097 = self.context.mk_leq(n1093, n1096)
        self.nets['sudoku/bounds10/geq'] = n1097
        # sudoku/bounds10/Logical Operator -> n1098
        n1098 = self.context.mk_and(n1095, n1097)
        self.nets['sudoku/bounds10/Logical Operator'] = n1098
        # sudoku/bounds10/Assumption
        self.context.mk_assumption(n1098)
        return 

    def bounds81(self, n1100):
        # In1 -> n1100
        # sudoku/bounds81/lb
        n1101 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds81/lb'] = n1101
        # sudoku/bounds81/leq -> n1102
        n1102 = self.context.mk_leq(n1101, n1100)
        self.nets['sudoku/bounds81/leq'] = n1102
        # sudoku/bounds81/ub
        n1103 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds81/ub'] = n1103
        # sudoku/bounds81/geq -> n1104
        n1104 = self.context.mk_leq(n1100, n1103)
        self.nets['sudoku/bounds81/geq'] = n1104
        # sudoku/bounds81/Logical Operator -> n1105
        n1105 = self.context.mk_and(n1102, n1104)
        self.nets['sudoku/bounds81/Logical Operator'] = n1105
        # sudoku/bounds81/Assumption
        self.context.mk_assumption(n1105)
        return 

    def bounds80(self, n1107):
        # In1 -> n1107
        # sudoku/bounds80/lb
        n1108 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds80/lb'] = n1108
        # sudoku/bounds80/leq -> n1109
        n1109 = self.context.mk_leq(n1108, n1107)
        self.nets['sudoku/bounds80/leq'] = n1109
        # sudoku/bounds80/ub
        n1110 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds80/ub'] = n1110
        # sudoku/bounds80/geq -> n1111
        n1111 = self.context.mk_leq(n1107, n1110)
        self.nets['sudoku/bounds80/geq'] = n1111
        # sudoku/bounds80/Logical Operator -> n1112
        n1112 = self.context.mk_and(n1109, n1111)
        self.nets['sudoku/bounds80/Logical Operator'] = n1112
        # sudoku/bounds80/Assumption
        self.context.mk_assumption(n1112)
        return 

    def BlockRewire(self, n1114, n1115, n1116, n1117, n1118, n1119, n1120, n1121, n1122, n1123, n1124, n1125, n1126, n1127, n1128, n1129, n1130, n1131, n1132, n1133, n1134, n1135, n1136, n1137, n1138, n1139, n1140, n1141, n1142, n1143, n1144, n1145, n1146, n1147, n1148, n1149, n1150, n1151, n1152, n1153, n1154, n1155, n1156, n1157, n1158, n1159, n1160, n1161, n1162, n1163, n1164, n1165, n1166, n1167, n1168, n1169, n1170, n1171, n1172, n1173, n1174, n1175, n1176, n1177, n1178, n1179, n1180, n1181, n1182, n1183, n1184, n1185, n1186, n1187, n1188, n1189, n1190, n1191, n1192, n1193, n1194):
        # In1 -> n1114
        # In2 -> n1115
        # In3 -> n1116
        # In4 -> n1117
        # In5 -> n1118
        # In6 -> n1119
        # In7 -> n1120
        # In8 -> n1121
        # In9 -> n1122
        # In10 -> n1123
        # In11 -> n1124
        # In12 -> n1125
        # In13 -> n1126
        # In14 -> n1127
        # In15 -> n1128
        # In16 -> n1129
        # In17 -> n1130
        # In18 -> n1131
        # In19 -> n1132
        # In20 -> n1133
        # In21 -> n1134
        # In22 -> n1135
        # In23 -> n1136
        # In24 -> n1137
        # In25 -> n1138
        # In26 -> n1139
        # In27 -> n1140
        # In28 -> n1141
        # In29 -> n1142
        # In30 -> n1143
        # In31 -> n1144
        # In32 -> n1145
        # In33 -> n1146
        # In34 -> n1147
        # In35 -> n1148
        # In36 -> n1149
        # In37 -> n1150
        # In38 -> n1151
        # In39 -> n1152
        # In40 -> n1153
        # In41 -> n1154
        # In42 -> n1155
        # In43 -> n1156
        # In44 -> n1157
        # In45 -> n1158
        # In46 -> n1159
        # In47 -> n1160
        # In48 -> n1161
        # In49 -> n1162
        # In50 -> n1163
        # In51 -> n1164
        # In52 -> n1165
        # In53 -> n1166
        # In54 -> n1167
        # In55 -> n1168
        # In56 -> n1169
        # In57 -> n1170
        # In58 -> n1171
        # In59 -> n1172
        # In60 -> n1173
        # In61 -> n1174
        # In62 -> n1175
        # In63 -> n1176
        # In64 -> n1177
        # In65 -> n1178
        # In66 -> n1179
        # In67 -> n1180
        # In68 -> n1181
        # In69 -> n1182
        # In70 -> n1183
        # In71 -> n1184
        # In72 -> n1185
        # In73 -> n1186
        # In74 -> n1187
        # In75 -> n1188
        # In76 -> n1189
        # In77 -> n1190
        # In78 -> n1191
        # In79 -> n1192
        # In80 -> n1193
        # In81 -> n1194
        # n1114 -> Out1
        # n1115 -> Out10
        # n1116 -> Out19
        # n1123 -> Out2
        # n1124 -> Out11
        # n1125 -> Out20
        # n1132 -> Out3
        # n1133 -> Out12
        # n1134 -> Out21
        # n1117 -> Out28
        # n1118 -> Out37
        # n1119 -> Out46
        # n1126 -> Out29
        # n1127 -> Out38
        # n1128 -> Out47
        # n1135 -> Out30
        # n1136 -> Out39
        # n1137 -> Out48
        # n1120 -> Out55
        # n1121 -> Out64
        # n1122 -> Out73
        # n1129 -> Out56
        # n1130 -> Out65
        # n1131 -> Out74
        # n1138 -> Out57
        # n1139 -> Out66
        # n1140 -> Out75
        # n1141 -> Out4
        # n1142 -> Out13
        # n1143 -> Out22
        # n1150 -> Out5
        # n1151 -> Out14
        # n1152 -> Out23
        # n1159 -> Out6
        # n1160 -> Out15
        # n1161 -> Out24
        # n1144 -> Out31
        # n1145 -> Out40
        # n1146 -> Out49
        # n1153 -> Out32
        # n1154 -> Out41
        # n1155 -> Out50
        # n1162 -> Out33
        # n1163 -> Out42
        # n1164 -> Out51
        # n1147 -> Out58
        # n1148 -> Out67
        # n1149 -> Out76
        # n1156 -> Out59
        # n1157 -> Out68
        # n1158 -> Out77
        # n1165 -> Out60
        # n1166 -> Out69
        # n1167 -> Out78
        # n1168 -> Out7
        # n1169 -> Out16
        # n1170 -> Out25
        # n1177 -> Out8
        # n1178 -> Out17
        # n1179 -> Out26
        # n1186 -> Out9
        # n1187 -> Out18
        # n1188 -> Out27
        # n1171 -> Out34
        # n1172 -> Out43
        # n1173 -> Out52
        # n1180 -> Out35
        # n1181 -> Out44
        # n1182 -> Out53
        # n1189 -> Out36
        # n1190 -> Out45
        # n1191 -> Out54
        # n1174 -> Out61
        # n1175 -> Out70
        # n1176 -> Out79
        # n1183 -> Out62
        # n1184 -> Out71
        # n1185 -> Out80
        # n1192 -> Out63
        # n1193 -> Out72
        # n1194 -> Out81
        return n1114, n1115, n1116, n1123, n1124, n1125, n1132, n1133, n1134, n1117, n1118, n1119, n1126, n1127, n1128, n1135, n1136, n1137, n1120, n1121, n1122, n1129, n1130, n1131, n1138, n1139, n1140, n1141, n1142, n1143, n1150, n1151, n1152, n1159, n1160, n1161, n1144, n1145, n1146, n1153, n1154, n1155, n1162, n1163, n1164, n1147, n1148, n1149, n1156, n1157, n1158, n1165, n1166, n1167, n1168, n1169, n1170, n1177, n1178, n1179, n1186, n1187, n1188, n1171, n1172, n1173, n1180, n1181, n1182, n1189, n1190, n1191, n1174, n1175, n1176, n1183, n1184, n1185, n1192, n1193, n1194

    def bounds71(self, n1276):
        # In1 -> n1276
        # sudoku/bounds71/lb
        n1277 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds71/lb'] = n1277
        # sudoku/bounds71/leq -> n1278
        n1278 = self.context.mk_leq(n1277, n1276)
        self.nets['sudoku/bounds71/leq'] = n1278
        # sudoku/bounds71/ub
        n1279 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds71/ub'] = n1279
        # sudoku/bounds71/geq -> n1280
        n1280 = self.context.mk_leq(n1276, n1279)
        self.nets['sudoku/bounds71/geq'] = n1280
        # sudoku/bounds71/Logical Operator -> n1281
        n1281 = self.context.mk_and(n1278, n1280)
        self.nets['sudoku/bounds71/Logical Operator'] = n1281
        # sudoku/bounds71/Assumption
        self.context.mk_assumption(n1281)
        return 

    def bounds70(self, n1283):
        # In1 -> n1283
        # sudoku/bounds70/lb
        n1284 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds70/lb'] = n1284
        # sudoku/bounds70/leq -> n1285
        n1285 = self.context.mk_leq(n1284, n1283)
        self.nets['sudoku/bounds70/leq'] = n1285
        # sudoku/bounds70/ub
        n1286 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds70/ub'] = n1286
        # sudoku/bounds70/geq -> n1287
        n1287 = self.context.mk_leq(n1283, n1286)
        self.nets['sudoku/bounds70/geq'] = n1287
        # sudoku/bounds70/Logical Operator -> n1288
        n1288 = self.context.mk_and(n1285, n1287)
        self.nets['sudoku/bounds70/Logical Operator'] = n1288
        # sudoku/bounds70/Assumption
        self.context.mk_assumption(n1288)
        return 

    def bounds75(self, n1290):
        # In1 -> n1290
        # sudoku/bounds75/lb
        n1291 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds75/lb'] = n1291
        # sudoku/bounds75/leq -> n1292
        n1292 = self.context.mk_leq(n1291, n1290)
        self.nets['sudoku/bounds75/leq'] = n1292
        # sudoku/bounds75/ub
        n1293 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds75/ub'] = n1293
        # sudoku/bounds75/geq -> n1294
        n1294 = self.context.mk_leq(n1290, n1293)
        self.nets['sudoku/bounds75/geq'] = n1294
        # sudoku/bounds75/Logical Operator -> n1295
        n1295 = self.context.mk_and(n1292, n1294)
        self.nets['sudoku/bounds75/Logical Operator'] = n1295
        # sudoku/bounds75/Assumption
        self.context.mk_assumption(n1295)
        return 

    def bounds74(self, n1297):
        # In1 -> n1297
        # sudoku/bounds74/lb
        n1298 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds74/lb'] = n1298
        # sudoku/bounds74/leq -> n1299
        n1299 = self.context.mk_leq(n1298, n1297)
        self.nets['sudoku/bounds74/leq'] = n1299
        # sudoku/bounds74/ub
        n1300 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds74/ub'] = n1300
        # sudoku/bounds74/geq -> n1301
        n1301 = self.context.mk_leq(n1297, n1300)
        self.nets['sudoku/bounds74/geq'] = n1301
        # sudoku/bounds74/Logical Operator -> n1302
        n1302 = self.context.mk_and(n1299, n1301)
        self.nets['sudoku/bounds74/Logical Operator'] = n1302
        # sudoku/bounds74/Assumption
        self.context.mk_assumption(n1302)
        return 

    def bounds73(self, n1304):
        # In1 -> n1304
        # sudoku/bounds73/lb
        n1305 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds73/lb'] = n1305
        # sudoku/bounds73/leq -> n1306
        n1306 = self.context.mk_leq(n1305, n1304)
        self.nets['sudoku/bounds73/leq'] = n1306
        # sudoku/bounds73/ub
        n1307 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds73/ub'] = n1307
        # sudoku/bounds73/geq -> n1308
        n1308 = self.context.mk_leq(n1304, n1307)
        self.nets['sudoku/bounds73/geq'] = n1308
        # sudoku/bounds73/Logical Operator -> n1309
        n1309 = self.context.mk_and(n1306, n1308)
        self.nets['sudoku/bounds73/Logical Operator'] = n1309
        # sudoku/bounds73/Assumption
        self.context.mk_assumption(n1309)
        return 

    def bounds72(self, n1311):
        # In1 -> n1311
        # sudoku/bounds72/lb
        n1312 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds72/lb'] = n1312
        # sudoku/bounds72/leq -> n1313
        n1313 = self.context.mk_leq(n1312, n1311)
        self.nets['sudoku/bounds72/leq'] = n1313
        # sudoku/bounds72/ub
        n1314 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds72/ub'] = n1314
        # sudoku/bounds72/geq -> n1315
        n1315 = self.context.mk_leq(n1311, n1314)
        self.nets['sudoku/bounds72/geq'] = n1315
        # sudoku/bounds72/Logical Operator -> n1316
        n1316 = self.context.mk_and(n1313, n1315)
        self.nets['sudoku/bounds72/Logical Operator'] = n1316
        # sudoku/bounds72/Assumption
        self.context.mk_assumption(n1316)
        return 

    def bounds79(self, n1318):
        # In1 -> n1318
        # sudoku/bounds79/lb
        n1319 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds79/lb'] = n1319
        # sudoku/bounds79/leq -> n1320
        n1320 = self.context.mk_leq(n1319, n1318)
        self.nets['sudoku/bounds79/leq'] = n1320
        # sudoku/bounds79/ub
        n1321 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds79/ub'] = n1321
        # sudoku/bounds79/geq -> n1322
        n1322 = self.context.mk_leq(n1318, n1321)
        self.nets['sudoku/bounds79/geq'] = n1322
        # sudoku/bounds79/Logical Operator -> n1323
        n1323 = self.context.mk_and(n1320, n1322)
        self.nets['sudoku/bounds79/Logical Operator'] = n1323
        # sudoku/bounds79/Assumption
        self.context.mk_assumption(n1323)
        return 

    def bounds78(self, n1325):
        # In1 -> n1325
        # sudoku/bounds78/lb
        n1326 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds78/lb'] = n1326
        # sudoku/bounds78/leq -> n1327
        n1327 = self.context.mk_leq(n1326, n1325)
        self.nets['sudoku/bounds78/leq'] = n1327
        # sudoku/bounds78/ub
        n1328 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds78/ub'] = n1328
        # sudoku/bounds78/geq -> n1329
        n1329 = self.context.mk_leq(n1325, n1328)
        self.nets['sudoku/bounds78/geq'] = n1329
        # sudoku/bounds78/Logical Operator -> n1330
        n1330 = self.context.mk_and(n1327, n1329)
        self.nets['sudoku/bounds78/Logical Operator'] = n1330
        # sudoku/bounds78/Assumption
        self.context.mk_assumption(n1330)
        return 

    def bounds77(self, n1332):
        # In1 -> n1332
        # sudoku/bounds77/lb
        n1333 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds77/lb'] = n1333
        # sudoku/bounds77/leq -> n1334
        n1334 = self.context.mk_leq(n1333, n1332)
        self.nets['sudoku/bounds77/leq'] = n1334
        # sudoku/bounds77/ub
        n1335 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds77/ub'] = n1335
        # sudoku/bounds77/geq -> n1336
        n1336 = self.context.mk_leq(n1332, n1335)
        self.nets['sudoku/bounds77/geq'] = n1336
        # sudoku/bounds77/Logical Operator -> n1337
        n1337 = self.context.mk_and(n1334, n1336)
        self.nets['sudoku/bounds77/Logical Operator'] = n1337
        # sudoku/bounds77/Assumption
        self.context.mk_assumption(n1337)
        return 

    def bounds76(self, n1339):
        # In1 -> n1339
        # sudoku/bounds76/lb
        n1340 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds76/lb'] = n1340
        # sudoku/bounds76/leq -> n1341
        n1341 = self.context.mk_leq(n1340, n1339)
        self.nets['sudoku/bounds76/leq'] = n1341
        # sudoku/bounds76/ub
        n1342 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds76/ub'] = n1342
        # sudoku/bounds76/geq -> n1343
        n1343 = self.context.mk_leq(n1339, n1342)
        self.nets['sudoku/bounds76/geq'] = n1343
        # sudoku/bounds76/Logical Operator -> n1344
        n1344 = self.context.mk_and(n1341, n1343)
        self.nets['sudoku/bounds76/Logical Operator'] = n1344
        # sudoku/bounds76/Assumption
        self.context.mk_assumption(n1344)
        return 

    def bounds60(self, n1346):
        # In1 -> n1346
        # sudoku/bounds60/lb
        n1347 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds60/lb'] = n1347
        # sudoku/bounds60/leq -> n1348
        n1348 = self.context.mk_leq(n1347, n1346)
        self.nets['sudoku/bounds60/leq'] = n1348
        # sudoku/bounds60/ub
        n1349 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds60/ub'] = n1349
        # sudoku/bounds60/geq -> n1350
        n1350 = self.context.mk_leq(n1346, n1349)
        self.nets['sudoku/bounds60/geq'] = n1350
        # sudoku/bounds60/Logical Operator -> n1351
        n1351 = self.context.mk_and(n1348, n1350)
        self.nets['sudoku/bounds60/Logical Operator'] = n1351
        # sudoku/bounds60/Assumption
        self.context.mk_assumption(n1351)
        return 

    def bounds69(self, n1353):
        # In1 -> n1353
        # sudoku/bounds69/lb
        n1354 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds69/lb'] = n1354
        # sudoku/bounds69/leq -> n1355
        n1355 = self.context.mk_leq(n1354, n1353)
        self.nets['sudoku/bounds69/leq'] = n1355
        # sudoku/bounds69/ub
        n1356 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds69/ub'] = n1356
        # sudoku/bounds69/geq -> n1357
        n1357 = self.context.mk_leq(n1353, n1356)
        self.nets['sudoku/bounds69/geq'] = n1357
        # sudoku/bounds69/Logical Operator -> n1358
        n1358 = self.context.mk_and(n1355, n1357)
        self.nets['sudoku/bounds69/Logical Operator'] = n1358
        # sudoku/bounds69/Assumption
        self.context.mk_assumption(n1358)
        return 

    def ColRewire(self, n1360, n1361, n1362, n1363, n1364, n1365, n1366, n1367, n1368, n1369, n1370, n1371, n1372, n1373, n1374, n1375, n1376, n1377, n1378, n1379, n1380, n1381, n1382, n1383, n1384, n1385, n1386, n1387, n1388, n1389, n1390, n1391, n1392, n1393, n1394, n1395, n1396, n1397, n1398, n1399, n1400, n1401, n1402, n1403, n1404, n1405, n1406, n1407, n1408, n1409, n1410, n1411, n1412, n1413, n1414, n1415, n1416, n1417, n1418, n1419, n1420, n1421, n1422, n1423, n1424, n1425, n1426, n1427, n1428, n1429, n1430, n1431, n1432, n1433, n1434, n1435, n1436, n1437, n1438, n1439, n1440):
        # In1 -> n1360
        # In2 -> n1361
        # In3 -> n1362
        # In4 -> n1363
        # In5 -> n1364
        # In6 -> n1365
        # In7 -> n1366
        # In8 -> n1367
        # In9 -> n1368
        # In10 -> n1369
        # In11 -> n1370
        # In12 -> n1371
        # In13 -> n1372
        # In14 -> n1373
        # In15 -> n1374
        # In16 -> n1375
        # In17 -> n1376
        # In18 -> n1377
        # In19 -> n1378
        # In20 -> n1379
        # In21 -> n1380
        # In22 -> n1381
        # In23 -> n1382
        # In24 -> n1383
        # In25 -> n1384
        # In26 -> n1385
        # In27 -> n1386
        # In28 -> n1387
        # In29 -> n1388
        # In30 -> n1389
        # In31 -> n1390
        # In32 -> n1391
        # In33 -> n1392
        # In34 -> n1393
        # In35 -> n1394
        # In36 -> n1395
        # In37 -> n1396
        # In38 -> n1397
        # In39 -> n1398
        # In40 -> n1399
        # In41 -> n1400
        # In42 -> n1401
        # In43 -> n1402
        # In44 -> n1403
        # In45 -> n1404
        # In46 -> n1405
        # In47 -> n1406
        # In48 -> n1407
        # In49 -> n1408
        # In50 -> n1409
        # In51 -> n1410
        # In52 -> n1411
        # In53 -> n1412
        # In54 -> n1413
        # In55 -> n1414
        # In56 -> n1415
        # In57 -> n1416
        # In58 -> n1417
        # In59 -> n1418
        # In60 -> n1419
        # In61 -> n1420
        # In62 -> n1421
        # In63 -> n1422
        # In64 -> n1423
        # In65 -> n1424
        # In66 -> n1425
        # In67 -> n1426
        # In68 -> n1427
        # In69 -> n1428
        # In70 -> n1429
        # In71 -> n1430
        # In72 -> n1431
        # In73 -> n1432
        # In74 -> n1433
        # In75 -> n1434
        # In76 -> n1435
        # In77 -> n1436
        # In78 -> n1437
        # In79 -> n1438
        # In80 -> n1439
        # In81 -> n1440
        # n1360 -> Out1
        # n1369 -> Out2
        # n1378 -> Out3
        # n1387 -> Out4
        # n1396 -> Out5
        # n1405 -> Out6
        # n1414 -> Out7
        # n1423 -> Out8
        # n1432 -> Out9
        # n1361 -> Out10
        # n1370 -> Out11
        # n1379 -> Out12
        # n1388 -> Out13
        # n1397 -> Out14
        # n1406 -> Out15
        # n1415 -> Out16
        # n1424 -> Out17
        # n1433 -> Out18
        # n1362 -> Out19
        # n1371 -> Out20
        # n1380 -> Out21
        # n1389 -> Out22
        # n1398 -> Out23
        # n1407 -> Out24
        # n1416 -> Out25
        # n1425 -> Out26
        # n1434 -> Out27
        # n1363 -> Out28
        # n1372 -> Out29
        # n1381 -> Out30
        # n1390 -> Out31
        # n1399 -> Out32
        # n1408 -> Out33
        # n1417 -> Out34
        # n1426 -> Out35
        # n1435 -> Out36
        # n1364 -> Out37
        # n1373 -> Out38
        # n1382 -> Out39
        # n1391 -> Out40
        # n1400 -> Out41
        # n1409 -> Out42
        # n1418 -> Out43
        # n1427 -> Out44
        # n1436 -> Out45
        # n1365 -> Out46
        # n1374 -> Out47
        # n1383 -> Out48
        # n1392 -> Out49
        # n1401 -> Out50
        # n1410 -> Out51
        # n1419 -> Out52
        # n1428 -> Out53
        # n1437 -> Out54
        # n1366 -> Out55
        # n1375 -> Out56
        # n1384 -> Out57
        # n1393 -> Out58
        # n1402 -> Out59
        # n1411 -> Out60
        # n1420 -> Out61
        # n1429 -> Out62
        # n1438 -> Out63
        # n1367 -> Out64
        # n1376 -> Out65
        # n1385 -> Out66
        # n1394 -> Out67
        # n1403 -> Out68
        # n1412 -> Out69
        # n1421 -> Out70
        # n1430 -> Out71
        # n1439 -> Out72
        # n1368 -> Out73
        # n1377 -> Out74
        # n1386 -> Out75
        # n1395 -> Out76
        # n1404 -> Out77
        # n1413 -> Out78
        # n1422 -> Out79
        # n1431 -> Out80
        # n1440 -> Out81
        return n1360, n1369, n1378, n1387, n1396, n1405, n1414, n1423, n1432, n1361, n1370, n1379, n1388, n1397, n1406, n1415, n1424, n1433, n1362, n1371, n1380, n1389, n1398, n1407, n1416, n1425, n1434, n1363, n1372, n1381, n1390, n1399, n1408, n1417, n1426, n1435, n1364, n1373, n1382, n1391, n1400, n1409, n1418, n1427, n1436, n1365, n1374, n1383, n1392, n1401, n1410, n1419, n1428, n1437, n1366, n1375, n1384, n1393, n1402, n1411, n1420, n1429, n1438, n1367, n1376, n1385, n1394, n1403, n1412, n1421, n1430, n1439, n1368, n1377, n1386, n1395, n1404, n1413, n1422, n1431, n1440

    def bounds64(self, n1522):
        # In1 -> n1522
        # sudoku/bounds64/lb
        n1523 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds64/lb'] = n1523
        # sudoku/bounds64/leq -> n1524
        n1524 = self.context.mk_leq(n1523, n1522)
        self.nets['sudoku/bounds64/leq'] = n1524
        # sudoku/bounds64/ub
        n1525 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds64/ub'] = n1525
        # sudoku/bounds64/geq -> n1526
        n1526 = self.context.mk_leq(n1522, n1525)
        self.nets['sudoku/bounds64/geq'] = n1526
        # sudoku/bounds64/Logical Operator -> n1527
        n1527 = self.context.mk_and(n1524, n1526)
        self.nets['sudoku/bounds64/Logical Operator'] = n1527
        # sudoku/bounds64/Assumption
        self.context.mk_assumption(n1527)
        return 

    def bounds63(self, n1529):
        # In1 -> n1529
        # sudoku/bounds63/lb
        n1530 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds63/lb'] = n1530
        # sudoku/bounds63/leq -> n1531
        n1531 = self.context.mk_leq(n1530, n1529)
        self.nets['sudoku/bounds63/leq'] = n1531
        # sudoku/bounds63/ub
        n1532 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds63/ub'] = n1532
        # sudoku/bounds63/geq -> n1533
        n1533 = self.context.mk_leq(n1529, n1532)
        self.nets['sudoku/bounds63/geq'] = n1533
        # sudoku/bounds63/Logical Operator -> n1534
        n1534 = self.context.mk_and(n1531, n1533)
        self.nets['sudoku/bounds63/Logical Operator'] = n1534
        # sudoku/bounds63/Assumption
        self.context.mk_assumption(n1534)
        return 

    def bounds62(self, n1536):
        # In1 -> n1536
        # sudoku/bounds62/lb
        n1537 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds62/lb'] = n1537
        # sudoku/bounds62/leq -> n1538
        n1538 = self.context.mk_leq(n1537, n1536)
        self.nets['sudoku/bounds62/leq'] = n1538
        # sudoku/bounds62/ub
        n1539 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds62/ub'] = n1539
        # sudoku/bounds62/geq -> n1540
        n1540 = self.context.mk_leq(n1536, n1539)
        self.nets['sudoku/bounds62/geq'] = n1540
        # sudoku/bounds62/Logical Operator -> n1541
        n1541 = self.context.mk_and(n1538, n1540)
        self.nets['sudoku/bounds62/Logical Operator'] = n1541
        # sudoku/bounds62/Assumption
        self.context.mk_assumption(n1541)
        return 

    def bounds61(self, n1543):
        # In1 -> n1543
        # sudoku/bounds61/lb
        n1544 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds61/lb'] = n1544
        # sudoku/bounds61/leq -> n1545
        n1545 = self.context.mk_leq(n1544, n1543)
        self.nets['sudoku/bounds61/leq'] = n1545
        # sudoku/bounds61/ub
        n1546 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds61/ub'] = n1546
        # sudoku/bounds61/geq -> n1547
        n1547 = self.context.mk_leq(n1543, n1546)
        self.nets['sudoku/bounds61/geq'] = n1547
        # sudoku/bounds61/Logical Operator -> n1548
        n1548 = self.context.mk_and(n1545, n1547)
        self.nets['sudoku/bounds61/Logical Operator'] = n1548
        # sudoku/bounds61/Assumption
        self.context.mk_assumption(n1548)
        return 

    def bounds68(self, n1550):
        # In1 -> n1550
        # sudoku/bounds68/lb
        n1551 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds68/lb'] = n1551
        # sudoku/bounds68/leq -> n1552
        n1552 = self.context.mk_leq(n1551, n1550)
        self.nets['sudoku/bounds68/leq'] = n1552
        # sudoku/bounds68/ub
        n1553 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds68/ub'] = n1553
        # sudoku/bounds68/geq -> n1554
        n1554 = self.context.mk_leq(n1550, n1553)
        self.nets['sudoku/bounds68/geq'] = n1554
        # sudoku/bounds68/Logical Operator -> n1555
        n1555 = self.context.mk_and(n1552, n1554)
        self.nets['sudoku/bounds68/Logical Operator'] = n1555
        # sudoku/bounds68/Assumption
        self.context.mk_assumption(n1555)
        return 

    def bounds67(self, n1557):
        # In1 -> n1557
        # sudoku/bounds67/lb
        n1558 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds67/lb'] = n1558
        # sudoku/bounds67/leq -> n1559
        n1559 = self.context.mk_leq(n1558, n1557)
        self.nets['sudoku/bounds67/leq'] = n1559
        # sudoku/bounds67/ub
        n1560 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds67/ub'] = n1560
        # sudoku/bounds67/geq -> n1561
        n1561 = self.context.mk_leq(n1557, n1560)
        self.nets['sudoku/bounds67/geq'] = n1561
        # sudoku/bounds67/Logical Operator -> n1562
        n1562 = self.context.mk_and(n1559, n1561)
        self.nets['sudoku/bounds67/Logical Operator'] = n1562
        # sudoku/bounds67/Assumption
        self.context.mk_assumption(n1562)
        return 

    def bounds66(self, n1564):
        # In1 -> n1564
        # sudoku/bounds66/lb
        n1565 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds66/lb'] = n1565
        # sudoku/bounds66/leq -> n1566
        n1566 = self.context.mk_leq(n1565, n1564)
        self.nets['sudoku/bounds66/leq'] = n1566
        # sudoku/bounds66/ub
        n1567 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds66/ub'] = n1567
        # sudoku/bounds66/geq -> n1568
        n1568 = self.context.mk_leq(n1564, n1567)
        self.nets['sudoku/bounds66/geq'] = n1568
        # sudoku/bounds66/Logical Operator -> n1569
        n1569 = self.context.mk_and(n1566, n1568)
        self.nets['sudoku/bounds66/Logical Operator'] = n1569
        # sudoku/bounds66/Assumption
        self.context.mk_assumption(n1569)
        return 

    def row_7(self, n1571, n1572, n1573, n1574, n1575, n1576, n1577, n1578, n1579):
        # In1 -> n1571
        # In2 -> n1572
        # In3 -> n1573
        # In4 -> n1574
        # In5 -> n1575
        # In6 -> n1576
        # In7 -> n1577
        # In8 -> n1578
        # In9 -> n1579
        # sudoku/Rows/row_7/diff36 -> n1580
        n1580 = self.context.mk_neq(n1578, n1579)
        self.nets['sudoku/Rows/row_7/diff36'] = n1580
        # sudoku/Rows/row_7/diff34 -> n1581
        n1581 = self.context.mk_neq(n1577, n1578)
        self.nets['sudoku/Rows/row_7/diff34'] = n1581
        # sudoku/Rows/row_7/diff35 -> n1582
        n1582 = self.context.mk_neq(n1577, n1579)
        self.nets['sudoku/Rows/row_7/diff35'] = n1582
        # sudoku/Rows/row_7/Logical Operator6 -> n1583
        n1583 = self.context.mk_and(n1581, n1582)
        self.nets['sudoku/Rows/row_7/Logical Operator6'] = n1583
        # sudoku/Rows/row_7/diff31 -> n1584
        n1584 = self.context.mk_neq(n1576, n1577)
        self.nets['sudoku/Rows/row_7/diff31'] = n1584
        # sudoku/Rows/row_7/diff32 -> n1585
        n1585 = self.context.mk_neq(n1576, n1578)
        self.nets['sudoku/Rows/row_7/diff32'] = n1585
        # sudoku/Rows/row_7/diff33 -> n1586
        n1586 = self.context.mk_neq(n1576, n1579)
        self.nets['sudoku/Rows/row_7/diff33'] = n1586
        # sudoku/Rows/row_7/Logical Operator5 -> n1587
        tn251 = self.context.mk_and(n1585, n1586)
        n1587 = self.context.mk_and(n1584, tn251)
        self.nets['sudoku/Rows/row_7/Logical Operator5'] = n1587
        # sudoku/Rows/row_7/diff27 -> n1588
        n1588 = self.context.mk_neq(n1575, n1576)
        self.nets['sudoku/Rows/row_7/diff27'] = n1588
        # sudoku/Rows/row_7/diff28 -> n1589
        n1589 = self.context.mk_neq(n1575, n1577)
        self.nets['sudoku/Rows/row_7/diff28'] = n1589
        # sudoku/Rows/row_7/diff29 -> n1590
        n1590 = self.context.mk_neq(n1575, n1578)
        self.nets['sudoku/Rows/row_7/diff29'] = n1590
        # sudoku/Rows/row_7/diff30 -> n1591
        n1591 = self.context.mk_neq(n1575, n1579)
        self.nets['sudoku/Rows/row_7/diff30'] = n1591
        # sudoku/Rows/row_7/Logical Operator4 -> n1592
        tn253 = self.context.mk_and(n1590, n1591)
        tn252 = self.context.mk_and(n1589, tn253)
        n1592 = self.context.mk_and(n1588, tn252)
        self.nets['sudoku/Rows/row_7/Logical Operator4'] = n1592
        # sudoku/Rows/row_7/diff22 -> n1593
        n1593 = self.context.mk_neq(n1574, n1575)
        self.nets['sudoku/Rows/row_7/diff22'] = n1593
        # sudoku/Rows/row_7/diff23 -> n1594
        n1594 = self.context.mk_neq(n1574, n1576)
        self.nets['sudoku/Rows/row_7/diff23'] = n1594
        # sudoku/Rows/row_7/diff24 -> n1595
        n1595 = self.context.mk_neq(n1574, n1577)
        self.nets['sudoku/Rows/row_7/diff24'] = n1595
        # sudoku/Rows/row_7/diff25 -> n1596
        n1596 = self.context.mk_neq(n1574, n1578)
        self.nets['sudoku/Rows/row_7/diff25'] = n1596
        # sudoku/Rows/row_7/diff26 -> n1597
        n1597 = self.context.mk_neq(n1574, n1579)
        self.nets['sudoku/Rows/row_7/diff26'] = n1597
        # sudoku/Rows/row_7/Logical Operator3 -> n1598
        tn256 = self.context.mk_and(n1596, n1597)
        tn255 = self.context.mk_and(n1595, tn256)
        tn254 = self.context.mk_and(n1594, tn255)
        n1598 = self.context.mk_and(n1593, tn254)
        self.nets['sudoku/Rows/row_7/Logical Operator3'] = n1598
        # sudoku/Rows/row_7/diff16 -> n1599
        n1599 = self.context.mk_neq(n1573, n1574)
        self.nets['sudoku/Rows/row_7/diff16'] = n1599
        # sudoku/Rows/row_7/diff17 -> n1600
        n1600 = self.context.mk_neq(n1573, n1575)
        self.nets['sudoku/Rows/row_7/diff17'] = n1600
        # sudoku/Rows/row_7/diff18 -> n1601
        n1601 = self.context.mk_neq(n1573, n1576)
        self.nets['sudoku/Rows/row_7/diff18'] = n1601
        # sudoku/Rows/row_7/diff19 -> n1602
        n1602 = self.context.mk_neq(n1573, n1577)
        self.nets['sudoku/Rows/row_7/diff19'] = n1602
        # sudoku/Rows/row_7/diff20 -> n1603
        n1603 = self.context.mk_neq(n1573, n1578)
        self.nets['sudoku/Rows/row_7/diff20'] = n1603
        # sudoku/Rows/row_7/diff21 -> n1604
        n1604 = self.context.mk_neq(n1573, n1579)
        self.nets['sudoku/Rows/row_7/diff21'] = n1604
        # sudoku/Rows/row_7/Logical Operator2 -> n1605
        tn260 = self.context.mk_and(n1603, n1604)
        tn259 = self.context.mk_and(n1602, tn260)
        tn258 = self.context.mk_and(n1601, tn259)
        tn257 = self.context.mk_and(n1600, tn258)
        n1605 = self.context.mk_and(n1599, tn257)
        self.nets['sudoku/Rows/row_7/Logical Operator2'] = n1605
        # sudoku/Rows/row_7/diff9 -> n1606
        n1606 = self.context.mk_neq(n1572, n1573)
        self.nets['sudoku/Rows/row_7/diff9'] = n1606
        # sudoku/Rows/row_7/diff10 -> n1607
        n1607 = self.context.mk_neq(n1572, n1574)
        self.nets['sudoku/Rows/row_7/diff10'] = n1607
        # sudoku/Rows/row_7/diff11 -> n1608
        n1608 = self.context.mk_neq(n1572, n1575)
        self.nets['sudoku/Rows/row_7/diff11'] = n1608
        # sudoku/Rows/row_7/diff12 -> n1609
        n1609 = self.context.mk_neq(n1572, n1576)
        self.nets['sudoku/Rows/row_7/diff12'] = n1609
        # sudoku/Rows/row_7/diff13 -> n1610
        n1610 = self.context.mk_neq(n1572, n1577)
        self.nets['sudoku/Rows/row_7/diff13'] = n1610
        # sudoku/Rows/row_7/diff14 -> n1611
        n1611 = self.context.mk_neq(n1572, n1578)
        self.nets['sudoku/Rows/row_7/diff14'] = n1611
        # sudoku/Rows/row_7/diff15 -> n1612
        n1612 = self.context.mk_neq(n1572, n1579)
        self.nets['sudoku/Rows/row_7/diff15'] = n1612
        # sudoku/Rows/row_7/Logical Operator1 -> n1613
        tn265 = self.context.mk_and(n1611, n1612)
        tn264 = self.context.mk_and(n1610, tn265)
        tn263 = self.context.mk_and(n1609, tn264)
        tn262 = self.context.mk_and(n1608, tn263)
        tn261 = self.context.mk_and(n1607, tn262)
        n1613 = self.context.mk_and(n1606, tn261)
        self.nets['sudoku/Rows/row_7/Logical Operator1'] = n1613
        # sudoku/Rows/row_7/diff1 -> n1614
        n1614 = self.context.mk_neq(n1571, n1572)
        self.nets['sudoku/Rows/row_7/diff1'] = n1614
        # sudoku/Rows/row_7/diff2 -> n1615
        n1615 = self.context.mk_neq(n1571, n1573)
        self.nets['sudoku/Rows/row_7/diff2'] = n1615
        # sudoku/Rows/row_7/diff3 -> n1616
        n1616 = self.context.mk_neq(n1571, n1574)
        self.nets['sudoku/Rows/row_7/diff3'] = n1616
        # sudoku/Rows/row_7/diff4 -> n1617
        n1617 = self.context.mk_neq(n1571, n1575)
        self.nets['sudoku/Rows/row_7/diff4'] = n1617
        # sudoku/Rows/row_7/diff5 -> n1618
        n1618 = self.context.mk_neq(n1571, n1576)
        self.nets['sudoku/Rows/row_7/diff5'] = n1618
        # sudoku/Rows/row_7/diff6 -> n1619
        n1619 = self.context.mk_neq(n1571, n1577)
        self.nets['sudoku/Rows/row_7/diff6'] = n1619
        # sudoku/Rows/row_7/diff7 -> n1620
        n1620 = self.context.mk_neq(n1571, n1578)
        self.nets['sudoku/Rows/row_7/diff7'] = n1620
        # sudoku/Rows/row_7/diff8 -> n1621
        n1621 = self.context.mk_neq(n1571, n1579)
        self.nets['sudoku/Rows/row_7/diff8'] = n1621
        # sudoku/Rows/row_7/Logical Operator -> n1622
        tn271 = self.context.mk_and(n1620, n1621)
        tn270 = self.context.mk_and(n1619, tn271)
        tn269 = self.context.mk_and(n1618, tn270)
        tn268 = self.context.mk_and(n1617, tn269)
        tn267 = self.context.mk_and(n1616, tn268)
        tn266 = self.context.mk_and(n1615, tn267)
        n1622 = self.context.mk_and(n1614, tn266)
        self.nets['sudoku/Rows/row_7/Logical Operator'] = n1622
        # sudoku/Rows/row_7/Logical Operator7 -> n1623
        tn277 = self.context.mk_and(n1613, n1622)
        tn276 = self.context.mk_and(n1605, tn277)
        tn275 = self.context.mk_and(n1598, tn276)
        tn274 = self.context.mk_and(n1592, tn275)
        tn273 = self.context.mk_and(n1587, tn274)
        tn272 = self.context.mk_and(n1583, tn273)
        n1623 = self.context.mk_and(n1580, tn272)
        self.nets['sudoku/Rows/row_7/Logical Operator7'] = n1623
        # n1623 -> Out1
        return n1623

    def row_8(self, n1625, n1626, n1627, n1628, n1629, n1630, n1631, n1632, n1633):
        # In1 -> n1625
        # In2 -> n1626
        # In3 -> n1627
        # In4 -> n1628
        # In5 -> n1629
        # In6 -> n1630
        # In7 -> n1631
        # In8 -> n1632
        # In9 -> n1633
        # sudoku/Rows/row_8/diff36 -> n1634
        n1634 = self.context.mk_neq(n1632, n1633)
        self.nets['sudoku/Rows/row_8/diff36'] = n1634
        # sudoku/Rows/row_8/diff34 -> n1635
        n1635 = self.context.mk_neq(n1631, n1632)
        self.nets['sudoku/Rows/row_8/diff34'] = n1635
        # sudoku/Rows/row_8/diff35 -> n1636
        n1636 = self.context.mk_neq(n1631, n1633)
        self.nets['sudoku/Rows/row_8/diff35'] = n1636
        # sudoku/Rows/row_8/Logical Operator6 -> n1637
        n1637 = self.context.mk_and(n1635, n1636)
        self.nets['sudoku/Rows/row_8/Logical Operator6'] = n1637
        # sudoku/Rows/row_8/diff31 -> n1638
        n1638 = self.context.mk_neq(n1630, n1631)
        self.nets['sudoku/Rows/row_8/diff31'] = n1638
        # sudoku/Rows/row_8/diff32 -> n1639
        n1639 = self.context.mk_neq(n1630, n1632)
        self.nets['sudoku/Rows/row_8/diff32'] = n1639
        # sudoku/Rows/row_8/diff33 -> n1640
        n1640 = self.context.mk_neq(n1630, n1633)
        self.nets['sudoku/Rows/row_8/diff33'] = n1640
        # sudoku/Rows/row_8/Logical Operator5 -> n1641
        tn278 = self.context.mk_and(n1639, n1640)
        n1641 = self.context.mk_and(n1638, tn278)
        self.nets['sudoku/Rows/row_8/Logical Operator5'] = n1641
        # sudoku/Rows/row_8/diff27 -> n1642
        n1642 = self.context.mk_neq(n1629, n1630)
        self.nets['sudoku/Rows/row_8/diff27'] = n1642
        # sudoku/Rows/row_8/diff28 -> n1643
        n1643 = self.context.mk_neq(n1629, n1631)
        self.nets['sudoku/Rows/row_8/diff28'] = n1643
        # sudoku/Rows/row_8/diff29 -> n1644
        n1644 = self.context.mk_neq(n1629, n1632)
        self.nets['sudoku/Rows/row_8/diff29'] = n1644
        # sudoku/Rows/row_8/diff30 -> n1645
        n1645 = self.context.mk_neq(n1629, n1633)
        self.nets['sudoku/Rows/row_8/diff30'] = n1645
        # sudoku/Rows/row_8/Logical Operator4 -> n1646
        tn280 = self.context.mk_and(n1644, n1645)
        tn279 = self.context.mk_and(n1643, tn280)
        n1646 = self.context.mk_and(n1642, tn279)
        self.nets['sudoku/Rows/row_8/Logical Operator4'] = n1646
        # sudoku/Rows/row_8/diff22 -> n1647
        n1647 = self.context.mk_neq(n1628, n1629)
        self.nets['sudoku/Rows/row_8/diff22'] = n1647
        # sudoku/Rows/row_8/diff23 -> n1648
        n1648 = self.context.mk_neq(n1628, n1630)
        self.nets['sudoku/Rows/row_8/diff23'] = n1648
        # sudoku/Rows/row_8/diff24 -> n1649
        n1649 = self.context.mk_neq(n1628, n1631)
        self.nets['sudoku/Rows/row_8/diff24'] = n1649
        # sudoku/Rows/row_8/diff25 -> n1650
        n1650 = self.context.mk_neq(n1628, n1632)
        self.nets['sudoku/Rows/row_8/diff25'] = n1650
        # sudoku/Rows/row_8/diff26 -> n1651
        n1651 = self.context.mk_neq(n1628, n1633)
        self.nets['sudoku/Rows/row_8/diff26'] = n1651
        # sudoku/Rows/row_8/Logical Operator3 -> n1652
        tn283 = self.context.mk_and(n1650, n1651)
        tn282 = self.context.mk_and(n1649, tn283)
        tn281 = self.context.mk_and(n1648, tn282)
        n1652 = self.context.mk_and(n1647, tn281)
        self.nets['sudoku/Rows/row_8/Logical Operator3'] = n1652
        # sudoku/Rows/row_8/diff16 -> n1653
        n1653 = self.context.mk_neq(n1627, n1628)
        self.nets['sudoku/Rows/row_8/diff16'] = n1653
        # sudoku/Rows/row_8/diff17 -> n1654
        n1654 = self.context.mk_neq(n1627, n1629)
        self.nets['sudoku/Rows/row_8/diff17'] = n1654
        # sudoku/Rows/row_8/diff18 -> n1655
        n1655 = self.context.mk_neq(n1627, n1630)
        self.nets['sudoku/Rows/row_8/diff18'] = n1655
        # sudoku/Rows/row_8/diff19 -> n1656
        n1656 = self.context.mk_neq(n1627, n1631)
        self.nets['sudoku/Rows/row_8/diff19'] = n1656
        # sudoku/Rows/row_8/diff20 -> n1657
        n1657 = self.context.mk_neq(n1627, n1632)
        self.nets['sudoku/Rows/row_8/diff20'] = n1657
        # sudoku/Rows/row_8/diff21 -> n1658
        n1658 = self.context.mk_neq(n1627, n1633)
        self.nets['sudoku/Rows/row_8/diff21'] = n1658
        # sudoku/Rows/row_8/Logical Operator2 -> n1659
        tn287 = self.context.mk_and(n1657, n1658)
        tn286 = self.context.mk_and(n1656, tn287)
        tn285 = self.context.mk_and(n1655, tn286)
        tn284 = self.context.mk_and(n1654, tn285)
        n1659 = self.context.mk_and(n1653, tn284)
        self.nets['sudoku/Rows/row_8/Logical Operator2'] = n1659
        # sudoku/Rows/row_8/diff9 -> n1660
        n1660 = self.context.mk_neq(n1626, n1627)
        self.nets['sudoku/Rows/row_8/diff9'] = n1660
        # sudoku/Rows/row_8/diff10 -> n1661
        n1661 = self.context.mk_neq(n1626, n1628)
        self.nets['sudoku/Rows/row_8/diff10'] = n1661
        # sudoku/Rows/row_8/diff11 -> n1662
        n1662 = self.context.mk_neq(n1626, n1629)
        self.nets['sudoku/Rows/row_8/diff11'] = n1662
        # sudoku/Rows/row_8/diff12 -> n1663
        n1663 = self.context.mk_neq(n1626, n1630)
        self.nets['sudoku/Rows/row_8/diff12'] = n1663
        # sudoku/Rows/row_8/diff13 -> n1664
        n1664 = self.context.mk_neq(n1626, n1631)
        self.nets['sudoku/Rows/row_8/diff13'] = n1664
        # sudoku/Rows/row_8/diff14 -> n1665
        n1665 = self.context.mk_neq(n1626, n1632)
        self.nets['sudoku/Rows/row_8/diff14'] = n1665
        # sudoku/Rows/row_8/diff15 -> n1666
        n1666 = self.context.mk_neq(n1626, n1633)
        self.nets['sudoku/Rows/row_8/diff15'] = n1666
        # sudoku/Rows/row_8/Logical Operator1 -> n1667
        tn292 = self.context.mk_and(n1665, n1666)
        tn291 = self.context.mk_and(n1664, tn292)
        tn290 = self.context.mk_and(n1663, tn291)
        tn289 = self.context.mk_and(n1662, tn290)
        tn288 = self.context.mk_and(n1661, tn289)
        n1667 = self.context.mk_and(n1660, tn288)
        self.nets['sudoku/Rows/row_8/Logical Operator1'] = n1667
        # sudoku/Rows/row_8/diff1 -> n1668
        n1668 = self.context.mk_neq(n1625, n1626)
        self.nets['sudoku/Rows/row_8/diff1'] = n1668
        # sudoku/Rows/row_8/diff2 -> n1669
        n1669 = self.context.mk_neq(n1625, n1627)
        self.nets['sudoku/Rows/row_8/diff2'] = n1669
        # sudoku/Rows/row_8/diff3 -> n1670
        n1670 = self.context.mk_neq(n1625, n1628)
        self.nets['sudoku/Rows/row_8/diff3'] = n1670
        # sudoku/Rows/row_8/diff4 -> n1671
        n1671 = self.context.mk_neq(n1625, n1629)
        self.nets['sudoku/Rows/row_8/diff4'] = n1671
        # sudoku/Rows/row_8/diff5 -> n1672
        n1672 = self.context.mk_neq(n1625, n1630)
        self.nets['sudoku/Rows/row_8/diff5'] = n1672
        # sudoku/Rows/row_8/diff6 -> n1673
        n1673 = self.context.mk_neq(n1625, n1631)
        self.nets['sudoku/Rows/row_8/diff6'] = n1673
        # sudoku/Rows/row_8/diff7 -> n1674
        n1674 = self.context.mk_neq(n1625, n1632)
        self.nets['sudoku/Rows/row_8/diff7'] = n1674
        # sudoku/Rows/row_8/diff8 -> n1675
        n1675 = self.context.mk_neq(n1625, n1633)
        self.nets['sudoku/Rows/row_8/diff8'] = n1675
        # sudoku/Rows/row_8/Logical Operator -> n1676
        tn298 = self.context.mk_and(n1674, n1675)
        tn297 = self.context.mk_and(n1673, tn298)
        tn296 = self.context.mk_and(n1672, tn297)
        tn295 = self.context.mk_and(n1671, tn296)
        tn294 = self.context.mk_and(n1670, tn295)
        tn293 = self.context.mk_and(n1669, tn294)
        n1676 = self.context.mk_and(n1668, tn293)
        self.nets['sudoku/Rows/row_8/Logical Operator'] = n1676
        # sudoku/Rows/row_8/Logical Operator7 -> n1677
        tn304 = self.context.mk_and(n1667, n1676)
        tn303 = self.context.mk_and(n1659, tn304)
        tn302 = self.context.mk_and(n1652, tn303)
        tn301 = self.context.mk_and(n1646, tn302)
        tn300 = self.context.mk_and(n1641, tn301)
        tn299 = self.context.mk_and(n1637, tn300)
        n1677 = self.context.mk_and(n1634, tn299)
        self.nets['sudoku/Rows/row_8/Logical Operator7'] = n1677
        # n1677 -> Out1
        return n1677

    def row_5(self, n1679, n1680, n1681, n1682, n1683, n1684, n1685, n1686, n1687):
        # In1 -> n1679
        # In2 -> n1680
        # In3 -> n1681
        # In4 -> n1682
        # In5 -> n1683
        # In6 -> n1684
        # In7 -> n1685
        # In8 -> n1686
        # In9 -> n1687
        # sudoku/Rows/row_5/diff36 -> n1688
        n1688 = self.context.mk_neq(n1686, n1687)
        self.nets['sudoku/Rows/row_5/diff36'] = n1688
        # sudoku/Rows/row_5/diff34 -> n1689
        n1689 = self.context.mk_neq(n1685, n1686)
        self.nets['sudoku/Rows/row_5/diff34'] = n1689
        # sudoku/Rows/row_5/diff35 -> n1690
        n1690 = self.context.mk_neq(n1685, n1687)
        self.nets['sudoku/Rows/row_5/diff35'] = n1690
        # sudoku/Rows/row_5/Logical Operator6 -> n1691
        n1691 = self.context.mk_and(n1689, n1690)
        self.nets['sudoku/Rows/row_5/Logical Operator6'] = n1691
        # sudoku/Rows/row_5/diff31 -> n1692
        n1692 = self.context.mk_neq(n1684, n1685)
        self.nets['sudoku/Rows/row_5/diff31'] = n1692
        # sudoku/Rows/row_5/diff32 -> n1693
        n1693 = self.context.mk_neq(n1684, n1686)
        self.nets['sudoku/Rows/row_5/diff32'] = n1693
        # sudoku/Rows/row_5/diff33 -> n1694
        n1694 = self.context.mk_neq(n1684, n1687)
        self.nets['sudoku/Rows/row_5/diff33'] = n1694
        # sudoku/Rows/row_5/Logical Operator5 -> n1695
        tn305 = self.context.mk_and(n1693, n1694)
        n1695 = self.context.mk_and(n1692, tn305)
        self.nets['sudoku/Rows/row_5/Logical Operator5'] = n1695
        # sudoku/Rows/row_5/diff27 -> n1696
        n1696 = self.context.mk_neq(n1683, n1684)
        self.nets['sudoku/Rows/row_5/diff27'] = n1696
        # sudoku/Rows/row_5/diff28 -> n1697
        n1697 = self.context.mk_neq(n1683, n1685)
        self.nets['sudoku/Rows/row_5/diff28'] = n1697
        # sudoku/Rows/row_5/diff29 -> n1698
        n1698 = self.context.mk_neq(n1683, n1686)
        self.nets['sudoku/Rows/row_5/diff29'] = n1698
        # sudoku/Rows/row_5/diff30 -> n1699
        n1699 = self.context.mk_neq(n1683, n1687)
        self.nets['sudoku/Rows/row_5/diff30'] = n1699
        # sudoku/Rows/row_5/Logical Operator4 -> n1700
        tn307 = self.context.mk_and(n1698, n1699)
        tn306 = self.context.mk_and(n1697, tn307)
        n1700 = self.context.mk_and(n1696, tn306)
        self.nets['sudoku/Rows/row_5/Logical Operator4'] = n1700
        # sudoku/Rows/row_5/diff22 -> n1701
        n1701 = self.context.mk_neq(n1682, n1683)
        self.nets['sudoku/Rows/row_5/diff22'] = n1701
        # sudoku/Rows/row_5/diff23 -> n1702
        n1702 = self.context.mk_neq(n1682, n1684)
        self.nets['sudoku/Rows/row_5/diff23'] = n1702
        # sudoku/Rows/row_5/diff24 -> n1703
        n1703 = self.context.mk_neq(n1682, n1685)
        self.nets['sudoku/Rows/row_5/diff24'] = n1703
        # sudoku/Rows/row_5/diff25 -> n1704
        n1704 = self.context.mk_neq(n1682, n1686)
        self.nets['sudoku/Rows/row_5/diff25'] = n1704
        # sudoku/Rows/row_5/diff26 -> n1705
        n1705 = self.context.mk_neq(n1682, n1687)
        self.nets['sudoku/Rows/row_5/diff26'] = n1705
        # sudoku/Rows/row_5/Logical Operator3 -> n1706
        tn310 = self.context.mk_and(n1704, n1705)
        tn309 = self.context.mk_and(n1703, tn310)
        tn308 = self.context.mk_and(n1702, tn309)
        n1706 = self.context.mk_and(n1701, tn308)
        self.nets['sudoku/Rows/row_5/Logical Operator3'] = n1706
        # sudoku/Rows/row_5/diff16 -> n1707
        n1707 = self.context.mk_neq(n1681, n1682)
        self.nets['sudoku/Rows/row_5/diff16'] = n1707
        # sudoku/Rows/row_5/diff17 -> n1708
        n1708 = self.context.mk_neq(n1681, n1683)
        self.nets['sudoku/Rows/row_5/diff17'] = n1708
        # sudoku/Rows/row_5/diff18 -> n1709
        n1709 = self.context.mk_neq(n1681, n1684)
        self.nets['sudoku/Rows/row_5/diff18'] = n1709
        # sudoku/Rows/row_5/diff19 -> n1710
        n1710 = self.context.mk_neq(n1681, n1685)
        self.nets['sudoku/Rows/row_5/diff19'] = n1710
        # sudoku/Rows/row_5/diff20 -> n1711
        n1711 = self.context.mk_neq(n1681, n1686)
        self.nets['sudoku/Rows/row_5/diff20'] = n1711
        # sudoku/Rows/row_5/diff21 -> n1712
        n1712 = self.context.mk_neq(n1681, n1687)
        self.nets['sudoku/Rows/row_5/diff21'] = n1712
        # sudoku/Rows/row_5/Logical Operator2 -> n1713
        tn314 = self.context.mk_and(n1711, n1712)
        tn313 = self.context.mk_and(n1710, tn314)
        tn312 = self.context.mk_and(n1709, tn313)
        tn311 = self.context.mk_and(n1708, tn312)
        n1713 = self.context.mk_and(n1707, tn311)
        self.nets['sudoku/Rows/row_5/Logical Operator2'] = n1713
        # sudoku/Rows/row_5/diff9 -> n1714
        n1714 = self.context.mk_neq(n1680, n1681)
        self.nets['sudoku/Rows/row_5/diff9'] = n1714
        # sudoku/Rows/row_5/diff10 -> n1715
        n1715 = self.context.mk_neq(n1680, n1682)
        self.nets['sudoku/Rows/row_5/diff10'] = n1715
        # sudoku/Rows/row_5/diff11 -> n1716
        n1716 = self.context.mk_neq(n1680, n1683)
        self.nets['sudoku/Rows/row_5/diff11'] = n1716
        # sudoku/Rows/row_5/diff12 -> n1717
        n1717 = self.context.mk_neq(n1680, n1684)
        self.nets['sudoku/Rows/row_5/diff12'] = n1717
        # sudoku/Rows/row_5/diff13 -> n1718
        n1718 = self.context.mk_neq(n1680, n1685)
        self.nets['sudoku/Rows/row_5/diff13'] = n1718
        # sudoku/Rows/row_5/diff14 -> n1719
        n1719 = self.context.mk_neq(n1680, n1686)
        self.nets['sudoku/Rows/row_5/diff14'] = n1719
        # sudoku/Rows/row_5/diff15 -> n1720
        n1720 = self.context.mk_neq(n1680, n1687)
        self.nets['sudoku/Rows/row_5/diff15'] = n1720
        # sudoku/Rows/row_5/Logical Operator1 -> n1721
        tn319 = self.context.mk_and(n1719, n1720)
        tn318 = self.context.mk_and(n1718, tn319)
        tn317 = self.context.mk_and(n1717, tn318)
        tn316 = self.context.mk_and(n1716, tn317)
        tn315 = self.context.mk_and(n1715, tn316)
        n1721 = self.context.mk_and(n1714, tn315)
        self.nets['sudoku/Rows/row_5/Logical Operator1'] = n1721
        # sudoku/Rows/row_5/diff1 -> n1722
        n1722 = self.context.mk_neq(n1679, n1680)
        self.nets['sudoku/Rows/row_5/diff1'] = n1722
        # sudoku/Rows/row_5/diff2 -> n1723
        n1723 = self.context.mk_neq(n1679, n1681)
        self.nets['sudoku/Rows/row_5/diff2'] = n1723
        # sudoku/Rows/row_5/diff3 -> n1724
        n1724 = self.context.mk_neq(n1679, n1682)
        self.nets['sudoku/Rows/row_5/diff3'] = n1724
        # sudoku/Rows/row_5/diff4 -> n1725
        n1725 = self.context.mk_neq(n1679, n1683)
        self.nets['sudoku/Rows/row_5/diff4'] = n1725
        # sudoku/Rows/row_5/diff5 -> n1726
        n1726 = self.context.mk_neq(n1679, n1684)
        self.nets['sudoku/Rows/row_5/diff5'] = n1726
        # sudoku/Rows/row_5/diff6 -> n1727
        n1727 = self.context.mk_neq(n1679, n1685)
        self.nets['sudoku/Rows/row_5/diff6'] = n1727
        # sudoku/Rows/row_5/diff7 -> n1728
        n1728 = self.context.mk_neq(n1679, n1686)
        self.nets['sudoku/Rows/row_5/diff7'] = n1728
        # sudoku/Rows/row_5/diff8 -> n1729
        n1729 = self.context.mk_neq(n1679, n1687)
        self.nets['sudoku/Rows/row_5/diff8'] = n1729
        # sudoku/Rows/row_5/Logical Operator -> n1730
        tn325 = self.context.mk_and(n1728, n1729)
        tn324 = self.context.mk_and(n1727, tn325)
        tn323 = self.context.mk_and(n1726, tn324)
        tn322 = self.context.mk_and(n1725, tn323)
        tn321 = self.context.mk_and(n1724, tn322)
        tn320 = self.context.mk_and(n1723, tn321)
        n1730 = self.context.mk_and(n1722, tn320)
        self.nets['sudoku/Rows/row_5/Logical Operator'] = n1730
        # sudoku/Rows/row_5/Logical Operator7 -> n1731
        tn331 = self.context.mk_and(n1721, n1730)
        tn330 = self.context.mk_and(n1713, tn331)
        tn329 = self.context.mk_and(n1706, tn330)
        tn328 = self.context.mk_and(n1700, tn329)
        tn327 = self.context.mk_and(n1695, tn328)
        tn326 = self.context.mk_and(n1691, tn327)
        n1731 = self.context.mk_and(n1688, tn326)
        self.nets['sudoku/Rows/row_5/Logical Operator7'] = n1731
        # n1731 -> Out1
        return n1731

    def row_6(self, n1733, n1734, n1735, n1736, n1737, n1738, n1739, n1740, n1741):
        # In1 -> n1733
        # In2 -> n1734
        # In3 -> n1735
        # In4 -> n1736
        # In5 -> n1737
        # In6 -> n1738
        # In7 -> n1739
        # In8 -> n1740
        # In9 -> n1741
        # sudoku/Rows/row_6/diff36 -> n1742
        n1742 = self.context.mk_neq(n1740, n1741)
        self.nets['sudoku/Rows/row_6/diff36'] = n1742
        # sudoku/Rows/row_6/diff34 -> n1743
        n1743 = self.context.mk_neq(n1739, n1740)
        self.nets['sudoku/Rows/row_6/diff34'] = n1743
        # sudoku/Rows/row_6/diff35 -> n1744
        n1744 = self.context.mk_neq(n1739, n1741)
        self.nets['sudoku/Rows/row_6/diff35'] = n1744
        # sudoku/Rows/row_6/Logical Operator6 -> n1745
        n1745 = self.context.mk_and(n1743, n1744)
        self.nets['sudoku/Rows/row_6/Logical Operator6'] = n1745
        # sudoku/Rows/row_6/diff31 -> n1746
        n1746 = self.context.mk_neq(n1738, n1739)
        self.nets['sudoku/Rows/row_6/diff31'] = n1746
        # sudoku/Rows/row_6/diff32 -> n1747
        n1747 = self.context.mk_neq(n1738, n1740)
        self.nets['sudoku/Rows/row_6/diff32'] = n1747
        # sudoku/Rows/row_6/diff33 -> n1748
        n1748 = self.context.mk_neq(n1738, n1741)
        self.nets['sudoku/Rows/row_6/diff33'] = n1748
        # sudoku/Rows/row_6/Logical Operator5 -> n1749
        tn332 = self.context.mk_and(n1747, n1748)
        n1749 = self.context.mk_and(n1746, tn332)
        self.nets['sudoku/Rows/row_6/Logical Operator5'] = n1749
        # sudoku/Rows/row_6/diff27 -> n1750
        n1750 = self.context.mk_neq(n1737, n1738)
        self.nets['sudoku/Rows/row_6/diff27'] = n1750
        # sudoku/Rows/row_6/diff28 -> n1751
        n1751 = self.context.mk_neq(n1737, n1739)
        self.nets['sudoku/Rows/row_6/diff28'] = n1751
        # sudoku/Rows/row_6/diff29 -> n1752
        n1752 = self.context.mk_neq(n1737, n1740)
        self.nets['sudoku/Rows/row_6/diff29'] = n1752
        # sudoku/Rows/row_6/diff30 -> n1753
        n1753 = self.context.mk_neq(n1737, n1741)
        self.nets['sudoku/Rows/row_6/diff30'] = n1753
        # sudoku/Rows/row_6/Logical Operator4 -> n1754
        tn334 = self.context.mk_and(n1752, n1753)
        tn333 = self.context.mk_and(n1751, tn334)
        n1754 = self.context.mk_and(n1750, tn333)
        self.nets['sudoku/Rows/row_6/Logical Operator4'] = n1754
        # sudoku/Rows/row_6/diff22 -> n1755
        n1755 = self.context.mk_neq(n1736, n1737)
        self.nets['sudoku/Rows/row_6/diff22'] = n1755
        # sudoku/Rows/row_6/diff23 -> n1756
        n1756 = self.context.mk_neq(n1736, n1738)
        self.nets['sudoku/Rows/row_6/diff23'] = n1756
        # sudoku/Rows/row_6/diff24 -> n1757
        n1757 = self.context.mk_neq(n1736, n1739)
        self.nets['sudoku/Rows/row_6/diff24'] = n1757
        # sudoku/Rows/row_6/diff25 -> n1758
        n1758 = self.context.mk_neq(n1736, n1740)
        self.nets['sudoku/Rows/row_6/diff25'] = n1758
        # sudoku/Rows/row_6/diff26 -> n1759
        n1759 = self.context.mk_neq(n1736, n1741)
        self.nets['sudoku/Rows/row_6/diff26'] = n1759
        # sudoku/Rows/row_6/Logical Operator3 -> n1760
        tn337 = self.context.mk_and(n1758, n1759)
        tn336 = self.context.mk_and(n1757, tn337)
        tn335 = self.context.mk_and(n1756, tn336)
        n1760 = self.context.mk_and(n1755, tn335)
        self.nets['sudoku/Rows/row_6/Logical Operator3'] = n1760
        # sudoku/Rows/row_6/diff16 -> n1761
        n1761 = self.context.mk_neq(n1735, n1736)
        self.nets['sudoku/Rows/row_6/diff16'] = n1761
        # sudoku/Rows/row_6/diff17 -> n1762
        n1762 = self.context.mk_neq(n1735, n1737)
        self.nets['sudoku/Rows/row_6/diff17'] = n1762
        # sudoku/Rows/row_6/diff18 -> n1763
        n1763 = self.context.mk_neq(n1735, n1738)
        self.nets['sudoku/Rows/row_6/diff18'] = n1763
        # sudoku/Rows/row_6/diff19 -> n1764
        n1764 = self.context.mk_neq(n1735, n1739)
        self.nets['sudoku/Rows/row_6/diff19'] = n1764
        # sudoku/Rows/row_6/diff20 -> n1765
        n1765 = self.context.mk_neq(n1735, n1740)
        self.nets['sudoku/Rows/row_6/diff20'] = n1765
        # sudoku/Rows/row_6/diff21 -> n1766
        n1766 = self.context.mk_neq(n1735, n1741)
        self.nets['sudoku/Rows/row_6/diff21'] = n1766
        # sudoku/Rows/row_6/Logical Operator2 -> n1767
        tn341 = self.context.mk_and(n1765, n1766)
        tn340 = self.context.mk_and(n1764, tn341)
        tn339 = self.context.mk_and(n1763, tn340)
        tn338 = self.context.mk_and(n1762, tn339)
        n1767 = self.context.mk_and(n1761, tn338)
        self.nets['sudoku/Rows/row_6/Logical Operator2'] = n1767
        # sudoku/Rows/row_6/diff9 -> n1768
        n1768 = self.context.mk_neq(n1734, n1735)
        self.nets['sudoku/Rows/row_6/diff9'] = n1768
        # sudoku/Rows/row_6/diff10 -> n1769
        n1769 = self.context.mk_neq(n1734, n1736)
        self.nets['sudoku/Rows/row_6/diff10'] = n1769
        # sudoku/Rows/row_6/diff11 -> n1770
        n1770 = self.context.mk_neq(n1734, n1737)
        self.nets['sudoku/Rows/row_6/diff11'] = n1770
        # sudoku/Rows/row_6/diff12 -> n1771
        n1771 = self.context.mk_neq(n1734, n1738)
        self.nets['sudoku/Rows/row_6/diff12'] = n1771
        # sudoku/Rows/row_6/diff13 -> n1772
        n1772 = self.context.mk_neq(n1734, n1739)
        self.nets['sudoku/Rows/row_6/diff13'] = n1772
        # sudoku/Rows/row_6/diff14 -> n1773
        n1773 = self.context.mk_neq(n1734, n1740)
        self.nets['sudoku/Rows/row_6/diff14'] = n1773
        # sudoku/Rows/row_6/diff15 -> n1774
        n1774 = self.context.mk_neq(n1734, n1741)
        self.nets['sudoku/Rows/row_6/diff15'] = n1774
        # sudoku/Rows/row_6/Logical Operator1 -> n1775
        tn346 = self.context.mk_and(n1773, n1774)
        tn345 = self.context.mk_and(n1772, tn346)
        tn344 = self.context.mk_and(n1771, tn345)
        tn343 = self.context.mk_and(n1770, tn344)
        tn342 = self.context.mk_and(n1769, tn343)
        n1775 = self.context.mk_and(n1768, tn342)
        self.nets['sudoku/Rows/row_6/Logical Operator1'] = n1775
        # sudoku/Rows/row_6/diff1 -> n1776
        n1776 = self.context.mk_neq(n1733, n1734)
        self.nets['sudoku/Rows/row_6/diff1'] = n1776
        # sudoku/Rows/row_6/diff2 -> n1777
        n1777 = self.context.mk_neq(n1733, n1735)
        self.nets['sudoku/Rows/row_6/diff2'] = n1777
        # sudoku/Rows/row_6/diff3 -> n1778
        n1778 = self.context.mk_neq(n1733, n1736)
        self.nets['sudoku/Rows/row_6/diff3'] = n1778
        # sudoku/Rows/row_6/diff4 -> n1779
        n1779 = self.context.mk_neq(n1733, n1737)
        self.nets['sudoku/Rows/row_6/diff4'] = n1779
        # sudoku/Rows/row_6/diff5 -> n1780
        n1780 = self.context.mk_neq(n1733, n1738)
        self.nets['sudoku/Rows/row_6/diff5'] = n1780
        # sudoku/Rows/row_6/diff6 -> n1781
        n1781 = self.context.mk_neq(n1733, n1739)
        self.nets['sudoku/Rows/row_6/diff6'] = n1781
        # sudoku/Rows/row_6/diff7 -> n1782
        n1782 = self.context.mk_neq(n1733, n1740)
        self.nets['sudoku/Rows/row_6/diff7'] = n1782
        # sudoku/Rows/row_6/diff8 -> n1783
        n1783 = self.context.mk_neq(n1733, n1741)
        self.nets['sudoku/Rows/row_6/diff8'] = n1783
        # sudoku/Rows/row_6/Logical Operator -> n1784
        tn352 = self.context.mk_and(n1782, n1783)
        tn351 = self.context.mk_and(n1781, tn352)
        tn350 = self.context.mk_and(n1780, tn351)
        tn349 = self.context.mk_and(n1779, tn350)
        tn348 = self.context.mk_and(n1778, tn349)
        tn347 = self.context.mk_and(n1777, tn348)
        n1784 = self.context.mk_and(n1776, tn347)
        self.nets['sudoku/Rows/row_6/Logical Operator'] = n1784
        # sudoku/Rows/row_6/Logical Operator7 -> n1785
        tn358 = self.context.mk_and(n1775, n1784)
        tn357 = self.context.mk_and(n1767, tn358)
        tn356 = self.context.mk_and(n1760, tn357)
        tn355 = self.context.mk_and(n1754, tn356)
        tn354 = self.context.mk_and(n1749, tn355)
        tn353 = self.context.mk_and(n1745, tn354)
        n1785 = self.context.mk_and(n1742, tn353)
        self.nets['sudoku/Rows/row_6/Logical Operator7'] = n1785
        # n1785 -> Out1
        return n1785

    def row_9(self, n1787, n1788, n1789, n1790, n1791, n1792, n1793, n1794, n1795):
        # In1 -> n1787
        # In2 -> n1788
        # In3 -> n1789
        # In4 -> n1790
        # In5 -> n1791
        # In6 -> n1792
        # In7 -> n1793
        # In8 -> n1794
        # In9 -> n1795
        # sudoku/Rows/row_9/diff36 -> n1796
        n1796 = self.context.mk_neq(n1794, n1795)
        self.nets['sudoku/Rows/row_9/diff36'] = n1796
        # sudoku/Rows/row_9/diff34 -> n1797
        n1797 = self.context.mk_neq(n1793, n1794)
        self.nets['sudoku/Rows/row_9/diff34'] = n1797
        # sudoku/Rows/row_9/diff35 -> n1798
        n1798 = self.context.mk_neq(n1793, n1795)
        self.nets['sudoku/Rows/row_9/diff35'] = n1798
        # sudoku/Rows/row_9/Logical Operator6 -> n1799
        n1799 = self.context.mk_and(n1797, n1798)
        self.nets['sudoku/Rows/row_9/Logical Operator6'] = n1799
        # sudoku/Rows/row_9/diff31 -> n1800
        n1800 = self.context.mk_neq(n1792, n1793)
        self.nets['sudoku/Rows/row_9/diff31'] = n1800
        # sudoku/Rows/row_9/diff32 -> n1801
        n1801 = self.context.mk_neq(n1792, n1794)
        self.nets['sudoku/Rows/row_9/diff32'] = n1801
        # sudoku/Rows/row_9/diff33 -> n1802
        n1802 = self.context.mk_neq(n1792, n1795)
        self.nets['sudoku/Rows/row_9/diff33'] = n1802
        # sudoku/Rows/row_9/Logical Operator5 -> n1803
        tn359 = self.context.mk_and(n1801, n1802)
        n1803 = self.context.mk_and(n1800, tn359)
        self.nets['sudoku/Rows/row_9/Logical Operator5'] = n1803
        # sudoku/Rows/row_9/diff27 -> n1804
        n1804 = self.context.mk_neq(n1791, n1792)
        self.nets['sudoku/Rows/row_9/diff27'] = n1804
        # sudoku/Rows/row_9/diff28 -> n1805
        n1805 = self.context.mk_neq(n1791, n1793)
        self.nets['sudoku/Rows/row_9/diff28'] = n1805
        # sudoku/Rows/row_9/diff29 -> n1806
        n1806 = self.context.mk_neq(n1791, n1794)
        self.nets['sudoku/Rows/row_9/diff29'] = n1806
        # sudoku/Rows/row_9/diff30 -> n1807
        n1807 = self.context.mk_neq(n1791, n1795)
        self.nets['sudoku/Rows/row_9/diff30'] = n1807
        # sudoku/Rows/row_9/Logical Operator4 -> n1808
        tn361 = self.context.mk_and(n1806, n1807)
        tn360 = self.context.mk_and(n1805, tn361)
        n1808 = self.context.mk_and(n1804, tn360)
        self.nets['sudoku/Rows/row_9/Logical Operator4'] = n1808
        # sudoku/Rows/row_9/diff22 -> n1809
        n1809 = self.context.mk_neq(n1790, n1791)
        self.nets['sudoku/Rows/row_9/diff22'] = n1809
        # sudoku/Rows/row_9/diff23 -> n1810
        n1810 = self.context.mk_neq(n1790, n1792)
        self.nets['sudoku/Rows/row_9/diff23'] = n1810
        # sudoku/Rows/row_9/diff24 -> n1811
        n1811 = self.context.mk_neq(n1790, n1793)
        self.nets['sudoku/Rows/row_9/diff24'] = n1811
        # sudoku/Rows/row_9/diff25 -> n1812
        n1812 = self.context.mk_neq(n1790, n1794)
        self.nets['sudoku/Rows/row_9/diff25'] = n1812
        # sudoku/Rows/row_9/diff26 -> n1813
        n1813 = self.context.mk_neq(n1790, n1795)
        self.nets['sudoku/Rows/row_9/diff26'] = n1813
        # sudoku/Rows/row_9/Logical Operator3 -> n1814
        tn364 = self.context.mk_and(n1812, n1813)
        tn363 = self.context.mk_and(n1811, tn364)
        tn362 = self.context.mk_and(n1810, tn363)
        n1814 = self.context.mk_and(n1809, tn362)
        self.nets['sudoku/Rows/row_9/Logical Operator3'] = n1814
        # sudoku/Rows/row_9/diff16 -> n1815
        n1815 = self.context.mk_neq(n1789, n1790)
        self.nets['sudoku/Rows/row_9/diff16'] = n1815
        # sudoku/Rows/row_9/diff17 -> n1816
        n1816 = self.context.mk_neq(n1789, n1791)
        self.nets['sudoku/Rows/row_9/diff17'] = n1816
        # sudoku/Rows/row_9/diff18 -> n1817
        n1817 = self.context.mk_neq(n1789, n1792)
        self.nets['sudoku/Rows/row_9/diff18'] = n1817
        # sudoku/Rows/row_9/diff19 -> n1818
        n1818 = self.context.mk_neq(n1789, n1793)
        self.nets['sudoku/Rows/row_9/diff19'] = n1818
        # sudoku/Rows/row_9/diff20 -> n1819
        n1819 = self.context.mk_neq(n1789, n1794)
        self.nets['sudoku/Rows/row_9/diff20'] = n1819
        # sudoku/Rows/row_9/diff21 -> n1820
        n1820 = self.context.mk_neq(n1789, n1795)
        self.nets['sudoku/Rows/row_9/diff21'] = n1820
        # sudoku/Rows/row_9/Logical Operator2 -> n1821
        tn368 = self.context.mk_and(n1819, n1820)
        tn367 = self.context.mk_and(n1818, tn368)
        tn366 = self.context.mk_and(n1817, tn367)
        tn365 = self.context.mk_and(n1816, tn366)
        n1821 = self.context.mk_and(n1815, tn365)
        self.nets['sudoku/Rows/row_9/Logical Operator2'] = n1821
        # sudoku/Rows/row_9/diff9 -> n1822
        n1822 = self.context.mk_neq(n1788, n1789)
        self.nets['sudoku/Rows/row_9/diff9'] = n1822
        # sudoku/Rows/row_9/diff10 -> n1823
        n1823 = self.context.mk_neq(n1788, n1790)
        self.nets['sudoku/Rows/row_9/diff10'] = n1823
        # sudoku/Rows/row_9/diff11 -> n1824
        n1824 = self.context.mk_neq(n1788, n1791)
        self.nets['sudoku/Rows/row_9/diff11'] = n1824
        # sudoku/Rows/row_9/diff12 -> n1825
        n1825 = self.context.mk_neq(n1788, n1792)
        self.nets['sudoku/Rows/row_9/diff12'] = n1825
        # sudoku/Rows/row_9/diff13 -> n1826
        n1826 = self.context.mk_neq(n1788, n1793)
        self.nets['sudoku/Rows/row_9/diff13'] = n1826
        # sudoku/Rows/row_9/diff14 -> n1827
        n1827 = self.context.mk_neq(n1788, n1794)
        self.nets['sudoku/Rows/row_9/diff14'] = n1827
        # sudoku/Rows/row_9/diff15 -> n1828
        n1828 = self.context.mk_neq(n1788, n1795)
        self.nets['sudoku/Rows/row_9/diff15'] = n1828
        # sudoku/Rows/row_9/Logical Operator1 -> n1829
        tn373 = self.context.mk_and(n1827, n1828)
        tn372 = self.context.mk_and(n1826, tn373)
        tn371 = self.context.mk_and(n1825, tn372)
        tn370 = self.context.mk_and(n1824, tn371)
        tn369 = self.context.mk_and(n1823, tn370)
        n1829 = self.context.mk_and(n1822, tn369)
        self.nets['sudoku/Rows/row_9/Logical Operator1'] = n1829
        # sudoku/Rows/row_9/diff1 -> n1830
        n1830 = self.context.mk_neq(n1787, n1788)
        self.nets['sudoku/Rows/row_9/diff1'] = n1830
        # sudoku/Rows/row_9/diff2 -> n1831
        n1831 = self.context.mk_neq(n1787, n1789)
        self.nets['sudoku/Rows/row_9/diff2'] = n1831
        # sudoku/Rows/row_9/diff3 -> n1832
        n1832 = self.context.mk_neq(n1787, n1790)
        self.nets['sudoku/Rows/row_9/diff3'] = n1832
        # sudoku/Rows/row_9/diff4 -> n1833
        n1833 = self.context.mk_neq(n1787, n1791)
        self.nets['sudoku/Rows/row_9/diff4'] = n1833
        # sudoku/Rows/row_9/diff5 -> n1834
        n1834 = self.context.mk_neq(n1787, n1792)
        self.nets['sudoku/Rows/row_9/diff5'] = n1834
        # sudoku/Rows/row_9/diff6 -> n1835
        n1835 = self.context.mk_neq(n1787, n1793)
        self.nets['sudoku/Rows/row_9/diff6'] = n1835
        # sudoku/Rows/row_9/diff7 -> n1836
        n1836 = self.context.mk_neq(n1787, n1794)
        self.nets['sudoku/Rows/row_9/diff7'] = n1836
        # sudoku/Rows/row_9/diff8 -> n1837
        n1837 = self.context.mk_neq(n1787, n1795)
        self.nets['sudoku/Rows/row_9/diff8'] = n1837
        # sudoku/Rows/row_9/Logical Operator -> n1838
        tn379 = self.context.mk_and(n1836, n1837)
        tn378 = self.context.mk_and(n1835, tn379)
        tn377 = self.context.mk_and(n1834, tn378)
        tn376 = self.context.mk_and(n1833, tn377)
        tn375 = self.context.mk_and(n1832, tn376)
        tn374 = self.context.mk_and(n1831, tn375)
        n1838 = self.context.mk_and(n1830, tn374)
        self.nets['sudoku/Rows/row_9/Logical Operator'] = n1838
        # sudoku/Rows/row_9/Logical Operator7 -> n1839
        tn385 = self.context.mk_and(n1829, n1838)
        tn384 = self.context.mk_and(n1821, tn385)
        tn383 = self.context.mk_and(n1814, tn384)
        tn382 = self.context.mk_and(n1808, tn383)
        tn381 = self.context.mk_and(n1803, tn382)
        tn380 = self.context.mk_and(n1799, tn381)
        n1839 = self.context.mk_and(n1796, tn380)
        self.nets['sudoku/Rows/row_9/Logical Operator7'] = n1839
        # n1839 -> Out1
        return n1839

    def row_3(self, n1841, n1842, n1843, n1844, n1845, n1846, n1847, n1848, n1849):
        # In1 -> n1841
        # In2 -> n1842
        # In3 -> n1843
        # In4 -> n1844
        # In5 -> n1845
        # In6 -> n1846
        # In7 -> n1847
        # In8 -> n1848
        # In9 -> n1849
        # sudoku/Rows/row_3/diff36 -> n1850
        n1850 = self.context.mk_neq(n1848, n1849)
        self.nets['sudoku/Rows/row_3/diff36'] = n1850
        # sudoku/Rows/row_3/diff34 -> n1851
        n1851 = self.context.mk_neq(n1847, n1848)
        self.nets['sudoku/Rows/row_3/diff34'] = n1851
        # sudoku/Rows/row_3/diff35 -> n1852
        n1852 = self.context.mk_neq(n1847, n1849)
        self.nets['sudoku/Rows/row_3/diff35'] = n1852
        # sudoku/Rows/row_3/Logical Operator6 -> n1853
        n1853 = self.context.mk_and(n1851, n1852)
        self.nets['sudoku/Rows/row_3/Logical Operator6'] = n1853
        # sudoku/Rows/row_3/diff31 -> n1854
        n1854 = self.context.mk_neq(n1846, n1847)
        self.nets['sudoku/Rows/row_3/diff31'] = n1854
        # sudoku/Rows/row_3/diff32 -> n1855
        n1855 = self.context.mk_neq(n1846, n1848)
        self.nets['sudoku/Rows/row_3/diff32'] = n1855
        # sudoku/Rows/row_3/diff33 -> n1856
        n1856 = self.context.mk_neq(n1846, n1849)
        self.nets['sudoku/Rows/row_3/diff33'] = n1856
        # sudoku/Rows/row_3/Logical Operator5 -> n1857
        tn386 = self.context.mk_and(n1855, n1856)
        n1857 = self.context.mk_and(n1854, tn386)
        self.nets['sudoku/Rows/row_3/Logical Operator5'] = n1857
        # sudoku/Rows/row_3/diff27 -> n1858
        n1858 = self.context.mk_neq(n1845, n1846)
        self.nets['sudoku/Rows/row_3/diff27'] = n1858
        # sudoku/Rows/row_3/diff28 -> n1859
        n1859 = self.context.mk_neq(n1845, n1847)
        self.nets['sudoku/Rows/row_3/diff28'] = n1859
        # sudoku/Rows/row_3/diff29 -> n1860
        n1860 = self.context.mk_neq(n1845, n1848)
        self.nets['sudoku/Rows/row_3/diff29'] = n1860
        # sudoku/Rows/row_3/diff30 -> n1861
        n1861 = self.context.mk_neq(n1845, n1849)
        self.nets['sudoku/Rows/row_3/diff30'] = n1861
        # sudoku/Rows/row_3/Logical Operator4 -> n1862
        tn388 = self.context.mk_and(n1860, n1861)
        tn387 = self.context.mk_and(n1859, tn388)
        n1862 = self.context.mk_and(n1858, tn387)
        self.nets['sudoku/Rows/row_3/Logical Operator4'] = n1862
        # sudoku/Rows/row_3/diff22 -> n1863
        n1863 = self.context.mk_neq(n1844, n1845)
        self.nets['sudoku/Rows/row_3/diff22'] = n1863
        # sudoku/Rows/row_3/diff23 -> n1864
        n1864 = self.context.mk_neq(n1844, n1846)
        self.nets['sudoku/Rows/row_3/diff23'] = n1864
        # sudoku/Rows/row_3/diff24 -> n1865
        n1865 = self.context.mk_neq(n1844, n1847)
        self.nets['sudoku/Rows/row_3/diff24'] = n1865
        # sudoku/Rows/row_3/diff25 -> n1866
        n1866 = self.context.mk_neq(n1844, n1848)
        self.nets['sudoku/Rows/row_3/diff25'] = n1866
        # sudoku/Rows/row_3/diff26 -> n1867
        n1867 = self.context.mk_neq(n1844, n1849)
        self.nets['sudoku/Rows/row_3/diff26'] = n1867
        # sudoku/Rows/row_3/Logical Operator3 -> n1868
        tn391 = self.context.mk_and(n1866, n1867)
        tn390 = self.context.mk_and(n1865, tn391)
        tn389 = self.context.mk_and(n1864, tn390)
        n1868 = self.context.mk_and(n1863, tn389)
        self.nets['sudoku/Rows/row_3/Logical Operator3'] = n1868
        # sudoku/Rows/row_3/diff16 -> n1869
        n1869 = self.context.mk_neq(n1843, n1844)
        self.nets['sudoku/Rows/row_3/diff16'] = n1869
        # sudoku/Rows/row_3/diff17 -> n1870
        n1870 = self.context.mk_neq(n1843, n1845)
        self.nets['sudoku/Rows/row_3/diff17'] = n1870
        # sudoku/Rows/row_3/diff18 -> n1871
        n1871 = self.context.mk_neq(n1843, n1846)
        self.nets['sudoku/Rows/row_3/diff18'] = n1871
        # sudoku/Rows/row_3/diff19 -> n1872
        n1872 = self.context.mk_neq(n1843, n1847)
        self.nets['sudoku/Rows/row_3/diff19'] = n1872
        # sudoku/Rows/row_3/diff20 -> n1873
        n1873 = self.context.mk_neq(n1843, n1848)
        self.nets['sudoku/Rows/row_3/diff20'] = n1873
        # sudoku/Rows/row_3/diff21 -> n1874
        n1874 = self.context.mk_neq(n1843, n1849)
        self.nets['sudoku/Rows/row_3/diff21'] = n1874
        # sudoku/Rows/row_3/Logical Operator2 -> n1875
        tn395 = self.context.mk_and(n1873, n1874)
        tn394 = self.context.mk_and(n1872, tn395)
        tn393 = self.context.mk_and(n1871, tn394)
        tn392 = self.context.mk_and(n1870, tn393)
        n1875 = self.context.mk_and(n1869, tn392)
        self.nets['sudoku/Rows/row_3/Logical Operator2'] = n1875
        # sudoku/Rows/row_3/diff9 -> n1876
        n1876 = self.context.mk_neq(n1842, n1843)
        self.nets['sudoku/Rows/row_3/diff9'] = n1876
        # sudoku/Rows/row_3/diff10 -> n1877
        n1877 = self.context.mk_neq(n1842, n1844)
        self.nets['sudoku/Rows/row_3/diff10'] = n1877
        # sudoku/Rows/row_3/diff11 -> n1878
        n1878 = self.context.mk_neq(n1842, n1845)
        self.nets['sudoku/Rows/row_3/diff11'] = n1878
        # sudoku/Rows/row_3/diff12 -> n1879
        n1879 = self.context.mk_neq(n1842, n1846)
        self.nets['sudoku/Rows/row_3/diff12'] = n1879
        # sudoku/Rows/row_3/diff13 -> n1880
        n1880 = self.context.mk_neq(n1842, n1847)
        self.nets['sudoku/Rows/row_3/diff13'] = n1880
        # sudoku/Rows/row_3/diff14 -> n1881
        n1881 = self.context.mk_neq(n1842, n1848)
        self.nets['sudoku/Rows/row_3/diff14'] = n1881
        # sudoku/Rows/row_3/diff15 -> n1882
        n1882 = self.context.mk_neq(n1842, n1849)
        self.nets['sudoku/Rows/row_3/diff15'] = n1882
        # sudoku/Rows/row_3/Logical Operator1 -> n1883
        tn400 = self.context.mk_and(n1881, n1882)
        tn399 = self.context.mk_and(n1880, tn400)
        tn398 = self.context.mk_and(n1879, tn399)
        tn397 = self.context.mk_and(n1878, tn398)
        tn396 = self.context.mk_and(n1877, tn397)
        n1883 = self.context.mk_and(n1876, tn396)
        self.nets['sudoku/Rows/row_3/Logical Operator1'] = n1883
        # sudoku/Rows/row_3/diff1 -> n1884
        n1884 = self.context.mk_neq(n1841, n1842)
        self.nets['sudoku/Rows/row_3/diff1'] = n1884
        # sudoku/Rows/row_3/diff2 -> n1885
        n1885 = self.context.mk_neq(n1841, n1843)
        self.nets['sudoku/Rows/row_3/diff2'] = n1885
        # sudoku/Rows/row_3/diff3 -> n1886
        n1886 = self.context.mk_neq(n1841, n1844)
        self.nets['sudoku/Rows/row_3/diff3'] = n1886
        # sudoku/Rows/row_3/diff4 -> n1887
        n1887 = self.context.mk_neq(n1841, n1845)
        self.nets['sudoku/Rows/row_3/diff4'] = n1887
        # sudoku/Rows/row_3/diff5 -> n1888
        n1888 = self.context.mk_neq(n1841, n1846)
        self.nets['sudoku/Rows/row_3/diff5'] = n1888
        # sudoku/Rows/row_3/diff6 -> n1889
        n1889 = self.context.mk_neq(n1841, n1847)
        self.nets['sudoku/Rows/row_3/diff6'] = n1889
        # sudoku/Rows/row_3/diff7 -> n1890
        n1890 = self.context.mk_neq(n1841, n1848)
        self.nets['sudoku/Rows/row_3/diff7'] = n1890
        # sudoku/Rows/row_3/diff8 -> n1891
        n1891 = self.context.mk_neq(n1841, n1849)
        self.nets['sudoku/Rows/row_3/diff8'] = n1891
        # sudoku/Rows/row_3/Logical Operator -> n1892
        tn406 = self.context.mk_and(n1890, n1891)
        tn405 = self.context.mk_and(n1889, tn406)
        tn404 = self.context.mk_and(n1888, tn405)
        tn403 = self.context.mk_and(n1887, tn404)
        tn402 = self.context.mk_and(n1886, tn403)
        tn401 = self.context.mk_and(n1885, tn402)
        n1892 = self.context.mk_and(n1884, tn401)
        self.nets['sudoku/Rows/row_3/Logical Operator'] = n1892
        # sudoku/Rows/row_3/Logical Operator7 -> n1893
        tn412 = self.context.mk_and(n1883, n1892)
        tn411 = self.context.mk_and(n1875, tn412)
        tn410 = self.context.mk_and(n1868, tn411)
        tn409 = self.context.mk_and(n1862, tn410)
        tn408 = self.context.mk_and(n1857, tn409)
        tn407 = self.context.mk_and(n1853, tn408)
        n1893 = self.context.mk_and(n1850, tn407)
        self.nets['sudoku/Rows/row_3/Logical Operator7'] = n1893
        # n1893 -> Out1
        return n1893

    def row_4(self, n1895, n1896, n1897, n1898, n1899, n1900, n1901, n1902, n1903):
        # In1 -> n1895
        # In2 -> n1896
        # In3 -> n1897
        # In4 -> n1898
        # In5 -> n1899
        # In6 -> n1900
        # In7 -> n1901
        # In8 -> n1902
        # In9 -> n1903
        # sudoku/Rows/row_4/diff36 -> n1904
        n1904 = self.context.mk_neq(n1902, n1903)
        self.nets['sudoku/Rows/row_4/diff36'] = n1904
        # sudoku/Rows/row_4/diff34 -> n1905
        n1905 = self.context.mk_neq(n1901, n1902)
        self.nets['sudoku/Rows/row_4/diff34'] = n1905
        # sudoku/Rows/row_4/diff35 -> n1906
        n1906 = self.context.mk_neq(n1901, n1903)
        self.nets['sudoku/Rows/row_4/diff35'] = n1906
        # sudoku/Rows/row_4/Logical Operator6 -> n1907
        n1907 = self.context.mk_and(n1905, n1906)
        self.nets['sudoku/Rows/row_4/Logical Operator6'] = n1907
        # sudoku/Rows/row_4/diff31 -> n1908
        n1908 = self.context.mk_neq(n1900, n1901)
        self.nets['sudoku/Rows/row_4/diff31'] = n1908
        # sudoku/Rows/row_4/diff32 -> n1909
        n1909 = self.context.mk_neq(n1900, n1902)
        self.nets['sudoku/Rows/row_4/diff32'] = n1909
        # sudoku/Rows/row_4/diff33 -> n1910
        n1910 = self.context.mk_neq(n1900, n1903)
        self.nets['sudoku/Rows/row_4/diff33'] = n1910
        # sudoku/Rows/row_4/Logical Operator5 -> n1911
        tn413 = self.context.mk_and(n1909, n1910)
        n1911 = self.context.mk_and(n1908, tn413)
        self.nets['sudoku/Rows/row_4/Logical Operator5'] = n1911
        # sudoku/Rows/row_4/diff27 -> n1912
        n1912 = self.context.mk_neq(n1899, n1900)
        self.nets['sudoku/Rows/row_4/diff27'] = n1912
        # sudoku/Rows/row_4/diff28 -> n1913
        n1913 = self.context.mk_neq(n1899, n1901)
        self.nets['sudoku/Rows/row_4/diff28'] = n1913
        # sudoku/Rows/row_4/diff29 -> n1914
        n1914 = self.context.mk_neq(n1899, n1902)
        self.nets['sudoku/Rows/row_4/diff29'] = n1914
        # sudoku/Rows/row_4/diff30 -> n1915
        n1915 = self.context.mk_neq(n1899, n1903)
        self.nets['sudoku/Rows/row_4/diff30'] = n1915
        # sudoku/Rows/row_4/Logical Operator4 -> n1916
        tn415 = self.context.mk_and(n1914, n1915)
        tn414 = self.context.mk_and(n1913, tn415)
        n1916 = self.context.mk_and(n1912, tn414)
        self.nets['sudoku/Rows/row_4/Logical Operator4'] = n1916
        # sudoku/Rows/row_4/diff22 -> n1917
        n1917 = self.context.mk_neq(n1898, n1899)
        self.nets['sudoku/Rows/row_4/diff22'] = n1917
        # sudoku/Rows/row_4/diff23 -> n1918
        n1918 = self.context.mk_neq(n1898, n1900)
        self.nets['sudoku/Rows/row_4/diff23'] = n1918
        # sudoku/Rows/row_4/diff24 -> n1919
        n1919 = self.context.mk_neq(n1898, n1901)
        self.nets['sudoku/Rows/row_4/diff24'] = n1919
        # sudoku/Rows/row_4/diff25 -> n1920
        n1920 = self.context.mk_neq(n1898, n1902)
        self.nets['sudoku/Rows/row_4/diff25'] = n1920
        # sudoku/Rows/row_4/diff26 -> n1921
        n1921 = self.context.mk_neq(n1898, n1903)
        self.nets['sudoku/Rows/row_4/diff26'] = n1921
        # sudoku/Rows/row_4/Logical Operator3 -> n1922
        tn418 = self.context.mk_and(n1920, n1921)
        tn417 = self.context.mk_and(n1919, tn418)
        tn416 = self.context.mk_and(n1918, tn417)
        n1922 = self.context.mk_and(n1917, tn416)
        self.nets['sudoku/Rows/row_4/Logical Operator3'] = n1922
        # sudoku/Rows/row_4/diff16 -> n1923
        n1923 = self.context.mk_neq(n1897, n1898)
        self.nets['sudoku/Rows/row_4/diff16'] = n1923
        # sudoku/Rows/row_4/diff17 -> n1924
        n1924 = self.context.mk_neq(n1897, n1899)
        self.nets['sudoku/Rows/row_4/diff17'] = n1924
        # sudoku/Rows/row_4/diff18 -> n1925
        n1925 = self.context.mk_neq(n1897, n1900)
        self.nets['sudoku/Rows/row_4/diff18'] = n1925
        # sudoku/Rows/row_4/diff19 -> n1926
        n1926 = self.context.mk_neq(n1897, n1901)
        self.nets['sudoku/Rows/row_4/diff19'] = n1926
        # sudoku/Rows/row_4/diff20 -> n1927
        n1927 = self.context.mk_neq(n1897, n1902)
        self.nets['sudoku/Rows/row_4/diff20'] = n1927
        # sudoku/Rows/row_4/diff21 -> n1928
        n1928 = self.context.mk_neq(n1897, n1903)
        self.nets['sudoku/Rows/row_4/diff21'] = n1928
        # sudoku/Rows/row_4/Logical Operator2 -> n1929
        tn422 = self.context.mk_and(n1927, n1928)
        tn421 = self.context.mk_and(n1926, tn422)
        tn420 = self.context.mk_and(n1925, tn421)
        tn419 = self.context.mk_and(n1924, tn420)
        n1929 = self.context.mk_and(n1923, tn419)
        self.nets['sudoku/Rows/row_4/Logical Operator2'] = n1929
        # sudoku/Rows/row_4/diff9 -> n1930
        n1930 = self.context.mk_neq(n1896, n1897)
        self.nets['sudoku/Rows/row_4/diff9'] = n1930
        # sudoku/Rows/row_4/diff10 -> n1931
        n1931 = self.context.mk_neq(n1896, n1898)
        self.nets['sudoku/Rows/row_4/diff10'] = n1931
        # sudoku/Rows/row_4/diff11 -> n1932
        n1932 = self.context.mk_neq(n1896, n1899)
        self.nets['sudoku/Rows/row_4/diff11'] = n1932
        # sudoku/Rows/row_4/diff12 -> n1933
        n1933 = self.context.mk_neq(n1896, n1900)
        self.nets['sudoku/Rows/row_4/diff12'] = n1933
        # sudoku/Rows/row_4/diff13 -> n1934
        n1934 = self.context.mk_neq(n1896, n1901)
        self.nets['sudoku/Rows/row_4/diff13'] = n1934
        # sudoku/Rows/row_4/diff14 -> n1935
        n1935 = self.context.mk_neq(n1896, n1902)
        self.nets['sudoku/Rows/row_4/diff14'] = n1935
        # sudoku/Rows/row_4/diff15 -> n1936
        n1936 = self.context.mk_neq(n1896, n1903)
        self.nets['sudoku/Rows/row_4/diff15'] = n1936
        # sudoku/Rows/row_4/Logical Operator1 -> n1937
        tn427 = self.context.mk_and(n1935, n1936)
        tn426 = self.context.mk_and(n1934, tn427)
        tn425 = self.context.mk_and(n1933, tn426)
        tn424 = self.context.mk_and(n1932, tn425)
        tn423 = self.context.mk_and(n1931, tn424)
        n1937 = self.context.mk_and(n1930, tn423)
        self.nets['sudoku/Rows/row_4/Logical Operator1'] = n1937
        # sudoku/Rows/row_4/diff1 -> n1938
        n1938 = self.context.mk_neq(n1895, n1896)
        self.nets['sudoku/Rows/row_4/diff1'] = n1938
        # sudoku/Rows/row_4/diff2 -> n1939
        n1939 = self.context.mk_neq(n1895, n1897)
        self.nets['sudoku/Rows/row_4/diff2'] = n1939
        # sudoku/Rows/row_4/diff3 -> n1940
        n1940 = self.context.mk_neq(n1895, n1898)
        self.nets['sudoku/Rows/row_4/diff3'] = n1940
        # sudoku/Rows/row_4/diff4 -> n1941
        n1941 = self.context.mk_neq(n1895, n1899)
        self.nets['sudoku/Rows/row_4/diff4'] = n1941
        # sudoku/Rows/row_4/diff5 -> n1942
        n1942 = self.context.mk_neq(n1895, n1900)
        self.nets['sudoku/Rows/row_4/diff5'] = n1942
        # sudoku/Rows/row_4/diff6 -> n1943
        n1943 = self.context.mk_neq(n1895, n1901)
        self.nets['sudoku/Rows/row_4/diff6'] = n1943
        # sudoku/Rows/row_4/diff7 -> n1944
        n1944 = self.context.mk_neq(n1895, n1902)
        self.nets['sudoku/Rows/row_4/diff7'] = n1944
        # sudoku/Rows/row_4/diff8 -> n1945
        n1945 = self.context.mk_neq(n1895, n1903)
        self.nets['sudoku/Rows/row_4/diff8'] = n1945
        # sudoku/Rows/row_4/Logical Operator -> n1946
        tn433 = self.context.mk_and(n1944, n1945)
        tn432 = self.context.mk_and(n1943, tn433)
        tn431 = self.context.mk_and(n1942, tn432)
        tn430 = self.context.mk_and(n1941, tn431)
        tn429 = self.context.mk_and(n1940, tn430)
        tn428 = self.context.mk_and(n1939, tn429)
        n1946 = self.context.mk_and(n1938, tn428)
        self.nets['sudoku/Rows/row_4/Logical Operator'] = n1946
        # sudoku/Rows/row_4/Logical Operator7 -> n1947
        tn439 = self.context.mk_and(n1937, n1946)
        tn438 = self.context.mk_and(n1929, tn439)
        tn437 = self.context.mk_and(n1922, tn438)
        tn436 = self.context.mk_and(n1916, tn437)
        tn435 = self.context.mk_and(n1911, tn436)
        tn434 = self.context.mk_and(n1907, tn435)
        n1947 = self.context.mk_and(n1904, tn434)
        self.nets['sudoku/Rows/row_4/Logical Operator7'] = n1947
        # n1947 -> Out1
        return n1947

    def row_1(self, n1949, n1950, n1951, n1952, n1953, n1954, n1955, n1956, n1957):
        # In1 -> n1949
        # In2 -> n1950
        # In3 -> n1951
        # In4 -> n1952
        # In5 -> n1953
        # In6 -> n1954
        # In7 -> n1955
        # In8 -> n1956
        # In9 -> n1957
        # sudoku/Rows/row_1/diff36 -> n1958
        n1958 = self.context.mk_neq(n1956, n1957)
        self.nets['sudoku/Rows/row_1/diff36'] = n1958
        # sudoku/Rows/row_1/diff34 -> n1959
        n1959 = self.context.mk_neq(n1955, n1956)
        self.nets['sudoku/Rows/row_1/diff34'] = n1959
        # sudoku/Rows/row_1/diff35 -> n1960
        n1960 = self.context.mk_neq(n1955, n1957)
        self.nets['sudoku/Rows/row_1/diff35'] = n1960
        # sudoku/Rows/row_1/Logical Operator6 -> n1961
        n1961 = self.context.mk_and(n1959, n1960)
        self.nets['sudoku/Rows/row_1/Logical Operator6'] = n1961
        # sudoku/Rows/row_1/diff31 -> n1962
        n1962 = self.context.mk_neq(n1954, n1955)
        self.nets['sudoku/Rows/row_1/diff31'] = n1962
        # sudoku/Rows/row_1/diff32 -> n1963
        n1963 = self.context.mk_neq(n1954, n1956)
        self.nets['sudoku/Rows/row_1/diff32'] = n1963
        # sudoku/Rows/row_1/diff33 -> n1964
        n1964 = self.context.mk_neq(n1954, n1957)
        self.nets['sudoku/Rows/row_1/diff33'] = n1964
        # sudoku/Rows/row_1/Logical Operator5 -> n1965
        tn440 = self.context.mk_and(n1963, n1964)
        n1965 = self.context.mk_and(n1962, tn440)
        self.nets['sudoku/Rows/row_1/Logical Operator5'] = n1965
        # sudoku/Rows/row_1/diff27 -> n1966
        n1966 = self.context.mk_neq(n1953, n1954)
        self.nets['sudoku/Rows/row_1/diff27'] = n1966
        # sudoku/Rows/row_1/diff28 -> n1967
        n1967 = self.context.mk_neq(n1953, n1955)
        self.nets['sudoku/Rows/row_1/diff28'] = n1967
        # sudoku/Rows/row_1/diff29 -> n1968
        n1968 = self.context.mk_neq(n1953, n1956)
        self.nets['sudoku/Rows/row_1/diff29'] = n1968
        # sudoku/Rows/row_1/diff30 -> n1969
        n1969 = self.context.mk_neq(n1953, n1957)
        self.nets['sudoku/Rows/row_1/diff30'] = n1969
        # sudoku/Rows/row_1/Logical Operator4 -> n1970
        tn442 = self.context.mk_and(n1968, n1969)
        tn441 = self.context.mk_and(n1967, tn442)
        n1970 = self.context.mk_and(n1966, tn441)
        self.nets['sudoku/Rows/row_1/Logical Operator4'] = n1970
        # sudoku/Rows/row_1/diff22 -> n1971
        n1971 = self.context.mk_neq(n1952, n1953)
        self.nets['sudoku/Rows/row_1/diff22'] = n1971
        # sudoku/Rows/row_1/diff23 -> n1972
        n1972 = self.context.mk_neq(n1952, n1954)
        self.nets['sudoku/Rows/row_1/diff23'] = n1972
        # sudoku/Rows/row_1/diff24 -> n1973
        n1973 = self.context.mk_neq(n1952, n1955)
        self.nets['sudoku/Rows/row_1/diff24'] = n1973
        # sudoku/Rows/row_1/diff25 -> n1974
        n1974 = self.context.mk_neq(n1952, n1956)
        self.nets['sudoku/Rows/row_1/diff25'] = n1974
        # sudoku/Rows/row_1/diff26 -> n1975
        n1975 = self.context.mk_neq(n1952, n1957)
        self.nets['sudoku/Rows/row_1/diff26'] = n1975
        # sudoku/Rows/row_1/Logical Operator3 -> n1976
        tn445 = self.context.mk_and(n1974, n1975)
        tn444 = self.context.mk_and(n1973, tn445)
        tn443 = self.context.mk_and(n1972, tn444)
        n1976 = self.context.mk_and(n1971, tn443)
        self.nets['sudoku/Rows/row_1/Logical Operator3'] = n1976
        # sudoku/Rows/row_1/diff16 -> n1977
        n1977 = self.context.mk_neq(n1951, n1952)
        self.nets['sudoku/Rows/row_1/diff16'] = n1977
        # sudoku/Rows/row_1/diff17 -> n1978
        n1978 = self.context.mk_neq(n1951, n1953)
        self.nets['sudoku/Rows/row_1/diff17'] = n1978
        # sudoku/Rows/row_1/diff18 -> n1979
        n1979 = self.context.mk_neq(n1951, n1954)
        self.nets['sudoku/Rows/row_1/diff18'] = n1979
        # sudoku/Rows/row_1/diff19 -> n1980
        n1980 = self.context.mk_neq(n1951, n1955)
        self.nets['sudoku/Rows/row_1/diff19'] = n1980
        # sudoku/Rows/row_1/diff20 -> n1981
        n1981 = self.context.mk_neq(n1951, n1956)
        self.nets['sudoku/Rows/row_1/diff20'] = n1981
        # sudoku/Rows/row_1/diff21 -> n1982
        n1982 = self.context.mk_neq(n1951, n1957)
        self.nets['sudoku/Rows/row_1/diff21'] = n1982
        # sudoku/Rows/row_1/Logical Operator2 -> n1983
        tn449 = self.context.mk_and(n1981, n1982)
        tn448 = self.context.mk_and(n1980, tn449)
        tn447 = self.context.mk_and(n1979, tn448)
        tn446 = self.context.mk_and(n1978, tn447)
        n1983 = self.context.mk_and(n1977, tn446)
        self.nets['sudoku/Rows/row_1/Logical Operator2'] = n1983
        # sudoku/Rows/row_1/diff9 -> n1984
        n1984 = self.context.mk_neq(n1950, n1951)
        self.nets['sudoku/Rows/row_1/diff9'] = n1984
        # sudoku/Rows/row_1/diff10 -> n1985
        n1985 = self.context.mk_neq(n1950, n1952)
        self.nets['sudoku/Rows/row_1/diff10'] = n1985
        # sudoku/Rows/row_1/diff11 -> n1986
        n1986 = self.context.mk_neq(n1950, n1953)
        self.nets['sudoku/Rows/row_1/diff11'] = n1986
        # sudoku/Rows/row_1/diff12 -> n1987
        n1987 = self.context.mk_neq(n1950, n1954)
        self.nets['sudoku/Rows/row_1/diff12'] = n1987
        # sudoku/Rows/row_1/diff13 -> n1988
        n1988 = self.context.mk_neq(n1950, n1955)
        self.nets['sudoku/Rows/row_1/diff13'] = n1988
        # sudoku/Rows/row_1/diff14 -> n1989
        n1989 = self.context.mk_neq(n1950, n1956)
        self.nets['sudoku/Rows/row_1/diff14'] = n1989
        # sudoku/Rows/row_1/diff15 -> n1990
        n1990 = self.context.mk_neq(n1950, n1957)
        self.nets['sudoku/Rows/row_1/diff15'] = n1990
        # sudoku/Rows/row_1/Logical Operator1 -> n1991
        tn454 = self.context.mk_and(n1989, n1990)
        tn453 = self.context.mk_and(n1988, tn454)
        tn452 = self.context.mk_and(n1987, tn453)
        tn451 = self.context.mk_and(n1986, tn452)
        tn450 = self.context.mk_and(n1985, tn451)
        n1991 = self.context.mk_and(n1984, tn450)
        self.nets['sudoku/Rows/row_1/Logical Operator1'] = n1991
        # sudoku/Rows/row_1/diff1 -> n1992
        n1992 = self.context.mk_neq(n1949, n1950)
        self.nets['sudoku/Rows/row_1/diff1'] = n1992
        # sudoku/Rows/row_1/diff2 -> n1993
        n1993 = self.context.mk_neq(n1949, n1951)
        self.nets['sudoku/Rows/row_1/diff2'] = n1993
        # sudoku/Rows/row_1/diff3 -> n1994
        n1994 = self.context.mk_neq(n1949, n1952)
        self.nets['sudoku/Rows/row_1/diff3'] = n1994
        # sudoku/Rows/row_1/diff4 -> n1995
        n1995 = self.context.mk_neq(n1949, n1953)
        self.nets['sudoku/Rows/row_1/diff4'] = n1995
        # sudoku/Rows/row_1/diff5 -> n1996
        n1996 = self.context.mk_neq(n1949, n1954)
        self.nets['sudoku/Rows/row_1/diff5'] = n1996
        # sudoku/Rows/row_1/diff6 -> n1997
        n1997 = self.context.mk_neq(n1949, n1955)
        self.nets['sudoku/Rows/row_1/diff6'] = n1997
        # sudoku/Rows/row_1/diff7 -> n1998
        n1998 = self.context.mk_neq(n1949, n1956)
        self.nets['sudoku/Rows/row_1/diff7'] = n1998
        # sudoku/Rows/row_1/diff8 -> n1999
        n1999 = self.context.mk_neq(n1949, n1957)
        self.nets['sudoku/Rows/row_1/diff8'] = n1999
        # sudoku/Rows/row_1/Logical Operator -> n2000
        tn460 = self.context.mk_and(n1998, n1999)
        tn459 = self.context.mk_and(n1997, tn460)
        tn458 = self.context.mk_and(n1996, tn459)
        tn457 = self.context.mk_and(n1995, tn458)
        tn456 = self.context.mk_and(n1994, tn457)
        tn455 = self.context.mk_and(n1993, tn456)
        n2000 = self.context.mk_and(n1992, tn455)
        self.nets['sudoku/Rows/row_1/Logical Operator'] = n2000
        # sudoku/Rows/row_1/Logical Operator7 -> n2001
        tn466 = self.context.mk_and(n1991, n2000)
        tn465 = self.context.mk_and(n1983, tn466)
        tn464 = self.context.mk_and(n1976, tn465)
        tn463 = self.context.mk_and(n1970, tn464)
        tn462 = self.context.mk_and(n1965, tn463)
        tn461 = self.context.mk_and(n1961, tn462)
        n2001 = self.context.mk_and(n1958, tn461)
        self.nets['sudoku/Rows/row_1/Logical Operator7'] = n2001
        # n2001 -> Out1
        return n2001

    def row_2(self, n2003, n2004, n2005, n2006, n2007, n2008, n2009, n2010, n2011):
        # In1 -> n2003
        # In2 -> n2004
        # In3 -> n2005
        # In4 -> n2006
        # In5 -> n2007
        # In6 -> n2008
        # In7 -> n2009
        # In8 -> n2010
        # In9 -> n2011
        # sudoku/Rows/row_2/diff36 -> n2012
        n2012 = self.context.mk_neq(n2010, n2011)
        self.nets['sudoku/Rows/row_2/diff36'] = n2012
        # sudoku/Rows/row_2/diff34 -> n2013
        n2013 = self.context.mk_neq(n2009, n2010)
        self.nets['sudoku/Rows/row_2/diff34'] = n2013
        # sudoku/Rows/row_2/diff35 -> n2014
        n2014 = self.context.mk_neq(n2009, n2011)
        self.nets['sudoku/Rows/row_2/diff35'] = n2014
        # sudoku/Rows/row_2/Logical Operator6 -> n2015
        n2015 = self.context.mk_and(n2013, n2014)
        self.nets['sudoku/Rows/row_2/Logical Operator6'] = n2015
        # sudoku/Rows/row_2/diff31 -> n2016
        n2016 = self.context.mk_neq(n2008, n2009)
        self.nets['sudoku/Rows/row_2/diff31'] = n2016
        # sudoku/Rows/row_2/diff32 -> n2017
        n2017 = self.context.mk_neq(n2008, n2010)
        self.nets['sudoku/Rows/row_2/diff32'] = n2017
        # sudoku/Rows/row_2/diff33 -> n2018
        n2018 = self.context.mk_neq(n2008, n2011)
        self.nets['sudoku/Rows/row_2/diff33'] = n2018
        # sudoku/Rows/row_2/Logical Operator5 -> n2019
        tn467 = self.context.mk_and(n2017, n2018)
        n2019 = self.context.mk_and(n2016, tn467)
        self.nets['sudoku/Rows/row_2/Logical Operator5'] = n2019
        # sudoku/Rows/row_2/diff27 -> n2020
        n2020 = self.context.mk_neq(n2007, n2008)
        self.nets['sudoku/Rows/row_2/diff27'] = n2020
        # sudoku/Rows/row_2/diff28 -> n2021
        n2021 = self.context.mk_neq(n2007, n2009)
        self.nets['sudoku/Rows/row_2/diff28'] = n2021
        # sudoku/Rows/row_2/diff29 -> n2022
        n2022 = self.context.mk_neq(n2007, n2010)
        self.nets['sudoku/Rows/row_2/diff29'] = n2022
        # sudoku/Rows/row_2/diff30 -> n2023
        n2023 = self.context.mk_neq(n2007, n2011)
        self.nets['sudoku/Rows/row_2/diff30'] = n2023
        # sudoku/Rows/row_2/Logical Operator4 -> n2024
        tn469 = self.context.mk_and(n2022, n2023)
        tn468 = self.context.mk_and(n2021, tn469)
        n2024 = self.context.mk_and(n2020, tn468)
        self.nets['sudoku/Rows/row_2/Logical Operator4'] = n2024
        # sudoku/Rows/row_2/diff22 -> n2025
        n2025 = self.context.mk_neq(n2006, n2007)
        self.nets['sudoku/Rows/row_2/diff22'] = n2025
        # sudoku/Rows/row_2/diff23 -> n2026
        n2026 = self.context.mk_neq(n2006, n2008)
        self.nets['sudoku/Rows/row_2/diff23'] = n2026
        # sudoku/Rows/row_2/diff24 -> n2027
        n2027 = self.context.mk_neq(n2006, n2009)
        self.nets['sudoku/Rows/row_2/diff24'] = n2027
        # sudoku/Rows/row_2/diff25 -> n2028
        n2028 = self.context.mk_neq(n2006, n2010)
        self.nets['sudoku/Rows/row_2/diff25'] = n2028
        # sudoku/Rows/row_2/diff26 -> n2029
        n2029 = self.context.mk_neq(n2006, n2011)
        self.nets['sudoku/Rows/row_2/diff26'] = n2029
        # sudoku/Rows/row_2/Logical Operator3 -> n2030
        tn472 = self.context.mk_and(n2028, n2029)
        tn471 = self.context.mk_and(n2027, tn472)
        tn470 = self.context.mk_and(n2026, tn471)
        n2030 = self.context.mk_and(n2025, tn470)
        self.nets['sudoku/Rows/row_2/Logical Operator3'] = n2030
        # sudoku/Rows/row_2/diff16 -> n2031
        n2031 = self.context.mk_neq(n2005, n2006)
        self.nets['sudoku/Rows/row_2/diff16'] = n2031
        # sudoku/Rows/row_2/diff17 -> n2032
        n2032 = self.context.mk_neq(n2005, n2007)
        self.nets['sudoku/Rows/row_2/diff17'] = n2032
        # sudoku/Rows/row_2/diff18 -> n2033
        n2033 = self.context.mk_neq(n2005, n2008)
        self.nets['sudoku/Rows/row_2/diff18'] = n2033
        # sudoku/Rows/row_2/diff19 -> n2034
        n2034 = self.context.mk_neq(n2005, n2009)
        self.nets['sudoku/Rows/row_2/diff19'] = n2034
        # sudoku/Rows/row_2/diff20 -> n2035
        n2035 = self.context.mk_neq(n2005, n2010)
        self.nets['sudoku/Rows/row_2/diff20'] = n2035
        # sudoku/Rows/row_2/diff21 -> n2036
        n2036 = self.context.mk_neq(n2005, n2011)
        self.nets['sudoku/Rows/row_2/diff21'] = n2036
        # sudoku/Rows/row_2/Logical Operator2 -> n2037
        tn476 = self.context.mk_and(n2035, n2036)
        tn475 = self.context.mk_and(n2034, tn476)
        tn474 = self.context.mk_and(n2033, tn475)
        tn473 = self.context.mk_and(n2032, tn474)
        n2037 = self.context.mk_and(n2031, tn473)
        self.nets['sudoku/Rows/row_2/Logical Operator2'] = n2037
        # sudoku/Rows/row_2/diff9 -> n2038
        n2038 = self.context.mk_neq(n2004, n2005)
        self.nets['sudoku/Rows/row_2/diff9'] = n2038
        # sudoku/Rows/row_2/diff10 -> n2039
        n2039 = self.context.mk_neq(n2004, n2006)
        self.nets['sudoku/Rows/row_2/diff10'] = n2039
        # sudoku/Rows/row_2/diff11 -> n2040
        n2040 = self.context.mk_neq(n2004, n2007)
        self.nets['sudoku/Rows/row_2/diff11'] = n2040
        # sudoku/Rows/row_2/diff12 -> n2041
        n2041 = self.context.mk_neq(n2004, n2008)
        self.nets['sudoku/Rows/row_2/diff12'] = n2041
        # sudoku/Rows/row_2/diff13 -> n2042
        n2042 = self.context.mk_neq(n2004, n2009)
        self.nets['sudoku/Rows/row_2/diff13'] = n2042
        # sudoku/Rows/row_2/diff14 -> n2043
        n2043 = self.context.mk_neq(n2004, n2010)
        self.nets['sudoku/Rows/row_2/diff14'] = n2043
        # sudoku/Rows/row_2/diff15 -> n2044
        n2044 = self.context.mk_neq(n2004, n2011)
        self.nets['sudoku/Rows/row_2/diff15'] = n2044
        # sudoku/Rows/row_2/Logical Operator1 -> n2045
        tn481 = self.context.mk_and(n2043, n2044)
        tn480 = self.context.mk_and(n2042, tn481)
        tn479 = self.context.mk_and(n2041, tn480)
        tn478 = self.context.mk_and(n2040, tn479)
        tn477 = self.context.mk_and(n2039, tn478)
        n2045 = self.context.mk_and(n2038, tn477)
        self.nets['sudoku/Rows/row_2/Logical Operator1'] = n2045
        # sudoku/Rows/row_2/diff1 -> n2046
        n2046 = self.context.mk_neq(n2003, n2004)
        self.nets['sudoku/Rows/row_2/diff1'] = n2046
        # sudoku/Rows/row_2/diff2 -> n2047
        n2047 = self.context.mk_neq(n2003, n2005)
        self.nets['sudoku/Rows/row_2/diff2'] = n2047
        # sudoku/Rows/row_2/diff3 -> n2048
        n2048 = self.context.mk_neq(n2003, n2006)
        self.nets['sudoku/Rows/row_2/diff3'] = n2048
        # sudoku/Rows/row_2/diff4 -> n2049
        n2049 = self.context.mk_neq(n2003, n2007)
        self.nets['sudoku/Rows/row_2/diff4'] = n2049
        # sudoku/Rows/row_2/diff5 -> n2050
        n2050 = self.context.mk_neq(n2003, n2008)
        self.nets['sudoku/Rows/row_2/diff5'] = n2050
        # sudoku/Rows/row_2/diff6 -> n2051
        n2051 = self.context.mk_neq(n2003, n2009)
        self.nets['sudoku/Rows/row_2/diff6'] = n2051
        # sudoku/Rows/row_2/diff7 -> n2052
        n2052 = self.context.mk_neq(n2003, n2010)
        self.nets['sudoku/Rows/row_2/diff7'] = n2052
        # sudoku/Rows/row_2/diff8 -> n2053
        n2053 = self.context.mk_neq(n2003, n2011)
        self.nets['sudoku/Rows/row_2/diff8'] = n2053
        # sudoku/Rows/row_2/Logical Operator -> n2054
        tn487 = self.context.mk_and(n2052, n2053)
        tn486 = self.context.mk_and(n2051, tn487)
        tn485 = self.context.mk_and(n2050, tn486)
        tn484 = self.context.mk_and(n2049, tn485)
        tn483 = self.context.mk_and(n2048, tn484)
        tn482 = self.context.mk_and(n2047, tn483)
        n2054 = self.context.mk_and(n2046, tn482)
        self.nets['sudoku/Rows/row_2/Logical Operator'] = n2054
        # sudoku/Rows/row_2/Logical Operator7 -> n2055
        tn493 = self.context.mk_and(n2045, n2054)
        tn492 = self.context.mk_and(n2037, tn493)
        tn491 = self.context.mk_and(n2030, tn492)
        tn490 = self.context.mk_and(n2024, tn491)
        tn489 = self.context.mk_and(n2019, tn490)
        tn488 = self.context.mk_and(n2015, tn489)
        n2055 = self.context.mk_and(n2012, tn488)
        self.nets['sudoku/Rows/row_2/Logical Operator7'] = n2055
        # n2055 -> Out1
        return n2055

    def Rows(self, n2057, n2058, n2059, n2060, n2061, n2062, n2063, n2064, n2065, n2066, n2067, n2068, n2069, n2070, n2071, n2072, n2073, n2074, n2075, n2076, n2077, n2078, n2079, n2080, n2081, n2082, n2083, n2084, n2085, n2086, n2087, n2088, n2089, n2090, n2091, n2092, n2093, n2094, n2095, n2096, n2097, n2098, n2099, n2100, n2101, n2102, n2103, n2104, n2105, n2106, n2107, n2108, n2109, n2110, n2111, n2112, n2113, n2114, n2115, n2116, n2117, n2118, n2119, n2120, n2121, n2122, n2123, n2124, n2125, n2126, n2127, n2128, n2129, n2130, n2131, n2132, n2133, n2134, n2135, n2136, n2137):
        # In1 -> n2057
        # In2 -> n2058
        # In3 -> n2059
        # In4 -> n2060
        # In5 -> n2061
        # In6 -> n2062
        # In7 -> n2063
        # In8 -> n2064
        # In9 -> n2065
        # In10 -> n2066
        # In11 -> n2067
        # In12 -> n2068
        # In13 -> n2069
        # In14 -> n2070
        # In15 -> n2071
        # In16 -> n2072
        # In17 -> n2073
        # In18 -> n2074
        # In19 -> n2075
        # In20 -> n2076
        # In21 -> n2077
        # In22 -> n2078
        # In23 -> n2079
        # In24 -> n2080
        # In25 -> n2081
        # In26 -> n2082
        # In27 -> n2083
        # In28 -> n2084
        # In29 -> n2085
        # In30 -> n2086
        # In31 -> n2087
        # In32 -> n2088
        # In33 -> n2089
        # In34 -> n2090
        # In35 -> n2091
        # In36 -> n2092
        # In37 -> n2093
        # In38 -> n2094
        # In39 -> n2095
        # In40 -> n2096
        # In41 -> n2097
        # In42 -> n2098
        # In43 -> n2099
        # In44 -> n2100
        # In45 -> n2101
        # In46 -> n2102
        # In47 -> n2103
        # In48 -> n2104
        # In49 -> n2105
        # In50 -> n2106
        # In51 -> n2107
        # In52 -> n2108
        # In53 -> n2109
        # In54 -> n2110
        # In55 -> n2111
        # In56 -> n2112
        # In57 -> n2113
        # In58 -> n2114
        # In59 -> n2115
        # In60 -> n2116
        # In61 -> n2117
        # In62 -> n2118
        # In63 -> n2119
        # In64 -> n2120
        # In65 -> n2121
        # In66 -> n2122
        # In67 -> n2123
        # In68 -> n2124
        # In69 -> n2125
        # In70 -> n2126
        # In71 -> n2127
        # In72 -> n2128
        # In73 -> n2129
        # In74 -> n2130
        # In75 -> n2131
        # In76 -> n2132
        # In77 -> n2133
        # In78 -> n2134
        # In79 -> n2135
        # In80 -> n2136
        # In81 -> n2137
        n2138_1 = self.row_1(n2057, n2058, n2059, n2060, n2061, n2062, n2063, n2064, n2065)
        n2139_1 = self.row_2(n2066, n2067, n2068, n2069, n2070, n2071, n2072, n2073, n2074)
        n2140_1 = self.row_3(n2075, n2076, n2077, n2078, n2079, n2080, n2081, n2082, n2083)
        n2141_1 = self.row_4(n2084, n2085, n2086, n2087, n2088, n2089, n2090, n2091, n2092)
        n2142_1 = self.row_5(n2093, n2094, n2095, n2096, n2097, n2098, n2099, n2100, n2101)
        n2143_1 = self.row_6(n2102, n2103, n2104, n2105, n2106, n2107, n2108, n2109, n2110)
        n2144_1 = self.row_7(n2111, n2112, n2113, n2114, n2115, n2116, n2117, n2118, n2119)
        n2145_1 = self.row_8(n2120, n2121, n2122, n2123, n2124, n2125, n2126, n2127, n2128)
        n2146_1 = self.row_9(n2129, n2130, n2131, n2132, n2133, n2134, n2135, n2136, n2137)
        # sudoku/Rows/Logical Operator -> n2147
        tn500 = self.context.mk_and(n2145_1, n2146_1)
        tn499 = self.context.mk_and(n2144_1, tn500)
        tn498 = self.context.mk_and(n2143_1, tn499)
        tn497 = self.context.mk_and(n2142_1, tn498)
        tn496 = self.context.mk_and(n2141_1, tn497)
        tn495 = self.context.mk_and(n2140_1, tn496)
        tn494 = self.context.mk_and(n2139_1, tn495)
        n2147 = self.context.mk_and(n2138_1, tn494)
        self.nets['sudoku/Rows/Logical Operator'] = n2147
        # n2147 -> Out1
        return n2147

    def bounds65(self, n2149):
        # In1 -> n2149
        # sudoku/bounds65/lb
        n2150 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds65/lb'] = n2150
        # sudoku/bounds65/leq -> n2151
        n2151 = self.context.mk_leq(n2150, n2149)
        self.nets['sudoku/bounds65/leq'] = n2151
        # sudoku/bounds65/ub
        n2152 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds65/ub'] = n2152
        # sudoku/bounds65/geq -> n2153
        n2153 = self.context.mk_leq(n2149, n2152)
        self.nets['sudoku/bounds65/geq'] = n2153
        # sudoku/bounds65/Logical Operator -> n2154
        n2154 = self.context.mk_and(n2151, n2153)
        self.nets['sudoku/bounds65/Logical Operator'] = n2154
        # sudoku/bounds65/Assumption
        self.context.mk_assumption(n2154)
        return 

    def block_2(self, n2156, n2157, n2158, n2159, n2160, n2161, n2162, n2163, n2164):
        # In1 -> n2156
        # In2 -> n2157
        # In3 -> n2158
        # In4 -> n2159
        # In5 -> n2160
        # In6 -> n2161
        # In7 -> n2162
        # In8 -> n2163
        # In9 -> n2164
        # sudoku/blocks/block_2/diff36 -> n2165
        n2165 = self.context.mk_neq(n2163, n2164)
        self.nets['sudoku/blocks/block_2/diff36'] = n2165
        # sudoku/blocks/block_2/diff34 -> n2166
        n2166 = self.context.mk_neq(n2162, n2163)
        self.nets['sudoku/blocks/block_2/diff34'] = n2166
        # sudoku/blocks/block_2/diff35 -> n2167
        n2167 = self.context.mk_neq(n2162, n2164)
        self.nets['sudoku/blocks/block_2/diff35'] = n2167
        # sudoku/blocks/block_2/Logical Operator6 -> n2168
        n2168 = self.context.mk_and(n2166, n2167)
        self.nets['sudoku/blocks/block_2/Logical Operator6'] = n2168
        # sudoku/blocks/block_2/diff31 -> n2169
        n2169 = self.context.mk_neq(n2161, n2162)
        self.nets['sudoku/blocks/block_2/diff31'] = n2169
        # sudoku/blocks/block_2/diff32 -> n2170
        n2170 = self.context.mk_neq(n2161, n2163)
        self.nets['sudoku/blocks/block_2/diff32'] = n2170
        # sudoku/blocks/block_2/diff33 -> n2171
        n2171 = self.context.mk_neq(n2161, n2164)
        self.nets['sudoku/blocks/block_2/diff33'] = n2171
        # sudoku/blocks/block_2/Logical Operator5 -> n2172
        tn501 = self.context.mk_and(n2170, n2171)
        n2172 = self.context.mk_and(n2169, tn501)
        self.nets['sudoku/blocks/block_2/Logical Operator5'] = n2172
        # sudoku/blocks/block_2/diff27 -> n2173
        n2173 = self.context.mk_neq(n2160, n2161)
        self.nets['sudoku/blocks/block_2/diff27'] = n2173
        # sudoku/blocks/block_2/diff28 -> n2174
        n2174 = self.context.mk_neq(n2160, n2162)
        self.nets['sudoku/blocks/block_2/diff28'] = n2174
        # sudoku/blocks/block_2/diff29 -> n2175
        n2175 = self.context.mk_neq(n2160, n2163)
        self.nets['sudoku/blocks/block_2/diff29'] = n2175
        # sudoku/blocks/block_2/diff30 -> n2176
        n2176 = self.context.mk_neq(n2160, n2164)
        self.nets['sudoku/blocks/block_2/diff30'] = n2176
        # sudoku/blocks/block_2/Logical Operator4 -> n2177
        tn503 = self.context.mk_and(n2175, n2176)
        tn502 = self.context.mk_and(n2174, tn503)
        n2177 = self.context.mk_and(n2173, tn502)
        self.nets['sudoku/blocks/block_2/Logical Operator4'] = n2177
        # sudoku/blocks/block_2/diff22 -> n2178
        n2178 = self.context.mk_neq(n2159, n2160)
        self.nets['sudoku/blocks/block_2/diff22'] = n2178
        # sudoku/blocks/block_2/diff23 -> n2179
        n2179 = self.context.mk_neq(n2159, n2161)
        self.nets['sudoku/blocks/block_2/diff23'] = n2179
        # sudoku/blocks/block_2/diff24 -> n2180
        n2180 = self.context.mk_neq(n2159, n2162)
        self.nets['sudoku/blocks/block_2/diff24'] = n2180
        # sudoku/blocks/block_2/diff25 -> n2181
        n2181 = self.context.mk_neq(n2159, n2163)
        self.nets['sudoku/blocks/block_2/diff25'] = n2181
        # sudoku/blocks/block_2/diff26 -> n2182
        n2182 = self.context.mk_neq(n2159, n2164)
        self.nets['sudoku/blocks/block_2/diff26'] = n2182
        # sudoku/blocks/block_2/Logical Operator3 -> n2183
        tn506 = self.context.mk_and(n2181, n2182)
        tn505 = self.context.mk_and(n2180, tn506)
        tn504 = self.context.mk_and(n2179, tn505)
        n2183 = self.context.mk_and(n2178, tn504)
        self.nets['sudoku/blocks/block_2/Logical Operator3'] = n2183
        # sudoku/blocks/block_2/diff16 -> n2184
        n2184 = self.context.mk_neq(n2158, n2159)
        self.nets['sudoku/blocks/block_2/diff16'] = n2184
        # sudoku/blocks/block_2/diff17 -> n2185
        n2185 = self.context.mk_neq(n2158, n2160)
        self.nets['sudoku/blocks/block_2/diff17'] = n2185
        # sudoku/blocks/block_2/diff18 -> n2186
        n2186 = self.context.mk_neq(n2158, n2161)
        self.nets['sudoku/blocks/block_2/diff18'] = n2186
        # sudoku/blocks/block_2/diff19 -> n2187
        n2187 = self.context.mk_neq(n2158, n2162)
        self.nets['sudoku/blocks/block_2/diff19'] = n2187
        # sudoku/blocks/block_2/diff20 -> n2188
        n2188 = self.context.mk_neq(n2158, n2163)
        self.nets['sudoku/blocks/block_2/diff20'] = n2188
        # sudoku/blocks/block_2/diff21 -> n2189
        n2189 = self.context.mk_neq(n2158, n2164)
        self.nets['sudoku/blocks/block_2/diff21'] = n2189
        # sudoku/blocks/block_2/Logical Operator2 -> n2190
        tn510 = self.context.mk_and(n2188, n2189)
        tn509 = self.context.mk_and(n2187, tn510)
        tn508 = self.context.mk_and(n2186, tn509)
        tn507 = self.context.mk_and(n2185, tn508)
        n2190 = self.context.mk_and(n2184, tn507)
        self.nets['sudoku/blocks/block_2/Logical Operator2'] = n2190
        # sudoku/blocks/block_2/diff9 -> n2191
        n2191 = self.context.mk_neq(n2157, n2158)
        self.nets['sudoku/blocks/block_2/diff9'] = n2191
        # sudoku/blocks/block_2/diff10 -> n2192
        n2192 = self.context.mk_neq(n2157, n2159)
        self.nets['sudoku/blocks/block_2/diff10'] = n2192
        # sudoku/blocks/block_2/diff11 -> n2193
        n2193 = self.context.mk_neq(n2157, n2160)
        self.nets['sudoku/blocks/block_2/diff11'] = n2193
        # sudoku/blocks/block_2/diff12 -> n2194
        n2194 = self.context.mk_neq(n2157, n2161)
        self.nets['sudoku/blocks/block_2/diff12'] = n2194
        # sudoku/blocks/block_2/diff13 -> n2195
        n2195 = self.context.mk_neq(n2157, n2162)
        self.nets['sudoku/blocks/block_2/diff13'] = n2195
        # sudoku/blocks/block_2/diff14 -> n2196
        n2196 = self.context.mk_neq(n2157, n2163)
        self.nets['sudoku/blocks/block_2/diff14'] = n2196
        # sudoku/blocks/block_2/diff15 -> n2197
        n2197 = self.context.mk_neq(n2157, n2164)
        self.nets['sudoku/blocks/block_2/diff15'] = n2197
        # sudoku/blocks/block_2/Logical Operator1 -> n2198
        tn515 = self.context.mk_and(n2196, n2197)
        tn514 = self.context.mk_and(n2195, tn515)
        tn513 = self.context.mk_and(n2194, tn514)
        tn512 = self.context.mk_and(n2193, tn513)
        tn511 = self.context.mk_and(n2192, tn512)
        n2198 = self.context.mk_and(n2191, tn511)
        self.nets['sudoku/blocks/block_2/Logical Operator1'] = n2198
        # sudoku/blocks/block_2/diff1 -> n2199
        n2199 = self.context.mk_neq(n2156, n2157)
        self.nets['sudoku/blocks/block_2/diff1'] = n2199
        # sudoku/blocks/block_2/diff2 -> n2200
        n2200 = self.context.mk_neq(n2156, n2158)
        self.nets['sudoku/blocks/block_2/diff2'] = n2200
        # sudoku/blocks/block_2/diff3 -> n2201
        n2201 = self.context.mk_neq(n2156, n2159)
        self.nets['sudoku/blocks/block_2/diff3'] = n2201
        # sudoku/blocks/block_2/diff4 -> n2202
        n2202 = self.context.mk_neq(n2156, n2160)
        self.nets['sudoku/blocks/block_2/diff4'] = n2202
        # sudoku/blocks/block_2/diff5 -> n2203
        n2203 = self.context.mk_neq(n2156, n2161)
        self.nets['sudoku/blocks/block_2/diff5'] = n2203
        # sudoku/blocks/block_2/diff6 -> n2204
        n2204 = self.context.mk_neq(n2156, n2162)
        self.nets['sudoku/blocks/block_2/diff6'] = n2204
        # sudoku/blocks/block_2/diff7 -> n2205
        n2205 = self.context.mk_neq(n2156, n2163)
        self.nets['sudoku/blocks/block_2/diff7'] = n2205
        # sudoku/blocks/block_2/diff8 -> n2206
        n2206 = self.context.mk_neq(n2156, n2164)
        self.nets['sudoku/blocks/block_2/diff8'] = n2206
        # sudoku/blocks/block_2/Logical Operator -> n2207
        tn521 = self.context.mk_and(n2205, n2206)
        tn520 = self.context.mk_and(n2204, tn521)
        tn519 = self.context.mk_and(n2203, tn520)
        tn518 = self.context.mk_and(n2202, tn519)
        tn517 = self.context.mk_and(n2201, tn518)
        tn516 = self.context.mk_and(n2200, tn517)
        n2207 = self.context.mk_and(n2199, tn516)
        self.nets['sudoku/blocks/block_2/Logical Operator'] = n2207
        # sudoku/blocks/block_2/Logical Operator7 -> n2208
        tn527 = self.context.mk_and(n2198, n2207)
        tn526 = self.context.mk_and(n2190, tn527)
        tn525 = self.context.mk_and(n2183, tn526)
        tn524 = self.context.mk_and(n2177, tn525)
        tn523 = self.context.mk_and(n2172, tn524)
        tn522 = self.context.mk_and(n2168, tn523)
        n2208 = self.context.mk_and(n2165, tn522)
        self.nets['sudoku/blocks/block_2/Logical Operator7'] = n2208
        # n2208 -> Out1
        return n2208

    def block_3(self, n2210, n2211, n2212, n2213, n2214, n2215, n2216, n2217, n2218):
        # In1 -> n2210
        # In2 -> n2211
        # In3 -> n2212
        # In4 -> n2213
        # In5 -> n2214
        # In6 -> n2215
        # In7 -> n2216
        # In8 -> n2217
        # In9 -> n2218
        # sudoku/blocks/block_3/diff36 -> n2219
        n2219 = self.context.mk_neq(n2217, n2218)
        self.nets['sudoku/blocks/block_3/diff36'] = n2219
        # sudoku/blocks/block_3/diff34 -> n2220
        n2220 = self.context.mk_neq(n2216, n2217)
        self.nets['sudoku/blocks/block_3/diff34'] = n2220
        # sudoku/blocks/block_3/diff35 -> n2221
        n2221 = self.context.mk_neq(n2216, n2218)
        self.nets['sudoku/blocks/block_3/diff35'] = n2221
        # sudoku/blocks/block_3/Logical Operator6 -> n2222
        n2222 = self.context.mk_and(n2220, n2221)
        self.nets['sudoku/blocks/block_3/Logical Operator6'] = n2222
        # sudoku/blocks/block_3/diff31 -> n2223
        n2223 = self.context.mk_neq(n2215, n2216)
        self.nets['sudoku/blocks/block_3/diff31'] = n2223
        # sudoku/blocks/block_3/diff32 -> n2224
        n2224 = self.context.mk_neq(n2215, n2217)
        self.nets['sudoku/blocks/block_3/diff32'] = n2224
        # sudoku/blocks/block_3/diff33 -> n2225
        n2225 = self.context.mk_neq(n2215, n2218)
        self.nets['sudoku/blocks/block_3/diff33'] = n2225
        # sudoku/blocks/block_3/Logical Operator5 -> n2226
        tn528 = self.context.mk_and(n2224, n2225)
        n2226 = self.context.mk_and(n2223, tn528)
        self.nets['sudoku/blocks/block_3/Logical Operator5'] = n2226
        # sudoku/blocks/block_3/diff27 -> n2227
        n2227 = self.context.mk_neq(n2214, n2215)
        self.nets['sudoku/blocks/block_3/diff27'] = n2227
        # sudoku/blocks/block_3/diff28 -> n2228
        n2228 = self.context.mk_neq(n2214, n2216)
        self.nets['sudoku/blocks/block_3/diff28'] = n2228
        # sudoku/blocks/block_3/diff29 -> n2229
        n2229 = self.context.mk_neq(n2214, n2217)
        self.nets['sudoku/blocks/block_3/diff29'] = n2229
        # sudoku/blocks/block_3/diff30 -> n2230
        n2230 = self.context.mk_neq(n2214, n2218)
        self.nets['sudoku/blocks/block_3/diff30'] = n2230
        # sudoku/blocks/block_3/Logical Operator4 -> n2231
        tn530 = self.context.mk_and(n2229, n2230)
        tn529 = self.context.mk_and(n2228, tn530)
        n2231 = self.context.mk_and(n2227, tn529)
        self.nets['sudoku/blocks/block_3/Logical Operator4'] = n2231
        # sudoku/blocks/block_3/diff22 -> n2232
        n2232 = self.context.mk_neq(n2213, n2214)
        self.nets['sudoku/blocks/block_3/diff22'] = n2232
        # sudoku/blocks/block_3/diff23 -> n2233
        n2233 = self.context.mk_neq(n2213, n2215)
        self.nets['sudoku/blocks/block_3/diff23'] = n2233
        # sudoku/blocks/block_3/diff24 -> n2234
        n2234 = self.context.mk_neq(n2213, n2216)
        self.nets['sudoku/blocks/block_3/diff24'] = n2234
        # sudoku/blocks/block_3/diff25 -> n2235
        n2235 = self.context.mk_neq(n2213, n2217)
        self.nets['sudoku/blocks/block_3/diff25'] = n2235
        # sudoku/blocks/block_3/diff26 -> n2236
        n2236 = self.context.mk_neq(n2213, n2218)
        self.nets['sudoku/blocks/block_3/diff26'] = n2236
        # sudoku/blocks/block_3/Logical Operator3 -> n2237
        tn533 = self.context.mk_and(n2235, n2236)
        tn532 = self.context.mk_and(n2234, tn533)
        tn531 = self.context.mk_and(n2233, tn532)
        n2237 = self.context.mk_and(n2232, tn531)
        self.nets['sudoku/blocks/block_3/Logical Operator3'] = n2237
        # sudoku/blocks/block_3/diff16 -> n2238
        n2238 = self.context.mk_neq(n2212, n2213)
        self.nets['sudoku/blocks/block_3/diff16'] = n2238
        # sudoku/blocks/block_3/diff17 -> n2239
        n2239 = self.context.mk_neq(n2212, n2214)
        self.nets['sudoku/blocks/block_3/diff17'] = n2239
        # sudoku/blocks/block_3/diff18 -> n2240
        n2240 = self.context.mk_neq(n2212, n2215)
        self.nets['sudoku/blocks/block_3/diff18'] = n2240
        # sudoku/blocks/block_3/diff19 -> n2241
        n2241 = self.context.mk_neq(n2212, n2216)
        self.nets['sudoku/blocks/block_3/diff19'] = n2241
        # sudoku/blocks/block_3/diff20 -> n2242
        n2242 = self.context.mk_neq(n2212, n2217)
        self.nets['sudoku/blocks/block_3/diff20'] = n2242
        # sudoku/blocks/block_3/diff21 -> n2243
        n2243 = self.context.mk_neq(n2212, n2218)
        self.nets['sudoku/blocks/block_3/diff21'] = n2243
        # sudoku/blocks/block_3/Logical Operator2 -> n2244
        tn537 = self.context.mk_and(n2242, n2243)
        tn536 = self.context.mk_and(n2241, tn537)
        tn535 = self.context.mk_and(n2240, tn536)
        tn534 = self.context.mk_and(n2239, tn535)
        n2244 = self.context.mk_and(n2238, tn534)
        self.nets['sudoku/blocks/block_3/Logical Operator2'] = n2244
        # sudoku/blocks/block_3/diff9 -> n2245
        n2245 = self.context.mk_neq(n2211, n2212)
        self.nets['sudoku/blocks/block_3/diff9'] = n2245
        # sudoku/blocks/block_3/diff10 -> n2246
        n2246 = self.context.mk_neq(n2211, n2213)
        self.nets['sudoku/blocks/block_3/diff10'] = n2246
        # sudoku/blocks/block_3/diff11 -> n2247
        n2247 = self.context.mk_neq(n2211, n2214)
        self.nets['sudoku/blocks/block_3/diff11'] = n2247
        # sudoku/blocks/block_3/diff12 -> n2248
        n2248 = self.context.mk_neq(n2211, n2215)
        self.nets['sudoku/blocks/block_3/diff12'] = n2248
        # sudoku/blocks/block_3/diff13 -> n2249
        n2249 = self.context.mk_neq(n2211, n2216)
        self.nets['sudoku/blocks/block_3/diff13'] = n2249
        # sudoku/blocks/block_3/diff14 -> n2250
        n2250 = self.context.mk_neq(n2211, n2217)
        self.nets['sudoku/blocks/block_3/diff14'] = n2250
        # sudoku/blocks/block_3/diff15 -> n2251
        n2251 = self.context.mk_neq(n2211, n2218)
        self.nets['sudoku/blocks/block_3/diff15'] = n2251
        # sudoku/blocks/block_3/Logical Operator1 -> n2252
        tn542 = self.context.mk_and(n2250, n2251)
        tn541 = self.context.mk_and(n2249, tn542)
        tn540 = self.context.mk_and(n2248, tn541)
        tn539 = self.context.mk_and(n2247, tn540)
        tn538 = self.context.mk_and(n2246, tn539)
        n2252 = self.context.mk_and(n2245, tn538)
        self.nets['sudoku/blocks/block_3/Logical Operator1'] = n2252
        # sudoku/blocks/block_3/diff1 -> n2253
        n2253 = self.context.mk_neq(n2210, n2211)
        self.nets['sudoku/blocks/block_3/diff1'] = n2253
        # sudoku/blocks/block_3/diff2 -> n2254
        n2254 = self.context.mk_neq(n2210, n2212)
        self.nets['sudoku/blocks/block_3/diff2'] = n2254
        # sudoku/blocks/block_3/diff3 -> n2255
        n2255 = self.context.mk_neq(n2210, n2213)
        self.nets['sudoku/blocks/block_3/diff3'] = n2255
        # sudoku/blocks/block_3/diff4 -> n2256
        n2256 = self.context.mk_neq(n2210, n2214)
        self.nets['sudoku/blocks/block_3/diff4'] = n2256
        # sudoku/blocks/block_3/diff5 -> n2257
        n2257 = self.context.mk_neq(n2210, n2215)
        self.nets['sudoku/blocks/block_3/diff5'] = n2257
        # sudoku/blocks/block_3/diff6 -> n2258
        n2258 = self.context.mk_neq(n2210, n2216)
        self.nets['sudoku/blocks/block_3/diff6'] = n2258
        # sudoku/blocks/block_3/diff7 -> n2259
        n2259 = self.context.mk_neq(n2210, n2217)
        self.nets['sudoku/blocks/block_3/diff7'] = n2259
        # sudoku/blocks/block_3/diff8 -> n2260
        n2260 = self.context.mk_neq(n2210, n2218)
        self.nets['sudoku/blocks/block_3/diff8'] = n2260
        # sudoku/blocks/block_3/Logical Operator -> n2261
        tn548 = self.context.mk_and(n2259, n2260)
        tn547 = self.context.mk_and(n2258, tn548)
        tn546 = self.context.mk_and(n2257, tn547)
        tn545 = self.context.mk_and(n2256, tn546)
        tn544 = self.context.mk_and(n2255, tn545)
        tn543 = self.context.mk_and(n2254, tn544)
        n2261 = self.context.mk_and(n2253, tn543)
        self.nets['sudoku/blocks/block_3/Logical Operator'] = n2261
        # sudoku/blocks/block_3/Logical Operator7 -> n2262
        tn554 = self.context.mk_and(n2252, n2261)
        tn553 = self.context.mk_and(n2244, tn554)
        tn552 = self.context.mk_and(n2237, tn553)
        tn551 = self.context.mk_and(n2231, tn552)
        tn550 = self.context.mk_and(n2226, tn551)
        tn549 = self.context.mk_and(n2222, tn550)
        n2262 = self.context.mk_and(n2219, tn549)
        self.nets['sudoku/blocks/block_3/Logical Operator7'] = n2262
        # n2262 -> Out1
        return n2262

    def block_4(self, n2264, n2265, n2266, n2267, n2268, n2269, n2270, n2271, n2272):
        # In1 -> n2264
        # In2 -> n2265
        # In3 -> n2266
        # In4 -> n2267
        # In5 -> n2268
        # In6 -> n2269
        # In7 -> n2270
        # In8 -> n2271
        # In9 -> n2272
        # sudoku/blocks/block_4/diff36 -> n2273
        n2273 = self.context.mk_neq(n2271, n2272)
        self.nets['sudoku/blocks/block_4/diff36'] = n2273
        # sudoku/blocks/block_4/diff34 -> n2274
        n2274 = self.context.mk_neq(n2270, n2271)
        self.nets['sudoku/blocks/block_4/diff34'] = n2274
        # sudoku/blocks/block_4/diff35 -> n2275
        n2275 = self.context.mk_neq(n2270, n2272)
        self.nets['sudoku/blocks/block_4/diff35'] = n2275
        # sudoku/blocks/block_4/Logical Operator6 -> n2276
        n2276 = self.context.mk_and(n2274, n2275)
        self.nets['sudoku/blocks/block_4/Logical Operator6'] = n2276
        # sudoku/blocks/block_4/diff31 -> n2277
        n2277 = self.context.mk_neq(n2269, n2270)
        self.nets['sudoku/blocks/block_4/diff31'] = n2277
        # sudoku/blocks/block_4/diff32 -> n2278
        n2278 = self.context.mk_neq(n2269, n2271)
        self.nets['sudoku/blocks/block_4/diff32'] = n2278
        # sudoku/blocks/block_4/diff33 -> n2279
        n2279 = self.context.mk_neq(n2269, n2272)
        self.nets['sudoku/blocks/block_4/diff33'] = n2279
        # sudoku/blocks/block_4/Logical Operator5 -> n2280
        tn555 = self.context.mk_and(n2278, n2279)
        n2280 = self.context.mk_and(n2277, tn555)
        self.nets['sudoku/blocks/block_4/Logical Operator5'] = n2280
        # sudoku/blocks/block_4/diff27 -> n2281
        n2281 = self.context.mk_neq(n2268, n2269)
        self.nets['sudoku/blocks/block_4/diff27'] = n2281
        # sudoku/blocks/block_4/diff28 -> n2282
        n2282 = self.context.mk_neq(n2268, n2270)
        self.nets['sudoku/blocks/block_4/diff28'] = n2282
        # sudoku/blocks/block_4/diff29 -> n2283
        n2283 = self.context.mk_neq(n2268, n2271)
        self.nets['sudoku/blocks/block_4/diff29'] = n2283
        # sudoku/blocks/block_4/diff30 -> n2284
        n2284 = self.context.mk_neq(n2268, n2272)
        self.nets['sudoku/blocks/block_4/diff30'] = n2284
        # sudoku/blocks/block_4/Logical Operator4 -> n2285
        tn557 = self.context.mk_and(n2283, n2284)
        tn556 = self.context.mk_and(n2282, tn557)
        n2285 = self.context.mk_and(n2281, tn556)
        self.nets['sudoku/blocks/block_4/Logical Operator4'] = n2285
        # sudoku/blocks/block_4/diff22 -> n2286
        n2286 = self.context.mk_neq(n2267, n2268)
        self.nets['sudoku/blocks/block_4/diff22'] = n2286
        # sudoku/blocks/block_4/diff23 -> n2287
        n2287 = self.context.mk_neq(n2267, n2269)
        self.nets['sudoku/blocks/block_4/diff23'] = n2287
        # sudoku/blocks/block_4/diff24 -> n2288
        n2288 = self.context.mk_neq(n2267, n2270)
        self.nets['sudoku/blocks/block_4/diff24'] = n2288
        # sudoku/blocks/block_4/diff25 -> n2289
        n2289 = self.context.mk_neq(n2267, n2271)
        self.nets['sudoku/blocks/block_4/diff25'] = n2289
        # sudoku/blocks/block_4/diff26 -> n2290
        n2290 = self.context.mk_neq(n2267, n2272)
        self.nets['sudoku/blocks/block_4/diff26'] = n2290
        # sudoku/blocks/block_4/Logical Operator3 -> n2291
        tn560 = self.context.mk_and(n2289, n2290)
        tn559 = self.context.mk_and(n2288, tn560)
        tn558 = self.context.mk_and(n2287, tn559)
        n2291 = self.context.mk_and(n2286, tn558)
        self.nets['sudoku/blocks/block_4/Logical Operator3'] = n2291
        # sudoku/blocks/block_4/diff16 -> n2292
        n2292 = self.context.mk_neq(n2266, n2267)
        self.nets['sudoku/blocks/block_4/diff16'] = n2292
        # sudoku/blocks/block_4/diff17 -> n2293
        n2293 = self.context.mk_neq(n2266, n2268)
        self.nets['sudoku/blocks/block_4/diff17'] = n2293
        # sudoku/blocks/block_4/diff18 -> n2294
        n2294 = self.context.mk_neq(n2266, n2269)
        self.nets['sudoku/blocks/block_4/diff18'] = n2294
        # sudoku/blocks/block_4/diff19 -> n2295
        n2295 = self.context.mk_neq(n2266, n2270)
        self.nets['sudoku/blocks/block_4/diff19'] = n2295
        # sudoku/blocks/block_4/diff20 -> n2296
        n2296 = self.context.mk_neq(n2266, n2271)
        self.nets['sudoku/blocks/block_4/diff20'] = n2296
        # sudoku/blocks/block_4/diff21 -> n2297
        n2297 = self.context.mk_neq(n2266, n2272)
        self.nets['sudoku/blocks/block_4/diff21'] = n2297
        # sudoku/blocks/block_4/Logical Operator2 -> n2298
        tn564 = self.context.mk_and(n2296, n2297)
        tn563 = self.context.mk_and(n2295, tn564)
        tn562 = self.context.mk_and(n2294, tn563)
        tn561 = self.context.mk_and(n2293, tn562)
        n2298 = self.context.mk_and(n2292, tn561)
        self.nets['sudoku/blocks/block_4/Logical Operator2'] = n2298
        # sudoku/blocks/block_4/diff9 -> n2299
        n2299 = self.context.mk_neq(n2265, n2266)
        self.nets['sudoku/blocks/block_4/diff9'] = n2299
        # sudoku/blocks/block_4/diff10 -> n2300
        n2300 = self.context.mk_neq(n2265, n2267)
        self.nets['sudoku/blocks/block_4/diff10'] = n2300
        # sudoku/blocks/block_4/diff11 -> n2301
        n2301 = self.context.mk_neq(n2265, n2268)
        self.nets['sudoku/blocks/block_4/diff11'] = n2301
        # sudoku/blocks/block_4/diff12 -> n2302
        n2302 = self.context.mk_neq(n2265, n2269)
        self.nets['sudoku/blocks/block_4/diff12'] = n2302
        # sudoku/blocks/block_4/diff13 -> n2303
        n2303 = self.context.mk_neq(n2265, n2270)
        self.nets['sudoku/blocks/block_4/diff13'] = n2303
        # sudoku/blocks/block_4/diff14 -> n2304
        n2304 = self.context.mk_neq(n2265, n2271)
        self.nets['sudoku/blocks/block_4/diff14'] = n2304
        # sudoku/blocks/block_4/diff15 -> n2305
        n2305 = self.context.mk_neq(n2265, n2272)
        self.nets['sudoku/blocks/block_4/diff15'] = n2305
        # sudoku/blocks/block_4/Logical Operator1 -> n2306
        tn569 = self.context.mk_and(n2304, n2305)
        tn568 = self.context.mk_and(n2303, tn569)
        tn567 = self.context.mk_and(n2302, tn568)
        tn566 = self.context.mk_and(n2301, tn567)
        tn565 = self.context.mk_and(n2300, tn566)
        n2306 = self.context.mk_and(n2299, tn565)
        self.nets['sudoku/blocks/block_4/Logical Operator1'] = n2306
        # sudoku/blocks/block_4/diff1 -> n2307
        n2307 = self.context.mk_neq(n2264, n2265)
        self.nets['sudoku/blocks/block_4/diff1'] = n2307
        # sudoku/blocks/block_4/diff2 -> n2308
        n2308 = self.context.mk_neq(n2264, n2266)
        self.nets['sudoku/blocks/block_4/diff2'] = n2308
        # sudoku/blocks/block_4/diff3 -> n2309
        n2309 = self.context.mk_neq(n2264, n2267)
        self.nets['sudoku/blocks/block_4/diff3'] = n2309
        # sudoku/blocks/block_4/diff4 -> n2310
        n2310 = self.context.mk_neq(n2264, n2268)
        self.nets['sudoku/blocks/block_4/diff4'] = n2310
        # sudoku/blocks/block_4/diff5 -> n2311
        n2311 = self.context.mk_neq(n2264, n2269)
        self.nets['sudoku/blocks/block_4/diff5'] = n2311
        # sudoku/blocks/block_4/diff6 -> n2312
        n2312 = self.context.mk_neq(n2264, n2270)
        self.nets['sudoku/blocks/block_4/diff6'] = n2312
        # sudoku/blocks/block_4/diff7 -> n2313
        n2313 = self.context.mk_neq(n2264, n2271)
        self.nets['sudoku/blocks/block_4/diff7'] = n2313
        # sudoku/blocks/block_4/diff8 -> n2314
        n2314 = self.context.mk_neq(n2264, n2272)
        self.nets['sudoku/blocks/block_4/diff8'] = n2314
        # sudoku/blocks/block_4/Logical Operator -> n2315
        tn575 = self.context.mk_and(n2313, n2314)
        tn574 = self.context.mk_and(n2312, tn575)
        tn573 = self.context.mk_and(n2311, tn574)
        tn572 = self.context.mk_and(n2310, tn573)
        tn571 = self.context.mk_and(n2309, tn572)
        tn570 = self.context.mk_and(n2308, tn571)
        n2315 = self.context.mk_and(n2307, tn570)
        self.nets['sudoku/blocks/block_4/Logical Operator'] = n2315
        # sudoku/blocks/block_4/Logical Operator7 -> n2316
        tn581 = self.context.mk_and(n2306, n2315)
        tn580 = self.context.mk_and(n2298, tn581)
        tn579 = self.context.mk_and(n2291, tn580)
        tn578 = self.context.mk_and(n2285, tn579)
        tn577 = self.context.mk_and(n2280, tn578)
        tn576 = self.context.mk_and(n2276, tn577)
        n2316 = self.context.mk_and(n2273, tn576)
        self.nets['sudoku/blocks/block_4/Logical Operator7'] = n2316
        # n2316 -> Out1
        return n2316

    def block_5(self, n2318, n2319, n2320, n2321, n2322, n2323, n2324, n2325, n2326):
        # In1 -> n2318
        # In2 -> n2319
        # In3 -> n2320
        # In4 -> n2321
        # In5 -> n2322
        # In6 -> n2323
        # In7 -> n2324
        # In8 -> n2325
        # In9 -> n2326
        # sudoku/blocks/block_5/diff36 -> n2327
        n2327 = self.context.mk_neq(n2325, n2326)
        self.nets['sudoku/blocks/block_5/diff36'] = n2327
        # sudoku/blocks/block_5/diff34 -> n2328
        n2328 = self.context.mk_neq(n2324, n2325)
        self.nets['sudoku/blocks/block_5/diff34'] = n2328
        # sudoku/blocks/block_5/diff35 -> n2329
        n2329 = self.context.mk_neq(n2324, n2326)
        self.nets['sudoku/blocks/block_5/diff35'] = n2329
        # sudoku/blocks/block_5/Logical Operator6 -> n2330
        n2330 = self.context.mk_and(n2328, n2329)
        self.nets['sudoku/blocks/block_5/Logical Operator6'] = n2330
        # sudoku/blocks/block_5/diff31 -> n2331
        n2331 = self.context.mk_neq(n2323, n2324)
        self.nets['sudoku/blocks/block_5/diff31'] = n2331
        # sudoku/blocks/block_5/diff32 -> n2332
        n2332 = self.context.mk_neq(n2323, n2325)
        self.nets['sudoku/blocks/block_5/diff32'] = n2332
        # sudoku/blocks/block_5/diff33 -> n2333
        n2333 = self.context.mk_neq(n2323, n2326)
        self.nets['sudoku/blocks/block_5/diff33'] = n2333
        # sudoku/blocks/block_5/Logical Operator5 -> n2334
        tn582 = self.context.mk_and(n2332, n2333)
        n2334 = self.context.mk_and(n2331, tn582)
        self.nets['sudoku/blocks/block_5/Logical Operator5'] = n2334
        # sudoku/blocks/block_5/diff27 -> n2335
        n2335 = self.context.mk_neq(n2322, n2323)
        self.nets['sudoku/blocks/block_5/diff27'] = n2335
        # sudoku/blocks/block_5/diff28 -> n2336
        n2336 = self.context.mk_neq(n2322, n2324)
        self.nets['sudoku/blocks/block_5/diff28'] = n2336
        # sudoku/blocks/block_5/diff29 -> n2337
        n2337 = self.context.mk_neq(n2322, n2325)
        self.nets['sudoku/blocks/block_5/diff29'] = n2337
        # sudoku/blocks/block_5/diff30 -> n2338
        n2338 = self.context.mk_neq(n2322, n2326)
        self.nets['sudoku/blocks/block_5/diff30'] = n2338
        # sudoku/blocks/block_5/Logical Operator4 -> n2339
        tn584 = self.context.mk_and(n2337, n2338)
        tn583 = self.context.mk_and(n2336, tn584)
        n2339 = self.context.mk_and(n2335, tn583)
        self.nets['sudoku/blocks/block_5/Logical Operator4'] = n2339
        # sudoku/blocks/block_5/diff22 -> n2340
        n2340 = self.context.mk_neq(n2321, n2322)
        self.nets['sudoku/blocks/block_5/diff22'] = n2340
        # sudoku/blocks/block_5/diff23 -> n2341
        n2341 = self.context.mk_neq(n2321, n2323)
        self.nets['sudoku/blocks/block_5/diff23'] = n2341
        # sudoku/blocks/block_5/diff24 -> n2342
        n2342 = self.context.mk_neq(n2321, n2324)
        self.nets['sudoku/blocks/block_5/diff24'] = n2342
        # sudoku/blocks/block_5/diff25 -> n2343
        n2343 = self.context.mk_neq(n2321, n2325)
        self.nets['sudoku/blocks/block_5/diff25'] = n2343
        # sudoku/blocks/block_5/diff26 -> n2344
        n2344 = self.context.mk_neq(n2321, n2326)
        self.nets['sudoku/blocks/block_5/diff26'] = n2344
        # sudoku/blocks/block_5/Logical Operator3 -> n2345
        tn587 = self.context.mk_and(n2343, n2344)
        tn586 = self.context.mk_and(n2342, tn587)
        tn585 = self.context.mk_and(n2341, tn586)
        n2345 = self.context.mk_and(n2340, tn585)
        self.nets['sudoku/blocks/block_5/Logical Operator3'] = n2345
        # sudoku/blocks/block_5/diff16 -> n2346
        n2346 = self.context.mk_neq(n2320, n2321)
        self.nets['sudoku/blocks/block_5/diff16'] = n2346
        # sudoku/blocks/block_5/diff17 -> n2347
        n2347 = self.context.mk_neq(n2320, n2322)
        self.nets['sudoku/blocks/block_5/diff17'] = n2347
        # sudoku/blocks/block_5/diff18 -> n2348
        n2348 = self.context.mk_neq(n2320, n2323)
        self.nets['sudoku/blocks/block_5/diff18'] = n2348
        # sudoku/blocks/block_5/diff19 -> n2349
        n2349 = self.context.mk_neq(n2320, n2324)
        self.nets['sudoku/blocks/block_5/diff19'] = n2349
        # sudoku/blocks/block_5/diff20 -> n2350
        n2350 = self.context.mk_neq(n2320, n2325)
        self.nets['sudoku/blocks/block_5/diff20'] = n2350
        # sudoku/blocks/block_5/diff21 -> n2351
        n2351 = self.context.mk_neq(n2320, n2326)
        self.nets['sudoku/blocks/block_5/diff21'] = n2351
        # sudoku/blocks/block_5/Logical Operator2 -> n2352
        tn591 = self.context.mk_and(n2350, n2351)
        tn590 = self.context.mk_and(n2349, tn591)
        tn589 = self.context.mk_and(n2348, tn590)
        tn588 = self.context.mk_and(n2347, tn589)
        n2352 = self.context.mk_and(n2346, tn588)
        self.nets['sudoku/blocks/block_5/Logical Operator2'] = n2352
        # sudoku/blocks/block_5/diff9 -> n2353
        n2353 = self.context.mk_neq(n2319, n2320)
        self.nets['sudoku/blocks/block_5/diff9'] = n2353
        # sudoku/blocks/block_5/diff10 -> n2354
        n2354 = self.context.mk_neq(n2319, n2321)
        self.nets['sudoku/blocks/block_5/diff10'] = n2354
        # sudoku/blocks/block_5/diff11 -> n2355
        n2355 = self.context.mk_neq(n2319, n2322)
        self.nets['sudoku/blocks/block_5/diff11'] = n2355
        # sudoku/blocks/block_5/diff12 -> n2356
        n2356 = self.context.mk_neq(n2319, n2323)
        self.nets['sudoku/blocks/block_5/diff12'] = n2356
        # sudoku/blocks/block_5/diff13 -> n2357
        n2357 = self.context.mk_neq(n2319, n2324)
        self.nets['sudoku/blocks/block_5/diff13'] = n2357
        # sudoku/blocks/block_5/diff14 -> n2358
        n2358 = self.context.mk_neq(n2319, n2325)
        self.nets['sudoku/blocks/block_5/diff14'] = n2358
        # sudoku/blocks/block_5/diff15 -> n2359
        n2359 = self.context.mk_neq(n2319, n2326)
        self.nets['sudoku/blocks/block_5/diff15'] = n2359
        # sudoku/blocks/block_5/Logical Operator1 -> n2360
        tn596 = self.context.mk_and(n2358, n2359)
        tn595 = self.context.mk_and(n2357, tn596)
        tn594 = self.context.mk_and(n2356, tn595)
        tn593 = self.context.mk_and(n2355, tn594)
        tn592 = self.context.mk_and(n2354, tn593)
        n2360 = self.context.mk_and(n2353, tn592)
        self.nets['sudoku/blocks/block_5/Logical Operator1'] = n2360
        # sudoku/blocks/block_5/diff1 -> n2361
        n2361 = self.context.mk_neq(n2318, n2319)
        self.nets['sudoku/blocks/block_5/diff1'] = n2361
        # sudoku/blocks/block_5/diff2 -> n2362
        n2362 = self.context.mk_neq(n2318, n2320)
        self.nets['sudoku/blocks/block_5/diff2'] = n2362
        # sudoku/blocks/block_5/diff3 -> n2363
        n2363 = self.context.mk_neq(n2318, n2321)
        self.nets['sudoku/blocks/block_5/diff3'] = n2363
        # sudoku/blocks/block_5/diff4 -> n2364
        n2364 = self.context.mk_neq(n2318, n2322)
        self.nets['sudoku/blocks/block_5/diff4'] = n2364
        # sudoku/blocks/block_5/diff5 -> n2365
        n2365 = self.context.mk_neq(n2318, n2323)
        self.nets['sudoku/blocks/block_5/diff5'] = n2365
        # sudoku/blocks/block_5/diff6 -> n2366
        n2366 = self.context.mk_neq(n2318, n2324)
        self.nets['sudoku/blocks/block_5/diff6'] = n2366
        # sudoku/blocks/block_5/diff7 -> n2367
        n2367 = self.context.mk_neq(n2318, n2325)
        self.nets['sudoku/blocks/block_5/diff7'] = n2367
        # sudoku/blocks/block_5/diff8 -> n2368
        n2368 = self.context.mk_neq(n2318, n2326)
        self.nets['sudoku/blocks/block_5/diff8'] = n2368
        # sudoku/blocks/block_5/Logical Operator -> n2369
        tn602 = self.context.mk_and(n2367, n2368)
        tn601 = self.context.mk_and(n2366, tn602)
        tn600 = self.context.mk_and(n2365, tn601)
        tn599 = self.context.mk_and(n2364, tn600)
        tn598 = self.context.mk_and(n2363, tn599)
        tn597 = self.context.mk_and(n2362, tn598)
        n2369 = self.context.mk_and(n2361, tn597)
        self.nets['sudoku/blocks/block_5/Logical Operator'] = n2369
        # sudoku/blocks/block_5/Logical Operator7 -> n2370
        tn608 = self.context.mk_and(n2360, n2369)
        tn607 = self.context.mk_and(n2352, tn608)
        tn606 = self.context.mk_and(n2345, tn607)
        tn605 = self.context.mk_and(n2339, tn606)
        tn604 = self.context.mk_and(n2334, tn605)
        tn603 = self.context.mk_and(n2330, tn604)
        n2370 = self.context.mk_and(n2327, tn603)
        self.nets['sudoku/blocks/block_5/Logical Operator7'] = n2370
        # n2370 -> Out1
        return n2370

    def block_6(self, n2372, n2373, n2374, n2375, n2376, n2377, n2378, n2379, n2380):
        # In1 -> n2372
        # In2 -> n2373
        # In3 -> n2374
        # In4 -> n2375
        # In5 -> n2376
        # In6 -> n2377
        # In7 -> n2378
        # In8 -> n2379
        # In9 -> n2380
        # sudoku/blocks/block_6/diff36 -> n2381
        n2381 = self.context.mk_neq(n2379, n2380)
        self.nets['sudoku/blocks/block_6/diff36'] = n2381
        # sudoku/blocks/block_6/diff34 -> n2382
        n2382 = self.context.mk_neq(n2378, n2379)
        self.nets['sudoku/blocks/block_6/diff34'] = n2382
        # sudoku/blocks/block_6/diff35 -> n2383
        n2383 = self.context.mk_neq(n2378, n2380)
        self.nets['sudoku/blocks/block_6/diff35'] = n2383
        # sudoku/blocks/block_6/Logical Operator6 -> n2384
        n2384 = self.context.mk_and(n2382, n2383)
        self.nets['sudoku/blocks/block_6/Logical Operator6'] = n2384
        # sudoku/blocks/block_6/diff31 -> n2385
        n2385 = self.context.mk_neq(n2377, n2378)
        self.nets['sudoku/blocks/block_6/diff31'] = n2385
        # sudoku/blocks/block_6/diff32 -> n2386
        n2386 = self.context.mk_neq(n2377, n2379)
        self.nets['sudoku/blocks/block_6/diff32'] = n2386
        # sudoku/blocks/block_6/diff33 -> n2387
        n2387 = self.context.mk_neq(n2377, n2380)
        self.nets['sudoku/blocks/block_6/diff33'] = n2387
        # sudoku/blocks/block_6/Logical Operator5 -> n2388
        tn609 = self.context.mk_and(n2386, n2387)
        n2388 = self.context.mk_and(n2385, tn609)
        self.nets['sudoku/blocks/block_6/Logical Operator5'] = n2388
        # sudoku/blocks/block_6/diff27 -> n2389
        n2389 = self.context.mk_neq(n2376, n2377)
        self.nets['sudoku/blocks/block_6/diff27'] = n2389
        # sudoku/blocks/block_6/diff28 -> n2390
        n2390 = self.context.mk_neq(n2376, n2378)
        self.nets['sudoku/blocks/block_6/diff28'] = n2390
        # sudoku/blocks/block_6/diff29 -> n2391
        n2391 = self.context.mk_neq(n2376, n2379)
        self.nets['sudoku/blocks/block_6/diff29'] = n2391
        # sudoku/blocks/block_6/diff30 -> n2392
        n2392 = self.context.mk_neq(n2376, n2380)
        self.nets['sudoku/blocks/block_6/diff30'] = n2392
        # sudoku/blocks/block_6/Logical Operator4 -> n2393
        tn611 = self.context.mk_and(n2391, n2392)
        tn610 = self.context.mk_and(n2390, tn611)
        n2393 = self.context.mk_and(n2389, tn610)
        self.nets['sudoku/blocks/block_6/Logical Operator4'] = n2393
        # sudoku/blocks/block_6/diff22 -> n2394
        n2394 = self.context.mk_neq(n2375, n2376)
        self.nets['sudoku/blocks/block_6/diff22'] = n2394
        # sudoku/blocks/block_6/diff23 -> n2395
        n2395 = self.context.mk_neq(n2375, n2377)
        self.nets['sudoku/blocks/block_6/diff23'] = n2395
        # sudoku/blocks/block_6/diff24 -> n2396
        n2396 = self.context.mk_neq(n2375, n2378)
        self.nets['sudoku/blocks/block_6/diff24'] = n2396
        # sudoku/blocks/block_6/diff25 -> n2397
        n2397 = self.context.mk_neq(n2375, n2379)
        self.nets['sudoku/blocks/block_6/diff25'] = n2397
        # sudoku/blocks/block_6/diff26 -> n2398
        n2398 = self.context.mk_neq(n2375, n2380)
        self.nets['sudoku/blocks/block_6/diff26'] = n2398
        # sudoku/blocks/block_6/Logical Operator3 -> n2399
        tn614 = self.context.mk_and(n2397, n2398)
        tn613 = self.context.mk_and(n2396, tn614)
        tn612 = self.context.mk_and(n2395, tn613)
        n2399 = self.context.mk_and(n2394, tn612)
        self.nets['sudoku/blocks/block_6/Logical Operator3'] = n2399
        # sudoku/blocks/block_6/diff16 -> n2400
        n2400 = self.context.mk_neq(n2374, n2375)
        self.nets['sudoku/blocks/block_6/diff16'] = n2400
        # sudoku/blocks/block_6/diff17 -> n2401
        n2401 = self.context.mk_neq(n2374, n2376)
        self.nets['sudoku/blocks/block_6/diff17'] = n2401
        # sudoku/blocks/block_6/diff18 -> n2402
        n2402 = self.context.mk_neq(n2374, n2377)
        self.nets['sudoku/blocks/block_6/diff18'] = n2402
        # sudoku/blocks/block_6/diff19 -> n2403
        n2403 = self.context.mk_neq(n2374, n2378)
        self.nets['sudoku/blocks/block_6/diff19'] = n2403
        # sudoku/blocks/block_6/diff20 -> n2404
        n2404 = self.context.mk_neq(n2374, n2379)
        self.nets['sudoku/blocks/block_6/diff20'] = n2404
        # sudoku/blocks/block_6/diff21 -> n2405
        n2405 = self.context.mk_neq(n2374, n2380)
        self.nets['sudoku/blocks/block_6/diff21'] = n2405
        # sudoku/blocks/block_6/Logical Operator2 -> n2406
        tn618 = self.context.mk_and(n2404, n2405)
        tn617 = self.context.mk_and(n2403, tn618)
        tn616 = self.context.mk_and(n2402, tn617)
        tn615 = self.context.mk_and(n2401, tn616)
        n2406 = self.context.mk_and(n2400, tn615)
        self.nets['sudoku/blocks/block_6/Logical Operator2'] = n2406
        # sudoku/blocks/block_6/diff9 -> n2407
        n2407 = self.context.mk_neq(n2373, n2374)
        self.nets['sudoku/blocks/block_6/diff9'] = n2407
        # sudoku/blocks/block_6/diff10 -> n2408
        n2408 = self.context.mk_neq(n2373, n2375)
        self.nets['sudoku/blocks/block_6/diff10'] = n2408
        # sudoku/blocks/block_6/diff11 -> n2409
        n2409 = self.context.mk_neq(n2373, n2376)
        self.nets['sudoku/blocks/block_6/diff11'] = n2409
        # sudoku/blocks/block_6/diff12 -> n2410
        n2410 = self.context.mk_neq(n2373, n2377)
        self.nets['sudoku/blocks/block_6/diff12'] = n2410
        # sudoku/blocks/block_6/diff13 -> n2411
        n2411 = self.context.mk_neq(n2373, n2378)
        self.nets['sudoku/blocks/block_6/diff13'] = n2411
        # sudoku/blocks/block_6/diff14 -> n2412
        n2412 = self.context.mk_neq(n2373, n2379)
        self.nets['sudoku/blocks/block_6/diff14'] = n2412
        # sudoku/blocks/block_6/diff15 -> n2413
        n2413 = self.context.mk_neq(n2373, n2380)
        self.nets['sudoku/blocks/block_6/diff15'] = n2413
        # sudoku/blocks/block_6/Logical Operator1 -> n2414
        tn623 = self.context.mk_and(n2412, n2413)
        tn622 = self.context.mk_and(n2411, tn623)
        tn621 = self.context.mk_and(n2410, tn622)
        tn620 = self.context.mk_and(n2409, tn621)
        tn619 = self.context.mk_and(n2408, tn620)
        n2414 = self.context.mk_and(n2407, tn619)
        self.nets['sudoku/blocks/block_6/Logical Operator1'] = n2414
        # sudoku/blocks/block_6/diff1 -> n2415
        n2415 = self.context.mk_neq(n2372, n2373)
        self.nets['sudoku/blocks/block_6/diff1'] = n2415
        # sudoku/blocks/block_6/diff2 -> n2416
        n2416 = self.context.mk_neq(n2372, n2374)
        self.nets['sudoku/blocks/block_6/diff2'] = n2416
        # sudoku/blocks/block_6/diff3 -> n2417
        n2417 = self.context.mk_neq(n2372, n2375)
        self.nets['sudoku/blocks/block_6/diff3'] = n2417
        # sudoku/blocks/block_6/diff4 -> n2418
        n2418 = self.context.mk_neq(n2372, n2376)
        self.nets['sudoku/blocks/block_6/diff4'] = n2418
        # sudoku/blocks/block_6/diff5 -> n2419
        n2419 = self.context.mk_neq(n2372, n2377)
        self.nets['sudoku/blocks/block_6/diff5'] = n2419
        # sudoku/blocks/block_6/diff6 -> n2420
        n2420 = self.context.mk_neq(n2372, n2378)
        self.nets['sudoku/blocks/block_6/diff6'] = n2420
        # sudoku/blocks/block_6/diff7 -> n2421
        n2421 = self.context.mk_neq(n2372, n2379)
        self.nets['sudoku/blocks/block_6/diff7'] = n2421
        # sudoku/blocks/block_6/diff8 -> n2422
        n2422 = self.context.mk_neq(n2372, n2380)
        self.nets['sudoku/blocks/block_6/diff8'] = n2422
        # sudoku/blocks/block_6/Logical Operator -> n2423
        tn629 = self.context.mk_and(n2421, n2422)
        tn628 = self.context.mk_and(n2420, tn629)
        tn627 = self.context.mk_and(n2419, tn628)
        tn626 = self.context.mk_and(n2418, tn627)
        tn625 = self.context.mk_and(n2417, tn626)
        tn624 = self.context.mk_and(n2416, tn625)
        n2423 = self.context.mk_and(n2415, tn624)
        self.nets['sudoku/blocks/block_6/Logical Operator'] = n2423
        # sudoku/blocks/block_6/Logical Operator7 -> n2424
        tn635 = self.context.mk_and(n2414, n2423)
        tn634 = self.context.mk_and(n2406, tn635)
        tn633 = self.context.mk_and(n2399, tn634)
        tn632 = self.context.mk_and(n2393, tn633)
        tn631 = self.context.mk_and(n2388, tn632)
        tn630 = self.context.mk_and(n2384, tn631)
        n2424 = self.context.mk_and(n2381, tn630)
        self.nets['sudoku/blocks/block_6/Logical Operator7'] = n2424
        # n2424 -> Out1
        return n2424

    def block_7(self, n2426, n2427, n2428, n2429, n2430, n2431, n2432, n2433, n2434):
        # In1 -> n2426
        # In2 -> n2427
        # In3 -> n2428
        # In4 -> n2429
        # In5 -> n2430
        # In6 -> n2431
        # In7 -> n2432
        # In8 -> n2433
        # In9 -> n2434
        # sudoku/blocks/block_7/diff36 -> n2435
        n2435 = self.context.mk_neq(n2433, n2434)
        self.nets['sudoku/blocks/block_7/diff36'] = n2435
        # sudoku/blocks/block_7/diff34 -> n2436
        n2436 = self.context.mk_neq(n2432, n2433)
        self.nets['sudoku/blocks/block_7/diff34'] = n2436
        # sudoku/blocks/block_7/diff35 -> n2437
        n2437 = self.context.mk_neq(n2432, n2434)
        self.nets['sudoku/blocks/block_7/diff35'] = n2437
        # sudoku/blocks/block_7/Logical Operator6 -> n2438
        n2438 = self.context.mk_and(n2436, n2437)
        self.nets['sudoku/blocks/block_7/Logical Operator6'] = n2438
        # sudoku/blocks/block_7/diff31 -> n2439
        n2439 = self.context.mk_neq(n2431, n2432)
        self.nets['sudoku/blocks/block_7/diff31'] = n2439
        # sudoku/blocks/block_7/diff32 -> n2440
        n2440 = self.context.mk_neq(n2431, n2433)
        self.nets['sudoku/blocks/block_7/diff32'] = n2440
        # sudoku/blocks/block_7/diff33 -> n2441
        n2441 = self.context.mk_neq(n2431, n2434)
        self.nets['sudoku/blocks/block_7/diff33'] = n2441
        # sudoku/blocks/block_7/Logical Operator5 -> n2442
        tn636 = self.context.mk_and(n2440, n2441)
        n2442 = self.context.mk_and(n2439, tn636)
        self.nets['sudoku/blocks/block_7/Logical Operator5'] = n2442
        # sudoku/blocks/block_7/diff27 -> n2443
        n2443 = self.context.mk_neq(n2430, n2431)
        self.nets['sudoku/blocks/block_7/diff27'] = n2443
        # sudoku/blocks/block_7/diff28 -> n2444
        n2444 = self.context.mk_neq(n2430, n2432)
        self.nets['sudoku/blocks/block_7/diff28'] = n2444
        # sudoku/blocks/block_7/diff29 -> n2445
        n2445 = self.context.mk_neq(n2430, n2433)
        self.nets['sudoku/blocks/block_7/diff29'] = n2445
        # sudoku/blocks/block_7/diff30 -> n2446
        n2446 = self.context.mk_neq(n2430, n2434)
        self.nets['sudoku/blocks/block_7/diff30'] = n2446
        # sudoku/blocks/block_7/Logical Operator4 -> n2447
        tn638 = self.context.mk_and(n2445, n2446)
        tn637 = self.context.mk_and(n2444, tn638)
        n2447 = self.context.mk_and(n2443, tn637)
        self.nets['sudoku/blocks/block_7/Logical Operator4'] = n2447
        # sudoku/blocks/block_7/diff22 -> n2448
        n2448 = self.context.mk_neq(n2429, n2430)
        self.nets['sudoku/blocks/block_7/diff22'] = n2448
        # sudoku/blocks/block_7/diff23 -> n2449
        n2449 = self.context.mk_neq(n2429, n2431)
        self.nets['sudoku/blocks/block_7/diff23'] = n2449
        # sudoku/blocks/block_7/diff24 -> n2450
        n2450 = self.context.mk_neq(n2429, n2432)
        self.nets['sudoku/blocks/block_7/diff24'] = n2450
        # sudoku/blocks/block_7/diff25 -> n2451
        n2451 = self.context.mk_neq(n2429, n2433)
        self.nets['sudoku/blocks/block_7/diff25'] = n2451
        # sudoku/blocks/block_7/diff26 -> n2452
        n2452 = self.context.mk_neq(n2429, n2434)
        self.nets['sudoku/blocks/block_7/diff26'] = n2452
        # sudoku/blocks/block_7/Logical Operator3 -> n2453
        tn641 = self.context.mk_and(n2451, n2452)
        tn640 = self.context.mk_and(n2450, tn641)
        tn639 = self.context.mk_and(n2449, tn640)
        n2453 = self.context.mk_and(n2448, tn639)
        self.nets['sudoku/blocks/block_7/Logical Operator3'] = n2453
        # sudoku/blocks/block_7/diff16 -> n2454
        n2454 = self.context.mk_neq(n2428, n2429)
        self.nets['sudoku/blocks/block_7/diff16'] = n2454
        # sudoku/blocks/block_7/diff17 -> n2455
        n2455 = self.context.mk_neq(n2428, n2430)
        self.nets['sudoku/blocks/block_7/diff17'] = n2455
        # sudoku/blocks/block_7/diff18 -> n2456
        n2456 = self.context.mk_neq(n2428, n2431)
        self.nets['sudoku/blocks/block_7/diff18'] = n2456
        # sudoku/blocks/block_7/diff19 -> n2457
        n2457 = self.context.mk_neq(n2428, n2432)
        self.nets['sudoku/blocks/block_7/diff19'] = n2457
        # sudoku/blocks/block_7/diff20 -> n2458
        n2458 = self.context.mk_neq(n2428, n2433)
        self.nets['sudoku/blocks/block_7/diff20'] = n2458
        # sudoku/blocks/block_7/diff21 -> n2459
        n2459 = self.context.mk_neq(n2428, n2434)
        self.nets['sudoku/blocks/block_7/diff21'] = n2459
        # sudoku/blocks/block_7/Logical Operator2 -> n2460
        tn645 = self.context.mk_and(n2458, n2459)
        tn644 = self.context.mk_and(n2457, tn645)
        tn643 = self.context.mk_and(n2456, tn644)
        tn642 = self.context.mk_and(n2455, tn643)
        n2460 = self.context.mk_and(n2454, tn642)
        self.nets['sudoku/blocks/block_7/Logical Operator2'] = n2460
        # sudoku/blocks/block_7/diff9 -> n2461
        n2461 = self.context.mk_neq(n2427, n2428)
        self.nets['sudoku/blocks/block_7/diff9'] = n2461
        # sudoku/blocks/block_7/diff10 -> n2462
        n2462 = self.context.mk_neq(n2427, n2429)
        self.nets['sudoku/blocks/block_7/diff10'] = n2462
        # sudoku/blocks/block_7/diff11 -> n2463
        n2463 = self.context.mk_neq(n2427, n2430)
        self.nets['sudoku/blocks/block_7/diff11'] = n2463
        # sudoku/blocks/block_7/diff12 -> n2464
        n2464 = self.context.mk_neq(n2427, n2431)
        self.nets['sudoku/blocks/block_7/diff12'] = n2464
        # sudoku/blocks/block_7/diff13 -> n2465
        n2465 = self.context.mk_neq(n2427, n2432)
        self.nets['sudoku/blocks/block_7/diff13'] = n2465
        # sudoku/blocks/block_7/diff14 -> n2466
        n2466 = self.context.mk_neq(n2427, n2433)
        self.nets['sudoku/blocks/block_7/diff14'] = n2466
        # sudoku/blocks/block_7/diff15 -> n2467
        n2467 = self.context.mk_neq(n2427, n2434)
        self.nets['sudoku/blocks/block_7/diff15'] = n2467
        # sudoku/blocks/block_7/Logical Operator1 -> n2468
        tn650 = self.context.mk_and(n2466, n2467)
        tn649 = self.context.mk_and(n2465, tn650)
        tn648 = self.context.mk_and(n2464, tn649)
        tn647 = self.context.mk_and(n2463, tn648)
        tn646 = self.context.mk_and(n2462, tn647)
        n2468 = self.context.mk_and(n2461, tn646)
        self.nets['sudoku/blocks/block_7/Logical Operator1'] = n2468
        # sudoku/blocks/block_7/diff1 -> n2469
        n2469 = self.context.mk_neq(n2426, n2427)
        self.nets['sudoku/blocks/block_7/diff1'] = n2469
        # sudoku/blocks/block_7/diff2 -> n2470
        n2470 = self.context.mk_neq(n2426, n2428)
        self.nets['sudoku/blocks/block_7/diff2'] = n2470
        # sudoku/blocks/block_7/diff3 -> n2471
        n2471 = self.context.mk_neq(n2426, n2429)
        self.nets['sudoku/blocks/block_7/diff3'] = n2471
        # sudoku/blocks/block_7/diff4 -> n2472
        n2472 = self.context.mk_neq(n2426, n2430)
        self.nets['sudoku/blocks/block_7/diff4'] = n2472
        # sudoku/blocks/block_7/diff5 -> n2473
        n2473 = self.context.mk_neq(n2426, n2431)
        self.nets['sudoku/blocks/block_7/diff5'] = n2473
        # sudoku/blocks/block_7/diff6 -> n2474
        n2474 = self.context.mk_neq(n2426, n2432)
        self.nets['sudoku/blocks/block_7/diff6'] = n2474
        # sudoku/blocks/block_7/diff7 -> n2475
        n2475 = self.context.mk_neq(n2426, n2433)
        self.nets['sudoku/blocks/block_7/diff7'] = n2475
        # sudoku/blocks/block_7/diff8 -> n2476
        n2476 = self.context.mk_neq(n2426, n2434)
        self.nets['sudoku/blocks/block_7/diff8'] = n2476
        # sudoku/blocks/block_7/Logical Operator -> n2477
        tn656 = self.context.mk_and(n2475, n2476)
        tn655 = self.context.mk_and(n2474, tn656)
        tn654 = self.context.mk_and(n2473, tn655)
        tn653 = self.context.mk_and(n2472, tn654)
        tn652 = self.context.mk_and(n2471, tn653)
        tn651 = self.context.mk_and(n2470, tn652)
        n2477 = self.context.mk_and(n2469, tn651)
        self.nets['sudoku/blocks/block_7/Logical Operator'] = n2477
        # sudoku/blocks/block_7/Logical Operator7 -> n2478
        tn662 = self.context.mk_and(n2468, n2477)
        tn661 = self.context.mk_and(n2460, tn662)
        tn660 = self.context.mk_and(n2453, tn661)
        tn659 = self.context.mk_and(n2447, tn660)
        tn658 = self.context.mk_and(n2442, tn659)
        tn657 = self.context.mk_and(n2438, tn658)
        n2478 = self.context.mk_and(n2435, tn657)
        self.nets['sudoku/blocks/block_7/Logical Operator7'] = n2478
        # n2478 -> Out1
        return n2478

    def block_8(self, n2480, n2481, n2482, n2483, n2484, n2485, n2486, n2487, n2488):
        # In1 -> n2480
        # In2 -> n2481
        # In3 -> n2482
        # In4 -> n2483
        # In5 -> n2484
        # In6 -> n2485
        # In7 -> n2486
        # In8 -> n2487
        # In9 -> n2488
        # sudoku/blocks/block_8/diff36 -> n2489
        n2489 = self.context.mk_neq(n2487, n2488)
        self.nets['sudoku/blocks/block_8/diff36'] = n2489
        # sudoku/blocks/block_8/diff34 -> n2490
        n2490 = self.context.mk_neq(n2486, n2487)
        self.nets['sudoku/blocks/block_8/diff34'] = n2490
        # sudoku/blocks/block_8/diff35 -> n2491
        n2491 = self.context.mk_neq(n2486, n2488)
        self.nets['sudoku/blocks/block_8/diff35'] = n2491
        # sudoku/blocks/block_8/Logical Operator6 -> n2492
        n2492 = self.context.mk_and(n2490, n2491)
        self.nets['sudoku/blocks/block_8/Logical Operator6'] = n2492
        # sudoku/blocks/block_8/diff31 -> n2493
        n2493 = self.context.mk_neq(n2485, n2486)
        self.nets['sudoku/blocks/block_8/diff31'] = n2493
        # sudoku/blocks/block_8/diff32 -> n2494
        n2494 = self.context.mk_neq(n2485, n2487)
        self.nets['sudoku/blocks/block_8/diff32'] = n2494
        # sudoku/blocks/block_8/diff33 -> n2495
        n2495 = self.context.mk_neq(n2485, n2488)
        self.nets['sudoku/blocks/block_8/diff33'] = n2495
        # sudoku/blocks/block_8/Logical Operator5 -> n2496
        tn663 = self.context.mk_and(n2494, n2495)
        n2496 = self.context.mk_and(n2493, tn663)
        self.nets['sudoku/blocks/block_8/Logical Operator5'] = n2496
        # sudoku/blocks/block_8/diff27 -> n2497
        n2497 = self.context.mk_neq(n2484, n2485)
        self.nets['sudoku/blocks/block_8/diff27'] = n2497
        # sudoku/blocks/block_8/diff28 -> n2498
        n2498 = self.context.mk_neq(n2484, n2486)
        self.nets['sudoku/blocks/block_8/diff28'] = n2498
        # sudoku/blocks/block_8/diff29 -> n2499
        n2499 = self.context.mk_neq(n2484, n2487)
        self.nets['sudoku/blocks/block_8/diff29'] = n2499
        # sudoku/blocks/block_8/diff30 -> n2500
        n2500 = self.context.mk_neq(n2484, n2488)
        self.nets['sudoku/blocks/block_8/diff30'] = n2500
        # sudoku/blocks/block_8/Logical Operator4 -> n2501
        tn665 = self.context.mk_and(n2499, n2500)
        tn664 = self.context.mk_and(n2498, tn665)
        n2501 = self.context.mk_and(n2497, tn664)
        self.nets['sudoku/blocks/block_8/Logical Operator4'] = n2501
        # sudoku/blocks/block_8/diff22 -> n2502
        n2502 = self.context.mk_neq(n2483, n2484)
        self.nets['sudoku/blocks/block_8/diff22'] = n2502
        # sudoku/blocks/block_8/diff23 -> n2503
        n2503 = self.context.mk_neq(n2483, n2485)
        self.nets['sudoku/blocks/block_8/diff23'] = n2503
        # sudoku/blocks/block_8/diff24 -> n2504
        n2504 = self.context.mk_neq(n2483, n2486)
        self.nets['sudoku/blocks/block_8/diff24'] = n2504
        # sudoku/blocks/block_8/diff25 -> n2505
        n2505 = self.context.mk_neq(n2483, n2487)
        self.nets['sudoku/blocks/block_8/diff25'] = n2505
        # sudoku/blocks/block_8/diff26 -> n2506
        n2506 = self.context.mk_neq(n2483, n2488)
        self.nets['sudoku/blocks/block_8/diff26'] = n2506
        # sudoku/blocks/block_8/Logical Operator3 -> n2507
        tn668 = self.context.mk_and(n2505, n2506)
        tn667 = self.context.mk_and(n2504, tn668)
        tn666 = self.context.mk_and(n2503, tn667)
        n2507 = self.context.mk_and(n2502, tn666)
        self.nets['sudoku/blocks/block_8/Logical Operator3'] = n2507
        # sudoku/blocks/block_8/diff16 -> n2508
        n2508 = self.context.mk_neq(n2482, n2483)
        self.nets['sudoku/blocks/block_8/diff16'] = n2508
        # sudoku/blocks/block_8/diff17 -> n2509
        n2509 = self.context.mk_neq(n2482, n2484)
        self.nets['sudoku/blocks/block_8/diff17'] = n2509
        # sudoku/blocks/block_8/diff18 -> n2510
        n2510 = self.context.mk_neq(n2482, n2485)
        self.nets['sudoku/blocks/block_8/diff18'] = n2510
        # sudoku/blocks/block_8/diff19 -> n2511
        n2511 = self.context.mk_neq(n2482, n2486)
        self.nets['sudoku/blocks/block_8/diff19'] = n2511
        # sudoku/blocks/block_8/diff20 -> n2512
        n2512 = self.context.mk_neq(n2482, n2487)
        self.nets['sudoku/blocks/block_8/diff20'] = n2512
        # sudoku/blocks/block_8/diff21 -> n2513
        n2513 = self.context.mk_neq(n2482, n2488)
        self.nets['sudoku/blocks/block_8/diff21'] = n2513
        # sudoku/blocks/block_8/Logical Operator2 -> n2514
        tn672 = self.context.mk_and(n2512, n2513)
        tn671 = self.context.mk_and(n2511, tn672)
        tn670 = self.context.mk_and(n2510, tn671)
        tn669 = self.context.mk_and(n2509, tn670)
        n2514 = self.context.mk_and(n2508, tn669)
        self.nets['sudoku/blocks/block_8/Logical Operator2'] = n2514
        # sudoku/blocks/block_8/diff9 -> n2515
        n2515 = self.context.mk_neq(n2481, n2482)
        self.nets['sudoku/blocks/block_8/diff9'] = n2515
        # sudoku/blocks/block_8/diff10 -> n2516
        n2516 = self.context.mk_neq(n2481, n2483)
        self.nets['sudoku/blocks/block_8/diff10'] = n2516
        # sudoku/blocks/block_8/diff11 -> n2517
        n2517 = self.context.mk_neq(n2481, n2484)
        self.nets['sudoku/blocks/block_8/diff11'] = n2517
        # sudoku/blocks/block_8/diff12 -> n2518
        n2518 = self.context.mk_neq(n2481, n2485)
        self.nets['sudoku/blocks/block_8/diff12'] = n2518
        # sudoku/blocks/block_8/diff13 -> n2519
        n2519 = self.context.mk_neq(n2481, n2486)
        self.nets['sudoku/blocks/block_8/diff13'] = n2519
        # sudoku/blocks/block_8/diff14 -> n2520
        n2520 = self.context.mk_neq(n2481, n2487)
        self.nets['sudoku/blocks/block_8/diff14'] = n2520
        # sudoku/blocks/block_8/diff15 -> n2521
        n2521 = self.context.mk_neq(n2481, n2488)
        self.nets['sudoku/blocks/block_8/diff15'] = n2521
        # sudoku/blocks/block_8/Logical Operator1 -> n2522
        tn677 = self.context.mk_and(n2520, n2521)
        tn676 = self.context.mk_and(n2519, tn677)
        tn675 = self.context.mk_and(n2518, tn676)
        tn674 = self.context.mk_and(n2517, tn675)
        tn673 = self.context.mk_and(n2516, tn674)
        n2522 = self.context.mk_and(n2515, tn673)
        self.nets['sudoku/blocks/block_8/Logical Operator1'] = n2522
        # sudoku/blocks/block_8/diff1 -> n2523
        n2523 = self.context.mk_neq(n2480, n2481)
        self.nets['sudoku/blocks/block_8/diff1'] = n2523
        # sudoku/blocks/block_8/diff2 -> n2524
        n2524 = self.context.mk_neq(n2480, n2482)
        self.nets['sudoku/blocks/block_8/diff2'] = n2524
        # sudoku/blocks/block_8/diff3 -> n2525
        n2525 = self.context.mk_neq(n2480, n2483)
        self.nets['sudoku/blocks/block_8/diff3'] = n2525
        # sudoku/blocks/block_8/diff4 -> n2526
        n2526 = self.context.mk_neq(n2480, n2484)
        self.nets['sudoku/blocks/block_8/diff4'] = n2526
        # sudoku/blocks/block_8/diff5 -> n2527
        n2527 = self.context.mk_neq(n2480, n2485)
        self.nets['sudoku/blocks/block_8/diff5'] = n2527
        # sudoku/blocks/block_8/diff6 -> n2528
        n2528 = self.context.mk_neq(n2480, n2486)
        self.nets['sudoku/blocks/block_8/diff6'] = n2528
        # sudoku/blocks/block_8/diff7 -> n2529
        n2529 = self.context.mk_neq(n2480, n2487)
        self.nets['sudoku/blocks/block_8/diff7'] = n2529
        # sudoku/blocks/block_8/diff8 -> n2530
        n2530 = self.context.mk_neq(n2480, n2488)
        self.nets['sudoku/blocks/block_8/diff8'] = n2530
        # sudoku/blocks/block_8/Logical Operator -> n2531
        tn683 = self.context.mk_and(n2529, n2530)
        tn682 = self.context.mk_and(n2528, tn683)
        tn681 = self.context.mk_and(n2527, tn682)
        tn680 = self.context.mk_and(n2526, tn681)
        tn679 = self.context.mk_and(n2525, tn680)
        tn678 = self.context.mk_and(n2524, tn679)
        n2531 = self.context.mk_and(n2523, tn678)
        self.nets['sudoku/blocks/block_8/Logical Operator'] = n2531
        # sudoku/blocks/block_8/Logical Operator7 -> n2532
        tn689 = self.context.mk_and(n2522, n2531)
        tn688 = self.context.mk_and(n2514, tn689)
        tn687 = self.context.mk_and(n2507, tn688)
        tn686 = self.context.mk_and(n2501, tn687)
        tn685 = self.context.mk_and(n2496, tn686)
        tn684 = self.context.mk_and(n2492, tn685)
        n2532 = self.context.mk_and(n2489, tn684)
        self.nets['sudoku/blocks/block_8/Logical Operator7'] = n2532
        # n2532 -> Out1
        return n2532

    def block_9(self, n2534, n2535, n2536, n2537, n2538, n2539, n2540, n2541, n2542):
        # In1 -> n2534
        # In2 -> n2535
        # In3 -> n2536
        # In4 -> n2537
        # In5 -> n2538
        # In6 -> n2539
        # In7 -> n2540
        # In8 -> n2541
        # In9 -> n2542
        # sudoku/blocks/block_9/diff36 -> n2543
        n2543 = self.context.mk_neq(n2541, n2542)
        self.nets['sudoku/blocks/block_9/diff36'] = n2543
        # sudoku/blocks/block_9/diff34 -> n2544
        n2544 = self.context.mk_neq(n2540, n2541)
        self.nets['sudoku/blocks/block_9/diff34'] = n2544
        # sudoku/blocks/block_9/diff35 -> n2545
        n2545 = self.context.mk_neq(n2540, n2542)
        self.nets['sudoku/blocks/block_9/diff35'] = n2545
        # sudoku/blocks/block_9/Logical Operator6 -> n2546
        n2546 = self.context.mk_and(n2544, n2545)
        self.nets['sudoku/blocks/block_9/Logical Operator6'] = n2546
        # sudoku/blocks/block_9/diff31 -> n2547
        n2547 = self.context.mk_neq(n2539, n2540)
        self.nets['sudoku/blocks/block_9/diff31'] = n2547
        # sudoku/blocks/block_9/diff32 -> n2548
        n2548 = self.context.mk_neq(n2539, n2541)
        self.nets['sudoku/blocks/block_9/diff32'] = n2548
        # sudoku/blocks/block_9/diff33 -> n2549
        n2549 = self.context.mk_neq(n2539, n2542)
        self.nets['sudoku/blocks/block_9/diff33'] = n2549
        # sudoku/blocks/block_9/Logical Operator5 -> n2550
        tn690 = self.context.mk_and(n2548, n2549)
        n2550 = self.context.mk_and(n2547, tn690)
        self.nets['sudoku/blocks/block_9/Logical Operator5'] = n2550
        # sudoku/blocks/block_9/diff27 -> n2551
        n2551 = self.context.mk_neq(n2538, n2539)
        self.nets['sudoku/blocks/block_9/diff27'] = n2551
        # sudoku/blocks/block_9/diff28 -> n2552
        n2552 = self.context.mk_neq(n2538, n2540)
        self.nets['sudoku/blocks/block_9/diff28'] = n2552
        # sudoku/blocks/block_9/diff29 -> n2553
        n2553 = self.context.mk_neq(n2538, n2541)
        self.nets['sudoku/blocks/block_9/diff29'] = n2553
        # sudoku/blocks/block_9/diff30 -> n2554
        n2554 = self.context.mk_neq(n2538, n2542)
        self.nets['sudoku/blocks/block_9/diff30'] = n2554
        # sudoku/blocks/block_9/Logical Operator4 -> n2555
        tn692 = self.context.mk_and(n2553, n2554)
        tn691 = self.context.mk_and(n2552, tn692)
        n2555 = self.context.mk_and(n2551, tn691)
        self.nets['sudoku/blocks/block_9/Logical Operator4'] = n2555
        # sudoku/blocks/block_9/diff22 -> n2556
        n2556 = self.context.mk_neq(n2537, n2538)
        self.nets['sudoku/blocks/block_9/diff22'] = n2556
        # sudoku/blocks/block_9/diff23 -> n2557
        n2557 = self.context.mk_neq(n2537, n2539)
        self.nets['sudoku/blocks/block_9/diff23'] = n2557
        # sudoku/blocks/block_9/diff24 -> n2558
        n2558 = self.context.mk_neq(n2537, n2540)
        self.nets['sudoku/blocks/block_9/diff24'] = n2558
        # sudoku/blocks/block_9/diff25 -> n2559
        n2559 = self.context.mk_neq(n2537, n2541)
        self.nets['sudoku/blocks/block_9/diff25'] = n2559
        # sudoku/blocks/block_9/diff26 -> n2560
        n2560 = self.context.mk_neq(n2537, n2542)
        self.nets['sudoku/blocks/block_9/diff26'] = n2560
        # sudoku/blocks/block_9/Logical Operator3 -> n2561
        tn695 = self.context.mk_and(n2559, n2560)
        tn694 = self.context.mk_and(n2558, tn695)
        tn693 = self.context.mk_and(n2557, tn694)
        n2561 = self.context.mk_and(n2556, tn693)
        self.nets['sudoku/blocks/block_9/Logical Operator3'] = n2561
        # sudoku/blocks/block_9/diff16 -> n2562
        n2562 = self.context.mk_neq(n2536, n2537)
        self.nets['sudoku/blocks/block_9/diff16'] = n2562
        # sudoku/blocks/block_9/diff17 -> n2563
        n2563 = self.context.mk_neq(n2536, n2538)
        self.nets['sudoku/blocks/block_9/diff17'] = n2563
        # sudoku/blocks/block_9/diff18 -> n2564
        n2564 = self.context.mk_neq(n2536, n2539)
        self.nets['sudoku/blocks/block_9/diff18'] = n2564
        # sudoku/blocks/block_9/diff19 -> n2565
        n2565 = self.context.mk_neq(n2536, n2540)
        self.nets['sudoku/blocks/block_9/diff19'] = n2565
        # sudoku/blocks/block_9/diff20 -> n2566
        n2566 = self.context.mk_neq(n2536, n2541)
        self.nets['sudoku/blocks/block_9/diff20'] = n2566
        # sudoku/blocks/block_9/diff21 -> n2567
        n2567 = self.context.mk_neq(n2536, n2542)
        self.nets['sudoku/blocks/block_9/diff21'] = n2567
        # sudoku/blocks/block_9/Logical Operator2 -> n2568
        tn699 = self.context.mk_and(n2566, n2567)
        tn698 = self.context.mk_and(n2565, tn699)
        tn697 = self.context.mk_and(n2564, tn698)
        tn696 = self.context.mk_and(n2563, tn697)
        n2568 = self.context.mk_and(n2562, tn696)
        self.nets['sudoku/blocks/block_9/Logical Operator2'] = n2568
        # sudoku/blocks/block_9/diff9 -> n2569
        n2569 = self.context.mk_neq(n2535, n2536)
        self.nets['sudoku/blocks/block_9/diff9'] = n2569
        # sudoku/blocks/block_9/diff10 -> n2570
        n2570 = self.context.mk_neq(n2535, n2537)
        self.nets['sudoku/blocks/block_9/diff10'] = n2570
        # sudoku/blocks/block_9/diff11 -> n2571
        n2571 = self.context.mk_neq(n2535, n2538)
        self.nets['sudoku/blocks/block_9/diff11'] = n2571
        # sudoku/blocks/block_9/diff12 -> n2572
        n2572 = self.context.mk_neq(n2535, n2539)
        self.nets['sudoku/blocks/block_9/diff12'] = n2572
        # sudoku/blocks/block_9/diff13 -> n2573
        n2573 = self.context.mk_neq(n2535, n2540)
        self.nets['sudoku/blocks/block_9/diff13'] = n2573
        # sudoku/blocks/block_9/diff14 -> n2574
        n2574 = self.context.mk_neq(n2535, n2541)
        self.nets['sudoku/blocks/block_9/diff14'] = n2574
        # sudoku/blocks/block_9/diff15 -> n2575
        n2575 = self.context.mk_neq(n2535, n2542)
        self.nets['sudoku/blocks/block_9/diff15'] = n2575
        # sudoku/blocks/block_9/Logical Operator1 -> n2576
        tn704 = self.context.mk_and(n2574, n2575)
        tn703 = self.context.mk_and(n2573, tn704)
        tn702 = self.context.mk_and(n2572, tn703)
        tn701 = self.context.mk_and(n2571, tn702)
        tn700 = self.context.mk_and(n2570, tn701)
        n2576 = self.context.mk_and(n2569, tn700)
        self.nets['sudoku/blocks/block_9/Logical Operator1'] = n2576
        # sudoku/blocks/block_9/diff1 -> n2577
        n2577 = self.context.mk_neq(n2534, n2535)
        self.nets['sudoku/blocks/block_9/diff1'] = n2577
        # sudoku/blocks/block_9/diff2 -> n2578
        n2578 = self.context.mk_neq(n2534, n2536)
        self.nets['sudoku/blocks/block_9/diff2'] = n2578
        # sudoku/blocks/block_9/diff3 -> n2579
        n2579 = self.context.mk_neq(n2534, n2537)
        self.nets['sudoku/blocks/block_9/diff3'] = n2579
        # sudoku/blocks/block_9/diff4 -> n2580
        n2580 = self.context.mk_neq(n2534, n2538)
        self.nets['sudoku/blocks/block_9/diff4'] = n2580
        # sudoku/blocks/block_9/diff5 -> n2581
        n2581 = self.context.mk_neq(n2534, n2539)
        self.nets['sudoku/blocks/block_9/diff5'] = n2581
        # sudoku/blocks/block_9/diff6 -> n2582
        n2582 = self.context.mk_neq(n2534, n2540)
        self.nets['sudoku/blocks/block_9/diff6'] = n2582
        # sudoku/blocks/block_9/diff7 -> n2583
        n2583 = self.context.mk_neq(n2534, n2541)
        self.nets['sudoku/blocks/block_9/diff7'] = n2583
        # sudoku/blocks/block_9/diff8 -> n2584
        n2584 = self.context.mk_neq(n2534, n2542)
        self.nets['sudoku/blocks/block_9/diff8'] = n2584
        # sudoku/blocks/block_9/Logical Operator -> n2585
        tn710 = self.context.mk_and(n2583, n2584)
        tn709 = self.context.mk_and(n2582, tn710)
        tn708 = self.context.mk_and(n2581, tn709)
        tn707 = self.context.mk_and(n2580, tn708)
        tn706 = self.context.mk_and(n2579, tn707)
        tn705 = self.context.mk_and(n2578, tn706)
        n2585 = self.context.mk_and(n2577, tn705)
        self.nets['sudoku/blocks/block_9/Logical Operator'] = n2585
        # sudoku/blocks/block_9/Logical Operator7 -> n2586
        tn716 = self.context.mk_and(n2576, n2585)
        tn715 = self.context.mk_and(n2568, tn716)
        tn714 = self.context.mk_and(n2561, tn715)
        tn713 = self.context.mk_and(n2555, tn714)
        tn712 = self.context.mk_and(n2550, tn713)
        tn711 = self.context.mk_and(n2546, tn712)
        n2586 = self.context.mk_and(n2543, tn711)
        self.nets['sudoku/blocks/block_9/Logical Operator7'] = n2586
        # n2586 -> Out1
        return n2586

    def block_1(self, n2588, n2589, n2590, n2591, n2592, n2593, n2594, n2595, n2596):
        # In1 -> n2588
        # In2 -> n2589
        # In3 -> n2590
        # In4 -> n2591
        # In5 -> n2592
        # In6 -> n2593
        # In7 -> n2594
        # In8 -> n2595
        # In9 -> n2596
        # sudoku/blocks/block_1/diff36 -> n2597
        n2597 = self.context.mk_neq(n2595, n2596)
        self.nets['sudoku/blocks/block_1/diff36'] = n2597
        # sudoku/blocks/block_1/diff34 -> n2598
        n2598 = self.context.mk_neq(n2594, n2595)
        self.nets['sudoku/blocks/block_1/diff34'] = n2598
        # sudoku/blocks/block_1/diff35 -> n2599
        n2599 = self.context.mk_neq(n2594, n2596)
        self.nets['sudoku/blocks/block_1/diff35'] = n2599
        # sudoku/blocks/block_1/Logical Operator6 -> n2600
        n2600 = self.context.mk_and(n2598, n2599)
        self.nets['sudoku/blocks/block_1/Logical Operator6'] = n2600
        # sudoku/blocks/block_1/diff31 -> n2601
        n2601 = self.context.mk_neq(n2593, n2594)
        self.nets['sudoku/blocks/block_1/diff31'] = n2601
        # sudoku/blocks/block_1/diff32 -> n2602
        n2602 = self.context.mk_neq(n2593, n2595)
        self.nets['sudoku/blocks/block_1/diff32'] = n2602
        # sudoku/blocks/block_1/diff33 -> n2603
        n2603 = self.context.mk_neq(n2593, n2596)
        self.nets['sudoku/blocks/block_1/diff33'] = n2603
        # sudoku/blocks/block_1/Logical Operator5 -> n2604
        tn717 = self.context.mk_and(n2602, n2603)
        n2604 = self.context.mk_and(n2601, tn717)
        self.nets['sudoku/blocks/block_1/Logical Operator5'] = n2604
        # sudoku/blocks/block_1/diff27 -> n2605
        n2605 = self.context.mk_neq(n2592, n2593)
        self.nets['sudoku/blocks/block_1/diff27'] = n2605
        # sudoku/blocks/block_1/diff28 -> n2606
        n2606 = self.context.mk_neq(n2592, n2594)
        self.nets['sudoku/blocks/block_1/diff28'] = n2606
        # sudoku/blocks/block_1/diff29 -> n2607
        n2607 = self.context.mk_neq(n2592, n2595)
        self.nets['sudoku/blocks/block_1/diff29'] = n2607
        # sudoku/blocks/block_1/diff30 -> n2608
        n2608 = self.context.mk_neq(n2592, n2596)
        self.nets['sudoku/blocks/block_1/diff30'] = n2608
        # sudoku/blocks/block_1/Logical Operator4 -> n2609
        tn719 = self.context.mk_and(n2607, n2608)
        tn718 = self.context.mk_and(n2606, tn719)
        n2609 = self.context.mk_and(n2605, tn718)
        self.nets['sudoku/blocks/block_1/Logical Operator4'] = n2609
        # sudoku/blocks/block_1/diff22 -> n2610
        n2610 = self.context.mk_neq(n2591, n2592)
        self.nets['sudoku/blocks/block_1/diff22'] = n2610
        # sudoku/blocks/block_1/diff23 -> n2611
        n2611 = self.context.mk_neq(n2591, n2593)
        self.nets['sudoku/blocks/block_1/diff23'] = n2611
        # sudoku/blocks/block_1/diff24 -> n2612
        n2612 = self.context.mk_neq(n2591, n2594)
        self.nets['sudoku/blocks/block_1/diff24'] = n2612
        # sudoku/blocks/block_1/diff25 -> n2613
        n2613 = self.context.mk_neq(n2591, n2595)
        self.nets['sudoku/blocks/block_1/diff25'] = n2613
        # sudoku/blocks/block_1/diff26 -> n2614
        n2614 = self.context.mk_neq(n2591, n2596)
        self.nets['sudoku/blocks/block_1/diff26'] = n2614
        # sudoku/blocks/block_1/Logical Operator3 -> n2615
        tn722 = self.context.mk_and(n2613, n2614)
        tn721 = self.context.mk_and(n2612, tn722)
        tn720 = self.context.mk_and(n2611, tn721)
        n2615 = self.context.mk_and(n2610, tn720)
        self.nets['sudoku/blocks/block_1/Logical Operator3'] = n2615
        # sudoku/blocks/block_1/diff16 -> n2616
        n2616 = self.context.mk_neq(n2590, n2591)
        self.nets['sudoku/blocks/block_1/diff16'] = n2616
        # sudoku/blocks/block_1/diff17 -> n2617
        n2617 = self.context.mk_neq(n2590, n2592)
        self.nets['sudoku/blocks/block_1/diff17'] = n2617
        # sudoku/blocks/block_1/diff18 -> n2618
        n2618 = self.context.mk_neq(n2590, n2593)
        self.nets['sudoku/blocks/block_1/diff18'] = n2618
        # sudoku/blocks/block_1/diff19 -> n2619
        n2619 = self.context.mk_neq(n2590, n2594)
        self.nets['sudoku/blocks/block_1/diff19'] = n2619
        # sudoku/blocks/block_1/diff20 -> n2620
        n2620 = self.context.mk_neq(n2590, n2595)
        self.nets['sudoku/blocks/block_1/diff20'] = n2620
        # sudoku/blocks/block_1/diff21 -> n2621
        n2621 = self.context.mk_neq(n2590, n2596)
        self.nets['sudoku/blocks/block_1/diff21'] = n2621
        # sudoku/blocks/block_1/Logical Operator2 -> n2622
        tn726 = self.context.mk_and(n2620, n2621)
        tn725 = self.context.mk_and(n2619, tn726)
        tn724 = self.context.mk_and(n2618, tn725)
        tn723 = self.context.mk_and(n2617, tn724)
        n2622 = self.context.mk_and(n2616, tn723)
        self.nets['sudoku/blocks/block_1/Logical Operator2'] = n2622
        # sudoku/blocks/block_1/diff9 -> n2623
        n2623 = self.context.mk_neq(n2589, n2590)
        self.nets['sudoku/blocks/block_1/diff9'] = n2623
        # sudoku/blocks/block_1/diff10 -> n2624
        n2624 = self.context.mk_neq(n2589, n2591)
        self.nets['sudoku/blocks/block_1/diff10'] = n2624
        # sudoku/blocks/block_1/diff11 -> n2625
        n2625 = self.context.mk_neq(n2589, n2592)
        self.nets['sudoku/blocks/block_1/diff11'] = n2625
        # sudoku/blocks/block_1/diff12 -> n2626
        n2626 = self.context.mk_neq(n2589, n2593)
        self.nets['sudoku/blocks/block_1/diff12'] = n2626
        # sudoku/blocks/block_1/diff13 -> n2627
        n2627 = self.context.mk_neq(n2589, n2594)
        self.nets['sudoku/blocks/block_1/diff13'] = n2627
        # sudoku/blocks/block_1/diff14 -> n2628
        n2628 = self.context.mk_neq(n2589, n2595)
        self.nets['sudoku/blocks/block_1/diff14'] = n2628
        # sudoku/blocks/block_1/diff15 -> n2629
        n2629 = self.context.mk_neq(n2589, n2596)
        self.nets['sudoku/blocks/block_1/diff15'] = n2629
        # sudoku/blocks/block_1/Logical Operator1 -> n2630
        tn731 = self.context.mk_and(n2628, n2629)
        tn730 = self.context.mk_and(n2627, tn731)
        tn729 = self.context.mk_and(n2626, tn730)
        tn728 = self.context.mk_and(n2625, tn729)
        tn727 = self.context.mk_and(n2624, tn728)
        n2630 = self.context.mk_and(n2623, tn727)
        self.nets['sudoku/blocks/block_1/Logical Operator1'] = n2630
        # sudoku/blocks/block_1/diff1 -> n2631
        n2631 = self.context.mk_neq(n2588, n2589)
        self.nets['sudoku/blocks/block_1/diff1'] = n2631
        # sudoku/blocks/block_1/diff2 -> n2632
        n2632 = self.context.mk_neq(n2588, n2590)
        self.nets['sudoku/blocks/block_1/diff2'] = n2632
        # sudoku/blocks/block_1/diff3 -> n2633
        n2633 = self.context.mk_neq(n2588, n2591)
        self.nets['sudoku/blocks/block_1/diff3'] = n2633
        # sudoku/blocks/block_1/diff4 -> n2634
        n2634 = self.context.mk_neq(n2588, n2592)
        self.nets['sudoku/blocks/block_1/diff4'] = n2634
        # sudoku/blocks/block_1/diff5 -> n2635
        n2635 = self.context.mk_neq(n2588, n2593)
        self.nets['sudoku/blocks/block_1/diff5'] = n2635
        # sudoku/blocks/block_1/diff6 -> n2636
        n2636 = self.context.mk_neq(n2588, n2594)
        self.nets['sudoku/blocks/block_1/diff6'] = n2636
        # sudoku/blocks/block_1/diff7 -> n2637
        n2637 = self.context.mk_neq(n2588, n2595)
        self.nets['sudoku/blocks/block_1/diff7'] = n2637
        # sudoku/blocks/block_1/diff8 -> n2638
        n2638 = self.context.mk_neq(n2588, n2596)
        self.nets['sudoku/blocks/block_1/diff8'] = n2638
        # sudoku/blocks/block_1/Logical Operator -> n2639
        tn737 = self.context.mk_and(n2637, n2638)
        tn736 = self.context.mk_and(n2636, tn737)
        tn735 = self.context.mk_and(n2635, tn736)
        tn734 = self.context.mk_and(n2634, tn735)
        tn733 = self.context.mk_and(n2633, tn734)
        tn732 = self.context.mk_and(n2632, tn733)
        n2639 = self.context.mk_and(n2631, tn732)
        self.nets['sudoku/blocks/block_1/Logical Operator'] = n2639
        # sudoku/blocks/block_1/Logical Operator7 -> n2640
        tn743 = self.context.mk_and(n2630, n2639)
        tn742 = self.context.mk_and(n2622, tn743)
        tn741 = self.context.mk_and(n2615, tn742)
        tn740 = self.context.mk_and(n2609, tn741)
        tn739 = self.context.mk_and(n2604, tn740)
        tn738 = self.context.mk_and(n2600, tn739)
        n2640 = self.context.mk_and(n2597, tn738)
        self.nets['sudoku/blocks/block_1/Logical Operator7'] = n2640
        # n2640 -> Out1
        return n2640

    def blocks(self, n2642, n2643, n2644, n2645, n2646, n2647, n2648, n2649, n2650, n2651, n2652, n2653, n2654, n2655, n2656, n2657, n2658, n2659, n2660, n2661, n2662, n2663, n2664, n2665, n2666, n2667, n2668, n2669, n2670, n2671, n2672, n2673, n2674, n2675, n2676, n2677, n2678, n2679, n2680, n2681, n2682, n2683, n2684, n2685, n2686, n2687, n2688, n2689, n2690, n2691, n2692, n2693, n2694, n2695, n2696, n2697, n2698, n2699, n2700, n2701, n2702, n2703, n2704, n2705, n2706, n2707, n2708, n2709, n2710, n2711, n2712, n2713, n2714, n2715, n2716, n2717, n2718, n2719, n2720, n2721, n2722):
        # In1 -> n2642
        # In2 -> n2643
        # In3 -> n2644
        # In4 -> n2645
        # In5 -> n2646
        # In6 -> n2647
        # In7 -> n2648
        # In8 -> n2649
        # In9 -> n2650
        # In10 -> n2651
        # In11 -> n2652
        # In12 -> n2653
        # In13 -> n2654
        # In14 -> n2655
        # In15 -> n2656
        # In16 -> n2657
        # In17 -> n2658
        # In18 -> n2659
        # In19 -> n2660
        # In20 -> n2661
        # In21 -> n2662
        # In22 -> n2663
        # In23 -> n2664
        # In24 -> n2665
        # In25 -> n2666
        # In26 -> n2667
        # In27 -> n2668
        # In28 -> n2669
        # In29 -> n2670
        # In30 -> n2671
        # In31 -> n2672
        # In32 -> n2673
        # In33 -> n2674
        # In34 -> n2675
        # In35 -> n2676
        # In36 -> n2677
        # In37 -> n2678
        # In38 -> n2679
        # In39 -> n2680
        # In40 -> n2681
        # In41 -> n2682
        # In42 -> n2683
        # In43 -> n2684
        # In44 -> n2685
        # In45 -> n2686
        # In46 -> n2687
        # In47 -> n2688
        # In48 -> n2689
        # In49 -> n2690
        # In50 -> n2691
        # In51 -> n2692
        # In52 -> n2693
        # In53 -> n2694
        # In54 -> n2695
        # In55 -> n2696
        # In56 -> n2697
        # In57 -> n2698
        # In58 -> n2699
        # In59 -> n2700
        # In60 -> n2701
        # In61 -> n2702
        # In62 -> n2703
        # In63 -> n2704
        # In64 -> n2705
        # In65 -> n2706
        # In66 -> n2707
        # In67 -> n2708
        # In68 -> n2709
        # In69 -> n2710
        # In70 -> n2711
        # In71 -> n2712
        # In72 -> n2713
        # In73 -> n2714
        # In74 -> n2715
        # In75 -> n2716
        # In76 -> n2717
        # In77 -> n2718
        # In78 -> n2719
        # In79 -> n2720
        # In80 -> n2721
        # In81 -> n2722
        n2723_1 = self.block_1(n2642, n2643, n2644, n2645, n2646, n2647, n2648, n2649, n2650)
        n2724_1 = self.block_2(n2651, n2652, n2653, n2654, n2655, n2656, n2657, n2658, n2659)
        n2725_1 = self.block_3(n2660, n2661, n2662, n2663, n2664, n2665, n2666, n2667, n2668)
        n2726_1 = self.block_4(n2669, n2670, n2671, n2672, n2673, n2674, n2675, n2676, n2677)
        n2727_1 = self.block_5(n2678, n2679, n2680, n2681, n2682, n2683, n2684, n2685, n2686)
        n2728_1 = self.block_6(n2687, n2688, n2689, n2690, n2691, n2692, n2693, n2694, n2695)
        n2729_1 = self.block_7(n2696, n2697, n2698, n2699, n2700, n2701, n2702, n2703, n2704)
        n2730_1 = self.block_8(n2705, n2706, n2707, n2708, n2709, n2710, n2711, n2712, n2713)
        n2731_1 = self.block_9(n2714, n2715, n2716, n2717, n2718, n2719, n2720, n2721, n2722)
        # sudoku/blocks/Logical Operator -> n2732
        tn750 = self.context.mk_and(n2730_1, n2731_1)
        tn749 = self.context.mk_and(n2729_1, tn750)
        tn748 = self.context.mk_and(n2728_1, tn749)
        tn747 = self.context.mk_and(n2727_1, tn748)
        tn746 = self.context.mk_and(n2726_1, tn747)
        tn745 = self.context.mk_and(n2725_1, tn746)
        tn744 = self.context.mk_and(n2724_1, tn745)
        n2732 = self.context.mk_and(n2723_1, tn744)
        self.nets['sudoku/blocks/Logical Operator'] = n2732
        # n2732 -> Out1
        return n2732

    def bounds59(self, n2734):
        # In1 -> n2734
        # sudoku/bounds59/lb
        n2735 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds59/lb'] = n2735
        # sudoku/bounds59/leq -> n2736
        n2736 = self.context.mk_leq(n2735, n2734)
        self.nets['sudoku/bounds59/leq'] = n2736
        # sudoku/bounds59/ub
        n2737 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds59/ub'] = n2737
        # sudoku/bounds59/geq -> n2738
        n2738 = self.context.mk_leq(n2734, n2737)
        self.nets['sudoku/bounds59/geq'] = n2738
        # sudoku/bounds59/Logical Operator -> n2739
        n2739 = self.context.mk_and(n2736, n2738)
        self.nets['sudoku/bounds59/Logical Operator'] = n2739
        # sudoku/bounds59/Assumption
        self.context.mk_assumption(n2739)
        return 

    def bounds58(self, n2741):
        # In1 -> n2741
        # sudoku/bounds58/lb
        n2742 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds58/lb'] = n2742
        # sudoku/bounds58/leq -> n2743
        n2743 = self.context.mk_leq(n2742, n2741)
        self.nets['sudoku/bounds58/leq'] = n2743
        # sudoku/bounds58/ub
        n2744 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds58/ub'] = n2744
        # sudoku/bounds58/geq -> n2745
        n2745 = self.context.mk_leq(n2741, n2744)
        self.nets['sudoku/bounds58/geq'] = n2745
        # sudoku/bounds58/Logical Operator -> n2746
        n2746 = self.context.mk_and(n2743, n2745)
        self.nets['sudoku/bounds58/Logical Operator'] = n2746
        # sudoku/bounds58/Assumption
        self.context.mk_assumption(n2746)
        return 

    def bounds53(self, n2748):
        # In1 -> n2748
        # sudoku/bounds53/lb
        n2749 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds53/lb'] = n2749
        # sudoku/bounds53/leq -> n2750
        n2750 = self.context.mk_leq(n2749, n2748)
        self.nets['sudoku/bounds53/leq'] = n2750
        # sudoku/bounds53/ub
        n2751 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds53/ub'] = n2751
        # sudoku/bounds53/geq -> n2752
        n2752 = self.context.mk_leq(n2748, n2751)
        self.nets['sudoku/bounds53/geq'] = n2752
        # sudoku/bounds53/Logical Operator -> n2753
        n2753 = self.context.mk_and(n2750, n2752)
        self.nets['sudoku/bounds53/Logical Operator'] = n2753
        # sudoku/bounds53/Assumption
        self.context.mk_assumption(n2753)
        return 

    def bounds52(self, n2755):
        # In1 -> n2755
        # sudoku/bounds52/lb
        n2756 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds52/lb'] = n2756
        # sudoku/bounds52/leq -> n2757
        n2757 = self.context.mk_leq(n2756, n2755)
        self.nets['sudoku/bounds52/leq'] = n2757
        # sudoku/bounds52/ub
        n2758 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds52/ub'] = n2758
        # sudoku/bounds52/geq -> n2759
        n2759 = self.context.mk_leq(n2755, n2758)
        self.nets['sudoku/bounds52/geq'] = n2759
        # sudoku/bounds52/Logical Operator -> n2760
        n2760 = self.context.mk_and(n2757, n2759)
        self.nets['sudoku/bounds52/Logical Operator'] = n2760
        # sudoku/bounds52/Assumption
        self.context.mk_assumption(n2760)
        return 

    def bounds51(self, n2762):
        # In1 -> n2762
        # sudoku/bounds51/lb
        n2763 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds51/lb'] = n2763
        # sudoku/bounds51/leq -> n2764
        n2764 = self.context.mk_leq(n2763, n2762)
        self.nets['sudoku/bounds51/leq'] = n2764
        # sudoku/bounds51/ub
        n2765 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds51/ub'] = n2765
        # sudoku/bounds51/geq -> n2766
        n2766 = self.context.mk_leq(n2762, n2765)
        self.nets['sudoku/bounds51/geq'] = n2766
        # sudoku/bounds51/Logical Operator -> n2767
        n2767 = self.context.mk_and(n2764, n2766)
        self.nets['sudoku/bounds51/Logical Operator'] = n2767
        # sudoku/bounds51/Assumption
        self.context.mk_assumption(n2767)
        return 

    def bounds50(self, n2769):
        # In1 -> n2769
        # sudoku/bounds50/lb
        n2770 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds50/lb'] = n2770
        # sudoku/bounds50/leq -> n2771
        n2771 = self.context.mk_leq(n2770, n2769)
        self.nets['sudoku/bounds50/leq'] = n2771
        # sudoku/bounds50/ub
        n2772 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds50/ub'] = n2772
        # sudoku/bounds50/geq -> n2773
        n2773 = self.context.mk_leq(n2769, n2772)
        self.nets['sudoku/bounds50/geq'] = n2773
        # sudoku/bounds50/Logical Operator -> n2774
        n2774 = self.context.mk_and(n2771, n2773)
        self.nets['sudoku/bounds50/Logical Operator'] = n2774
        # sudoku/bounds50/Assumption
        self.context.mk_assumption(n2774)
        return 

    def bounds57(self, n2776):
        # In1 -> n2776
        # sudoku/bounds57/lb
        n2777 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds57/lb'] = n2777
        # sudoku/bounds57/leq -> n2778
        n2778 = self.context.mk_leq(n2777, n2776)
        self.nets['sudoku/bounds57/leq'] = n2778
        # sudoku/bounds57/ub
        n2779 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds57/ub'] = n2779
        # sudoku/bounds57/geq -> n2780
        n2780 = self.context.mk_leq(n2776, n2779)
        self.nets['sudoku/bounds57/geq'] = n2780
        # sudoku/bounds57/Logical Operator -> n2781
        n2781 = self.context.mk_and(n2778, n2780)
        self.nets['sudoku/bounds57/Logical Operator'] = n2781
        # sudoku/bounds57/Assumption
        self.context.mk_assumption(n2781)
        return 

    def bounds56(self, n2783):
        # In1 -> n2783
        # sudoku/bounds56/lb
        n2784 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds56/lb'] = n2784
        # sudoku/bounds56/leq -> n2785
        n2785 = self.context.mk_leq(n2784, n2783)
        self.nets['sudoku/bounds56/leq'] = n2785
        # sudoku/bounds56/ub
        n2786 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds56/ub'] = n2786
        # sudoku/bounds56/geq -> n2787
        n2787 = self.context.mk_leq(n2783, n2786)
        self.nets['sudoku/bounds56/geq'] = n2787
        # sudoku/bounds56/Logical Operator -> n2788
        n2788 = self.context.mk_and(n2785, n2787)
        self.nets['sudoku/bounds56/Logical Operator'] = n2788
        # sudoku/bounds56/Assumption
        self.context.mk_assumption(n2788)
        return 

    def bounds55(self, n2790):
        # In1 -> n2790
        # sudoku/bounds55/lb
        n2791 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds55/lb'] = n2791
        # sudoku/bounds55/leq -> n2792
        n2792 = self.context.mk_leq(n2791, n2790)
        self.nets['sudoku/bounds55/leq'] = n2792
        # sudoku/bounds55/ub
        n2793 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds55/ub'] = n2793
        # sudoku/bounds55/geq -> n2794
        n2794 = self.context.mk_leq(n2790, n2793)
        self.nets['sudoku/bounds55/geq'] = n2794
        # sudoku/bounds55/Logical Operator -> n2795
        n2795 = self.context.mk_and(n2792, n2794)
        self.nets['sudoku/bounds55/Logical Operator'] = n2795
        # sudoku/bounds55/Assumption
        self.context.mk_assumption(n2795)
        return 

    def bounds54(self, n2797):
        # In1 -> n2797
        # sudoku/bounds54/lb
        n2798 = self.context.mk_number('1', self.context.mk_int8_type())
        self.nets['sudoku/bounds54/lb'] = n2798
        # sudoku/bounds54/leq -> n2799
        n2799 = self.context.mk_leq(n2798, n2797)
        self.nets['sudoku/bounds54/leq'] = n2799
        # sudoku/bounds54/ub
        n2800 = self.context.mk_number('9', self.context.mk_int8_type())
        self.nets['sudoku/bounds54/ub'] = n2800
        # sudoku/bounds54/geq -> n2801
        n2801 = self.context.mk_leq(n2797, n2800)
        self.nets['sudoku/bounds54/geq'] = n2801
        # sudoku/bounds54/Logical Operator -> n2802
        n2802 = self.context.mk_and(n2799, n2801)
        self.nets['sudoku/bounds54/Logical Operator'] = n2802
        # sudoku/bounds54/Assumption
        self.context.mk_assumption(n2802)
        return 


from sympy.parsing.sympy_parser import parse_expr
import os

def reference():
    reference = '[1] Li, Yilei et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters vol. 13,7 (2013): 3329-33. doi: 10.1021/n/401561г.' \
                '\n[2] Fiebig, Manfred et al. "Second-harmonic generation as a tool for studying electronic and magnetic structures of crystals: review."Journalof The Optical Societyof America B-optical Physics 22 (2005): 96-118.' \
                '\n[3] http://symmetry.jacobs-university.de/group.html.' \
                '\n[4] Gallego et al. "Automatic calculation of symmetry-adapted tensors in magnetic and non-magnetic materials: a new tool of the Bilbao Crystallographic Server" Acta Cryst. A (2019) 75, 438-447.' \
                '\n[5] Boyd, Robert W., Alexander L.Gaeta, and Enno Giese. "Nonlinear optics." Springer Handbook of Atomic, Molecular, and Optical Physics.Cham: Springer International Publishing, 2008.1097 - 1110.' \
                '\n[6] Torchinsky, D. H., et al. "Structural distortion-induced magnetoelastic locking in Sr 2 IrO 4 revealed through nonlinear optical harmonic generation." Physical review letters 114.9 (2015): 096404.' \
                '\n[7] Fichera, Bryan T., et al. "Second harmonic generation as a probe of broken mirror symmetry." Physical Review B 101.24 (2020): 241106.' \
                '\n[8] Fonseca, Jordan, et al. "Anomalous Second Harmonic Generation from Atomically Thin MnBi2Te4." Nano Letters (2022).' \
                '\n[9] Li, Yilei, et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters 13.7 (2013): 3329-3333.' \
                '\n[10] Germer, Thomas A., et al. "Depletion-electric-field-induced second-harmonic generation near oxidized GaAs (001) surfaces." Physical Review B 55.16 (1997): 10694.' \
                '\n[11] Luo, Xiangpeng, et al. "Ultrafast modulations and detection of a ferro-rotational charge density wave using time-resolved electric quadrupole second harmonic generation." Physical review letters 127.12 (2021): 126401.' \
                '\n[12] Jin, Wencan, et al. "Observation of a ferro-rotational order coupled with second-order nonlinear optical fields." Nature Physics 16.1 (2020): 42-46.' \
                '\n[13] Anisimov, A. N., N. A. Perekopaiko, and Aleksei Valerevich Petukhov. "Relationship between the anisotropy of reflected second harmonic radiation and the orientation of the crystal surface." -Soviet journal of quantum electronics 21.1 (1991): 82.' \
                '\n[14] Newnham, Robert E.Properties of materials: anisotropy, symmetry, structure.Oxford university press, 2005.'
    return reference

def disclaimer():
    disclaimer = 'Apache License' \
                 '\nVersion 2.0, January 2004' \
                 '\nhttp://www.apache.org/licenses/' \
                 '\n\nTERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION' \
                 '\n1. Definitions.' \
                 '\n"License" shall mean the terms and conditions for use, reproduction,' \
                 'and distribution as defined by Sections 1 through 9 of this document.' \
                 '\n\n"Licensor" shall mean the copyright owner or entity authorized by' \
                 'the copyright owner that is granting the License.' \
                 '\n\n"Legal Entity" shall mean the union of the acting entity and all' \
                 'other entities that control, are controlled by, or are under common' \
                 'control with that entity. For the purposes of this definition,' \
                 '\n\n"control" means (i) the power, direct or indirect, to cause the ' \
                 'direction or management of such entity, whether by contract or ' \
                 'otherwise, or (ii) ownership of fifty percent (50%) or more of the' \
                 'outstanding shares, or (iii) beneficial ownership of such entity.' \
                 '\n\n"You" (or "Your") shall mean an individual or Legal Entity ' \
                 'exercising permissions granted by this License.' \
                 '\n\n"Source" form shall mean the preferred form for making modifications, ' \
                 'including but not limited to software source code, documentation ' \
                 'source, and configuration files. ' \
                 '\n\n"Object" form shall mean any form resulting from mechanical ' \
                 'transformation or translation of a Source form, including but' \
                 ' not limited to compiled object code, generated documentation,' \
                 ' and conversions to other media types.' \
                 '\n\n"Work" shall mean the work of authorship, whether in Source or' \
                 ' Object form, made available under the License, as indicated by a ' \
                 'copyright notice that is included in or attached to the work' \
                 ' (an example is provided in the Appendix below). ' \
                 '\n\n"Derivative Works" shall mean any work, whether in Source or Object' \
                 ' form, that is based on (or derived from) the Work and for which the' \
                 ' editorial revisions, annotations, elaborations, or other modifications ' \
                 'represent, as a whole, an original work of authorship. For the purposes ' \
                 'of this License, Derivative Works shall not include works that remain ' \
                 'separable from, or merely link (or bind by name) to the interfaces of, ' \
                 'the Work and Derivative Works thereof.' \
                 '\n\n"Contribution" shall mean any work of authorship, including ' \
                 'the original version of the Work and any modifications or additions ' \
                 'to that Work or Derivative Works thereof, that is intentionally ' \
                 'submitted to Licensor for inclusion in the Work by the copyright owner ' \
                 'or by an individual or Legal Entity authorized to submit on behalf of ' \
                 'the copyright owner. For the purposes of this definition, "submitted" ' \
                 'means any form of electronic, verbal, or written communication sent ' \
                 'to the Licensor or its representatives, including but not limited to ' \
                 'communication on electronic mailing lists, source code control systems ,' \
                 'and issue tracking systems that are managed by, or on behalf of, the ' \
                 'Licensor for the purpose of discussing and improving the Work, but ' \
                 'excluding communication that is conspicuously marked or otherwise ' \
                 'designated in writing by the copyright owner as "Not a Contribution."' \
                 '\n\n"Contributor" shall mean Licensor and any individual or Legal Entity on ' \
                 'behalf of whom a Contribution has been received by Licensor and ' \
                 'subsequently incorporated within the Work.' \
                 '\n\n2. Grant of Copyright License. Subject to the terms and conditions of' \
                 ' this License, each Contributor hereby grants to You a perpetual, ' \
                 'worldwide, non-exclusive, no-charge, royalty-free, irrevocable ' \
                 'copyright license to reproduce, prepare Derivative Works of, ' \
                 'publicly display, publicly perform, sublicense, and distribute the ' \
                 'Work and such Derivative Works in Source or Object form. ' \
                 '\n\n3. Grant of Patent License. Subject to the terms and conditions of ' \
                 'this License, each Contributor hereby grants to You a perpetual, ' \
                 'worldwide, non-exclusive, no-charge, royalty-free, irrevocable ' \
                 '(except as stated in this section) patent license to make, have made, ' \
                 'use, offer to sell, sell, import, and otherwise transfer the Work, ' \
                 'where such license applies only to those patent claims licensable ' \
                 'by such Contributor that are necessarily infringed by their ' \
                 'Contribution(s) alone or by combination of their Contribution(s) ' \
                 'with the Work to which such Contribution(s) was submitted. If You ' \
                 'institute patent litigation against any entity (including a ' \
                 'cross-claim or counterclaim in a lawsuit) alleging that the Work ' \
                 'or a Contribution incorporated within the Work constitutes direct ' \
                 'or contributory patent infringement, then any patent licenses ' \
                 'granted to You under this License for that Work shall terminate ' \
                 'as of the date such litigation is filed. ' \
                 '\n\n4. Redistribution. You may reproduce and distribute copies of the ' \
                 'Work or Derivative Works thereof in any medium, with or without ' \
                 'modifications, and in Source or Object form, provided that You' \
                 ' meet the following conditions: ' \
                 '\n(a) You must give any other recipients of the Work or' \
                 'Derivative Works a copy of this License; and' \
                 '\n\n(b) You must cause any modified files to carry prominent notices ' \
                 'stating that You changed the files; and ' \
                 '\n\n(c) You must retain, in the Source form of any Derivative Works' \
                 ' that You distribute, all copyright, patent, trademark, and ' \
                 'attribution notices from the Source form of the Work,' \
                 'excluding those notices that do not pertain to any part of ' \
                 'the Derivative Works; and ' \
                 '\n\n(d) If the Work includes a "NOTICE" text file as part of its ' \
                 'distribution, then any Derivative Works that You distribute must ' \
                 'include a readable copy of the attribution notices contained ' \
                 'within such NOTICE file, excluding those notices that do not ' \
                 'pertain to any part of the Derivative Works, in at least one ' \
                 'of the following places: within a NOTICE text file distributed ' \
                 'as part of the Derivative Works; within the Source form or ' \
                 'documentation, if provided along with the Derivative Works; or, ' \
                 'within a display generated by the Derivative Works, if and ' \
                 'wherever such third-party notices normally appear. The contents ' \
                 'of the NOTICE file are for informational purposes only and ' \
                 'do not modify the License. You may add Your own attribution ' \
                 'notices within Derivative Works that You distribute, alongside' \
                 ' or as an addendum to the NOTICE text from the Work, provided ' \
                 'that such additional attribution notices cannot be construed ' \
                 'as modifying the License.' \
                 '\n\nYou may add Your own copyright statement to Your modifications and ' \
                 'may provide additional or different license terms and conditions ' \
                 'for use, reproduction, or distribution of Your modifications, or ' \
                 'for any such Derivative Works as a whole, provided Your use, ' \
                 'reproduction, and distribution of the Work otherwise complies with' \
                 ' the conditions stated in this License.' \
                 '\n\n5. Submission of Contributions. Unless You explicitly state otherwise, ' \
                 'any Contribution intentionally submitted for inclusion in the Work ' \
                 'by You to the Licensor shall be under the terms and conditions of ' \
                 'this License, without any additional terms or conditions. ' \
                 'Notwithstanding the above, nothing herein shall supersede or modify ' \
                 'the terms of any separate license agreement you may have executed ' \
                 'with Licensor regarding such Contributions. ' \
                 '\n\n6. Trademarks. This License does not grant permission to use the trade ' \
                 'names, trademarks, service marks, or product names of the Licensor, ' \
                 'except as required for reasonable and customary use in describing the ' \
                 'origin of the Work and reproducing the content of the NOTICE file.' \
                 '\n\n7. Disclaimer of Warranty. Unless required by applicable law or ' \
                 'agreed to in writing, Licensor provides the Work (and each ' \
                 'Contributor provides its Contributions) on an "AS IS" BASIS, ' \
                 ' WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or ' \
                 'implied, including, without limitation, any warranties or conditions ' \
                 'of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A ' \
                 'PARTICULAR PURPOSE. You are solely responsible for determining the ' \
                 'appropriateness of using or redistributing the Work and assume any ' \
                 'risks associated with Your exercise of permissions under this License.' \
                 '\n\n8. Limitation of Liability. In no event and under no legal theory, ' \
                 'whether in tort (including negligence), contract, or otherwise, ' \
                 'unless required by applicable law (such as deliberate and grossly ' \
                 'negligent acts) or agreed to in writing, shall any Contributor be ' \
                 'liable to You for damages, including any direct, indirect, special, ' \
                 'incidental, or consequential damages of any character arising as a ' \
                 'result of this License or out of the use or inability to use the ' \
                 'Work (including but not limited to damages for loss of goodwill, ' \
                 'work stoppage, computer failure or malfunction, or any and all ' \
                 'other commercial damages or losses), even if such Contributor ' \
                 'has been advised of the possibility of such damages. ' \
                 '\n\n9. Accepting Warranty or Additional Liability. While redistributing ' \
                 'the Work or Derivative Works thereof, You may choose to offer, ' \
                 'and charge a fee for, acceptance of support, warranty, indemnity, ' \
                 'or other liability obligations and/or rights consistent with this ' \
                 'License. However, in accepting such obligations, You may act only ' \
                 'on Your own behalf and on Your sole responsibility, not on behalf ' \
                 'of any other Contributor, and only if You agree to indemnify, ' \
                 'defend, and hold each Contributor harmless for any liability ' \
                 'incurred by, or claims asserted against, such Contributor by reason ' \
                 'of your accepting any such warranty or additional liability.' \
                 '\n\nEND OF TERMS AND CONDITIONS' \
                 '\n\nCopyright 2023 Chunli Tang' \
                 '\n\nLicensed under the Apache License, Version 2.0 (the "License");' \
                 '\nyou may not use this file except in compliance with the License.' \
                 '\nYou may obtain a copy of the License at' \
                 '\n\n\thttp://www.apache.org/licenses/LICENSE-2.0' \
                 '\n\nUnless required by applicable law or agreed to in writing, software' \
                 ' distributed under the License is distributed on an "AS IS" BASIS, ' \
                 'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ' \
                 'See the License for the specific language governing permissions and ' \
                 'limitations under the License.'
    return disclaimer

def ack():
    acknowledge = 'This work was supported by NSF EPM Grant No. DMR-2129879 ' \
                  '\n\nWe would like to give a special thanks to: \nBrian Opatosky, Matt Galinger, J Isaac Garcia'
    return acknowledge


def showSymbol(symbol):
    if str(symbol) == 'theta':
        return chr(952)
    else:
        return symbol

def parse(d):
    dictionary = {}
    # Removes curly braces and splits the pairs into a list
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        # Other symbols from the key-value pair should be stripped.
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary
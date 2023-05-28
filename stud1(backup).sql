PGDMP                         {            GoStudy    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16493    GoStudy    DATABASE     }   CREATE DATABASE "GoStudy" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE "GoStudy";
                postgres    false                       0    0    GoStudy    DATABASE PROPERTIES     0   ALTER DATABASE "GoStudy" CONNECTION LIMIT = 10;
                     postgres    false            �            1259    24629    student_tt1    TABLE     �  CREATE TABLE public.student_tt1 (
    group_number character varying(10) NOT NULL,
    period_number integer NOT NULL,
    monday_subject character varying(180),
    monday_class character varying(32),
    tuesday_subject character varying(180),
    tuesday_class character varying(32),
    wednesday_subject character varying(180),
    wednesday_class character varying(32),
    thursday_subject character varying(180),
    thursday_class character varying(32),
    friday_subject character varying(180),
    friday_class character varying(32),
    saturday_subject character varying(180),
    saturday_class character varying(32),
    id integer NOT NULL
);
    DROP TABLE public.student_tt1;
       public         heap    postgres    false            �            1259    24634    student_tt1_id_seq    SEQUENCE     �   CREATE SEQUENCE public.student_tt1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.student_tt1_id_seq;
       public          postgres    false    222                       0    0    student_tt1_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.student_tt1_id_seq OWNED BY public.student_tt1.id;
          public          postgres    false    223            w           2604    24635    student_tt1 id    DEFAULT     p   ALTER TABLE ONLY public.student_tt1 ALTER COLUMN id SET DEFAULT nextval('public.student_tt1_id_seq'::regclass);
 =   ALTER TABLE public.student_tt1 ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    222                      0    24629    student_tt1 
   TABLE DATA           
  COPY public.student_tt1 (group_number, period_number, monday_subject, monday_class, tuesday_subject, tuesday_class, wednesday_subject, wednesday_class, thursday_subject, thursday_class, friday_subject, friday_class, saturday_subject, saturday_class, id) FROM stdin;
    public          postgres    false    222   S                  0    0    student_tt1_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.student_tt1_id_seq', 890, true);
          public          postgres    false    223            y           2606    24642    student_tt1 student_tt1_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.student_tt1
    ADD CONSTRAINT student_tt1_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.student_tt1 DROP CONSTRAINT student_tt1_pkey;
       public            postgres    false    222                  x��=ˎ�q��Wܥp���Y:6q`���*@ �䍁� R��X�(Y�ǑL�NV
����/���|INթ:������k��Z�̽�UU��U����(>�����|���O�g�y}�P���l�]�r�@�%�������ó��>�O�K���F�p]����)~�z��қw��e�Y����{b��ƥ\�B|(~����Ɏ�7b�כ��b�W��o���_˟a̸�l��	������+5�5����v��������9T|x��m��U��bɧ���������+��C�߇�Op�bq$�5��~�+�n��M������A~P�I��R�>��:����;���s��2j#6��-W �,�{��:�uh{����dA���K���Ɠ���O�W�o6���������V��>��<p�M�!I��2e�G΃�l��~�,~.	��/�DѼ	��XA���4`�k���no��2�?��3D��b`n�������9�O��FK/�X����������0I㭿�"E@<۵����Y��踉�N���ޭ��n�	&~�$����pG��n�2����O�;��!�HH���A&x!����	͐�nJ��8R�r�#�0n�X�Q���#�\qf����.p̙AeO B��l>�N�p�p"Q����T�4�D�|j R�-�NlI'�ci�R� >C��]�n5�Z
��[1v��,��0��%ӓ�����+���c��W��H�}�p�:��jz�;��u$�N��ᑁj���a 2�W&1�����c�����6��
�rԒG�UZe��}gQ�~�. �K�����M\%(������KcL�K-���.���pIP�� ?钠x�������*�C��/���l�&Ⱥ�E�9�77����_:�b�>�K�z��Kk���C\ʁkH���C*=�,��SC���������!.Qj�^*05�,Rhʽ낋`�����nS&(�XL�J���T�,Ki ����/[���b�2_u+�J��S��g�}�`��������g8(�;)����>[�|�!A�����I��!p��es��B"� -��1[�$������D��DS���X[P[PxL���/��)�0�rj�S�o�v!e�H �v�$��/в�iQx|I:���4����bd��Q��t"(�W�lK�)L��&ۭ�)L����}Ez�!Y"��Q���Ʉ4J�?��F��'�(�C���P�g��z�/�S��B��%��+����9k �wx�s���?ŏgJ<�s�l{M��������Y����ҡ��fsH��ĞT����=�Wx�_!�!*}	�ř��<�C۶�5�������8�h�!�x���Bb06n���F�u��6����-(\8Mc��<��>$-��E�^7I&��m	�F�&�j������ӗb��)�`��z�D-A��#Y�ɐ�FU�n��ۙ���'���@YOA���k�ma�Sm��6JB�] ]�K���d	s kq��=�1���Hܓ�s�~Arj+����dX$A�hФ܎㨭-{�qxn�\>o�F V�Q�6B4�m�����f��!_zHw���E��L����{���۱)?��~��H
�_���'t}�	oK`�P��c}ѱ{�m��p��|!͐��.}��Y�=����C��%�x�	pGJu���4�u<6d12X�@����Z�%Nr�M6�<ȩz���Ɖ��ͅg��|�z�K����Z�6T&�q�=��1N'�ٶ$ow@f1}�[��aH�I?_F�F<�e�/L{�K��T��2(1p�D��DIK��Nqۦ�a�lz}l���󒌔W�)E�*��%�͚ᄖ?���#�\�H�E���������J��wb���>�7n��]�[x%h��|��*�g���c9`YvCA�h�k`����K���2&�Ե]y}I�d���L��9�f����5�K@��\�<�n@�P�,�tL`�%�f�x�|	L��t���/~�ӟ�gX�؃�f16D�m��2r�>�c�Kln����wsA��������b����`��s3t�?7�~��A���s?뀬�1�)w��d�:5�9��]s���x}��OU)U�OW�����f9:����fv�а�B��uY�Iz7�I��d�T����� Zƈs�ek�7��zMx?xp��(hhߛ	�q 7�gbX�=?tï��!v�6��a�f�5���x&v�'N�P�B�aN"�,؏�x��s$��8֭��蘟������;6�!�"1^�f�-�J�NJN���j}8A�9=)�"i��ŝ4�vh&%�cx'�(����b���8P\{�|��_R	A	�^H[E�!6h�3n����%:���uaz��u@�b ��,�OZ�U����:�.z�"���ԿC�~k����d��$q0
�a�J���U9�m� ���d��YH������O�]1A�j��X�KCv��9d�$D��9uvK�����4��q�d�yI=�O#��Fj%N鑨�V2R�T�@6W0���ތfm�`�2��v�X��o5Wk[��]������i1�t_
��g�B%�V�|V=���|���7�<���]	Ħq���Ӛ�8�~Z�`yr@��*��Y"������ei�30���*�L�f��Q����[�J@�.fDa�A�tw�>�M�\Mt�V��U��<,h�D�u��T��y��-C�3S;�x�'KJb�ɒ���J�K9SȖ@:Λ�7���4��poƥ��Fz�^(��'�q�������)�Nwk�/ڀ��~�\Uky�S�Q��77�C<+R�\�HI
=ĳ"%1����@�d�F0	����z>�QÚr�N�]Н>&[nz�<k��� a(��:r��y��Y����Ձ�4g(xRJZ� O���<�S"��&���YR�ۀ��vQ��GV ��ˏ���軻z��/D>ԧh��؉�혯
�~+������(/��^�
��]��z���Л�t{�ɘRэ�9�٩��,�DW�1aT��N�U���=7
{�����:�樞���LiN*�͉/~����C�=�-�Z�� ս}�.��{v�$��f��{ĩ��1;�R!`c�U���UFD"K�V��!&��W�rn�4a�XȎ���rLg
��_!�
���ǶX˾���I>3�Y`{����π�=��9܌�YU	0�C�n@H����M�p�;��iݑ=P1����w���4H��S�Z�d�RVK	��#��;�D�;3Ϟ�D��!�w���y�R}���V�@�+��M��-�[Bl"��F=[��Qc��K�4WɦL�?��!�q{;���Pb�D���p�>�[rYS]<�z��d�0"�!�Msm5����e�X�DW���݄�GJ�*��:���tEZ�f��.LuWt4�0��Q�4�5ҫ�J����*��}���ݴhnĚ��ZHm���|,�Y�<��3�ǔ#��J��S������O:	�[e�9�|&� s�`���{�B�QCC���v?��&�L�ę��Q7�f�C,����U?��w]�]g/�����iȥW�wߵ4�<�<��<�a=-��MxZO�n�� O����9��z����Wz�/D�z���Z(��i�@Ώ�ޣ7��Ƙ�q�߉Wl��R�@������|���t�z_��ƚ�*��JG�'\���8 7��- l��~P寱�>iTԂ�٣�y���o�6��|jg�ޝ>s�P :�)��N��fo<� �W��f_�e�=���7����^�nۺ���=.��
\4�o7��m��_�吚z�7]Gq�֋XSp�3��ѯ��֢�[ݖq	�'3XȢ�Q��㗡��=��VXv���Q�w8Y����Q��Pѫ�6ZV3˽w�Q�ƴ���жh)���+������o�a�}V?km6�.,2�f��p�dE٧hԏ+Ѯ�f�tЏ2�+����9�C�r�`�z���O-V�($�Vz��Ќ���T#�F��me�u�N{)���o��f1�
�[>?� f0h��_    ���|��p8�'��丞c��Q�zkH��+,f��^ݞ�\��%���k��[XT��f%2�(�����Zu>e��L��{}TF)�X�h՛ۮ'�*J�@Q �[׹�)�|e�������\*g�6k�)�sx
ɲ��B�,y���d1�Pog��V/�YeQEz�g�E�!�т*�C<�U��xb����Rw����]6��'������hM�ŗ�tg����yǓJ�Yp�@o=�#ۗ�m�vVK��ݧ���7�yg>U ��O j���]_w�O��ͬ���[�˯�����{\�N\yaq�5�QP=�W����T⬒h^�tn�+w�����*@�gʚo��
&�����Uе��ޥ�L���^�NZ'X�F*�G���F�jh��-�Gf�-"?9�[�oQ�)�3�ϒR�8Zulh��~u���r4x��8���QWH�����awgA/�%d��I�HZR�(3��S�߫�cҒ|Q#<+J��c�J�m1�QpM1���(��[phbظ��Ra��2�K���� /6_*).1�9/��ф���;���t�a����^�s4���g���:���i���6۪�L�0�,}�@�..�~>�2gUiC���f�Y��qX��bz��v������7�6MgQƐ
��S.� >;#�#�,Y�H��-!�;'R�0����R�V�JSn��f�`?�%�*৸dі�).Y��pxn�3Ϟ�p'Mz�I,j����i㝱�ű2�\�������&�������!VS�V͋�PE���Q-��_"�^+���ŉ��`j�_T��ٲ8�0��Vgq���y��8�C<9GlP}#{񰝽x"��Lg�qm#	��=����󂻜�ݙ�q�y�ϛ>!��q��U:��<"�19j�hAؔ�<�y���y_���>����� ��8ѥ�v�����A�U���v���'�N@t�JB�Y+#�,T�)���ɪ�WTX�bl'�\a�W;���l/!�9��M�0P(��{���R���qJD�YzR\�çTh�t�1v� �*���W�#�R��ſ2�����ᆑ�f�W?�f��)�u!��+��6��ΉV�
�u�wf	��Y���ˡߌ"m���b�ZP��~Ͱ�fe�Ų���^��2Xƴ��\�b�����nIp���
|l��w�f�g��w�f�e��w�f���������X��(O�����ve�d��1�X͈)���!Î��/^P��ГZyd�\n�%���X5���7{<���iU�0ŐD6�y)�>]wtk�����[�Ͱ/wE)�3	M����BW���dIɈHV���v��.�!^2h-���g�4�����T�bX#��E�� ̊	3
�APC�gQST:0�8b0��2A��	o�V
��l-[8�;bȤ-S\v;-V���zw�#���Q��O�x� Ok4Mx��5��<��M����6���W�a��/�~�/y�V9�mYZ�u���W��3�A��m�ei��4D'K��ڛ���x�`�!�3�v(�u�bt Vlr'?�6f��$�=5�6f��4���.��F?���L���R�x��-��üR�#\(�ǚ9��7�����!���z��h��j����pߒ~��TmŚ�������T��������:���$�~�Y�p�,��s�$sQ+����ń
�8��V��q����rߩ#aX�i�T��pB��]FH��}D5gx~��Į{S#X�k��MEr�䅶~l&�x�"�]�ɧx��ZdX�W��M�pq����˟�_����X|� h���l�U;��T^+���3�3�w�n�����h�"'�־3�L� qi��ی�n�233��V�EO;�-�햬��#*𷃰'*̺YĜ�^į"9�S=�3�+��O[6���b��Ǝ��V��eӊ;��E��к����Su�/1f������y����Dp�+P���(���L�ew�	׻�Z�kޓX~>�6ט��c�qv[)�zb�9��XT�t��!>��"Dm�w38�ڵ�/��0�˷��Qe�F�V�{�a�U`v�64-�� z���Dz�T�׍LA����~�r�n�t�{עjV��S����hL���+�ʊq�O����r�N.o�P|�ӣAT:4�x$9��4�/�o'�XǏS��1\̄�_�Y��΃CVV��SM����_B%�ߘ�#lQ`�?i��P���u�֑h��w%yȧ[B���e��de?CG{�6h�VX(���O�h���&��-.�jOd�Q���1�>�}r+��]$�l�]��C5TPd�����"�WzN�0ʩ�Y�0Z�Ͷ��#��\s3z@���:�h�W���	"RxY4��vEOH]�xv1��"z_�i|I� ����Hٿ�*����F*g	��;��0���*U�E��Dπ�n5�#����N�P{��u��ZM��2��Ӄ�m�� ��ML=�{�]��b��-�Gv��_{j�vPly�#�&�.Ny����hAr��GPڮ_J��j�{�������w}���1�6d�M�QDj�����U!!
[��b���?�'��C<]��V�te�����,c=�;)b��2+������'��ͦ�T˙��1r5N��0M���xiv8_yD]j��t�}�?���^ח�Y�l�����z��ߠ�B��nCz(q=�%���	uJKS|�%~}����dɋDZ����@����ZĚ/l�^�4� �mH1��V��tjJI >|"	�*�m�i߈T���b��6���3�u���[K���G�0�&��E��R��j��9[�Mw�_7�J���y�����^�'M�?�j�������!(���1:��i��!Р��Pϊ�:F���3�1	+���*2�ina�4���&֩�����@"�ޮ�oqB�K�K��e���>�O�Յ��n�AZn��!�Zn��!�ZnU�!�ZnU�!����L]H���^���������v���C)LHe��=��-��o�/�RW�:����.�=_ VD�Vw�}A�1b��s~$7י �=��돇OaȃX2��I�� �Z-��"'��+�_1k�`f��Śz�.oUDz���
c��%�Dl�Jń ��R#J��,T�'�������bU���ժH��+��Z#��*R�1?VT��0[941`��	�d�1iӫ+�K.Rڭ�..��=����|9�č�V��$�<����ĜuT��X�)���i}��x�g�Lq���\gՙNsPC�Cy�#c�o�����ݶ������ ���b28��3KjϚ�d���{Z�ےxZ��J�
��;�;9|OZ��0�oK��dz8K&��b�!�O�y�̛o�*1}з�2q��h��<�]�؁�q�2*چ��\�*���2i�α����G���`[]�;oj/P�|,h��g�St�<~�zi?GI%z���$�R=�᪛�Z!�2��I��i2�'�"9&�~x�TƩ�����;�$%l����<���0'T�'�����Ψ]$
v��b?J}H_�~,�'����Q�a��lFp)UeQ���d\DVbN�[�5c�����|����]K]K�2��&��(#����$_-��IO�f��0�f�Ս��;˱�}~#n3=�a��ڳeX�]1��^�M���A����[�?Ԝ�W΢���'r�0 �X��OE���<��#�̞g�e��!��͏~����=���Is�}���Z�a
W��Rd�JL{)޷�w��1X��a:��Sדn������e<�C"	�ou��05|�j�{ՆI�߉=å��(�%%[��k���7?�#����얖mf���tE�o|���C�o|���C���\���q��x*�q��x*��V�'�I���nOt9z��.9=����޴�� �\��v��/�V��F/�>�Pv��z�b���<�'B�`5y1��h���K�Ew��a91pݡ<��'���ܒ�, '"f�'��i�4�ڑrh>qᰘ�A�͵� 0  �I�뤚yU��������g��kk@��}#7����蝵���^��a�;��M�ᤖ����[���;�fV�(��]�-�c�Џ�Q�/9��������Ο����/P�I�x�v-���9�K��T�M��� ��HY�g��w\�1���o��0>¡'�R_��ctK�hm�1?�9���iV�ôI�suMSgxj]^��g�}m1��X���5pm[S*��љ|	 u4?|�)�/�p8t�=�Eh����)��=�h��
Ox�d������ �������U���X�l.�n⼍��F�R:�
m+�l=� =7�d���=Zo*���C��Z�_aRz/:庴֎��Bf�<W@�T\*T��OW~��}����?��(hӯp;f[S$R�L-�"!o�ͫ��_�\FOQf=8��
E��t��~7������=z4(�簊���A�sB��6,�b�X\�{���t(�7����:4_�^�a=��|�
̷�0��*J�dL#*���M�<5, ʫkhz�k���Qhh��0|Y�k��7a'���)	z�U>�V����K|䌏����VɌjr}�@�O��vi���ܳ~������v!�E�J��o��wq��>Ǉ�
#���!�4T����3��R|i�M�@��7jKuGc(����}�q��};q(DMY��NEx\���s���2H�̬ʣ��qE��U�7�]�=#:��K���HĀdu]į�ռĮ~��x1t_U)��+�J����i�*W:�����Дf�0�����젙�� 7r��{��.a�����rtf-J�`�E1�L���R5C孒����^���;��z����=�h̠�Zz�(����!�s�~ᣖƤ���ڬ�t�K{*/i�|�V�&��z8����[��_Ip�Ez�g�K�!�Y/Y��xf�d����ezH�N9N`W��Ț�r�9��T��Sg�#��������T�~�C�l�Τ`��/O�*`q��T�k��{�ܱ���-�}����#͏JiPSp?HR?���n�'ȏ��J����-r���w��S^�)���cg�/�)�w^�c�u��f*Y4j<�3�zTb5\�eQN�?�ȗ������T�۠\p](5��͒Q�� ��A�P��+{�'��$�O��ۊF��Z�Ų �)lW�me�͒\�fM�k��+�4Tr|*�4�FZ��Sހg�od�qP01;�bg%���K^�;ّ�z4���O�Y��>���X����%�$W��K�	(oᴗ,B�e)���ʘ������K�8�*��&�dJ1k�<Az�6��"�}�cV�j�0=Ǜ���<�(��/��;��]e��w�A^�"�C<�(E��xzQ�R����BA���9ie�i�����.�;���>^w��$�kw6{p�FJ�4��>uw}v�0ԩ]��gxON�����tK�ܮR�.������BTQF�*JO�p��ըB;���om��6�B�!j�B#�}�!��<�l��/�U�;+Y:|�̰�����X���-I�����6z��]#|���s�g�MMc�j���^�6�$���N��5�\1L~�:��l~C�eTU�F������O��Y�y�%=`,�-:.�C��;�$����WҴ�j�]���i���;�}ק��0YwF�eDd��<�jǸ��%2k�^�(��� T�@[g+���W��N�U@�v\��Jn���)ԩ0�qCM������m�ȎY���DXo&��aͱE��,�o�jNl�ѭ�y1L��J�g��>��o3�\`TU[A�2���r��M�X<h1 �����������2a�� O��U��S&l3���<�ԙ&t�e΍��V׻��`~�*�n�9���m�<����4::�,ٮluz�ޒ�{�O�I[+��U��Ӻ��ڙΜ��S�ř	4��ڕ��تz�^GVXj�GJ(02����6�.0�cK��`��+�8��S恬����-"DH�V�³h:�'��+2�nro
P~���f9�G��F����`̌�|Ͷd�3�Ӡ7o��e�bY`����â��^[�E�'��;z�w��V�     
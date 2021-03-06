PGDMP     -                    y            automation_build    10.12    10.12 ?    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            ?           1262    4807877    automation_build    DATABASE     ?   CREATE DATABASE automation_build WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';
     DROP DATABASE automation_build;
             sysdba    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            ?           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            ?           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            ?            1259    4807878    ab_base_unit    TABLE     ^   CREATE TABLE public.ab_base_unit (
    id bigint NOT NULL,
    name character varying(255)
);
     DROP TABLE public.ab_base_unit;
       public         postgres    false    3            ?            1259    4807881    ab_base_volume    TABLE     ?   CREATE TABLE public.ab_base_volume (
    id bigint NOT NULL,
    name character varying,
    project_id bigint,
    base_unit_id bigint
);
 "   DROP TABLE public.ab_base_volume;
       public         postgres    false    3            ?            1259    4807887    ab_city    TABLE     ]   CREATE TABLE public.ab_city (
    id bigint NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.ab_city;
       public         postgres    false    3            ?            1259    4807893    ab_equipment    TABLE     ^   CREATE TABLE public.ab_equipment (
    id bigint NOT NULL,
    name character varying(255)
);
     DROP TABLE public.ab_equipment;
       public         postgres    false    3            ?            1259    4807896    ab_material    TABLE     ?   CREATE TABLE public.ab_material (
    id bigint NOT NULL,
    name character varying,
    articul character varying,
    unit_id bigint,
    subgroup_id bigint
);
    DROP TABLE public.ab_material;
       public         postgres    false    3            ?            1259    4807902    ab_material_category    TABLE     a   CREATE TABLE public.ab_material_category (
    id bigint NOT NULL,
    name character varying
);
 (   DROP TABLE public.ab_material_category;
       public         postgres    false    3            ?            1259    4807908    ab_material_group    TABLE        CREATE TABLE public.ab_material_group (
    id bigint NOT NULL,
    name character varying,
    material_category_id bigint
);
 %   DROP TABLE public.ab_material_group;
       public         postgres    false    3            ?            1259    4807914    ab_material_property    TABLE     ?   CREATE TABLE public.ab_material_property (
    id bigint NOT NULL,
    amount double precision,
    material_id bigint,
    prop_id bigint,
    unit_id bigint
);
 (   DROP TABLE public.ab_material_property;
       public         postgres    false    3            ?            1259    4807917    ab_material_subgroup    TABLE        CREATE TABLE public.ab_material_subgroup (
    id bigint NOT NULL,
    name character varying,
    material_group_id bigint
);
 (   DROP TABLE public.ab_material_subgroup;
       public         postgres    false    3            ?            1259    4807923 
   ab_product    TABLE     ?   CREATE TABLE public.ab_product (
    id bigint NOT NULL,
    price double precision,
    amount_for_one double precision,
    provider_id bigint,
    material_id bigint
);
    DROP TABLE public.ab_product;
       public         postgres    false    3            ?            1259    4807926 
   ab_project    TABLE     `   CREATE TABLE public.ab_project (
    id bigint NOT NULL,
    name character varying NOT NULL
);
    DROP TABLE public.ab_project;
       public         postgres    false    3            ?            1259    4807932    ab_property    TABLE     X   CREATE TABLE public.ab_property (
    id bigint NOT NULL,
    name character varying
);
    DROP TABLE public.ab_property;
       public         postgres    false    3            ?            1259    4807938    ab_provider    TABLE     q   CREATE TABLE public.ab_provider (
    id bigint NOT NULL,
    name character varying(255),
    city_id bigint
);
    DROP TABLE public.ab_provider;
       public         postgres    false    3            ?            1259    4807941    ab_technology_equipment    TABLE     {   CREATE TABLE public.ab_technology_equipment (
    id bigint NOT NULL,
    technology_id bigint,
    equipment_id bigint
);
 +   DROP TABLE public.ab_technology_equipment;
       public         postgres    false    3            ?            1259    4807944    ab_unit    TABLE     Y   CREATE TABLE public.ab_unit (
    id bigint NOT NULL,
    name character varying(255)
);
    DROP TABLE public.ab_unit;
       public         postgres    false    3            ?            1259    4807947    ab_work    TABLE     ?   CREATE TABLE public.ab_work (
    id bigint NOT NULL,
    name character varying,
    work_coefficient double precision,
    client_price double precision,
    work_price double precision,
    base_unit_id bigint,
    group_work_id bigint
);
    DROP TABLE public.ab_work;
       public         postgres    false    3            ?            1259    4807953    ab_work_group    TABLE     y   CREATE TABLE public.ab_work_group (
    id bigint NOT NULL,
    name character varying,
    work_technology_id bigint
);
 !   DROP TABLE public.ab_work_group;
       public         postgres    false    3            ?            1259    4807959    ab_work_material    TABLE     ?   CREATE TABLE public.ab_work_material (
    id bigint NOT NULL,
    amount double precision,
    material_id bigint,
    work_id bigint
);
 $   DROP TABLE public.ab_work_material;
       public         postgres    false    3            ?            1259    4807962    ab_work_stage    TABLE     Z   CREATE TABLE public.ab_work_stage (
    id bigint NOT NULL,
    name character varying
);
 !   DROP TABLE public.ab_work_stage;
       public         postgres    false    3            ?            1259    4807968    ab_work_technology    TABLE     y   CREATE TABLE public.ab_work_technology (
    id bigint NOT NULL,
    name character varying,
    work_stage_id bigint
);
 &   DROP TABLE public.ab_work_technology;
       public         postgres    false    3            ?            1259    4807974    base_unit_id_seq    SEQUENCE     y   CREATE SEQUENCE public.base_unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.base_unit_id_seq;
       public       postgres    false    3    196            ?           0    0    base_unit_id_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.base_unit_id_seq OWNED BY public.ab_base_unit.id;
            public       postgres    false    216            ?            1259    4807976    base_volume_id_seq    SEQUENCE     {   CREATE SEQUENCE public.base_volume_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.base_volume_id_seq;
       public       postgres    false    3    197            ?           0    0    base_volume_id_seq    SEQUENCE OWNED BY     L   ALTER SEQUENCE public.base_volume_id_seq OWNED BY public.ab_base_volume.id;
            public       postgres    false    217            ?            1259    4807978    city_id_seq    SEQUENCE     t   CREATE SEQUENCE public.city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.city_id_seq;
       public       postgres    false    198    3            ?           0    0    city_id_seq    SEQUENCE OWNED BY     >   ALTER SEQUENCE public.city_id_seq OWNED BY public.ab_city.id;
            public       postgres    false    218            ?            1259    4807980    equipment_id_seq    SEQUENCE     y   CREATE SEQUENCE public.equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.equipment_id_seq;
       public       postgres    false    3    199            ?           0    0    equipment_id_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.equipment_id_seq OWNED BY public.ab_equipment.id;
            public       postgres    false    219            ?            1259    4807982    material_category_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.material_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.material_category_id_seq;
       public       postgres    false    201    3            ?           0    0    material_category_id_seq    SEQUENCE OWNED BY     X   ALTER SEQUENCE public.material_category_id_seq OWNED BY public.ab_material_category.id;
            public       postgres    false    220            ?            1259    4807984    material_group_id_seq    SEQUENCE     ~   CREATE SEQUENCE public.material_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.material_group_id_seq;
       public       postgres    false    202    3            ?           0    0    material_group_id_seq    SEQUENCE OWNED BY     R   ALTER SEQUENCE public.material_group_id_seq OWNED BY public.ab_material_group.id;
            public       postgres    false    221            ?            1259    4807986    material_id_seq    SEQUENCE     x   CREATE SEQUENCE public.material_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.material_id_seq;
       public       postgres    false    200    3            ?           0    0    material_id_seq    SEQUENCE OWNED BY     F   ALTER SEQUENCE public.material_id_seq OWNED BY public.ab_material.id;
            public       postgres    false    222            ?            1259    4807988    material_property_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.material_property_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.material_property_id_seq;
       public       postgres    false    3    203            ?           0    0    material_property_id_seq    SEQUENCE OWNED BY     X   ALTER SEQUENCE public.material_property_id_seq OWNED BY public.ab_material_property.id;
            public       postgres    false    223            ?            1259    4807990    material_subgroup_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.material_subgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.material_subgroup_id_seq;
       public       postgres    false    3    204            ?           0    0    material_subgroup_id_seq    SEQUENCE OWNED BY     X   ALTER SEQUENCE public.material_subgroup_id_seq OWNED BY public.ab_material_subgroup.id;
            public       postgres    false    224            ?            1259    4807992    product_id_seq    SEQUENCE     w   CREATE SEQUENCE public.product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.product_id_seq;
       public       postgres    false    3    205            ?           0    0    product_id_seq    SEQUENCE OWNED BY     D   ALTER SEQUENCE public.product_id_seq OWNED BY public.ab_product.id;
            public       postgres    false    225            ?            1259    4807994    project_id_seq    SEQUENCE     w   CREATE SEQUENCE public.project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.project_id_seq;
       public       postgres    false    3    206            ?           0    0    project_id_seq    SEQUENCE OWNED BY     D   ALTER SEQUENCE public.project_id_seq OWNED BY public.ab_project.id;
            public       postgres    false    226            ?            1259    4807996    property_id_seq    SEQUENCE     x   CREATE SEQUENCE public.property_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.property_id_seq;
       public       postgres    false    3    207            ?           0    0    property_id_seq    SEQUENCE OWNED BY     F   ALTER SEQUENCE public.property_id_seq OWNED BY public.ab_property.id;
            public       postgres    false    227            ?            1259    4807998    provider_id_seq    SEQUENCE     x   CREATE SEQUENCE public.provider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.provider_id_seq;
       public       postgres    false    3    208            ?           0    0    provider_id_seq    SEQUENCE OWNED BY     F   ALTER SEQUENCE public.provider_id_seq OWNED BY public.ab_provider.id;
            public       postgres    false    228            ?            1259    4808000    technology_equipment_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.technology_equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.technology_equipment_id_seq;
       public       postgres    false    3    209            ?           0    0    technology_equipment_id_seq    SEQUENCE OWNED BY     ^   ALTER SEQUENCE public.technology_equipment_id_seq OWNED BY public.ab_technology_equipment.id;
            public       postgres    false    229            ?            1259    4808002    unit_id_seq    SEQUENCE     t   CREATE SEQUENCE public.unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.unit_id_seq;
       public       postgres    false    3    210            ?           0    0    unit_id_seq    SEQUENCE OWNED BY     >   ALTER SEQUENCE public.unit_id_seq OWNED BY public.ab_unit.id;
            public       postgres    false    230            ?            1259    4808004    work_group_id_seq    SEQUENCE     z   CREATE SEQUENCE public.work_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.work_group_id_seq;
       public       postgres    false    3    212            ?           0    0    work_group_id_seq    SEQUENCE OWNED BY     J   ALTER SEQUENCE public.work_group_id_seq OWNED BY public.ab_work_group.id;
            public       postgres    false    231            ?            1259    4808006    work_id_seq    SEQUENCE     t   CREATE SEQUENCE public.work_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.work_id_seq;
       public       postgres    false    3    211            ?           0    0    work_id_seq    SEQUENCE OWNED BY     >   ALTER SEQUENCE public.work_id_seq OWNED BY public.ab_work.id;
            public       postgres    false    232            ?            1259    4808008    work_material_id_seq    SEQUENCE     }   CREATE SEQUENCE public.work_material_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.work_material_id_seq;
       public       postgres    false    3    213            ?           0    0    work_material_id_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE public.work_material_id_seq OWNED BY public.ab_work_material.id;
            public       postgres    false    233            ?            1259    4808010    work_stage_id_seq    SEQUENCE     z   CREATE SEQUENCE public.work_stage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.work_stage_id_seq;
       public       postgres    false    214    3            ?           0    0    work_stage_id_seq    SEQUENCE OWNED BY     J   ALTER SEQUENCE public.work_stage_id_seq OWNED BY public.ab_work_stage.id;
            public       postgres    false    234            ?            1259    4808012    work_technology_id_seq    SEQUENCE        CREATE SEQUENCE public.work_technology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.work_technology_id_seq;
       public       postgres    false    3    215            ?           0    0    work_technology_id_seq    SEQUENCE OWNED BY     T   ALTER SEQUENCE public.work_technology_id_seq OWNED BY public.ab_work_technology.id;
            public       postgres    false    235            ?
           2604    4808014    ab_base_unit id    DEFAULT     o   ALTER TABLE ONLY public.ab_base_unit ALTER COLUMN id SET DEFAULT nextval('public.base_unit_id_seq'::regclass);
 >   ALTER TABLE public.ab_base_unit ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    216    196            ?
           2604    4808015    ab_base_volume id    DEFAULT     s   ALTER TABLE ONLY public.ab_base_volume ALTER COLUMN id SET DEFAULT nextval('public.base_volume_id_seq'::regclass);
 @   ALTER TABLE public.ab_base_volume ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    217    197            ?
           2604    4808016 
   ab_city id    DEFAULT     e   ALTER TABLE ONLY public.ab_city ALTER COLUMN id SET DEFAULT nextval('public.city_id_seq'::regclass);
 9   ALTER TABLE public.ab_city ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    218    198            ?
           2604    4808017    ab_equipment id    DEFAULT     o   ALTER TABLE ONLY public.ab_equipment ALTER COLUMN id SET DEFAULT nextval('public.equipment_id_seq'::regclass);
 >   ALTER TABLE public.ab_equipment ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    219    199            ?
           2604    4808018    ab_material id    DEFAULT     m   ALTER TABLE ONLY public.ab_material ALTER COLUMN id SET DEFAULT nextval('public.material_id_seq'::regclass);
 =   ALTER TABLE public.ab_material ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    222    200            ?
           2604    4808019    ab_material_category id    DEFAULT        ALTER TABLE ONLY public.ab_material_category ALTER COLUMN id SET DEFAULT nextval('public.material_category_id_seq'::regclass);
 F   ALTER TABLE public.ab_material_category ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    220    201            ?
           2604    4808020    ab_material_group id    DEFAULT     y   ALTER TABLE ONLY public.ab_material_group ALTER COLUMN id SET DEFAULT nextval('public.material_group_id_seq'::regclass);
 C   ALTER TABLE public.ab_material_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    221    202            ?
           2604    4808021    ab_material_property id    DEFAULT        ALTER TABLE ONLY public.ab_material_property ALTER COLUMN id SET DEFAULT nextval('public.material_property_id_seq'::regclass);
 F   ALTER TABLE public.ab_material_property ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    223    203            ?
           2604    4808022    ab_material_subgroup id    DEFAULT        ALTER TABLE ONLY public.ab_material_subgroup ALTER COLUMN id SET DEFAULT nextval('public.material_subgroup_id_seq'::regclass);
 F   ALTER TABLE public.ab_material_subgroup ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    224    204            ?
           2604    4808023    ab_product id    DEFAULT     k   ALTER TABLE ONLY public.ab_product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);
 <   ALTER TABLE public.ab_product ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    225    205            ?
           2604    4808024    ab_project id    DEFAULT     k   ALTER TABLE ONLY public.ab_project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);
 <   ALTER TABLE public.ab_project ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    226    206            ?
           2604    4808025    ab_property id    DEFAULT     m   ALTER TABLE ONLY public.ab_property ALTER COLUMN id SET DEFAULT nextval('public.property_id_seq'::regclass);
 =   ALTER TABLE public.ab_property ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    227    207            ?
           2604    4808026    ab_provider id    DEFAULT     m   ALTER TABLE ONLY public.ab_provider ALTER COLUMN id SET DEFAULT nextval('public.provider_id_seq'::regclass);
 =   ALTER TABLE public.ab_provider ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    228    208            ?
           2604    4808027    ab_technology_equipment id    DEFAULT     ?   ALTER TABLE ONLY public.ab_technology_equipment ALTER COLUMN id SET DEFAULT nextval('public.technology_equipment_id_seq'::regclass);
 I   ALTER TABLE public.ab_technology_equipment ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    229    209            ?
           2604    4808028 
   ab_unit id    DEFAULT     e   ALTER TABLE ONLY public.ab_unit ALTER COLUMN id SET DEFAULT nextval('public.unit_id_seq'::regclass);
 9   ALTER TABLE public.ab_unit ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    230    210            ?
           2604    4808029 
   ab_work id    DEFAULT     e   ALTER TABLE ONLY public.ab_work ALTER COLUMN id SET DEFAULT nextval('public.work_id_seq'::regclass);
 9   ALTER TABLE public.ab_work ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    232    211            ?
           2604    4808030    ab_work_group id    DEFAULT     q   ALTER TABLE ONLY public.ab_work_group ALTER COLUMN id SET DEFAULT nextval('public.work_group_id_seq'::regclass);
 ?   ALTER TABLE public.ab_work_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    231    212            ?
           2604    4808031    ab_work_material id    DEFAULT     w   ALTER TABLE ONLY public.ab_work_material ALTER COLUMN id SET DEFAULT nextval('public.work_material_id_seq'::regclass);
 B   ALTER TABLE public.ab_work_material ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    233    213            ?
           2604    4808032    ab_work_stage id    DEFAULT     q   ALTER TABLE ONLY public.ab_work_stage ALTER COLUMN id SET DEFAULT nextval('public.work_stage_id_seq'::regclass);
 ?   ALTER TABLE public.ab_work_stage ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    234    214            ?
           2604    4808033    ab_work_technology id    DEFAULT     {   ALTER TABLE ONLY public.ab_work_technology ALTER COLUMN id SET DEFAULT nextval('public.work_technology_id_seq'::regclass);
 D   ALTER TABLE public.ab_work_technology ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    235    215            ?          0    4807878    ab_base_unit 
   TABLE DATA               0   COPY public.ab_base_unit (id, name) FROM stdin;
    public       postgres    false    196   V?       ?          0    4807881    ab_base_volume 
   TABLE DATA               L   COPY public.ab_base_volume (id, name, project_id, base_unit_id) FROM stdin;
    public       postgres    false    197   s?       ?          0    4807887    ab_city 
   TABLE DATA               +   COPY public.ab_city (id, name) FROM stdin;
    public       postgres    false    198   ??       ?          0    4807893    ab_equipment 
   TABLE DATA               0   COPY public.ab_equipment (id, name) FROM stdin;
    public       postgres    false    199   ??       ?          0    4807896    ab_material 
   TABLE DATA               N   COPY public.ab_material (id, name, articul, unit_id, subgroup_id) FROM stdin;
    public       postgres    false    200   ?       ?          0    4807902    ab_material_category 
   TABLE DATA               8   COPY public.ab_material_category (id, name) FROM stdin;
    public       postgres    false    201   ?       ?          0    4807908    ab_material_group 
   TABLE DATA               K   COPY public.ab_material_group (id, name, material_category_id) FROM stdin;
    public       postgres    false    202   ;?       ?          0    4807914    ab_material_property 
   TABLE DATA               Y   COPY public.ab_material_property (id, amount, material_id, prop_id, unit_id) FROM stdin;
    public       postgres    false    203   X?       ?          0    4807917    ab_material_subgroup 
   TABLE DATA               K   COPY public.ab_material_subgroup (id, name, material_group_id) FROM stdin;
    public       postgres    false    204   u?       ?          0    4807923 
   ab_product 
   TABLE DATA               Y   COPY public.ab_product (id, price, amount_for_one, provider_id, material_id) FROM stdin;
    public       postgres    false    205   ??       ?          0    4807926 
   ab_project 
   TABLE DATA               .   COPY public.ab_project (id, name) FROM stdin;
    public       postgres    false    206   ??       ?          0    4807932    ab_property 
   TABLE DATA               /   COPY public.ab_property (id, name) FROM stdin;
    public       postgres    false    207   ??       ?          0    4807938    ab_provider 
   TABLE DATA               8   COPY public.ab_provider (id, name, city_id) FROM stdin;
    public       postgres    false    208   ??       ?          0    4807941    ab_technology_equipment 
   TABLE DATA               R   COPY public.ab_technology_equipment (id, technology_id, equipment_id) FROM stdin;
    public       postgres    false    209   W?       ?          0    4807944    ab_unit 
   TABLE DATA               +   COPY public.ab_unit (id, name) FROM stdin;
    public       postgres    false    210   t?       ?          0    4807947    ab_work 
   TABLE DATA               t   COPY public.ab_work (id, name, work_coefficient, client_price, work_price, base_unit_id, group_work_id) FROM stdin;
    public       postgres    false    211   ??       ?          0    4807953    ab_work_group 
   TABLE DATA               E   COPY public.ab_work_group (id, name, work_technology_id) FROM stdin;
    public       postgres    false    212   ??       ?          0    4807959    ab_work_material 
   TABLE DATA               L   COPY public.ab_work_material (id, amount, material_id, work_id) FROM stdin;
    public       postgres    false    213   ??       ?          0    4807962    ab_work_stage 
   TABLE DATA               1   COPY public.ab_work_stage (id, name) FROM stdin;
    public       postgres    false    214   ??       ?          0    4807968    ab_work_technology 
   TABLE DATA               E   COPY public.ab_work_technology (id, name, work_stage_id) FROM stdin;
    public       postgres    false    215   ?       ?           0    0    base_unit_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.base_unit_id_seq', 2, true);
            public       postgres    false    216            ?           0    0    base_volume_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.base_volume_id_seq', 1, false);
            public       postgres    false    217            ?           0    0    city_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.city_id_seq', 24, true);
            public       postgres    false    218            ?           0    0    equipment_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.equipment_id_seq', 1, false);
            public       postgres    false    219            ?           0    0    material_category_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.material_category_id_seq', 2, true);
            public       postgres    false    220            ?           0    0    material_group_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.material_group_id_seq', 6, true);
            public       postgres    false    221            ?           0    0    material_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.material_id_seq', 1, true);
            public       postgres    false    222                        0    0    material_property_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.material_property_id_seq', 2, true);
            public       postgres    false    223                       0    0    material_subgroup_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.material_subgroup_id_seq', 3, true);
            public       postgres    false    224                       0    0    product_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.product_id_seq', 1, true);
            public       postgres    false    225                       0    0    project_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.project_id_seq', 1, true);
            public       postgres    false    226                       0    0    property_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.property_id_seq', 1, true);
            public       postgres    false    227                       0    0    provider_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.provider_id_seq', 21, true);
            public       postgres    false    228                       0    0    technology_equipment_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.technology_equipment_id_seq', 1, false);
            public       postgres    false    229                       0    0    unit_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.unit_id_seq', 24, true);
            public       postgres    false    230                       0    0    work_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.work_group_id_seq', 1, true);
            public       postgres    false    231            	           0    0    work_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.work_id_seq', 2, true);
            public       postgres    false    232            
           0    0    work_material_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.work_material_id_seq', 2, true);
            public       postgres    false    233                       0    0    work_stage_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.work_stage_id_seq', 2, true);
            public       postgres    false    234                       0    0    work_technology_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.work_technology_id_seq', 1, true);
            public       postgres    false    235                       2606    4808035    ab_base_unit ab_base_unit_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.ab_base_unit
    ADD CONSTRAINT ab_base_unit_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.ab_base_unit DROP CONSTRAINT ab_base_unit_pkey;
       public         postgres    false    196                       2606    4808037 "   ab_base_volume ab_base_volume_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.ab_base_volume DROP CONSTRAINT ab_base_volume_pkey;
       public         postgres    false    197                       2606    4808039    ab_city ab_city_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.ab_city
    ADD CONSTRAINT ab_city_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.ab_city DROP CONSTRAINT ab_city_pkey;
       public         postgres    false    198                       2606    4808041    ab_equipment ab_equipment_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.ab_equipment
    ADD CONSTRAINT ab_equipment_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.ab_equipment DROP CONSTRAINT ab_equipment_pkey;
       public         postgres    false    199                       2606    4808043 .   ab_material_category ab_material_category_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.ab_material_category
    ADD CONSTRAINT ab_material_category_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.ab_material_category DROP CONSTRAINT ab_material_category_pkey;
       public         postgres    false    201                       2606    4808045 (   ab_material_group ab_material_group_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ab_material_group
    ADD CONSTRAINT ab_material_group_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.ab_material_group DROP CONSTRAINT ab_material_group_pkey;
       public         postgres    false    202            	           2606    4808047    ab_material ab_material_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.ab_material DROP CONSTRAINT ab_material_pkey;
       public         postgres    false    200                       2606    4808049 .   ab_material_property ab_material_property_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.ab_material_property DROP CONSTRAINT ab_material_property_pkey;
       public         postgres    false    203                       2606    4808051 .   ab_material_subgroup ab_material_subgroup_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.ab_material_subgroup
    ADD CONSTRAINT ab_material_subgroup_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.ab_material_subgroup DROP CONSTRAINT ab_material_subgroup_pkey;
       public         postgres    false    204                       2606    4808053    ab_product ab_product_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.ab_product DROP CONSTRAINT ab_product_pkey;
       public         postgres    false    205                       2606    4808055    ab_project ab_project_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.ab_project
    ADD CONSTRAINT ab_project_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.ab_project DROP CONSTRAINT ab_project_pkey;
       public         postgres    false    206                       2606    4808057    ab_property ab_property_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ab_property
    ADD CONSTRAINT ab_property_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.ab_property DROP CONSTRAINT ab_property_pkey;
       public         postgres    false    207                       2606    4808059    ab_provider ab_provider_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.ab_provider
    ADD CONSTRAINT ab_provider_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.ab_provider DROP CONSTRAINT ab_provider_pkey;
       public         postgres    false    208                       2606    4808061 4   ab_technology_equipment ab_technology_equipment_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.ab_technology_equipment DROP CONSTRAINT ab_technology_equipment_pkey;
       public         postgres    false    209                       2606    4808063    ab_unit ab_unit_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.ab_unit
    ADD CONSTRAINT ab_unit_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.ab_unit DROP CONSTRAINT ab_unit_pkey;
       public         postgres    false    210            !           2606    4808065     ab_work_group ab_work_group_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.ab_work_group
    ADD CONSTRAINT ab_work_group_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.ab_work_group DROP CONSTRAINT ab_work_group_pkey;
       public         postgres    false    212            #           2606    4808067 &   ab_work_material ab_work_material_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.ab_work_material DROP CONSTRAINT ab_work_material_pkey;
       public         postgres    false    213                       2606    4808069    ab_work ab_work_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.ab_work DROP CONSTRAINT ab_work_pkey;
       public         postgres    false    211            %           2606    4808071     ab_work_stage ab_work_stage_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.ab_work_stage
    ADD CONSTRAINT ab_work_stage_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.ab_work_stage DROP CONSTRAINT ab_work_stage_pkey;
       public         postgres    false    214            '           2606    4808073 *   ab_work_technology ab_work_technology_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.ab_work_technology
    ADD CONSTRAINT ab_work_technology_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.ab_work_technology DROP CONSTRAINT ab_work_technology_pkey;
       public         postgres    false    215            (           2606    4808074 ,   ab_base_volume ab_base_volume_base_unit_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_base_unit_fkey FOREIGN KEY (base_unit_id) REFERENCES public.ab_base_unit(id) NOT VALID;
 V   ALTER TABLE ONLY public.ab_base_volume DROP CONSTRAINT ab_base_volume_base_unit_fkey;
       public       postgres    false    196    197    2817            )           2606    4808079 *   ab_base_volume ab_base_volume_project_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_project_fkey FOREIGN KEY (project_id) REFERENCES public.ab_project(id) NOT VALID;
 T   ALTER TABLE ONLY public.ab_base_volume DROP CONSTRAINT ab_base_volume_project_fkey;
       public       postgres    false    2837    197    206            ,           2606    4808175 =   ab_material_group ab_material_group_material_category_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material_group
    ADD CONSTRAINT ab_material_group_material_category_id_fkey FOREIGN KEY (material_category_id) REFERENCES public.ab_material_category(id) NOT VALID;
 g   ALTER TABLE ONLY public.ab_material_group DROP CONSTRAINT ab_material_group_material_category_id_fkey;
       public       postgres    false    2827    202    201            -           2606    4808089 7   ab_material_property ab_material_property_material_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;
 a   ALTER TABLE ONLY public.ab_material_property DROP CONSTRAINT ab_material_property_material_fkey;
       public       postgres    false    2825    203    200            .           2606    4808094 7   ab_material_property ab_material_property_property_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_property_fkey FOREIGN KEY (prop_id) REFERENCES public.ab_property(id) NOT VALID;
 a   ALTER TABLE ONLY public.ab_material_property DROP CONSTRAINT ab_material_property_property_fkey;
       public       postgres    false    203    2839    207            /           2606    4808099 3   ab_material_property ab_material_property_unit_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_unit_fkey FOREIGN KEY (unit_id) REFERENCES public.ab_unit(id) NOT VALID;
 ]   ALTER TABLE ONLY public.ab_material_property DROP CONSTRAINT ab_material_property_unit_fkey;
       public       postgres    false    2845    203    210            *           2606    4808104 %   ab_material ab_material_subgroup_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_subgroup_fkey FOREIGN KEY (subgroup_id) REFERENCES public.ab_material_subgroup(id) NOT VALID;
 O   ALTER TABLE ONLY public.ab_material DROP CONSTRAINT ab_material_subgroup_fkey;
       public       postgres    false    2833    200    204            0           2606    4808109 =   ab_material_subgroup ab_material_subgroup_material_group_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material_subgroup
    ADD CONSTRAINT ab_material_subgroup_material_group_fkey FOREIGN KEY (material_group_id) REFERENCES public.ab_material_group(id) NOT VALID;
 g   ALTER TABLE ONLY public.ab_material_subgroup DROP CONSTRAINT ab_material_subgroup_material_group_fkey;
       public       postgres    false    202    204    2829            +           2606    4808114 !   ab_material ab_material_unit_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_unit_fkey FOREIGN KEY (unit_id) REFERENCES public.ab_unit(id) NOT VALID;
 K   ALTER TABLE ONLY public.ab_material DROP CONSTRAINT ab_material_unit_fkey;
       public       postgres    false    200    210    2845            1           2606    4808119 #   ab_product ab_product_material_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;
 M   ALTER TABLE ONLY public.ab_product DROP CONSTRAINT ab_product_material_fkey;
       public       postgres    false    200    2825    205            2           2606    4808124 #   ab_product ab_product_provider_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_provider_fkey FOREIGN KEY (provider_id) REFERENCES public.ab_provider(id) NOT VALID;
 M   ALTER TABLE ONLY public.ab_product DROP CONSTRAINT ab_product_provider_fkey;
       public       postgres    false    205    2841    208            3           2606    4808129 $   ab_provider ab_provider_city_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_provider
    ADD CONSTRAINT ab_provider_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.ab_city(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;
 N   ALTER TABLE ONLY public.ab_provider DROP CONSTRAINT ab_provider_city_id_fkey;
       public       postgres    false    2821    208    198            4           2606    4808134 >   ab_technology_equipment ab_technology_equipment_equipment_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_equipment_fkey FOREIGN KEY (equipment_id) REFERENCES public.ab_equipment(id) NOT VALID;
 h   ALTER TABLE ONLY public.ab_technology_equipment DROP CONSTRAINT ab_technology_equipment_equipment_fkey;
       public       postgres    false    209    199    2823            5           2606    4808139 ?   ab_technology_equipment ab_technology_equipment_technology_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_technology_fkey FOREIGN KEY (technology_id) REFERENCES public.ab_work_technology(id) NOT VALID;
 i   ALTER TABLE ONLY public.ab_technology_equipment DROP CONSTRAINT ab_technology_equipment_technology_fkey;
       public       postgres    false    215    2855    209            6           2606    4808144    ab_work ab_work_base_unit_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_base_unit_fkey FOREIGN KEY (base_unit_id) REFERENCES public.ab_base_unit(id) NOT VALID;
 H   ALTER TABLE ONLY public.ab_work DROP CONSTRAINT ab_work_base_unit_fkey;
       public       postgres    false    211    196    2817            7           2606    4808149    ab_work ab_work_group_work_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_group_work_fkey FOREIGN KEY (group_work_id) REFERENCES public.ab_work_group(id) NOT VALID;
 I   ALTER TABLE ONLY public.ab_work DROP CONSTRAINT ab_work_group_work_fkey;
       public       postgres    false    212    2849    211            8           2606    4808154 0   ab_work_group ab_work_group_work_technology_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work_group
    ADD CONSTRAINT ab_work_group_work_technology_fkey FOREIGN KEY (work_technology_id) REFERENCES public.ab_work_technology(id) NOT VALID;
 Z   ALTER TABLE ONLY public.ab_work_group DROP CONSTRAINT ab_work_group_work_technology_fkey;
       public       postgres    false    215    2855    212            9           2606    4808159 /   ab_work_material ab_work_material_material_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;
 Y   ALTER TABLE ONLY public.ab_work_material DROP CONSTRAINT ab_work_material_material_fkey;
       public       postgres    false    2825    213    200            :           2606    4808164 +   ab_work_material ab_work_material_work_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_work_fkey FOREIGN KEY (work_id) REFERENCES public.ab_work(id) NOT VALID;
 U   ALTER TABLE ONLY public.ab_work_material DROP CONSTRAINT ab_work_material_work_fkey;
       public       postgres    false    211    213    2847            ;           2606    4808169 5   ab_work_technology ab_work_technology_work_stage_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.ab_work_technology
    ADD CONSTRAINT ab_work_technology_work_stage_fkey FOREIGN KEY (work_stage_id) REFERENCES public.ab_work_stage(id) NOT VALID;
 _   ALTER TABLE ONLY public.ab_work_technology DROP CONSTRAINT ab_work_technology_work_stage_fkey;
       public       postgres    false    215    2853    214            ?      x?????? ? ?      ?      x?????? ? ?      ?   D   x?9 ??21	Рыбинск
22	Ярославль
24	Тест
\.


?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?   ^   x?M??	?0 ??)?@̫t?Q;{kE'B ~???4??uw??s?`eK?è?|~¿޳s??+s?ӀcO#?Ө??_\??vܸ|???<??>?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?     
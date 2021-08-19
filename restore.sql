--
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 10.9
-- Dumped by pg_dump version 13.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE automation_build;
--
-- Name: automation_build; Type: DATABASE; Schema: -; Owner: sysdba
--

CREATE DATABASE automation_build WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Russian_Russia.1251';


ALTER DATABASE automation_build OWNER TO sysdba;

\connect automation_build

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- Name: ab_base_unit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_base_unit (
    id bigint NOT NULL,
    name character varying(255)
);


ALTER TABLE public.ab_base_unit OWNER TO postgres;

--
-- Name: ab_base_volume; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_base_volume (
    id bigint NOT NULL,
    name character varying,
    project_id bigint,
    base_unit_id bigint
);


ALTER TABLE public.ab_base_volume OWNER TO postgres;

--
-- Name: ab_city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_city (
    id bigint NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.ab_city OWNER TO postgres;

--
-- Name: ab_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_equipment (
    id bigint NOT NULL,
    name character varying(255)
);


ALTER TABLE public.ab_equipment OWNER TO postgres;

--
-- Name: ab_material; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_material (
    id bigint NOT NULL,
    name character varying,
    articul character varying,
    unit_id bigint,
    subgroup_id bigint
);


ALTER TABLE public.ab_material OWNER TO postgres;

--
-- Name: ab_material_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_material_category (
    id bigint NOT NULL,
    name character varying
);


ALTER TABLE public.ab_material_category OWNER TO postgres;

--
-- Name: ab_material_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_material_group (
    id bigint NOT NULL,
    name character varying,
    material_category_id bigint
);


ALTER TABLE public.ab_material_group OWNER TO postgres;

--
-- Name: ab_material_property; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_material_property (
    id bigint NOT NULL,
    amount double precision,
    material_id bigint,
    prop_id bigint,
    unit_id bigint
);


ALTER TABLE public.ab_material_property OWNER TO postgres;

--
-- Name: ab_material_subgroup; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_material_subgroup (
    id bigint NOT NULL,
    name character varying,
    material_group_id bigint
);


ALTER TABLE public.ab_material_subgroup OWNER TO postgres;

--
-- Name: ab_product; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_product (
    id bigint NOT NULL,
    price double precision,
    amount_for_one double precision,
    provider_id bigint,
    material_id bigint
);


ALTER TABLE public.ab_product OWNER TO postgres;

--
-- Name: ab_project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_project (
    id bigint NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.ab_project OWNER TO postgres;

--
-- Name: ab_property; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_property (
    id bigint NOT NULL,
    name character varying
);


ALTER TABLE public.ab_property OWNER TO postgres;

--
-- Name: ab_provider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_provider (
    id bigint NOT NULL,
    name character varying(255),
    city_id bigint
);


ALTER TABLE public.ab_provider OWNER TO postgres;

--
-- Name: ab_technology_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_technology_equipment (
    id bigint NOT NULL,
    technology_id bigint,
    equipment_id bigint
);


ALTER TABLE public.ab_technology_equipment OWNER TO postgres;

--
-- Name: ab_unit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_unit (
    id bigint NOT NULL,
    name character varying(255)
);


ALTER TABLE public.ab_unit OWNER TO postgres;

--
-- Name: ab_work; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_work (
    id bigint NOT NULL,
    name character varying,
    work_coefficient double precision,
    client_price double precision,
    work_price double precision,
    base_unit_id bigint,
    group_work_id bigint
);


ALTER TABLE public.ab_work OWNER TO postgres;

--
-- Name: ab_work_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_work_group (
    id bigint NOT NULL,
    name character varying,
    work_technology_id bigint
);


ALTER TABLE public.ab_work_group OWNER TO postgres;

--
-- Name: ab_work_material; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_work_material (
    id bigint NOT NULL,
    amount double precision,
    material_id bigint,
    work_id bigint
);


ALTER TABLE public.ab_work_material OWNER TO postgres;

--
-- Name: ab_work_stage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_work_stage (
    id bigint NOT NULL,
    name character varying
);


ALTER TABLE public.ab_work_stage OWNER TO postgres;

--
-- Name: ab_work_technology; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ab_work_technology (
    id bigint NOT NULL,
    name character varying,
    work_stage_id bigint
);


ALTER TABLE public.ab_work_technology OWNER TO postgres;

--
-- Name: base_unit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.base_unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_unit_id_seq OWNER TO postgres;

--
-- Name: base_unit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.base_unit_id_seq OWNED BY public.ab_base_unit.id;


--
-- Name: base_volume_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.base_volume_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_volume_id_seq OWNER TO postgres;

--
-- Name: base_volume_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.base_volume_id_seq OWNED BY public.ab_base_volume.id;


--
-- Name: city_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.city_id_seq OWNER TO postgres;

--
-- Name: city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.city_id_seq OWNED BY public.ab_city.id;


--
-- Name: equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipment_id_seq OWNER TO postgres;

--
-- Name: equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_id_seq OWNED BY public.ab_equipment.id;


--
-- Name: material_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.material_category_id_seq OWNER TO postgres;

--
-- Name: material_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_category_id_seq OWNED BY public.ab_material_category.id;


--
-- Name: material_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.material_group_id_seq OWNER TO postgres;

--
-- Name: material_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_group_id_seq OWNED BY public.ab_material_group.id;


--
-- Name: material_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.material_id_seq OWNER TO postgres;

--
-- Name: material_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_id_seq OWNED BY public.ab_material.id;


--
-- Name: material_property_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_property_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.material_property_id_seq OWNER TO postgres;

--
-- Name: material_property_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_property_id_seq OWNED BY public.ab_material_property.id;


--
-- Name: material_subgroup_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.material_subgroup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.material_subgroup_id_seq OWNER TO postgres;

--
-- Name: material_subgroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.material_subgroup_id_seq OWNED BY public.ab_material_subgroup.id;


--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO postgres;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.product_id_seq OWNED BY public.ab_product.id;


--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO postgres;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.ab_project.id;


--
-- Name: property_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.property_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.property_id_seq OWNER TO postgres;

--
-- Name: property_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.property_id_seq OWNED BY public.ab_property.id;


--
-- Name: provider_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.provider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.provider_id_seq OWNER TO postgres;

--
-- Name: provider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.provider_id_seq OWNED BY public.ab_provider.id;


--
-- Name: technology_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.technology_equipment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.technology_equipment_id_seq OWNER TO postgres;

--
-- Name: technology_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.technology_equipment_id_seq OWNED BY public.ab_technology_equipment.id;


--
-- Name: unit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.unit_id_seq OWNER TO postgres;

--
-- Name: unit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.unit_id_seq OWNED BY public.ab_unit.id;


--
-- Name: work_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.work_group_id_seq OWNER TO postgres;

--
-- Name: work_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_group_id_seq OWNED BY public.ab_work_group.id;


--
-- Name: work_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.work_id_seq OWNER TO postgres;

--
-- Name: work_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_id_seq OWNED BY public.ab_work.id;


--
-- Name: work_material_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_material_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.work_material_id_seq OWNER TO postgres;

--
-- Name: work_material_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_material_id_seq OWNED BY public.ab_work_material.id;


--
-- Name: work_stage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_stage_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.work_stage_id_seq OWNER TO postgres;

--
-- Name: work_stage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_stage_id_seq OWNED BY public.ab_work_stage.id;


--
-- Name: work_technology_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.work_technology_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.work_technology_id_seq OWNER TO postgres;

--
-- Name: work_technology_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.work_technology_id_seq OWNED BY public.ab_work_technology.id;


--
-- Name: ab_base_unit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_unit ALTER COLUMN id SET DEFAULT nextval('public.base_unit_id_seq'::regclass);


--
-- Name: ab_base_volume id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_volume ALTER COLUMN id SET DEFAULT nextval('public.base_volume_id_seq'::regclass);


--
-- Name: ab_city id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_city ALTER COLUMN id SET DEFAULT nextval('public.city_id_seq'::regclass);


--
-- Name: ab_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_equipment ALTER COLUMN id SET DEFAULT nextval('public.equipment_id_seq'::regclass);


--
-- Name: ab_material id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material ALTER COLUMN id SET DEFAULT nextval('public.material_id_seq'::regclass);


--
-- Name: ab_material_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_category ALTER COLUMN id SET DEFAULT nextval('public.material_category_id_seq'::regclass);


--
-- Name: ab_material_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_group ALTER COLUMN id SET DEFAULT nextval('public.material_group_id_seq'::regclass);


--
-- Name: ab_material_property id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_property ALTER COLUMN id SET DEFAULT nextval('public.material_property_id_seq'::regclass);


--
-- Name: ab_material_subgroup id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_subgroup ALTER COLUMN id SET DEFAULT nextval('public.material_subgroup_id_seq'::regclass);


--
-- Name: ab_product id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_product ALTER COLUMN id SET DEFAULT nextval('public.product_id_seq'::regclass);


--
-- Name: ab_project id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Name: ab_property id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_property ALTER COLUMN id SET DEFAULT nextval('public.property_id_seq'::regclass);


--
-- Name: ab_provider id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_provider ALTER COLUMN id SET DEFAULT nextval('public.provider_id_seq'::regclass);


--
-- Name: ab_technology_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_technology_equipment ALTER COLUMN id SET DEFAULT nextval('public.technology_equipment_id_seq'::regclass);


--
-- Name: ab_unit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_unit ALTER COLUMN id SET DEFAULT nextval('public.unit_id_seq'::regclass);


--
-- Name: ab_work id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work ALTER COLUMN id SET DEFAULT nextval('public.work_id_seq'::regclass);


--
-- Name: ab_work_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_group ALTER COLUMN id SET DEFAULT nextval('public.work_group_id_seq'::regclass);


--
-- Name: ab_work_material id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_material ALTER COLUMN id SET DEFAULT nextval('public.work_material_id_seq'::regclass);


--
-- Name: ab_work_stage id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_stage ALTER COLUMN id SET DEFAULT nextval('public.work_stage_id_seq'::regclass);


--
-- Name: ab_work_technology id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_technology ALTER COLUMN id SET DEFAULT nextval('public.work_technology_id_seq'::regclass);


--
-- Data for Name: ab_base_unit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_base_unit (id, name) FROM stdin;
\.
COPY public.ab_base_unit (id, name) FROM '$$PATH$$/3008.dat';

--
-- Data for Name: ab_base_volume; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_base_volume (id, name, project_id, base_unit_id) FROM stdin;
\.
COPY public.ab_base_volume (id, name, project_id, base_unit_id) FROM '$$PATH$$/3034.dat';

--
-- Data for Name: ab_city; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_city (id, name) FROM stdin;
\.
COPY public.ab_city (id, name) FROM '$$PATH$$/2997.dat';

--
-- Data for Name: ab_equipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_equipment (id, name) FROM stdin;
\.
COPY public.ab_equipment (id, name) FROM '$$PATH$$/3001.dat';

--
-- Data for Name: ab_material; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_material (id, name, articul, unit_id, subgroup_id) FROM stdin;
\.
COPY public.ab_material (id, name, articul, unit_id, subgroup_id) FROM '$$PATH$$/3018.dat';

--
-- Data for Name: ab_material_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_material_category (id, name) FROM stdin;
\.
COPY public.ab_material_category (id, name) FROM '$$PATH$$/3012.dat';

--
-- Data for Name: ab_material_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_material_group (id, name, material_category_id) FROM stdin;
\.
COPY public.ab_material_group (id, name, material_category_id) FROM '$$PATH$$/3014.dat';

--
-- Data for Name: ab_material_property; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_material_property (id, amount, material_id, prop_id, unit_id) FROM stdin;
\.
COPY public.ab_material_property (id, amount, material_id, prop_id, unit_id) FROM '$$PATH$$/3020.dat';

--
-- Data for Name: ab_material_subgroup; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_material_subgroup (id, name, material_group_id) FROM stdin;
\.
COPY public.ab_material_subgroup (id, name, material_group_id) FROM '$$PATH$$/3016.dat';

--
-- Data for Name: ab_product; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_product (id, price, amount_for_one, provider_id, material_id) FROM stdin;
\.
COPY public.ab_product (id, price, amount_for_one, provider_id, material_id) FROM '$$PATH$$/3022.dat';

--
-- Data for Name: ab_project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_project (id, name) FROM stdin;
\.
COPY public.ab_project (id, name) FROM '$$PATH$$/3002.dat';

--
-- Data for Name: ab_property; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_property (id, name) FROM stdin;
\.
COPY public.ab_property (id, name) FROM '$$PATH$$/3010.dat';

--
-- Data for Name: ab_provider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_provider (id, name, city_id) FROM stdin;
\.
COPY public.ab_provider (id, name, city_id) FROM '$$PATH$$/2998.dat';

--
-- Data for Name: ab_technology_equipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_technology_equipment (id, technology_id, equipment_id) FROM stdin;
\.
COPY public.ab_technology_equipment (id, technology_id, equipment_id) FROM '$$PATH$$/3036.dat';

--
-- Data for Name: ab_unit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_unit (id, name) FROM stdin;
\.
COPY public.ab_unit (id, name) FROM '$$PATH$$/3003.dat';

--
-- Data for Name: ab_work; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_work (id, name, work_coefficient, client_price, work_price, base_unit_id, group_work_id) FROM stdin;
\.
COPY public.ab_work (id, name, work_coefficient, client_price, work_price, base_unit_id, group_work_id) FROM '$$PATH$$/3030.dat';

--
-- Data for Name: ab_work_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_work_group (id, name, work_technology_id) FROM stdin;
\.
COPY public.ab_work_group (id, name, work_technology_id) FROM '$$PATH$$/3028.dat';

--
-- Data for Name: ab_work_material; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_work_material (id, amount, material_id, work_id) FROM stdin;
\.
COPY public.ab_work_material (id, amount, material_id, work_id) FROM '$$PATH$$/3032.dat';

--
-- Data for Name: ab_work_stage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_work_stage (id, name) FROM stdin;
\.
COPY public.ab_work_stage (id, name) FROM '$$PATH$$/3024.dat';

--
-- Data for Name: ab_work_technology; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ab_work_technology (id, name, work_stage_id) FROM stdin;
\.
COPY public.ab_work_technology (id, name, work_stage_id) FROM '$$PATH$$/3026.dat';

--
-- Name: base_unit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.base_unit_id_seq', 1, true);


--
-- Name: base_volume_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.base_volume_id_seq', 1, false);


--
-- Name: city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.city_id_seq', 19, true);


--
-- Name: equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.equipment_id_seq', 1, false);


--
-- Name: material_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_category_id_seq', 1, true);


--
-- Name: material_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_group_id_seq', 2, true);


--
-- Name: material_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_id_seq', 1, true);


--
-- Name: material_property_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_property_id_seq', 2, true);


--
-- Name: material_subgroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.material_subgroup_id_seq', 2, true);


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.product_id_seq', 1, false);


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_id_seq', 1, true);


--
-- Name: property_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.property_id_seq', 1, true);


--
-- Name: provider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.provider_id_seq', 14, true);


--
-- Name: technology_equipment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.technology_equipment_id_seq', 1, false);


--
-- Name: unit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.unit_id_seq', 24, true);


--
-- Name: work_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_group_id_seq', 1, true);


--
-- Name: work_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_id_seq', 2, true);


--
-- Name: work_material_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_material_id_seq', 2, true);


--
-- Name: work_stage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_stage_id_seq', 2, true);


--
-- Name: work_technology_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.work_technology_id_seq', 1, true);


--
-- Name: ab_base_unit ab_base_unit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_unit
    ADD CONSTRAINT ab_base_unit_pkey PRIMARY KEY (id);


--
-- Name: ab_base_volume ab_base_volume_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_pkey PRIMARY KEY (id);


--
-- Name: ab_city ab_city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_city
    ADD CONSTRAINT ab_city_pkey PRIMARY KEY (id);


--
-- Name: ab_equipment ab_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_equipment
    ADD CONSTRAINT ab_equipment_pkey PRIMARY KEY (id);


--
-- Name: ab_material_category ab_material_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_category
    ADD CONSTRAINT ab_material_category_pkey PRIMARY KEY (id);


--
-- Name: ab_material_group ab_material_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_group
    ADD CONSTRAINT ab_material_group_pkey PRIMARY KEY (id);


--
-- Name: ab_material ab_material_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_pkey PRIMARY KEY (id);


--
-- Name: ab_material_property ab_material_property_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_pkey PRIMARY KEY (id);


--
-- Name: ab_material_subgroup ab_material_subgroup_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_subgroup
    ADD CONSTRAINT ab_material_subgroup_pkey PRIMARY KEY (id);


--
-- Name: ab_product ab_product_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_pkey PRIMARY KEY (id);


--
-- Name: ab_project ab_project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_project
    ADD CONSTRAINT ab_project_pkey PRIMARY KEY (id);


--
-- Name: ab_property ab_property_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_property
    ADD CONSTRAINT ab_property_pkey PRIMARY KEY (id);


--
-- Name: ab_provider ab_provider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_provider
    ADD CONSTRAINT ab_provider_pkey PRIMARY KEY (id);


--
-- Name: ab_technology_equipment ab_technology_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_pkey PRIMARY KEY (id);


--
-- Name: ab_unit ab_unit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_unit
    ADD CONSTRAINT ab_unit_pkey PRIMARY KEY (id);


--
-- Name: ab_work_group ab_work_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_group
    ADD CONSTRAINT ab_work_group_pkey PRIMARY KEY (id);


--
-- Name: ab_work_material ab_work_material_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_pkey PRIMARY KEY (id);


--
-- Name: ab_work ab_work_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_pkey PRIMARY KEY (id);


--
-- Name: ab_work_stage ab_work_stage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_stage
    ADD CONSTRAINT ab_work_stage_pkey PRIMARY KEY (id);


--
-- Name: ab_work_technology ab_work_technology_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_technology
    ADD CONSTRAINT ab_work_technology_pkey PRIMARY KEY (id);


--
-- Name: ab_base_volume ab_base_volume_base_unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_base_unit_fkey FOREIGN KEY (base_unit_id) REFERENCES public.ab_base_unit(id) NOT VALID;


--
-- Name: ab_base_volume ab_base_volume_project_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_base_volume
    ADD CONSTRAINT ab_base_volume_project_fkey FOREIGN KEY (project_id) REFERENCES public.ab_project(id) NOT VALID;


--
-- Name: ab_material_group ab_material_group_material_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_group
    ADD CONSTRAINT ab_material_group_material_category_fkey FOREIGN KEY (material_category_id) REFERENCES public.ab_material_group(id) NOT VALID;


--
-- Name: ab_material_property ab_material_property_material_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;


--
-- Name: ab_material_property ab_material_property_property_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_property_fkey FOREIGN KEY (prop_id) REFERENCES public.ab_property(id) NOT VALID;


--
-- Name: ab_material_property ab_material_property_unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_property
    ADD CONSTRAINT ab_material_property_unit_fkey FOREIGN KEY (unit_id) REFERENCES public.ab_unit(id) NOT VALID;


--
-- Name: ab_material ab_material_subgroup_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_subgroup_fkey FOREIGN KEY (subgroup_id) REFERENCES public.ab_material_subgroup(id) NOT VALID;


--
-- Name: ab_material_subgroup ab_material_subgroup_material_group_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material_subgroup
    ADD CONSTRAINT ab_material_subgroup_material_group_fkey FOREIGN KEY (material_group_id) REFERENCES public.ab_material_group(id) NOT VALID;


--
-- Name: ab_material ab_material_unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_material
    ADD CONSTRAINT ab_material_unit_fkey FOREIGN KEY (unit_id) REFERENCES public.ab_unit(id) NOT VALID;


--
-- Name: ab_product ab_product_material_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;


--
-- Name: ab_product ab_product_provider_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_product
    ADD CONSTRAINT ab_product_provider_fkey FOREIGN KEY (provider_id) REFERENCES public.ab_provider(id) NOT VALID;


--
-- Name: ab_provider ab_provider_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_provider
    ADD CONSTRAINT ab_provider_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.ab_city(id) ON UPDATE CASCADE ON DELETE RESTRICT NOT VALID;


--
-- Name: ab_technology_equipment ab_technology_equipment_equipment_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_equipment_fkey FOREIGN KEY (equipment_id) REFERENCES public.ab_equipment(id) NOT VALID;


--
-- Name: ab_technology_equipment ab_technology_equipment_technology_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_technology_equipment
    ADD CONSTRAINT ab_technology_equipment_technology_fkey FOREIGN KEY (technology_id) REFERENCES public.ab_work_technology(id) NOT VALID;


--
-- Name: ab_work ab_work_base_unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_base_unit_fkey FOREIGN KEY (base_unit_id) REFERENCES public.ab_base_unit(id) NOT VALID;


--
-- Name: ab_work ab_work_group_work_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work
    ADD CONSTRAINT ab_work_group_work_fkey FOREIGN KEY (group_work_id) REFERENCES public.ab_work_group(id) NOT VALID;


--
-- Name: ab_work_group ab_work_group_work_technology_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_group
    ADD CONSTRAINT ab_work_group_work_technology_fkey FOREIGN KEY (work_technology_id) REFERENCES public.ab_work_technology(id) NOT VALID;


--
-- Name: ab_work_material ab_work_material_material_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_material_fkey FOREIGN KEY (material_id) REFERENCES public.ab_material(id) NOT VALID;


--
-- Name: ab_work_material ab_work_material_work_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_material
    ADD CONSTRAINT ab_work_material_work_fkey FOREIGN KEY (work_id) REFERENCES public.ab_work(id) NOT VALID;


--
-- Name: ab_work_technology ab_work_technology_work_stage_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ab_work_technology
    ADD CONSTRAINT ab_work_technology_work_stage_fkey FOREIGN KEY (work_stage_id) REFERENCES public.ab_work_stage(id) NOT VALID;


--
-- PostgreSQL database dump complete
--


BEGIN;

CREATE TABLE IF NOT EXISTS public.auth_group
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_group_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_name_key UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS public.auth_group_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id)
);

CREATE TABLE IF NOT EXISTS public.auth_permission
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename)
);

CREATE TABLE IF NOT EXISTS public.authtoken_token
(
    key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL,
    CONSTRAINT authtoken_token_pkey PRIMARY KEY (key),
    CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id)
);

CREATE TABLE IF NOT EXISTS public.cart_cart
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    quantity integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    has_discount boolean NOT NULL,
    total_price numeric(10, 3) NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT cart_cart_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.customer_customer
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(250) COLLATE pg_catalog."default" NOT NULL,
    full_name character varying(250) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(12) COLLATE pg_catalog."default" NOT NULL,
    password character varying(250) COLLATE pg_catalog."default" NOT NULL,
    cart_id bigint,
    CONSTRAINT customer_customer_pkey PRIMARY KEY (id),
    CONSTRAINT customer_customer_cart_id_key UNIQUE (cart_id),
    CONSTRAINT customer_customer_email_key UNIQUE (email),
    CONSTRAINT customer_customer_phone_number_key UNIQUE (phone_number),
    CONSTRAINT customer_customer_username_key UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS public.customer_customer_groups
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    customer_id bigint NOT NULL,
    group_id integer NOT NULL,
    CONSTRAINT customer_customer_groups_pkey PRIMARY KEY (id),
    CONSTRAINT customer_customer_groups_customer_id_group_id_7b37e958_uniq UNIQUE (customer_id, group_id)
);

CREATE TABLE IF NOT EXISTS public.customer_customer_user_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    customer_id bigint NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT customer_customer_user_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT customer_customer_user_p_customer_id_permission_i_d54c5202_uniq UNIQUE (customer_id, permission_id)
);

CREATE TABLE IF NOT EXISTS public.customer_profile
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    gender character varying(6) COLLATE pg_catalog."default",
    date_of_birth date,
    photo character varying(100) COLLATE pg_catalog."default",
    address_id bigint,
    customer_id bigint NOT NULL,
    CONSTRAINT customer_profile_pkey PRIMARY KEY (id),
    CONSTRAINT customer_profile_customer_id_key UNIQUE (customer_id)
);

CREATE TABLE IF NOT EXISTS public.django_admin_log
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    action_time timestamp with time zone NOT NULL,
    object_id text COLLATE pg_catalog."default",
    object_repr character varying(200) COLLATE pg_catalog."default" NOT NULL,
    action_flag smallint NOT NULL,
    change_message text COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_content_type
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    app_label character varying(100) COLLATE pg_catalog."default" NOT NULL,
    model character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
    CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model)
);

CREATE TABLE IF NOT EXISTS public.django_migrations
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    applied timestamp with time zone NOT NULL,
    CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.django_session
(
    session_key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    session_data text COLLATE pg_catalog."default" NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);

CREATE TABLE IF NOT EXISTS public.location_address
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    line1 character varying(50) COLLATE pg_catalog."default",
    line2 character varying(30) COLLATE pg_catalog."default",
    city character varying(30) COLLATE pg_catalog."default" NOT NULL,
    governorate character varying(30) COLLATE pg_catalog."default",
    "zipCode" integer,
    CONSTRAINT location_address_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.merchant_inventory
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    phone_number character varying(15) COLLATE pg_catalog."default" NOT NULL,
    postal_code character varying(30) COLLATE pg_catalog."default" NOT NULL,
    fax character varying(20) COLLATE pg_catalog."default" NOT NULL,
    email character varying(200) COLLATE pg_catalog."default" NOT NULL,
    address_id bigint NOT NULL,
    CONSTRAINT merchant_inventory_pkey PRIMARY KEY (id),
    CONSTRAINT merchant_inventory_email_key UNIQUE (email),
    CONSTRAINT merchant_inventory_phone_number_key UNIQUE (phone_number)
);

CREATE TABLE IF NOT EXISTS public.oauth2_provider_accesstoken
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    token character varying(255) COLLATE pg_catalog."default" NOT NULL,
    expires timestamp with time zone NOT NULL,
    scope text COLLATE pg_catalog."default" NOT NULL,
    application_id bigint,
    user_id bigint,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    source_refresh_token_id bigint,
    id_token_id bigint,
    CONSTRAINT oauth2_provider_accesstoken_pkey PRIMARY KEY (id),
    CONSTRAINT oauth2_provider_accesstoken_id_token_id_key UNIQUE (id_token_id),
    CONSTRAINT oauth2_provider_accesstoken_source_refresh_token_id_key UNIQUE (source_refresh_token_id),
    CONSTRAINT oauth2_provider_accesstoken_token_key UNIQUE (token)
);

CREATE TABLE IF NOT EXISTS public.oauth2_provider_application
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    client_id character varying(100) COLLATE pg_catalog."default" NOT NULL,
    redirect_uris text COLLATE pg_catalog."default" NOT NULL,
    client_type character varying(32) COLLATE pg_catalog."default" NOT NULL,
    authorization_grant_type character varying(32) COLLATE pg_catalog."default" NOT NULL,
    client_secret character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    user_id bigint,
    skip_authorization boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    algorithm character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT oauth2_provider_application_pkey PRIMARY KEY (id),
    CONSTRAINT oauth2_provider_application_client_id_key UNIQUE (client_id)
);

CREATE TABLE IF NOT EXISTS public.oauth2_provider_grant
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    code character varying(255) COLLATE pg_catalog."default" NOT NULL,
    expires timestamp with time zone NOT NULL,
    redirect_uri text COLLATE pg_catalog."default" NOT NULL,
    scope text COLLATE pg_catalog."default" NOT NULL,
    application_id bigint NOT NULL,
    user_id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    code_challenge character varying(128) COLLATE pg_catalog."default" NOT NULL,
    code_challenge_method character varying(10) COLLATE pg_catalog."default" NOT NULL,
    nonce character varying(255) COLLATE pg_catalog."default" NOT NULL,
    claims text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT oauth2_provider_grant_pkey PRIMARY KEY (id),
    CONSTRAINT oauth2_provider_grant_code_key UNIQUE (code)
);

CREATE TABLE IF NOT EXISTS public.oauth2_provider_idtoken
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    jti uuid NOT NULL,
    expires timestamp with time zone NOT NULL,
    scope text COLLATE pg_catalog."default" NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    application_id bigint,
    user_id bigint,
    CONSTRAINT oauth2_provider_idtoken_pkey PRIMARY KEY (id),
    CONSTRAINT oauth2_provider_idtoken_jti_key UNIQUE (jti)
);

CREATE TABLE IF NOT EXISTS public.oauth2_provider_refreshtoken
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    token character varying(255) COLLATE pg_catalog."default" NOT NULL,
    access_token_id bigint,
    application_id bigint NOT NULL,
    user_id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    revoked timestamp with time zone,
    CONSTRAINT oauth2_provider_refreshtoken_pkey PRIMARY KEY (id),
    CONSTRAINT oauth2_provider_refreshtoken_access_token_id_key UNIQUE (access_token_id),
    CONSTRAINT oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq UNIQUE (token, revoked)
);

CREATE TABLE IF NOT EXISTS public.order_order
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    created_at timestamp with time zone NOT NULL,
    order_tracking_number character varying(100) COLLATE pg_catalog."default" NOT NULL,
    order_taxes double precision NOT NULL,
    order_state character varying(12) COLLATE pg_catalog."default" NOT NULL,
    order_amount integer NOT NULL,
    estimated_delivery_time date NOT NULL,
    address_id bigint NOT NULL,
    cart_id bigint NOT NULL,
    customer_id bigint NOT NULL,
    CONSTRAINT order_order_pkey PRIMARY KEY (id),
    CONSTRAINT order_order_cart_id_key UNIQUE (cart_id),
    CONSTRAINT order_order_customer_id_key UNIQUE (customer_id),
    CONSTRAINT order_order_order_tracking_number_key UNIQUE (order_tracking_number)
);

CREATE TABLE IF NOT EXISTS public.product_brand
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT product_brand_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.product_category
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(200) COLLATE pg_catalog."default" NOT NULL,
    slug character varying(200) COLLATE pg_catalog."default" NOT NULL,
    active boolean,
    description text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT product_category_pkey PRIMARY KEY (id),
    CONSTRAINT product_category_slug_key UNIQUE (slug)
);

CREATE TABLE IF NOT EXISTS public.product_imagemodel
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    images character varying(100) COLLATE pg_catalog."default" NOT NULL,
    product_id bigint NOT NULL,
    CONSTRAINT product_imagemodel_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.product_product
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    name character varying(200) COLLATE pg_catalog."default" NOT NULL,
    slug character varying(200) COLLATE pg_catalog."default",
    image character varying(100) COLLATE pg_catalog."default" NOT NULL,
    description text COLLATE pg_catalog."default" NOT NULL,
    price numeric(10, 3) NOT NULL,
    available boolean NOT NULL,
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    discount_available boolean,
    category_id bigint NOT NULL,
    inventory_id bigint NOT NULL,
    CONSTRAINT product_product_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.product_productreview
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    comment text COLLATE pg_catalog."default",
    rating double precision,
    product_id bigint NOT NULL,
    CONSTRAINT product_productreview_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.product_productreview_customer
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    productreview_id bigint NOT NULL,
    customer_id bigint NOT NULL,
    CONSTRAINT product_productreview_customer_pkey PRIMARY KEY (id),
    CONSTRAINT product_productreview_cu_productreview_id_custome_67d9a1a8_uniq UNIQUE (productreview_id, customer_id)
);

CREATE TABLE IF NOT EXISTS public.social_auth_association
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    server_url character varying(255) COLLATE pg_catalog."default" NOT NULL,
    handle character varying(255) COLLATE pg_catalog."default" NOT NULL,
    secret character varying(255) COLLATE pg_catalog."default" NOT NULL,
    issued integer NOT NULL,
    lifetime integer NOT NULL,
    assoc_type character varying(64) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT social_auth_association_pkey PRIMARY KEY (id),
    CONSTRAINT social_auth_association_server_url_handle_078befa2_uniq UNIQUE (server_url, handle)
);

CREATE TABLE IF NOT EXISTS public.social_auth_code
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    code character varying(32) COLLATE pg_catalog."default" NOT NULL,
    verified boolean NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    CONSTRAINT social_auth_code_pkey PRIMARY KEY (id),
    CONSTRAINT social_auth_code_email_code_801b2d02_uniq UNIQUE (email, code)
);

CREATE TABLE IF NOT EXISTS public.social_auth_nonce
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    server_url character varying(255) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" integer NOT NULL,
    salt character varying(65) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT social_auth_nonce_pkey PRIMARY KEY (id),
    CONSTRAINT social_auth_nonce_server_url_timestamp_salt_f6284463_uniq UNIQUE (server_url, "timestamp", salt)
);

CREATE TABLE IF NOT EXISTS public.social_auth_partial
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    token character varying(32) COLLATE pg_catalog."default" NOT NULL,
    next_step smallint NOT NULL,
    backend character varying(32) COLLATE pg_catalog."default" NOT NULL,
    data text COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    CONSTRAINT social_auth_partial_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.social_auth_usersocialauth
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    provider character varying(32) COLLATE pg_catalog."default" NOT NULL,
    uid character varying(255) COLLATE pg_catalog."default" NOT NULL,
    extra_data text COLLATE pg_catalog."default" NOT NULL,
    user_id bigint NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    CONSTRAINT social_auth_usersocialauth_pkey PRIMARY KEY (id),
    CONSTRAINT social_auth_usersocialauth_provider_uid_e6b5e668_uniq UNIQUE (provider, uid)
);

ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e
    ON public.auth_group_permissions(permission_id);


ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9
    ON public.auth_group_permissions(group_id);


ALTER TABLE IF EXISTS public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b
    ON public.auth_permission(content_type_id);


ALTER TABLE IF EXISTS public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_customer_customer_id FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS authtoken_token_user_id_key
    ON public.authtoken_token(user_id);


ALTER TABLE IF EXISTS public.cart_cart
    ADD CONSTRAINT cart_cart_product_id_b5f94649_fk_product_product_id FOREIGN KEY (product_id)
    REFERENCES public.product_product (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS cart_cart_product_id_b5f94649
    ON public.cart_cart(product_id);


ALTER TABLE IF EXISTS public.customer_customer
    ADD CONSTRAINT customer_customer_cart_id_e42c51a0_fk_cart_cart_id FOREIGN KEY (cart_id)
    REFERENCES public.cart_cart (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_customer_cart_id_key
    ON public.customer_customer(cart_id);


ALTER TABLE IF EXISTS public.customer_customer_groups
    ADD CONSTRAINT customer_customer_gr_customer_id_cc388c92_fk_customer_ FOREIGN KEY (customer_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_customer_groups_customer_id_cc388c92
    ON public.customer_customer_groups(customer_id);


ALTER TABLE IF EXISTS public.customer_customer_groups
    ADD CONSTRAINT customer_customer_groups_group_id_a005825a_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_customer_groups_group_id_a005825a
    ON public.customer_customer_groups(group_id);


ALTER TABLE IF EXISTS public.customer_customer_user_permissions
    ADD CONSTRAINT customer_customer_us_customer_id_0dffe549_fk_customer_ FOREIGN KEY (customer_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_customer_user_permissions_customer_id_0dffe549
    ON public.customer_customer_user_permissions(customer_id);


ALTER TABLE IF EXISTS public.customer_customer_user_permissions
    ADD CONSTRAINT customer_customer_us_permission_id_b5679413_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_customer_user_permissions_permission_id_b5679413
    ON public.customer_customer_user_permissions(permission_id);


ALTER TABLE IF EXISTS public.customer_profile
    ADD CONSTRAINT customer_profile_address_id_b6416b33_fk_location_address_id FOREIGN KEY (address_id)
    REFERENCES public.location_address (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_profile_address_id_b6416b33
    ON public.customer_profile(address_id);


ALTER TABLE IF EXISTS public.customer_profile
    ADD CONSTRAINT customer_profile_customer_id_8513ee2c_fk_customer_customer_id FOREIGN KEY (customer_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS customer_profile_customer_id_key
    ON public.customer_profile(customer_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb
    ON public.django_admin_log(content_type_id);


ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_customer_customer_id FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6
    ON public.django_admin_log(user_id);


ALTER TABLE IF EXISTS public.merchant_inventory
    ADD CONSTRAINT merchant_inventory_address_id_013ba19f_fk_location_address_id FOREIGN KEY (address_id)
    REFERENCES public.location_address (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS merchant_inventory_address_id_013ba19f
    ON public.merchant_inventory(address_id);


ALTER TABLE IF EXISTS public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr FOREIGN KEY (application_id)
    REFERENCES public.oauth2_provider_application (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_accesstoken_application_id_b22886e1
    ON public.oauth2_provider_accesstoken(application_id);


ALTER TABLE IF EXISTS public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr FOREIGN KEY (id_token_id)
    REFERENCES public.oauth2_provider_idtoken (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_accesstoken_id_token_id_key
    ON public.oauth2_provider_accesstoken(id_token_id);


ALTER TABLE IF EXISTS public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr FOREIGN KEY (source_refresh_token_id)
    REFERENCES public.oauth2_provider_refreshtoken (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_accesstoken_source_refresh_token_id_key
    ON public.oauth2_provider_accesstoken(source_refresh_token_id);


ALTER TABLE IF EXISTS public.oauth2_provider_accesstoken
    ADD CONSTRAINT oauth2_provider_acce_user_id_6e4c9a65_fk_customer_ FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_accesstoken_user_id_6e4c9a65
    ON public.oauth2_provider_accesstoken(user_id);


ALTER TABLE IF EXISTS public.oauth2_provider_application
    ADD CONSTRAINT oauth2_provider_appl_user_id_79829054_fk_customer_ FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_application_user_id_79829054
    ON public.oauth2_provider_application(user_id);


ALTER TABLE IF EXISTS public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_gran_application_id_81923564_fk_oauth2_pr FOREIGN KEY (application_id)
    REFERENCES public.oauth2_provider_application (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_grant_application_id_81923564
    ON public.oauth2_provider_grant(application_id);


ALTER TABLE IF EXISTS public.oauth2_provider_grant
    ADD CONSTRAINT oauth2_provider_grant_user_id_e8f62af8_fk_customer_customer_id FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_grant_user_id_e8f62af8
    ON public.oauth2_provider_grant(user_id);


ALTER TABLE IF EXISTS public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr FOREIGN KEY (application_id)
    REFERENCES public.oauth2_provider_application (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_idtoken_application_id_08c5ff4f
    ON public.oauth2_provider_idtoken(application_id);


ALTER TABLE IF EXISTS public.oauth2_provider_idtoken
    ADD CONSTRAINT oauth2_provider_idto_user_id_dd512b59_fk_customer_ FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_idtoken_user_id_dd512b59
    ON public.oauth2_provider_idtoken(user_id);


ALTER TABLE IF EXISTS public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr FOREIGN KEY (access_token_id)
    REFERENCES public.oauth2_provider_accesstoken (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_refreshtoken_access_token_id_key
    ON public.oauth2_provider_refreshtoken(access_token_id);


ALTER TABLE IF EXISTS public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr FOREIGN KEY (application_id)
    REFERENCES public.oauth2_provider_application (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_refreshtoken_application_id_2d1c311b
    ON public.oauth2_provider_refreshtoken(application_id);


ALTER TABLE IF EXISTS public.oauth2_provider_refreshtoken
    ADD CONSTRAINT oauth2_provider_refr_user_id_da837fce_fk_customer_ FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS oauth2_provider_refreshtoken_user_id_da837fce
    ON public.oauth2_provider_refreshtoken(user_id);


ALTER TABLE IF EXISTS public.order_order
    ADD CONSTRAINT order_order_address_id_f6eb43ad_fk_location_address_id FOREIGN KEY (address_id)
    REFERENCES public.location_address (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS order_order_address_id_f6eb43ad
    ON public.order_order(address_id);


ALTER TABLE IF EXISTS public.order_order
    ADD CONSTRAINT order_order_cart_id_d14f666c_fk_cart_cart_id FOREIGN KEY (cart_id)
    REFERENCES public.cart_cart (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS order_order_cart_id_key
    ON public.order_order(cart_id);


ALTER TABLE IF EXISTS public.order_order
    ADD CONSTRAINT order_order_customer_id_5bbbd957_fk_customer_customer_id FOREIGN KEY (customer_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS order_order_customer_id_key
    ON public.order_order(customer_id);


ALTER TABLE IF EXISTS public.product_imagemodel
    ADD CONSTRAINT product_imagemodel_product_id_95162b97_fk_product_product_id FOREIGN KEY (product_id)
    REFERENCES public.product_product (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_imagemodel_product_id_95162b97
    ON public.product_imagemodel(product_id);


ALTER TABLE IF EXISTS public.product_product
    ADD CONSTRAINT product_product_category_id_0c725779_fk_product_category_id FOREIGN KEY (category_id)
    REFERENCES public.product_category (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_product_category_id_0c725779
    ON public.product_product(category_id);


ALTER TABLE IF EXISTS public.product_product
    ADD CONSTRAINT product_product_inventory_id_af2f3df4_fk_merchant_inventory_id FOREIGN KEY (inventory_id)
    REFERENCES public.merchant_inventory (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_product_inventory_id_af2f3df4
    ON public.product_product(inventory_id);


ALTER TABLE IF EXISTS public.product_productreview
    ADD CONSTRAINT product_productreview_product_id_f3a2ae11_fk_product_product_id FOREIGN KEY (product_id)
    REFERENCES public.product_product (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_productreview_product_id_f3a2ae11
    ON public.product_productreview(product_id);


ALTER TABLE IF EXISTS public.product_productreview_customer
    ADD CONSTRAINT product_productrevie_customer_id_2224758a_fk_customer_ FOREIGN KEY (customer_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_productreview_customer_customer_id_2224758a
    ON public.product_productreview_customer(customer_id);


ALTER TABLE IF EXISTS public.product_productreview_customer
    ADD CONSTRAINT product_productrevie_productreview_id_ccb992eb_fk_product_p FOREIGN KEY (productreview_id)
    REFERENCES public.product_productreview (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS product_productreview_customer_productreview_id_ccb992eb
    ON public.product_productreview_customer(productreview_id);


ALTER TABLE IF EXISTS public.social_auth_usersocialauth
    ADD CONSTRAINT social_auth_usersoci_user_id_17d28448_fk_customer_ FOREIGN KEY (user_id)
    REFERENCES public.customer_customer (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS social_auth_usersocialauth_user_id_17d28448
    ON public.social_auth_usersocialauth(user_id);

END;

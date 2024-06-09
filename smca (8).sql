-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-06-2024 a las 00:38:27
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `smca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comments`
--

CREATE TABLE `comments` (
  `id_comment` int(11) NOT NULL,
  `content_comment` varchar(1000) NOT NULL,
  `email_comment` varchar(50) NOT NULL,
  `date_comment` date NOT NULL,
  `nameUser_comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comments`
--

INSERT INTO `comments` (`id_comment`, `content_comment`, `email_comment`, `date_comment`, `nameUser_comment`) VALUES
(1, 'esta de aquellas', 'isabel@gmail.com', '2024-05-22', 'LaMadrina'),
(2, 'no me jalo\r\n', 'isabel@gmail.com', '2024-06-02', 'LaMadrina');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `opinions`
--

CREATE TABLE `opinions` (
  `id_opinion` int(50) NOT NULL,
  `username_opinion` varchar(50) NOT NULL,
  `id_product` int(15) NOT NULL,
  `rating_product` varchar(5) NOT NULL,
  `comment_opinion` varchar(350) NOT NULL,
  `date_opinion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `opinions`
--

INSERT INTO `opinions` (`id_opinion`, `username_opinion`, `id_product`, `rating_product`, `comment_opinion`, `date_opinion`) VALUES
(1, 'LaMadrina', 1, '5', 'asdasdasd', '2024-05-22'),
(2, 'LaMadrina', 2, '3', 'asdqwe', '2024-05-22'),
(3, 'LaMadrina', 1, '4', 'Esta bastante bien por su precio es calidad sobre calidad', '2024-06-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `id_product` int(15) NOT NULL,
  `product_name` text NOT NULL,
  `product_price` int(15) NOT NULL,
  `product_description` varchar(300) NOT NULL,
  `product_image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id_product`, `product_name`, `product_price`, `product_description`, `product_image`) VALUES
(1, 'SMCA V1.0', 2400, 'Este producto evita que te caigas men', 'SMCA V1.0-arte-vectorial-latas-aerosol-graffiti-blanco-negro-letras-rojas-dibujadas-mano-elementos-diseno-arte-removebg-preview.png'),
(2, 'SMCA V2.0', 1300, 'Este tambien', 'SMCA V2.0-arte-vectorial-latas-aerosol-graffiti-blanco-negro-letras-rojas-dibujadas-mano-elementos-diseno-arte-removebg-preview.png'),
(4, 'Prueba', 3501, 'imagen', 'Prueba-arte-vectorial-latas-aerosol-graffiti-blanco-negro-letras-rojas-dibujadas-mano-elementos-diseno-arte-removebg-preview.png'),
(5, 'Prueba1', 24000, 'Prueba distribución', 'Prueba1-arte-vectorial-latas-aerosol-graffiti-blanco-negro-letras-rojas-dibujadas-mano-elementos-diseno-arte-removebg-preview.png'),
(6, 'Prueba2', 3501, 'asdasdasd', 'Prueba2-arte-vectorial-latas-aerosol-graffiti-blanco-negro-letras-rojas-dibujadas-mano-elementos-diseno-arte-removebg-preview.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sales`
--

CREATE TABLE `sales` (
  `id_sale` int(15) NOT NULL,
  `id_user` int(15) NOT NULL,
  `id_product` int(15) NOT NULL,
  `sale_date` date NOT NULL,
  `total_sale` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `type`
--

CREATE TABLE `type` (
  `id_type` int(2) NOT NULL,
  `type_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `type`
--

INSERT INTO `type` (`id_type`, `type_name`) VALUES
(1, 'Administrador'),
(2, 'Visitante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(15) NOT NULL,
  `id_type` int(2) NOT NULL,
  `user_username` varchar(15) NOT NULL,
  `user_name` text NOT NULL,
  `user_lastname` text NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_password` varchar(250) NOT NULL,
  `user_direction` varchar(100) NOT NULL,
  `user_phoneNumber` varchar(15) NOT NULL,
  `user_image` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id_user`, `id_type`, `user_username`, `user_name`, `user_lastname`, `user_email`, `user_password`, `user_direction`, `user_phoneNumber`, `user_image`) VALUES
(1, 1, 'admin1', 'Administrador', 'Prueba', 'admin1@gmail.com', 'pbkdf2:sha256:600000$lR6dMzvUARun7mdd$d992a1f94bf8d0b080423d28b5a0d83bf6262f04dfd860a7fe4196478ef9394a', 'Privada 20 de noviembre #4', '2462214081', ''),
(2, 2, 'LaMadrina', 'Isabel', 'Hernandez Fernandez', 'isabel@gmail.com', 'pbkdf2:sha256:600000$BwXxOkHFu4sGtiH7$d8f2b609799fafd842048d9d128ade391ad48f01b49f428dd710ea19cc7a654d', 'Privada 20 de noviembre #4', '2462214081', 'LaMadrina-Majestic2.2.jpg');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_opiniones`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_opiniones` (
`id de opinion` int(50)
,`comentario` varchar(350)
,`fecha` date
,`calificacion` varchar(5)
,`nombre de usuario` varchar(50)
,`nombre del producto` text
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_usuarios`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_usuarios` (
`id de usuario` int(15)
,`tipo de usuario` text
,`nombre de usuario` varchar(15)
,`nombre` text
,`apellido` text
,`correo electronico` varchar(50)
,`direccion` varchar(100)
,`numero de telefono` varchar(15)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_opiniones`
--
DROP TABLE IF EXISTS `vista_opiniones`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_opiniones`  AS SELECT `o`.`id_opinion` AS `id de opinion`, `o`.`comment_opinion` AS `comentario`, `o`.`date_opinion` AS `fecha`, `o`.`rating_product` AS `calificacion`, `o`.`username_opinion` AS `nombre de usuario`, `p`.`product_name` AS `nombre del producto` FROM (`opinions` `o` join `products` `p` on(`o`.`id_product` = `p`.`id_product`)) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_usuarios`
--
DROP TABLE IF EXISTS `vista_usuarios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_usuarios`  AS SELECT `users`.`id_user` AS `id de usuario`, `type`.`type_name` AS `tipo de usuario`, `users`.`user_username` AS `nombre de usuario`, `users`.`user_name` AS `nombre`, `users`.`user_lastname` AS `apellido`, `users`.`user_email` AS `correo electronico`, `users`.`user_direction` AS `direccion`, `users`.`user_phoneNumber` AS `numero de telefono` FROM (`users` join `type` on(`users`.`id_type` = `type`.`id_type`)) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id_comment`);

--
-- Indices de la tabla `opinions`
--
ALTER TABLE `opinions`
  ADD PRIMARY KEY (`id_opinion`),
  ADD KEY `id_product` (`id_product`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id_product`);

--
-- Indices de la tabla `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id_sale`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_product` (`id_product`);

--
-- Indices de la tabla `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id_type`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `id_type` (`id_type`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comments`
--
ALTER TABLE `comments`
  MODIFY `id_comment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `opinions`
--
ALTER TABLE `opinions`
  MODIFY `id_opinion` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `id_product` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `sales`
--
ALTER TABLE `sales`
  MODIFY `id_sale` int(15) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `type`
--
ALTER TABLE `type`
  MODIFY `id_type` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `opinions`
--
ALTER TABLE `opinions`
  ADD CONSTRAINT `opinions_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `products` (`id_product`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`id_type`) REFERENCES `type` (`id_type`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

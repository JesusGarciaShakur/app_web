-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-05-2024 a las 00:06:09
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

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
  `content_comment` varchar(1000) DEFAULT NULL,
  `email_comment` varchar(50) DEFAULT NULL,
  `date_comment` date DEFAULT NULL,
  `nameUser_comment` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comments`
--

INSERT INTO `comments` (`id_comment`, `content_comment`, `email_comment`, `date_comment`, `nameUser_comment`) VALUES
(1, 'luisestrada@gmail.com', '2024-05-19', '0000-00-00', ''),
(2, 'Si jala', 'luisestrada@gmail.com', '2024-05-19', 'ElPadrino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `id_product` int(15) NOT NULL,
  `product_name` text NOT NULL,
  `product_price` int(15) NOT NULL,
  `product_description` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`id_product`, `product_name`, `product_price`, `product_description`) VALUES
(1, 'Sistema de Monitoreo para Contenedores de Agua', 2400, 'El sistema de monitoreo de agua evita que te caigas de tu techo we :)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sales`
--

CREATE TABLE `sales` (
  `id_sale` int(15) NOT NULL,
  `id_user` int(15) DEFAULT NULL,
  `id_product` int(15) DEFAULT NULL,
  `sale_date` date DEFAULT NULL,
  `total_sale` int(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `type`
--

CREATE TABLE `type` (
  `id_type` int(2) NOT NULL,
  `type_name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `type`
--

INSERT INTO `type` (`id_type`, `type_name`) VALUES
(1, 'Administrador\r\n'),
(2, 'Visitante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(15) NOT NULL,
  `id_type` int(2) DEFAULT NULL,
  `user_username` varchar(15) DEFAULT NULL,
  `user_name` text DEFAULT NULL,
  `user_lastname` text DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  `user_password` varchar(250) DEFAULT NULL,
  `user_direction` varchar(100) DEFAULT NULL,
  `user_phoneNumber` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id_user`, `id_type`, `user_username`, `user_name`, `user_lastname`, `user_email`, `user_password`, `user_direction`, `user_phoneNumber`) VALUES
(3, 1, 'admin1', 'Jesus Guadalupe', 'Rodriguez Garcia', 'jesusrguez97@gmail.com', 'pbkdf2:sha256:600000$99N1zaoqWtNBrJaf$2a4b198e2429e35be042bc5bdfe3983398cf456653f1966dea9bc5c748928f1c', 'Privada 20 de noviembre #4', '2462214081'),
(5, 2, 'usuario1', 'Isabel', 'Hernandez Fernandez', 'isabel@gmail.com', 'pbkdf2:sha256:600000$zzWfZySobgg6WF6A$270f534861e865cb2e2a8aa0d09af82a7ce0fdf620be829b9e875f5f164fddd7', 'Privada 20 de noviembre #', '2147483647'),
(21, 2, 'ElPadrino', 'Luis', 'Estrada', 'luisestrada@gmail.com', 'pbkdf2:sha256:600000$7Z4DMx2pw1WynG4p$9b3e55fba923cd56a502c3ea53e2a438164efe8def7289ae4e286a4d8057fbee', 'Privada 20 de noviembre #4 ', '2462214081'),
(22, 1, 'admin2', 'Administrador', 'Fijo de prueba', 'admin@gmail.com', 'pbkdf2:sha256:600000$bslj9Yx9Z4D7HSCG$0befaccae0e087e8a8582a0fe4998396ff2d679ff5160bf17f4bb958baae6275', 'Privada 20 de noviembre #4', '2462214081');

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vista_usuarios`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vista_usuarios` (
`id de usuario` int(15)
,`tipo de usuario` int(2)
,`nombre de usuario` varchar(15)
,`nombre` text
,`apellido` text
,`correo electronico` varchar(50)
,`direccion` varchar(100)
,`numero de telefono` varchar(15)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vista_usuarios`
--
DROP TABLE IF EXISTS `vista_usuarios`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vista_usuarios`  AS SELECT `users`.`id_user` AS `id de usuario`, `users`.`id_type` AS `tipo de usuario`, `users`.`user_username` AS `nombre de usuario`, `users`.`user_name` AS `nombre`, `users`.`user_lastname` AS `apellido`, `users`.`user_email` AS `correo electronico`, `users`.`user_direction` AS `direccion`, `users`.`user_phoneNumber` AS `numero de telefono` FROM `users` ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id_comment`);

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
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `id_product` (`id_product`);

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
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `id_product` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  MODIFY `id_user` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Restricciones para tablas volcadas
--

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

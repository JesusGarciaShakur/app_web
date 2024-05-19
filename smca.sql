-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-05-2024 a las 19:22:53
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
(1, 'admin\r\n'),
(2, 'visit_user');

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
(3, 1, 'admin1', 'Jesus Guadalupe', 'Rodriguez Garcia', 'jesusrguez97@gmail.com', 'pbkdf2:sha256:600000$QdfJfpXSzn6LP5rX$8fdd113ed52d6113e27ec62b7cfb562ce7652155d541cde569022614cd5ba657', 'Privada 20 de noviembre #', '2147483647'),
(5, 2, 'usuario1', 'Isabel', 'Hernandez Fernandez', 'isabel@gmail.com', 'pbkdf2:sha256:600000$zzWfZySobgg6WF6A$270f534861e865cb2e2a8aa0d09af82a7ce0fdf620be829b9e875f5f164fddd7', 'Privada 20 de noviembre #', '2147483647'),
(21, 2, 'ElPadrino', 'Luis', 'Estrada', 'luisestrada@gmail.com', 'pbkdf2:sha256:600000$7Z4DMx2pw1WynG4p$9b3e55fba923cd56a502c3ea53e2a438164efe8def7289ae4e286a4d8057fbee', 'Privada 20 de noviembre #4 ', '2462214081');

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
  MODIFY `id_user` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

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

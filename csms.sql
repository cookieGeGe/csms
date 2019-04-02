/*
 Navicat Premium Data Transfer

 Source Server         : 47.106.140.239
 Source Server Type    : MySQL
 Source Server Version : 50640
 Source Host           : 47.106.140.239:3306
 Source Schema         : csms

 Target Server Type    : MySQL
 Target Server Version : 50640
 File Encoding         : 65001

 Date: 02/04/2019 22:56:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Tb_Progress
-- ----------------------------
DROP TABLE IF EXISTS `Tb_Progress`;
CREATE TABLE `Tb_Progress`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ProjectID` int(11) NULL DEFAULT NULL COMMENT '项目ID',
  `UploadTime` datetime(0) NULL DEFAULT NULL COMMENT '项目进度时间',
  `Pictures` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '施工方上传图片',
  `Content` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '进度报告',
  `Status` int(11) NULL DEFAULT NULL COMMENT '项目状态',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_17`(`ProjectID`) USING BTREE,
  CONSTRAINT `FK_Reference_17` FOREIGN KEY (`ProjectID`) REFERENCES `tb_project` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '项目进度表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_area
-- ----------------------------
DROP TABLE IF EXISTS `tb_area`;
CREATE TABLE `tb_area`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `FatherID` int(11) NULL DEFAULT NULL,
  `HasChild` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 205 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '地区表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_area
-- ----------------------------
INSERT INTO `tb_area` VALUES (1, '四川省', 0, 1);
INSERT INTO `tb_area` VALUES (2, '成都市', 1, 1);
INSERT INTO `tb_area` VALUES (3, '自贡市', 1, 1);
INSERT INTO `tb_area` VALUES (4, '攀枝花市', 1, 1);
INSERT INTO `tb_area` VALUES (5, '泸州市', 1, 1);
INSERT INTO `tb_area` VALUES (6, '德阳市', 1, 1);
INSERT INTO `tb_area` VALUES (7, '绵阳市', 1, 1);
INSERT INTO `tb_area` VALUES (8, '广元市', 1, 1);
INSERT INTO `tb_area` VALUES (9, '遂宁市', 1, 1);
INSERT INTO `tb_area` VALUES (10, '内江市', 1, 1);
INSERT INTO `tb_area` VALUES (11, '乐山市', 1, 1);
INSERT INTO `tb_area` VALUES (12, '南充市', 1, 1);
INSERT INTO `tb_area` VALUES (13, '眉山市', 1, 1);
INSERT INTO `tb_area` VALUES (14, '宜宾市', 1, 1);
INSERT INTO `tb_area` VALUES (15, '广安市', 1, 1);
INSERT INTO `tb_area` VALUES (16, '达州市', 1, 1);
INSERT INTO `tb_area` VALUES (17, '雅安市', 1, 1);
INSERT INTO `tb_area` VALUES (18, '巴中市', 1, 1);
INSERT INTO `tb_area` VALUES (19, '资阳市', 1, 1);
INSERT INTO `tb_area` VALUES (20, '阿坝藏族羌族自治州', 1, 1);
INSERT INTO `tb_area` VALUES (21, '甘孜藏族自治州', 1, 1);
INSERT INTO `tb_area` VALUES (22, '凉山彝族自治州', 1, 1);
INSERT INTO `tb_area` VALUES (23, '锦江区', 2, 0);
INSERT INTO `tb_area` VALUES (24, '青羊区', 2, 0);
INSERT INTO `tb_area` VALUES (25, '金牛区', 2, 0);
INSERT INTO `tb_area` VALUES (26, '武侯区', 2, 0);
INSERT INTO `tb_area` VALUES (27, '成华区', 2, 0);
INSERT INTO `tb_area` VALUES (28, '龙泉驿区', 2, 0);
INSERT INTO `tb_area` VALUES (29, '青白江区', 2, 0);
INSERT INTO `tb_area` VALUES (30, '新都区', 2, 0);
INSERT INTO `tb_area` VALUES (31, '温江区', 2, 0);
INSERT INTO `tb_area` VALUES (32, '金堂县', 2, 0);
INSERT INTO `tb_area` VALUES (33, '双流区', 2, 0);
INSERT INTO `tb_area` VALUES (34, '郫都区', 2, 0);
INSERT INTO `tb_area` VALUES (35, '大邑县', 2, 0);
INSERT INTO `tb_area` VALUES (36, '蒲江县', 2, 0);
INSERT INTO `tb_area` VALUES (37, '新津县', 2, 0);
INSERT INTO `tb_area` VALUES (38, '都江堰市', 2, 0);
INSERT INTO `tb_area` VALUES (39, '彭州市', 2, 0);
INSERT INTO `tb_area` VALUES (40, '邛崃市', 2, 0);
INSERT INTO `tb_area` VALUES (41, '崇州市', 2, 0);
INSERT INTO `tb_area` VALUES (42, '自流井区', 3, 0);
INSERT INTO `tb_area` VALUES (43, '贡井区', 3, 0);
INSERT INTO `tb_area` VALUES (44, '大安区', 3, 0);
INSERT INTO `tb_area` VALUES (45, '沿滩区', 3, 0);
INSERT INTO `tb_area` VALUES (46, '荣县', 3, 0);
INSERT INTO `tb_area` VALUES (47, '富顺县', 3, 0);
INSERT INTO `tb_area` VALUES (48, '东区', 4, 0);
INSERT INTO `tb_area` VALUES (49, '西区', 4, 0);
INSERT INTO `tb_area` VALUES (50, '仁和区', 4, 0);
INSERT INTO `tb_area` VALUES (51, '米易县', 4, 0);
INSERT INTO `tb_area` VALUES (52, '盐边县', 4, 0);
INSERT INTO `tb_area` VALUES (53, '江阳区', 5, 0);
INSERT INTO `tb_area` VALUES (54, '纳溪区', 5, 0);
INSERT INTO `tb_area` VALUES (55, '龙马潭区', 5, 0);
INSERT INTO `tb_area` VALUES (56, '泸县', 5, 0);
INSERT INTO `tb_area` VALUES (57, '合江县', 5, 0);
INSERT INTO `tb_area` VALUES (58, '叙永县', 5, 0);
INSERT INTO `tb_area` VALUES (59, '古蔺县', 5, 0);
INSERT INTO `tb_area` VALUES (60, '旌阳区', 6, 0);
INSERT INTO `tb_area` VALUES (61, '中江县', 6, 0);
INSERT INTO `tb_area` VALUES (62, '罗江区', 6, 0);
INSERT INTO `tb_area` VALUES (63, '广汉市', 6, 0);
INSERT INTO `tb_area` VALUES (64, '什邡市', 6, 0);
INSERT INTO `tb_area` VALUES (65, '绵竹市', 6, 0);
INSERT INTO `tb_area` VALUES (66, '涪城区', 7, 0);
INSERT INTO `tb_area` VALUES (67, '游仙区', 7, 0);
INSERT INTO `tb_area` VALUES (68, '三台县', 7, 0);
INSERT INTO `tb_area` VALUES (69, '盐亭县', 7, 0);
INSERT INTO `tb_area` VALUES (70, '安州区', 7, 0);
INSERT INTO `tb_area` VALUES (71, '梓潼县', 7, 0);
INSERT INTO `tb_area` VALUES (72, '北川羌族自治县', 7, 0);
INSERT INTO `tb_area` VALUES (73, '平武县', 7, 0);
INSERT INTO `tb_area` VALUES (74, '江油市', 7, 0);
INSERT INTO `tb_area` VALUES (75, '利州区', 8, 0);
INSERT INTO `tb_area` VALUES (76, '昭化区', 8, 0);
INSERT INTO `tb_area` VALUES (77, '朝天区', 8, 0);
INSERT INTO `tb_area` VALUES (78, '旺苍县', 8, 0);
INSERT INTO `tb_area` VALUES (79, '青川县', 8, 0);
INSERT INTO `tb_area` VALUES (80, '剑阁县', 8, 0);
INSERT INTO `tb_area` VALUES (81, '苍溪县', 8, 0);
INSERT INTO `tb_area` VALUES (82, '船山区', 9, 0);
INSERT INTO `tb_area` VALUES (83, '安居区', 9, 0);
INSERT INTO `tb_area` VALUES (84, '蓬溪县', 9, 0);
INSERT INTO `tb_area` VALUES (85, '射洪县', 9, 0);
INSERT INTO `tb_area` VALUES (86, '大英县', 9, 0);
INSERT INTO `tb_area` VALUES (87, '市中区', 10, 0);
INSERT INTO `tb_area` VALUES (88, '东兴区', 10, 0);
INSERT INTO `tb_area` VALUES (89, '威远县', 10, 0);
INSERT INTO `tb_area` VALUES (90, '资中区', 10, 0);
INSERT INTO `tb_area` VALUES (91, '隆昌市', 10, 0);
INSERT INTO `tb_area` VALUES (92, '犍为县', 11, 0);
INSERT INTO `tb_area` VALUES (93, '井研县', 11, 0);
INSERT INTO `tb_area` VALUES (94, '夹江县', 11, 0);
INSERT INTO `tb_area` VALUES (95, '沐川县', 11, 0);
INSERT INTO `tb_area` VALUES (96, '峨边彝族自治县', 11, 0);
INSERT INTO `tb_area` VALUES (97, '马边彝族自治县', 11, 0);
INSERT INTO `tb_area` VALUES (98, '峨眉山市', 11, 0);
INSERT INTO `tb_area` VALUES (99, '嘉陵区', 12, 0);
INSERT INTO `tb_area` VALUES (100, '南部县', 12, 0);
INSERT INTO `tb_area` VALUES (101, '营山县', 12, 0);
INSERT INTO `tb_area` VALUES (102, '蓬安县', 12, 0);
INSERT INTO `tb_area` VALUES (103, '仪陇县', 12, 0);
INSERT INTO `tb_area` VALUES (104, '西充县', 12, 0);
INSERT INTO `tb_area` VALUES (105, '阆中市', 12, 0);
INSERT INTO `tb_area` VALUES (106, '顺庆区', 12, 0);
INSERT INTO `tb_area` VALUES (107, '高坪区', 12, 0);
INSERT INTO `tb_area` VALUES (108, '市中区', 11, 0);
INSERT INTO `tb_area` VALUES (109, '沙湾区', 11, 0);
INSERT INTO `tb_area` VALUES (110, '五通桥区', 11, 0);
INSERT INTO `tb_area` VALUES (111, '金口河区', 11, 0);
INSERT INTO `tb_area` VALUES (112, '东坡区', 13, 0);
INSERT INTO `tb_area` VALUES (113, '仁寿县', 13, 0);
INSERT INTO `tb_area` VALUES (114, '彭山区', 13, 0);
INSERT INTO `tb_area` VALUES (115, '洪雅县', 13, 0);
INSERT INTO `tb_area` VALUES (116, '丹棱县', 13, 0);
INSERT INTO `tb_area` VALUES (117, '青神县', 13, 0);
INSERT INTO `tb_area` VALUES (118, '翠屏区', 14, 0);
INSERT INTO `tb_area` VALUES (119, '宜宾县', 14, 0);
INSERT INTO `tb_area` VALUES (120, '南溪区', 14, 0);
INSERT INTO `tb_area` VALUES (121, '江安县', 14, 0);
INSERT INTO `tb_area` VALUES (122, '长宁县', 14, 0);
INSERT INTO `tb_area` VALUES (123, '高县', 14, 0);
INSERT INTO `tb_area` VALUES (124, '珙县', 14, 0);
INSERT INTO `tb_area` VALUES (125, '筠连县', 14, 0);
INSERT INTO `tb_area` VALUES (126, '兴文县', 14, 0);
INSERT INTO `tb_area` VALUES (127, '屏山县', 14, 0);
INSERT INTO `tb_area` VALUES (128, '广安区', 15, 0);
INSERT INTO `tb_area` VALUES (129, '前锋区', 15, 0);
INSERT INTO `tb_area` VALUES (130, '岳池县', 15, 0);
INSERT INTO `tb_area` VALUES (131, '武胜县', 15, 0);
INSERT INTO `tb_area` VALUES (132, '邻水县', 15, 0);
INSERT INTO `tb_area` VALUES (133, '华蓥市', 15, 0);
INSERT INTO `tb_area` VALUES (134, '通川区', 16, 0);
INSERT INTO `tb_area` VALUES (135, '达州区', 16, 0);
INSERT INTO `tb_area` VALUES (136, '宣汉县', 16, 0);
INSERT INTO `tb_area` VALUES (137, '开江县', 16, 0);
INSERT INTO `tb_area` VALUES (138, '大竹县', 16, 0);
INSERT INTO `tb_area` VALUES (139, '渠县', 16, 0);
INSERT INTO `tb_area` VALUES (140, '万源市', 16, 0);
INSERT INTO `tb_area` VALUES (141, '雨城区', 17, 0);
INSERT INTO `tb_area` VALUES (142, '名山区', 17, 0);
INSERT INTO `tb_area` VALUES (143, '荥经县', 17, 0);
INSERT INTO `tb_area` VALUES (144, '汉源县', 17, 0);
INSERT INTO `tb_area` VALUES (145, '石棉县', 17, 0);
INSERT INTO `tb_area` VALUES (146, '天全县', 17, 0);
INSERT INTO `tb_area` VALUES (147, '芦山县', 17, 0);
INSERT INTO `tb_area` VALUES (148, '宝兴县', 17, 0);
INSERT INTO `tb_area` VALUES (149, '巴州区', 18, 0);
INSERT INTO `tb_area` VALUES (150, '恩阳区', 18, 0);
INSERT INTO `tb_area` VALUES (151, '通江县', 18, 0);
INSERT INTO `tb_area` VALUES (152, '南江县', 18, 0);
INSERT INTO `tb_area` VALUES (153, '平昌县', 18, 0);
INSERT INTO `tb_area` VALUES (154, '雁江区', 19, 0);
INSERT INTO `tb_area` VALUES (155, '安岳县', 19, 0);
INSERT INTO `tb_area` VALUES (156, '乐至县', 19, 0);
INSERT INTO `tb_area` VALUES (157, '汶川县', 20, 0);
INSERT INTO `tb_area` VALUES (158, '理县', 20, 0);
INSERT INTO `tb_area` VALUES (159, '茂县', 20, 0);
INSERT INTO `tb_area` VALUES (160, '松潘县', 20, 0);
INSERT INTO `tb_area` VALUES (161, '九寨沟县', 20, 0);
INSERT INTO `tb_area` VALUES (162, '金川县', 20, 0);
INSERT INTO `tb_area` VALUES (163, '小金县', 20, 0);
INSERT INTO `tb_area` VALUES (164, '黑水县', 20, 0);
INSERT INTO `tb_area` VALUES (165, '马尔康市', 20, 0);
INSERT INTO `tb_area` VALUES (166, '壤塘县', 20, 0);
INSERT INTO `tb_area` VALUES (167, '  阿坝县', 20, 0);
INSERT INTO `tb_area` VALUES (168, '红原县', 20, 0);
INSERT INTO `tb_area` VALUES (169, '康定市', 21, 0);
INSERT INTO `tb_area` VALUES (170, '泸定县', 21, 0);
INSERT INTO `tb_area` VALUES (171, '丹巴县', 21, 0);
INSERT INTO `tb_area` VALUES (172, '九龙县', 21, 0);
INSERT INTO `tb_area` VALUES (173, '雅江县', 21, 0);
INSERT INTO `tb_area` VALUES (174, '道孚县', 21, 0);
INSERT INTO `tb_area` VALUES (175, '炉霍县', 21, 0);
INSERT INTO `tb_area` VALUES (176, '甘孜县', 21, 0);
INSERT INTO `tb_area` VALUES (177, '新龙县', 21, 0);
INSERT INTO `tb_area` VALUES (178, '德格县', 21, 0);
INSERT INTO `tb_area` VALUES (179, '白玉县', 21, 0);
INSERT INTO `tb_area` VALUES (180, '石渠县', 21, 0);
INSERT INTO `tb_area` VALUES (181, '色达县', 21, 0);
INSERT INTO `tb_area` VALUES (182, '理塘县', 21, 0);
INSERT INTO `tb_area` VALUES (183, '巴塘县', 21, 0);
INSERT INTO `tb_area` VALUES (184, '乡城县', 21, 0);
INSERT INTO `tb_area` VALUES (185, '稻城县', 21, 0);
INSERT INTO `tb_area` VALUES (186, '得荣县', 21, 0);
INSERT INTO `tb_area` VALUES (187, '西昌市', 22, 0);
INSERT INTO `tb_area` VALUES (188, '木里藏族自治县', 22, 0);
INSERT INTO `tb_area` VALUES (190, '盐源县', 22, 0);
INSERT INTO `tb_area` VALUES (191, '德昌县', 22, 0);
INSERT INTO `tb_area` VALUES (192, '会理县', 22, 0);
INSERT INTO `tb_area` VALUES (193, '会理东', 22, 0);
INSERT INTO `tb_area` VALUES (194, '宁南县', 22, 0);
INSERT INTO `tb_area` VALUES (195, '普格县', 22, 0);
INSERT INTO `tb_area` VALUES (196, '布拖县', 22, 0);
INSERT INTO `tb_area` VALUES (197, '金阳县', 22, 0);
INSERT INTO `tb_area` VALUES (198, '昭觉县', 22, 0);
INSERT INTO `tb_area` VALUES (199, '喜德县', 22, 0);
INSERT INTO `tb_area` VALUES (200, '冕宁县', 22, 0);
INSERT INTO `tb_area` VALUES (201, '越西县', 22, 0);
INSERT INTO `tb_area` VALUES (202, '甘洛县', 22, 0);
INSERT INTO `tb_area` VALUES (203, '美姑县', 22, 0);
INSERT INTO `tb_area` VALUES (204, '雷波县', 22, 0);

-- ----------------------------
-- Table structure for tb_attendance
-- ----------------------------
DROP TABLE IF EXISTS `tb_attendance`;
CREATE TABLE `tb_attendance`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `LaborID` int(11) NULL DEFAULT NULL COMMENT '劳工ID',
  `AttenTime` datetime(0) NULL DEFAULT NULL COMMENT '打卡时间',
  `Remark` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '考勤记录表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_badrecord
-- ----------------------------
DROP TABLE IF EXISTS `tb_badrecord`;
CREATE TABLE `tb_badrecord`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Type` int(11) NULL DEFAULT NULL COMMENT '不良记录类型',
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '不良记录描述',
  `RecordTime` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '不良记录表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_class
-- ----------------------------
DROP TABLE IF EXISTS `tb_class`;
CREATE TABLE `tb_class`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '公司ID',
  `ClassName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班组名字',
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_10`(`CompanyID`) USING BTREE,
  CONSTRAINT `FK_Reference_10` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班组表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_company
-- ----------------------------
DROP TABLE IF EXISTS `tb_company`;
CREATE TABLE `tb_company`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司名字',
  `Legal` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '法人',
  `Address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司地址',
  `Phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '联系方式',
  `License` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '营业执照',
  `OtherPic` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司照片',
  `BadRecord` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '不良记录',
  `Type` int(11) NULL DEFAULT NULL COMMENT '公司类型',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '企业公司表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_company_badrecord
-- ----------------------------
DROP TABLE IF EXISTS `tb_company_badrecord`;
CREATE TABLE `tb_company_badrecord`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '公司ID',
  `BadrecordID` int(11) NULL DEFAULT NULL COMMENT '不良记录ID',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_6`(`CompanyID`) USING BTREE,
  INDEX `FK_Reference_7`(`BadrecordID`) USING BTREE,
  CONSTRAINT `FK_Reference_6` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_7` FOREIGN KEY (`BadrecordID`) REFERENCES `tb_badrecord` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '公司不良记录表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_guarantee
-- ----------------------------
DROP TABLE IF EXISTS `tb_guarantee`;
CREATE TABLE `tb_guarantee`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ProjectID` int(11) NULL DEFAULT NULL COMMENT '项目ID',
  `Number` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '保函编号',
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '担保公司ID',
  `SignTime` datetime(0) NULL DEFAULT NULL COMMENT '合同签订日期',
  `Validity` int(11) NULL DEFAULT NULL COMMENT '有效期（月）',
  `Amount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '金额',
  `Status` int(11) NULL DEFAULT NULL COMMENT '状态',
  `Others` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '附件',
  `Category` int(11) NULL DEFAULT NULL COMMENT '担保类别',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_15`(`ProjectID`) USING BTREE,
  INDEX `FK_Reference_16`(`CompanyID`) USING BTREE,
  CONSTRAINT `FK_Reference_15` FOREIGN KEY (`ProjectID`) REFERENCES `tb_project` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_16` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '保函表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_labor_badrecord
-- ----------------------------
DROP TABLE IF EXISTS `tb_labor_badrecord`;
CREATE TABLE `tb_labor_badrecord`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `LaborID` int(11) NULL DEFAULT NULL COMMENT '劳工ID',
  `BadRecordID` int(11) NULL DEFAULT NULL COMMENT '不良记录ID',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_4`(`LaborID`) USING BTREE,
  INDEX `FK_Reference_5`(`BadRecordID`) USING BTREE,
  CONSTRAINT `FK_Reference_4` FOREIGN KEY (`LaborID`) REFERENCES `tb_laborinfo` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_5` FOREIGN KEY (`BadRecordID`) REFERENCES `tb_badrecord` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '劳工不良记录表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_laborinfo
-- ----------------------------
DROP TABLE IF EXISTS `tb_laborinfo`;
CREATE TABLE `tb_laborinfo`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '姓名',
  `Age` int(11) NULL DEFAULT NULL COMMENT '年龄',
  `Sex` int(11) NULL DEFAULT NULL COMMENT '性别(0表示女，1表示男)',
  `Birthday` datetime(0) NULL DEFAULT NULL COMMENT '生日',
  `Address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '地址',
  `Nationality` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名族',
  `IDCard` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '身份证号码',
  `Phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '电话号码',
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '公司ID',
  `JobNum` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '工号',
  `ClassID` int(11) NULL DEFAULT NULL COMMENT '班组ID',
  `WorkType` int(11) NULL DEFAULT NULL COMMENT '工种',
  `Identity` int(11) NULL DEFAULT NULL COMMENT '身份（配置字典映射）',
  `DepartureDate` datetime(0) NULL DEFAULT NULL COMMENT '离场日期',
  `EntryDate` datetime(0) NULL DEFAULT NULL COMMENT '进场日期',
  `Hardhatnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '安全帽号',
  `IDPhoto` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '证件照片',
  `ConPhoto` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '合同照片',
  `CloseupPhoto` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '近身照片',
  `Education` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学历',
  `CreateTime` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_11`(`CompanyID`) USING BTREE,
  INDEX `FK_Reference_3`(`ClassID`) USING BTREE,
  CONSTRAINT `FK_Reference_11` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_3` FOREIGN KEY (`ClassID`) REFERENCES `tb_class` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '劳工信息表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_permission
-- ----------------------------
DROP TABLE IF EXISTS `tb_permission`;
CREATE TABLE `tb_permission`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PerName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '权限名称',
  `Permission` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '权限',
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述',
  `FatherID` int(11) NULL DEFAULT NULL COMMENT '父ID',
  `URLName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '子级URL',
  `HasChild` int(11) NULL DEFAULT NULL COMMENT '是否有子目录',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '权限表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_pro_class
-- ----------------------------
DROP TABLE IF EXISTS `tb_pro_class`;
CREATE TABLE `tb_pro_class`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ProjectID` int(11) NULL DEFAULT NULL,
  `ClassID` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_12`(`ClassID`) USING BTREE,
  INDEX `FK_Reference_13`(`ProjectID`) USING BTREE,
  CONSTRAINT `FK_Reference_12` FOREIGN KEY (`ClassID`) REFERENCES `tb_class` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_13` FOREIGN KEY (`ProjectID`) REFERENCES `tb_project` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '项目班组表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_project
-- ----------------------------
DROP TABLE IF EXISTS `tb_project`;
CREATE TABLE `tb_project`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '项目名称',
  `Type` int(11) NULL DEFAULT NULL COMMENT '项目类型',
  `Duration` int(11) NULL DEFAULT NULL COMMENT '项目工期（单位：月）',
  `Participants` int(11) NULL DEFAULT NULL COMMENT '参与人数',
  `Price` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '中标价格',
  `GAmount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '担保金额',
  `StartTime` datetime(0) NULL DEFAULT NULL COMMENT '开工时间',
  `Address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '项目地址',
  `OwnerManager` int(11) NULL DEFAULT NULL COMMENT '业主负责人',
  `ConsManager` int(11) NULL DEFAULT NULL COMMENT '施工方负责人',
  `Supervisor` int(11) NULL DEFAULT NULL COMMENT '监理负责人',
  `LaborManager` int(11) NULL DEFAULT NULL COMMENT '劳务专员',
  `LaborCompany` int(11) NULL DEFAULT NULL COMMENT '劳务公司',
  `Pay` int(11) NULL DEFAULT NULL COMMENT '项目支付情况',
  `TotalPrice` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '总产值',
  `TotalPayment` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '总领款',
  `RealHair` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '最终发放统计',
  `Status` int(11) NULL DEFAULT NULL COMMENT '项目状态',
  `WagePercent` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '工资到账比例',
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '所属公司ID',
  `AreaID` int(11) NULL DEFAULT NULL COMMENT '县级区域ID',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_14`(`CompanyID`) USING BTREE,
  INDEX `FK_Reference_21`(`AreaID`) USING BTREE,
  CONSTRAINT `FK_Reference_14` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_21` FOREIGN KEY (`AreaID`) REFERENCES `tb_area` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '项目表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `LoginName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '登录名称',
  `UserName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户名称',
  `Password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `Email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `Phone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '电话',
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述',
  `AdminType` int(11) NULL DEFAULT NULL COMMENT '管理员类型（0表示超级管理员，1表示普通用户）',
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '所属公司ID',
  `Avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_18`(`CompanyID`) USING BTREE,
  CONSTRAINT `FK_Reference_18` FOREIGN KEY (`CompanyID`) REFERENCES `tb_company` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_user_area
-- ----------------------------
DROP TABLE IF EXISTS `tb_user_area`;
CREATE TABLE `tb_user_area`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `UserID` int(11) NULL DEFAULT NULL,
  `AreaID` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_19`(`UserID`) USING BTREE,
  INDEX `FK_Reference_20`(`AreaID`) USING BTREE,
  CONSTRAINT `FK_Reference_19` FOREIGN KEY (`UserID`) REFERENCES `tb_user` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_20` FOREIGN KEY (`AreaID`) REFERENCES `tb_area` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户管理区域表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_user_per
-- ----------------------------
DROP TABLE IF EXISTS `tb_user_per`;
CREATE TABLE `tb_user_per`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `UID` int(11) NULL DEFAULT NULL COMMENT '用户ID',
  `PID` int(11) NULL DEFAULT NULL COMMENT '权限ID',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `FK_Reference_1`(`UID`) USING BTREE,
  INDEX `FK_Reference_2`(`PID`) USING BTREE,
  CONSTRAINT `FK_Reference_1` FOREIGN KEY (`UID`) REFERENCES `tb_user` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Reference_2` FOREIGN KEY (`PID`) REFERENCES `tb_permission` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户权限关联表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for tb_wage
-- ----------------------------
DROP TABLE IF EXISTS `tb_wage`;
CREATE TABLE `tb_wage`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ProjectID` int(11) NULL DEFAULT NULL COMMENT '项目ID',
  `January` int(11) NULL DEFAULT NULL COMMENT '（0表示全额到，1,表示部分到，2表示未到）',
  `February` int(11) NULL DEFAULT NULL,
  `March` int(11) NULL DEFAULT NULL,
  `April` int(11) NULL DEFAULT NULL,
  `May` int(11) NULL DEFAULT NULL,
  `June` int(11) NULL DEFAULT NULL,
  `July` int(11) NULL DEFAULT NULL,
  `August` int(11) NULL DEFAULT NULL,
  `September` int(11) NULL DEFAULT NULL,
  `October` int(11) NULL DEFAULT NULL,
  `November` int(11) NULL DEFAULT NULL,
  `December` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '工资表' ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

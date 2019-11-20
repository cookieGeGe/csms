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

 Date: 14/04/2019 16:43:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_api
-- ----------------------------
DROP TABLE IF EXISTS `tb_api`;
CREATE TABLE `tb_api`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'api名称',
  `Description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'API描述',
  `PID` int(11) NULL DEFAULT NULL COMMENT '权限ID',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `pid`(`PID`) USING BTREE,
  CONSTRAINT `pid` FOREIGN KEY (`PID`) REFERENCES `tb_permission` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

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
) ENGINE = InnoDB AUTO_INCREMENT = 3375 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '地区表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_area
-- ----------------------------
INSERT INTO `tb_area` VALUES (1, '北京市', 0, 1);
INSERT INTO `tb_area` VALUES (2, '天津市', 0, 1);
INSERT INTO `tb_area` VALUES (3, '河北省', 0, 1);
INSERT INTO `tb_area` VALUES (4, '山西省', 0, 1);
INSERT INTO `tb_area` VALUES (5, '内蒙古自治区', 0, 1);
INSERT INTO `tb_area` VALUES (6, '辽宁省', 0, 1);
INSERT INTO `tb_area` VALUES (7, '吉林省', 0, 1);
INSERT INTO `tb_area` VALUES (8, '市辖区', 1, 1);
INSERT INTO `tb_area` VALUES (9, '黑龙江省', 0, 1);
INSERT INTO `tb_area` VALUES (10, '上海市', 0, 1);
INSERT INTO `tb_area` VALUES (11, '江苏省', 0, 1);
INSERT INTO `tb_area` VALUES (12, '呼和浩特市', 5, 1);
INSERT INTO `tb_area` VALUES (13, '浙江省', 0, 1);
INSERT INTO `tb_area` VALUES (14, '包头市', 5, 1);
INSERT INTO `tb_area` VALUES (15, '太原市', 4, 1);
INSERT INTO `tb_area` VALUES (16, '市辖区', 2, 1);
INSERT INTO `tb_area` VALUES (17, '石家庄市', 3, 1);
INSERT INTO `tb_area` VALUES (18, '安徽省', 0, 1);
INSERT INTO `tb_area` VALUES (19, '乌海市', 5, 1);
INSERT INTO `tb_area` VALUES (20, '大同市', 4, 1);
INSERT INTO `tb_area` VALUES (21, '哈尔滨市', 9, 1);
INSERT INTO `tb_area` VALUES (22, '唐山市', 3, 1);
INSERT INTO `tb_area` VALUES (23, '福建省', 0, 1);
INSERT INTO `tb_area` VALUES (24, '赤峰市', 5, 1);
INSERT INTO `tb_area` VALUES (25, '阳泉市', 4, 1);
INSERT INTO `tb_area` VALUES (26, '市辖区', 10, 1);
INSERT INTO `tb_area` VALUES (27, '沈阳市', 6, 1);
INSERT INTO `tb_area` VALUES (28, '长春市', 7, 1);
INSERT INTO `tb_area` VALUES (29, '新城区', 12, 0);
INSERT INTO `tb_area` VALUES (30, '回民区', 12, 0);
INSERT INTO `tb_area` VALUES (31, '玉泉区', 12, 0);
INSERT INTO `tb_area` VALUES (32, '赛罕区', 12, 0);
INSERT INTO `tb_area` VALUES (33, '土默特左旗', 12, 0);
INSERT INTO `tb_area` VALUES (34, '托克托县', 12, 0);
INSERT INTO `tb_area` VALUES (35, '和林格尔县', 12, 0);
INSERT INTO `tb_area` VALUES (36, '清水河县', 12, 0);
INSERT INTO `tb_area` VALUES (37, '武川县', 12, 0);
INSERT INTO `tb_area` VALUES (38, '呼和浩特金海工业园区', 12, 0);
INSERT INTO `tb_area` VALUES (39, '呼和浩特经济技术开发区', 12, 0);
INSERT INTO `tb_area` VALUES (40, '东城区', 8, 0);
INSERT INTO `tb_area` VALUES (41, '西城区', 8, 0);
INSERT INTO `tb_area` VALUES (42, '朝阳区', 8, 0);
INSERT INTO `tb_area` VALUES (43, '丰台区', 8, 0);
INSERT INTO `tb_area` VALUES (44, '石景山区', 8, 0);
INSERT INTO `tb_area` VALUES (45, '海淀区', 8, 0);
INSERT INTO `tb_area` VALUES (46, '门头沟区', 8, 0);
INSERT INTO `tb_area` VALUES (47, '房山区', 8, 0);
INSERT INTO `tb_area` VALUES (48, '通州区', 8, 0);
INSERT INTO `tb_area` VALUES (49, '顺义区', 8, 0);
INSERT INTO `tb_area` VALUES (50, '昌平区', 8, 0);
INSERT INTO `tb_area` VALUES (51, '大兴区', 8, 0);
INSERT INTO `tb_area` VALUES (52, '怀柔区', 8, 0);
INSERT INTO `tb_area` VALUES (53, '平谷区', 8, 0);
INSERT INTO `tb_area` VALUES (54, '密云区', 8, 0);
INSERT INTO `tb_area` VALUES (55, '延庆区', 8, 0);
INSERT INTO `tb_area` VALUES (56, '齐齐哈尔市', 9, 1);
INSERT INTO `tb_area` VALUES (57, '秦皇岛市', 3, 1);
INSERT INTO `tb_area` VALUES (58, '江西省', 0, 1);
INSERT INTO `tb_area` VALUES (59, '通辽市', 5, 1);
INSERT INTO `tb_area` VALUES (60, '长治市', 4, 1);
INSERT INTO `tb_area` VALUES (61, '和平区', 16, 0);
INSERT INTO `tb_area` VALUES (62, '河东区', 16, 0);
INSERT INTO `tb_area` VALUES (63, '河西区', 16, 0);
INSERT INTO `tb_area` VALUES (64, '南开区', 16, 0);
INSERT INTO `tb_area` VALUES (65, '河北区', 16, 0);
INSERT INTO `tb_area` VALUES (66, '红桥区', 16, 0);
INSERT INTO `tb_area` VALUES (67, '东丽区', 16, 0);
INSERT INTO `tb_area` VALUES (68, '西青区', 16, 0);
INSERT INTO `tb_area` VALUES (69, '津南区', 16, 0);
INSERT INTO `tb_area` VALUES (70, '北辰区', 16, 0);
INSERT INTO `tb_area` VALUES (71, '武清区', 16, 0);
INSERT INTO `tb_area` VALUES (72, '宝坻区', 16, 0);
INSERT INTO `tb_area` VALUES (73, '滨海新区', 16, 0);
INSERT INTO `tb_area` VALUES (74, '宁河区', 16, 0);
INSERT INTO `tb_area` VALUES (75, '静海区', 16, 0);
INSERT INTO `tb_area` VALUES (76, '蓟州区', 16, 0);
INSERT INTO `tb_area` VALUES (77, '小店区', 15, 0);
INSERT INTO `tb_area` VALUES (78, '迎泽区', 15, 0);
INSERT INTO `tb_area` VALUES (79, '杏花岭区', 15, 0);
INSERT INTO `tb_area` VALUES (80, '尖草坪区', 15, 0);
INSERT INTO `tb_area` VALUES (81, '万柏林区', 15, 0);
INSERT INTO `tb_area` VALUES (82, '晋源区', 15, 0);
INSERT INTO `tb_area` VALUES (83, '清徐县', 15, 0);
INSERT INTO `tb_area` VALUES (84, '阳曲县', 15, 0);
INSERT INTO `tb_area` VALUES (85, '娄烦县', 15, 0);
INSERT INTO `tb_area` VALUES (86, '山西转型综合改革示范区', 15, 0);
INSERT INTO `tb_area` VALUES (87, '古交市', 15, 0);
INSERT INTO `tb_area` VALUES (88, '东河区', 14, 0);
INSERT INTO `tb_area` VALUES (89, '昆都仑区', 14, 0);
INSERT INTO `tb_area` VALUES (90, '青山区', 14, 0);
INSERT INTO `tb_area` VALUES (91, '石拐区', 14, 0);
INSERT INTO `tb_area` VALUES (92, '白云鄂博矿区', 14, 0);
INSERT INTO `tb_area` VALUES (93, '九原区', 14, 0);
INSERT INTO `tb_area` VALUES (94, '土默特右旗', 14, 0);
INSERT INTO `tb_area` VALUES (95, '固阳县', 14, 0);
INSERT INTO `tb_area` VALUES (96, '达尔罕茂明安联合旗', 14, 0);
INSERT INTO `tb_area` VALUES (97, '包头稀土高新技术产业开发区', 14, 0);
INSERT INTO `tb_area` VALUES (98, '长安区', 17, 0);
INSERT INTO `tb_area` VALUES (99, '桥西区', 17, 0);
INSERT INTO `tb_area` VALUES (100, '新华区', 17, 0);
INSERT INTO `tb_area` VALUES (101, '井陉矿区', 17, 0);
INSERT INTO `tb_area` VALUES (102, '裕华区', 17, 0);
INSERT INTO `tb_area` VALUES (103, '藁城区', 17, 0);
INSERT INTO `tb_area` VALUES (104, '鹿泉区', 17, 0);
INSERT INTO `tb_area` VALUES (105, '栾城区', 17, 0);
INSERT INTO `tb_area` VALUES (106, '井陉县', 17, 0);
INSERT INTO `tb_area` VALUES (107, '正定县', 17, 0);
INSERT INTO `tb_area` VALUES (108, '行唐县', 17, 0);
INSERT INTO `tb_area` VALUES (109, '灵寿县', 17, 0);
INSERT INTO `tb_area` VALUES (110, '高邑县', 17, 0);
INSERT INTO `tb_area` VALUES (111, '深泽县', 17, 0);
INSERT INTO `tb_area` VALUES (112, '赞皇县', 17, 0);
INSERT INTO `tb_area` VALUES (113, '无极县', 17, 0);
INSERT INTO `tb_area` VALUES (114, '平山县', 17, 0);
INSERT INTO `tb_area` VALUES (115, '元氏县', 17, 0);
INSERT INTO `tb_area` VALUES (116, '赵县', 17, 0);
INSERT INTO `tb_area` VALUES (117, '石家庄高新技术产业开发区', 17, 0);
INSERT INTO `tb_area` VALUES (118, '石家庄循环化工园区', 17, 0);
INSERT INTO `tb_area` VALUES (119, '辛集市', 17, 0);
INSERT INTO `tb_area` VALUES (120, '晋州市', 17, 0);
INSERT INTO `tb_area` VALUES (121, '新乐市', 17, 0);
INSERT INTO `tb_area` VALUES (122, '大连市', 6, 1);
INSERT INTO `tb_area` VALUES (123, '吉林市', 7, 1);
INSERT INTO `tb_area` VALUES (124, '南京市', 11, 1);
INSERT INTO `tb_area` VALUES (125, '鸡西市', 9, 1);
INSERT INTO `tb_area` VALUES (126, '邯郸市', 3, 1);
INSERT INTO `tb_area` VALUES (127, '山东省', 0, 1);
INSERT INTO `tb_area` VALUES (128, '鄂尔多斯市', 5, 1);
INSERT INTO `tb_area` VALUES (129, '晋城市', 4, 1);
INSERT INTO `tb_area` VALUES (130, '路南区', 22, 0);
INSERT INTO `tb_area` VALUES (131, '路北区', 22, 0);
INSERT INTO `tb_area` VALUES (132, '古冶区', 22, 0);
INSERT INTO `tb_area` VALUES (133, '开平区', 22, 0);
INSERT INTO `tb_area` VALUES (134, '丰南区', 22, 0);
INSERT INTO `tb_area` VALUES (135, '丰润区', 22, 0);
INSERT INTO `tb_area` VALUES (136, '曹妃甸区', 22, 0);
INSERT INTO `tb_area` VALUES (137, '滦南县', 22, 0);
INSERT INTO `tb_area` VALUES (138, '乐亭县', 22, 0);
INSERT INTO `tb_area` VALUES (139, '迁西县', 22, 0);
INSERT INTO `tb_area` VALUES (140, '玉田县', 22, 0);
INSERT INTO `tb_area` VALUES (141, '唐山市芦台经济技术开发区', 22, 0);
INSERT INTO `tb_area` VALUES (142, '唐山市汉沽管理区', 22, 0);
INSERT INTO `tb_area` VALUES (143, '唐山高新技术产业开发区', 22, 0);
INSERT INTO `tb_area` VALUES (144, '河北唐山海港经济开发区', 22, 0);
INSERT INTO `tb_area` VALUES (145, '遵化市', 22, 0);
INSERT INTO `tb_area` VALUES (146, '迁安市', 22, 0);
INSERT INTO `tb_area` VALUES (147, '滦州市', 22, 0);
INSERT INTO `tb_area` VALUES (148, '道里区', 21, 0);
INSERT INTO `tb_area` VALUES (149, '南岗区', 21, 0);
INSERT INTO `tb_area` VALUES (150, '道外区', 21, 0);
INSERT INTO `tb_area` VALUES (151, '平房区', 21, 0);
INSERT INTO `tb_area` VALUES (152, '松北区', 21, 0);
INSERT INTO `tb_area` VALUES (153, '香坊区', 21, 0);
INSERT INTO `tb_area` VALUES (154, '呼兰区', 21, 0);
INSERT INTO `tb_area` VALUES (155, '阿城区', 21, 0);
INSERT INTO `tb_area` VALUES (156, '双城区', 21, 0);
INSERT INTO `tb_area` VALUES (157, '依兰县', 21, 0);
INSERT INTO `tb_area` VALUES (158, '方正县', 21, 0);
INSERT INTO `tb_area` VALUES (159, '宾县', 21, 0);
INSERT INTO `tb_area` VALUES (160, '巴彦县', 21, 0);
INSERT INTO `tb_area` VALUES (161, '木兰县', 21, 0);
INSERT INTO `tb_area` VALUES (162, '通河县', 21, 0);
INSERT INTO `tb_area` VALUES (163, '延寿县', 21, 0);
INSERT INTO `tb_area` VALUES (164, '尚志市', 21, 0);
INSERT INTO `tb_area` VALUES (165, '五常市', 21, 0);
INSERT INTO `tb_area` VALUES (166, '新荣区', 20, 0);
INSERT INTO `tb_area` VALUES (167, '平城区', 20, 0);
INSERT INTO `tb_area` VALUES (168, '云冈区', 20, 0);
INSERT INTO `tb_area` VALUES (169, '云州区', 20, 0);
INSERT INTO `tb_area` VALUES (170, '阳高县', 20, 0);
INSERT INTO `tb_area` VALUES (171, '天镇县', 20, 0);
INSERT INTO `tb_area` VALUES (172, '广灵县', 20, 0);
INSERT INTO `tb_area` VALUES (173, '灵丘县', 20, 0);
INSERT INTO `tb_area` VALUES (174, '浑源县', 20, 0);
INSERT INTO `tb_area` VALUES (175, '左云县', 20, 0);
INSERT INTO `tb_area` VALUES (176, '山西大同经济开发区', 20, 0);
INSERT INTO `tb_area` VALUES (177, '鞍山市', 6, 1);
INSERT INTO `tb_area` VALUES (178, '四平市', 7, 1);
INSERT INTO `tb_area` VALUES (179, '无锡市', 11, 1);
INSERT INTO `tb_area` VALUES (180, '鹤岗市', 9, 1);
INSERT INTO `tb_area` VALUES (181, '邢台市', 3, 1);
INSERT INTO `tb_area` VALUES (182, '河南省', 0, 1);
INSERT INTO `tb_area` VALUES (183, '呼伦贝尔市', 5, 1);
INSERT INTO `tb_area` VALUES (184, '朔州市', 4, 1);
INSERT INTO `tb_area` VALUES (185, '海勃湾区', 19, 0);
INSERT INTO `tb_area` VALUES (186, '海南区', 19, 0);
INSERT INTO `tb_area` VALUES (187, '乌达区', 19, 0);
INSERT INTO `tb_area` VALUES (188, '海港区', 57, 0);
INSERT INTO `tb_area` VALUES (189, '山海关区', 57, 0);
INSERT INTO `tb_area` VALUES (190, '北戴河区', 57, 0);
INSERT INTO `tb_area` VALUES (191, '抚宁区', 57, 0);
INSERT INTO `tb_area` VALUES (192, '青龙满族自治县', 57, 0);
INSERT INTO `tb_area` VALUES (193, '昌黎县', 57, 0);
INSERT INTO `tb_area` VALUES (194, '卢龙县', 57, 0);
INSERT INTO `tb_area` VALUES (195, '秦皇岛市经济技术开发区', 57, 0);
INSERT INTO `tb_area` VALUES (196, '北戴河新区', 57, 0);
INSERT INTO `tb_area` VALUES (197, '龙沙区', 56, 0);
INSERT INTO `tb_area` VALUES (198, '建华区', 56, 0);
INSERT INTO `tb_area` VALUES (199, '铁锋区', 56, 0);
INSERT INTO `tb_area` VALUES (200, '昂昂溪区', 56, 0);
INSERT INTO `tb_area` VALUES (201, '富拉尔基区', 56, 0);
INSERT INTO `tb_area` VALUES (202, '碾子山区', 56, 0);
INSERT INTO `tb_area` VALUES (203, '梅里斯达斡尔族区', 56, 0);
INSERT INTO `tb_area` VALUES (204, '龙江县', 56, 0);
INSERT INTO `tb_area` VALUES (205, '依安县', 56, 0);
INSERT INTO `tb_area` VALUES (206, '泰来县', 56, 0);
INSERT INTO `tb_area` VALUES (207, '甘南县', 56, 0);
INSERT INTO `tb_area` VALUES (208, '富裕县', 56, 0);
INSERT INTO `tb_area` VALUES (209, '克山县', 56, 0);
INSERT INTO `tb_area` VALUES (210, '克东县', 56, 0);
INSERT INTO `tb_area` VALUES (211, '拜泉县', 56, 0);
INSERT INTO `tb_area` VALUES (212, '讷河市', 56, 0);
INSERT INTO `tb_area` VALUES (213, '抚顺市', 6, 1);
INSERT INTO `tb_area` VALUES (214, '辽源市', 7, 1);
INSERT INTO `tb_area` VALUES (215, '徐州市', 11, 1);
INSERT INTO `tb_area` VALUES (216, '双鸭山市', 9, 1);
INSERT INTO `tb_area` VALUES (217, '保定市', 3, 1);
INSERT INTO `tb_area` VALUES (218, '湖北省', 0, 1);
INSERT INTO `tb_area` VALUES (219, '巴彦淖尔市', 5, 1);
INSERT INTO `tb_area` VALUES (220, '晋中市', 4, 1);
INSERT INTO `tb_area` VALUES (221, '合肥市', 18, 1);
INSERT INTO `tb_area` VALUES (222, '南关区', 28, 0);
INSERT INTO `tb_area` VALUES (223, '宽城区', 28, 0);
INSERT INTO `tb_area` VALUES (224, '朝阳区', 28, 0);
INSERT INTO `tb_area` VALUES (225, '二道区', 28, 0);
INSERT INTO `tb_area` VALUES (226, '绿园区', 28, 0);
INSERT INTO `tb_area` VALUES (227, '双阳区', 28, 0);
INSERT INTO `tb_area` VALUES (228, '九台区', 28, 0);
INSERT INTO `tb_area` VALUES (229, '农安县', 28, 0);
INSERT INTO `tb_area` VALUES (230, '长春经济技术开发区', 28, 0);
INSERT INTO `tb_area` VALUES (231, '长春净月高新技术产业开发区', 28, 0);
INSERT INTO `tb_area` VALUES (232, '长春高新技术产业开发区', 28, 0);
INSERT INTO `tb_area` VALUES (233, '长春汽车经济技术开发区', 28, 0);
INSERT INTO `tb_area` VALUES (234, '榆树市', 28, 0);
INSERT INTO `tb_area` VALUES (235, '德惠市', 28, 0);
INSERT INTO `tb_area` VALUES (236, '和平区', 27, 0);
INSERT INTO `tb_area` VALUES (237, '沈河区', 27, 0);
INSERT INTO `tb_area` VALUES (238, '大东区', 27, 0);
INSERT INTO `tb_area` VALUES (239, '皇姑区', 27, 0);
INSERT INTO `tb_area` VALUES (240, '铁西区', 27, 0);
INSERT INTO `tb_area` VALUES (241, '苏家屯区', 27, 0);
INSERT INTO `tb_area` VALUES (242, '浑南区', 27, 0);
INSERT INTO `tb_area` VALUES (243, '沈北新区', 27, 0);
INSERT INTO `tb_area` VALUES (244, '于洪区', 27, 0);
INSERT INTO `tb_area` VALUES (245, '辽中区', 27, 0);
INSERT INTO `tb_area` VALUES (246, '康平县', 27, 0);
INSERT INTO `tb_area` VALUES (247, '法库县', 27, 0);
INSERT INTO `tb_area` VALUES (248, '新民市', 27, 0);
INSERT INTO `tb_area` VALUES (249, '黄浦区', 26, 0);
INSERT INTO `tb_area` VALUES (250, '徐汇区', 26, 0);
INSERT INTO `tb_area` VALUES (251, '长宁区', 26, 0);
INSERT INTO `tb_area` VALUES (252, '静安区', 26, 0);
INSERT INTO `tb_area` VALUES (253, '普陀区', 26, 0);
INSERT INTO `tb_area` VALUES (254, '虹口区', 26, 0);
INSERT INTO `tb_area` VALUES (255, '杨浦区', 26, 0);
INSERT INTO `tb_area` VALUES (256, '闵行区', 26, 0);
INSERT INTO `tb_area` VALUES (257, '宝山区', 26, 0);
INSERT INTO `tb_area` VALUES (258, '嘉定区', 26, 0);
INSERT INTO `tb_area` VALUES (259, '浦东新区', 26, 0);
INSERT INTO `tb_area` VALUES (260, '金山区', 26, 0);
INSERT INTO `tb_area` VALUES (261, '松江区', 26, 0);
INSERT INTO `tb_area` VALUES (262, '青浦区', 26, 0);
INSERT INTO `tb_area` VALUES (263, '奉贤区', 26, 0);
INSERT INTO `tb_area` VALUES (264, '崇明区', 26, 0);
INSERT INTO `tb_area` VALUES (265, '杭州市', 13, 1);
INSERT INTO `tb_area` VALUES (266, '本溪市', 6, 1);
INSERT INTO `tb_area` VALUES (267, '通化市', 7, 1);
INSERT INTO `tb_area` VALUES (268, '常州市', 11, 1);
INSERT INTO `tb_area` VALUES (269, '大庆市', 9, 1);
INSERT INTO `tb_area` VALUES (270, '张家口市', 3, 1);
INSERT INTO `tb_area` VALUES (271, '湖南省', 0, 1);
INSERT INTO `tb_area` VALUES (272, '乌兰察布市', 5, 1);
INSERT INTO `tb_area` VALUES (273, '运城市', 4, 1);
INSERT INTO `tb_area` VALUES (274, '城区', 25, 0);
INSERT INTO `tb_area` VALUES (275, '矿区', 25, 0);
INSERT INTO `tb_area` VALUES (276, '郊区', 25, 0);
INSERT INTO `tb_area` VALUES (277, '平定县', 25, 0);
INSERT INTO `tb_area` VALUES (278, '盂县', 25, 0);
INSERT INTO `tb_area` VALUES (279, '红山区', 24, 0);
INSERT INTO `tb_area` VALUES (280, '元宝山区', 24, 0);
INSERT INTO `tb_area` VALUES (281, '松山区', 24, 0);
INSERT INTO `tb_area` VALUES (282, '阿鲁科尔沁旗', 24, 0);
INSERT INTO `tb_area` VALUES (283, '巴林左旗', 24, 0);
INSERT INTO `tb_area` VALUES (284, '巴林右旗', 24, 0);
INSERT INTO `tb_area` VALUES (285, '林西县', 24, 0);
INSERT INTO `tb_area` VALUES (286, '克什克腾旗', 24, 0);
INSERT INTO `tb_area` VALUES (287, '翁牛特旗', 24, 0);
INSERT INTO `tb_area` VALUES (288, '喀喇沁旗', 24, 0);
INSERT INTO `tb_area` VALUES (289, '宁城县', 24, 0);
INSERT INTO `tb_area` VALUES (290, '敖汉旗', 24, 0);
INSERT INTO `tb_area` VALUES (291, '邯山区', 126, 0);
INSERT INTO `tb_area` VALUES (292, '丛台区', 126, 0);
INSERT INTO `tb_area` VALUES (293, '复兴区', 126, 0);
INSERT INTO `tb_area` VALUES (294, '峰峰矿区', 126, 0);
INSERT INTO `tb_area` VALUES (295, '肥乡区', 126, 0);
INSERT INTO `tb_area` VALUES (296, '永年区', 126, 0);
INSERT INTO `tb_area` VALUES (297, '临漳县', 126, 0);
INSERT INTO `tb_area` VALUES (298, '成安县', 126, 0);
INSERT INTO `tb_area` VALUES (299, '大名县', 126, 0);
INSERT INTO `tb_area` VALUES (300, '涉县', 126, 0);
INSERT INTO `tb_area` VALUES (301, '磁县', 126, 0);
INSERT INTO `tb_area` VALUES (302, '邱县', 126, 0);
INSERT INTO `tb_area` VALUES (303, '鸡泽县', 126, 0);
INSERT INTO `tb_area` VALUES (304, '广平县', 126, 0);
INSERT INTO `tb_area` VALUES (305, '馆陶县', 126, 0);
INSERT INTO `tb_area` VALUES (306, '魏县', 126, 0);
INSERT INTO `tb_area` VALUES (307, '曲周县', 126, 0);
INSERT INTO `tb_area` VALUES (308, '邯郸经济技术开发区', 126, 0);
INSERT INTO `tb_area` VALUES (309, '邯郸冀南新区', 126, 0);
INSERT INTO `tb_area` VALUES (310, '武安市', 126, 0);
INSERT INTO `tb_area` VALUES (311, '鸡冠区', 125, 0);
INSERT INTO `tb_area` VALUES (312, '恒山区', 125, 0);
INSERT INTO `tb_area` VALUES (313, '滴道区', 125, 0);
INSERT INTO `tb_area` VALUES (314, '梨树区', 125, 0);
INSERT INTO `tb_area` VALUES (315, '城子河区', 125, 0);
INSERT INTO `tb_area` VALUES (316, '麻山区', 125, 0);
INSERT INTO `tb_area` VALUES (317, '鸡东县', 125, 0);
INSERT INTO `tb_area` VALUES (318, '虎林市', 125, 0);
INSERT INTO `tb_area` VALUES (319, '密山市', 125, 0);
INSERT INTO `tb_area` VALUES (320, '芜湖市', 18, 1);
INSERT INTO `tb_area` VALUES (321, '宁波市', 13, 1);
INSERT INTO `tb_area` VALUES (322, '丹东市', 6, 1);
INSERT INTO `tb_area` VALUES (323, '白山市', 7, 1);
INSERT INTO `tb_area` VALUES (324, '苏州市', 11, 1);
INSERT INTO `tb_area` VALUES (325, '伊春市', 9, 1);
INSERT INTO `tb_area` VALUES (326, '承德市', 3, 1);
INSERT INTO `tb_area` VALUES (327, '广东省', 0, 1);
INSERT INTO `tb_area` VALUES (328, '兴安盟', 5, 1);
INSERT INTO `tb_area` VALUES (329, '忻州市', 4, 1);
INSERT INTO `tb_area` VALUES (330, '玄武区', 124, 0);
INSERT INTO `tb_area` VALUES (331, '秦淮区', 124, 0);
INSERT INTO `tb_area` VALUES (332, '建邺区', 124, 0);
INSERT INTO `tb_area` VALUES (333, '鼓楼区', 124, 0);
INSERT INTO `tb_area` VALUES (334, '浦口区', 124, 0);
INSERT INTO `tb_area` VALUES (335, '栖霞区', 124, 0);
INSERT INTO `tb_area` VALUES (336, '雨花台区', 124, 0);
INSERT INTO `tb_area` VALUES (337, '江宁区', 124, 0);
INSERT INTO `tb_area` VALUES (338, '六合区', 124, 0);
INSERT INTO `tb_area` VALUES (339, '溧水区', 124, 0);
INSERT INTO `tb_area` VALUES (340, '高淳区', 124, 0);
INSERT INTO `tb_area` VALUES (341, '昌邑区', 123, 0);
INSERT INTO `tb_area` VALUES (342, '龙潭区', 123, 0);
INSERT INTO `tb_area` VALUES (343, '船营区', 123, 0);
INSERT INTO `tb_area` VALUES (344, '丰满区', 123, 0);
INSERT INTO `tb_area` VALUES (345, '永吉县', 123, 0);
INSERT INTO `tb_area` VALUES (346, '吉林经济开发区', 123, 0);
INSERT INTO `tb_area` VALUES (347, '吉林高新技术产业开发区', 123, 0);
INSERT INTO `tb_area` VALUES (348, '吉林中国新加坡食品区', 123, 0);
INSERT INTO `tb_area` VALUES (349, '蛟河市', 123, 0);
INSERT INTO `tb_area` VALUES (350, '桦甸市', 123, 0);
INSERT INTO `tb_area` VALUES (351, '舒兰市', 123, 0);
INSERT INTO `tb_area` VALUES (352, '磐石市', 123, 0);
INSERT INTO `tb_area` VALUES (353, '中山区', 122, 0);
INSERT INTO `tb_area` VALUES (354, '西岗区', 122, 0);
INSERT INTO `tb_area` VALUES (355, '沙河口区', 122, 0);
INSERT INTO `tb_area` VALUES (356, '甘井子区', 122, 0);
INSERT INTO `tb_area` VALUES (357, '旅顺口区', 122, 0);
INSERT INTO `tb_area` VALUES (358, '金州区', 122, 0);
INSERT INTO `tb_area` VALUES (359, '普兰店区', 122, 0);
INSERT INTO `tb_area` VALUES (360, '长海县', 122, 0);
INSERT INTO `tb_area` VALUES (361, '瓦房店市', 122, 0);
INSERT INTO `tb_area` VALUES (362, '庄河市', 122, 0);
INSERT INTO `tb_area` VALUES (363, '福州市', 23, 1);
INSERT INTO `tb_area` VALUES (364, '蚌埠市', 18, 1);
INSERT INTO `tb_area` VALUES (365, '温州市', 13, 1);
INSERT INTO `tb_area` VALUES (366, '锦州市', 6, 1);
INSERT INTO `tb_area` VALUES (367, '松原市', 7, 1);
INSERT INTO `tb_area` VALUES (368, '南通市', 11, 1);
INSERT INTO `tb_area` VALUES (369, '佳木斯市', 9, 1);
INSERT INTO `tb_area` VALUES (370, '沧州市', 3, 1);
INSERT INTO `tb_area` VALUES (371, '广西壮族自治区', 0, 1);
INSERT INTO `tb_area` VALUES (372, '锡林郭勒盟', 5, 1);
INSERT INTO `tb_area` VALUES (373, '临汾市', 4, 1);
INSERT INTO `tb_area` VALUES (374, '潞州区', 60, 0);
INSERT INTO `tb_area` VALUES (375, '上党区', 60, 0);
INSERT INTO `tb_area` VALUES (376, '屯留区', 60, 0);
INSERT INTO `tb_area` VALUES (377, '潞城区', 60, 0);
INSERT INTO `tb_area` VALUES (378, '襄垣县', 60, 0);
INSERT INTO `tb_area` VALUES (379, '平顺县', 60, 0);
INSERT INTO `tb_area` VALUES (380, '黎城县', 60, 0);
INSERT INTO `tb_area` VALUES (381, '壶关县', 60, 0);
INSERT INTO `tb_area` VALUES (382, '长子县', 60, 0);
INSERT INTO `tb_area` VALUES (383, '武乡县', 60, 0);
INSERT INTO `tb_area` VALUES (384, '沁县', 60, 0);
INSERT INTO `tb_area` VALUES (385, '沁源县', 60, 0);
INSERT INTO `tb_area` VALUES (386, '山西长治高新技术产业园区', 60, 0);
INSERT INTO `tb_area` VALUES (387, '科尔沁区', 59, 0);
INSERT INTO `tb_area` VALUES (388, '科尔沁左翼中旗', 59, 0);
INSERT INTO `tb_area` VALUES (389, '科尔沁左翼后旗', 59, 0);
INSERT INTO `tb_area` VALUES (390, '开鲁县', 59, 0);
INSERT INTO `tb_area` VALUES (391, '库伦旗', 59, 0);
INSERT INTO `tb_area` VALUES (392, '奈曼旗', 59, 0);
INSERT INTO `tb_area` VALUES (393, '扎鲁特旗', 59, 0);
INSERT INTO `tb_area` VALUES (394, '通辽经济技术开发区', 59, 0);
INSERT INTO `tb_area` VALUES (395, '霍林郭勒市', 59, 0);
INSERT INTO `tb_area` VALUES (396, '桥东区', 181, 0);
INSERT INTO `tb_area` VALUES (397, '桥西区', 181, 0);
INSERT INTO `tb_area` VALUES (398, '邢台县', 181, 0);
INSERT INTO `tb_area` VALUES (399, '临城县', 181, 0);
INSERT INTO `tb_area` VALUES (400, '内丘县', 181, 0);
INSERT INTO `tb_area` VALUES (401, '柏乡县', 181, 0);
INSERT INTO `tb_area` VALUES (402, '隆尧县', 181, 0);
INSERT INTO `tb_area` VALUES (403, '任县', 181, 0);
INSERT INTO `tb_area` VALUES (404, '南和县', 181, 0);
INSERT INTO `tb_area` VALUES (405, '宁晋县', 181, 0);
INSERT INTO `tb_area` VALUES (406, '巨鹿县', 181, 0);
INSERT INTO `tb_area` VALUES (407, '新河县', 181, 0);
INSERT INTO `tb_area` VALUES (408, '广宗县', 181, 0);
INSERT INTO `tb_area` VALUES (409, '平乡县', 181, 0);
INSERT INTO `tb_area` VALUES (410, '威县', 181, 0);
INSERT INTO `tb_area` VALUES (411, '清河县', 181, 0);
INSERT INTO `tb_area` VALUES (412, '临西县', 181, 0);
INSERT INTO `tb_area` VALUES (413, '河北邢台经济开发区', 181, 0);
INSERT INTO `tb_area` VALUES (414, '南宫市', 181, 0);
INSERT INTO `tb_area` VALUES (415, '沙河市', 181, 0);
INSERT INTO `tb_area` VALUES (416, '向阳区', 180, 0);
INSERT INTO `tb_area` VALUES (417, '工农区', 180, 0);
INSERT INTO `tb_area` VALUES (418, '南山区', 180, 0);
INSERT INTO `tb_area` VALUES (419, '兴安区', 180, 0);
INSERT INTO `tb_area` VALUES (420, '东山区', 180, 0);
INSERT INTO `tb_area` VALUES (421, '兴山区', 180, 0);
INSERT INTO `tb_area` VALUES (422, '萝北县', 180, 0);
INSERT INTO `tb_area` VALUES (423, '绥滨县', 180, 0);
INSERT INTO `tb_area` VALUES (424, '厦门市', 23, 1);
INSERT INTO `tb_area` VALUES (425, '淮南市', 18, 1);
INSERT INTO `tb_area` VALUES (426, '嘉兴市', 13, 1);
INSERT INTO `tb_area` VALUES (427, '营口市', 6, 1);
INSERT INTO `tb_area` VALUES (428, '白城市', 7, 1);
INSERT INTO `tb_area` VALUES (429, '连云港市', 11, 1);
INSERT INTO `tb_area` VALUES (430, '七台河市', 9, 1);
INSERT INTO `tb_area` VALUES (431, '廊坊市', 3, 1);
INSERT INTO `tb_area` VALUES (432, '海南省', 0, 1);
INSERT INTO `tb_area` VALUES (433, '阿拉善盟', 5, 1);
INSERT INTO `tb_area` VALUES (434, '吕梁市', 4, 1);
INSERT INTO `tb_area` VALUES (435, '锡山区', 179, 0);
INSERT INTO `tb_area` VALUES (436, '惠山区', 179, 0);
INSERT INTO `tb_area` VALUES (437, '滨湖区', 179, 0);
INSERT INTO `tb_area` VALUES (438, '梁溪区', 179, 0);
INSERT INTO `tb_area` VALUES (439, '新吴区', 179, 0);
INSERT INTO `tb_area` VALUES (440, '江阴市', 179, 0);
INSERT INTO `tb_area` VALUES (441, '宜兴市', 179, 0);
INSERT INTO `tb_area` VALUES (442, '铁西区', 178, 0);
INSERT INTO `tb_area` VALUES (443, '铁东区', 178, 0);
INSERT INTO `tb_area` VALUES (444, '梨树县', 178, 0);
INSERT INTO `tb_area` VALUES (445, '伊通满族自治县', 178, 0);
INSERT INTO `tb_area` VALUES (446, '公主岭市', 178, 0);
INSERT INTO `tb_area` VALUES (447, '双辽市', 178, 0);
INSERT INTO `tb_area` VALUES (448, '铁东区', 177, 0);
INSERT INTO `tb_area` VALUES (449, '铁西区', 177, 0);
INSERT INTO `tb_area` VALUES (450, '立山区', 177, 0);
INSERT INTO `tb_area` VALUES (451, '千山区', 177, 0);
INSERT INTO `tb_area` VALUES (452, '台安县', 177, 0);
INSERT INTO `tb_area` VALUES (453, '岫岩满族自治县', 177, 0);
INSERT INTO `tb_area` VALUES (454, '海城市', 177, 0);
INSERT INTO `tb_area` VALUES (455, '南昌市', 58, 1);
INSERT INTO `tb_area` VALUES (456, '莆田市', 23, 1);
INSERT INTO `tb_area` VALUES (457, '马鞍山市', 18, 1);
INSERT INTO `tb_area` VALUES (458, '湖州市', 13, 1);
INSERT INTO `tb_area` VALUES (459, '阜新市', 6, 1);
INSERT INTO `tb_area` VALUES (460, '延边朝鲜族自治州', 7, 1);
INSERT INTO `tb_area` VALUES (461, '淮安市', 11, 1);
INSERT INTO `tb_area` VALUES (462, '牡丹江市', 9, 1);
INSERT INTO `tb_area` VALUES (463, '衡水市', 3, 1);
INSERT INTO `tb_area` VALUES (464, '重庆市', 0, 1);
INSERT INTO `tb_area` VALUES (465, '城区', 129, 0);
INSERT INTO `tb_area` VALUES (466, '沁水县', 129, 0);
INSERT INTO `tb_area` VALUES (467, '阳城县', 129, 0);
INSERT INTO `tb_area` VALUES (468, '陵川县', 129, 0);
INSERT INTO `tb_area` VALUES (469, '泽州县', 129, 0);
INSERT INTO `tb_area` VALUES (470, '高平市', 129, 0);
INSERT INTO `tb_area` VALUES (471, '东胜区', 128, 0);
INSERT INTO `tb_area` VALUES (472, '康巴什区', 128, 0);
INSERT INTO `tb_area` VALUES (473, '达拉特旗', 128, 0);
INSERT INTO `tb_area` VALUES (474, '准格尔旗', 128, 0);
INSERT INTO `tb_area` VALUES (475, '鄂托克前旗', 128, 0);
INSERT INTO `tb_area` VALUES (476, '鄂托克旗', 128, 0);
INSERT INTO `tb_area` VALUES (477, '杭锦旗', 128, 0);
INSERT INTO `tb_area` VALUES (478, '乌审旗', 128, 0);
INSERT INTO `tb_area` VALUES (479, '伊金霍洛旗', 128, 0);
INSERT INTO `tb_area` VALUES (480, '竞秀区', 217, 0);
INSERT INTO `tb_area` VALUES (481, '莲池区', 217, 0);
INSERT INTO `tb_area` VALUES (482, '满城区', 217, 0);
INSERT INTO `tb_area` VALUES (483, '清苑区', 217, 0);
INSERT INTO `tb_area` VALUES (484, '徐水区', 217, 0);
INSERT INTO `tb_area` VALUES (485, '涞水县', 217, 0);
INSERT INTO `tb_area` VALUES (486, '阜平县', 217, 0);
INSERT INTO `tb_area` VALUES (487, '定兴县', 217, 0);
INSERT INTO `tb_area` VALUES (488, '唐县', 217, 0);
INSERT INTO `tb_area` VALUES (489, '高阳县', 217, 0);
INSERT INTO `tb_area` VALUES (490, '容城县', 217, 0);
INSERT INTO `tb_area` VALUES (491, '涞源县', 217, 0);
INSERT INTO `tb_area` VALUES (492, '望都县', 217, 0);
INSERT INTO `tb_area` VALUES (493, '安新县', 217, 0);
INSERT INTO `tb_area` VALUES (494, '易县', 217, 0);
INSERT INTO `tb_area` VALUES (495, '曲阳县', 217, 0);
INSERT INTO `tb_area` VALUES (496, '蠡县', 217, 0);
INSERT INTO `tb_area` VALUES (497, '顺平县', 217, 0);
INSERT INTO `tb_area` VALUES (498, '博野县', 217, 0);
INSERT INTO `tb_area` VALUES (499, '雄县', 217, 0);
INSERT INTO `tb_area` VALUES (500, '保定高新技术产业开发区', 217, 0);
INSERT INTO `tb_area` VALUES (501, '保定白沟新城', 217, 0);
INSERT INTO `tb_area` VALUES (502, '涿州市', 217, 0);
INSERT INTO `tb_area` VALUES (503, '定州市', 217, 0);
INSERT INTO `tb_area` VALUES (504, '安国市', 217, 0);
INSERT INTO `tb_area` VALUES (505, '高碑店市', 217, 0);
INSERT INTO `tb_area` VALUES (506, '景德镇市', 58, 1);
INSERT INTO `tb_area` VALUES (507, '三明市', 23, 1);
INSERT INTO `tb_area` VALUES (508, '淮北市', 18, 1);
INSERT INTO `tb_area` VALUES (509, '绍兴市', 13, 1);
INSERT INTO `tb_area` VALUES (510, '辽阳市', 6, 1);
INSERT INTO `tb_area` VALUES (511, '盐城市', 11, 1);
INSERT INTO `tb_area` VALUES (512, '黑河市', 9, 1);
INSERT INTO `tb_area` VALUES (513, '四川省', 0, 1);
INSERT INTO `tb_area` VALUES (514, '济南市', 127, 1);
INSERT INTO `tb_area` VALUES (515, '鼓楼区', 215, 0);
INSERT INTO `tb_area` VALUES (516, '云龙区', 215, 0);
INSERT INTO `tb_area` VALUES (517, '贾汪区', 215, 0);
INSERT INTO `tb_area` VALUES (518, '泉山区', 215, 0);
INSERT INTO `tb_area` VALUES (519, '铜山区', 215, 0);
INSERT INTO `tb_area` VALUES (520, '丰县', 215, 0);
INSERT INTO `tb_area` VALUES (521, '沛县', 215, 0);
INSERT INTO `tb_area` VALUES (522, '睢宁县', 215, 0);
INSERT INTO `tb_area` VALUES (523, '徐州经济技术开发区', 215, 0);
INSERT INTO `tb_area` VALUES (524, '新沂市', 215, 0);
INSERT INTO `tb_area` VALUES (525, '邳州市', 215, 0);
INSERT INTO `tb_area` VALUES (526, '龙山区', 214, 0);
INSERT INTO `tb_area` VALUES (527, '西安区', 214, 0);
INSERT INTO `tb_area` VALUES (528, '东丰县', 214, 0);
INSERT INTO `tb_area` VALUES (529, '东辽县', 214, 0);
INSERT INTO `tb_area` VALUES (530, '新抚区', 213, 0);
INSERT INTO `tb_area` VALUES (531, '东洲区', 213, 0);
INSERT INTO `tb_area` VALUES (532, '望花区', 213, 0);
INSERT INTO `tb_area` VALUES (533, '顺城区', 213, 0);
INSERT INTO `tb_area` VALUES (534, '抚顺县', 213, 0);
INSERT INTO `tb_area` VALUES (535, '新宾满族自治县', 213, 0);
INSERT INTO `tb_area` VALUES (536, '清原满族自治县', 213, 0);
INSERT INTO `tb_area` VALUES (537, '萍乡市', 58, 1);
INSERT INTO `tb_area` VALUES (538, '泉州市', 23, 1);
INSERT INTO `tb_area` VALUES (539, '铜陵市', 18, 1);
INSERT INTO `tb_area` VALUES (540, '金华市', 13, 1);
INSERT INTO `tb_area` VALUES (541, '盘锦市', 6, 1);
INSERT INTO `tb_area` VALUES (542, '扬州市', 11, 1);
INSERT INTO `tb_area` VALUES (543, '绥化市', 9, 1);
INSERT INTO `tb_area` VALUES (544, '贵州省', 0, 1);
INSERT INTO `tb_area` VALUES (545, '青岛市', 127, 1);
INSERT INTO `tb_area` VALUES (546, '朔城区', 184, 0);
INSERT INTO `tb_area` VALUES (547, '平鲁区', 184, 0);
INSERT INTO `tb_area` VALUES (548, '山阴县', 184, 0);
INSERT INTO `tb_area` VALUES (549, '应县', 184, 0);
INSERT INTO `tb_area` VALUES (550, '右玉县', 184, 0);
INSERT INTO `tb_area` VALUES (551, '山西朔州经济开发区', 184, 0);
INSERT INTO `tb_area` VALUES (552, '怀仁市', 184, 0);
INSERT INTO `tb_area` VALUES (553, '海拉尔区', 183, 0);
INSERT INTO `tb_area` VALUES (554, '扎赉诺尔区', 183, 0);
INSERT INTO `tb_area` VALUES (555, '阿荣旗', 183, 0);
INSERT INTO `tb_area` VALUES (556, '莫力达瓦达斡尔族自治旗', 183, 0);
INSERT INTO `tb_area` VALUES (557, '鄂伦春自治旗', 183, 0);
INSERT INTO `tb_area` VALUES (558, '鄂温克族自治旗', 183, 0);
INSERT INTO `tb_area` VALUES (559, '陈巴尔虎旗', 183, 0);
INSERT INTO `tb_area` VALUES (560, '新巴尔虎左旗', 183, 0);
INSERT INTO `tb_area` VALUES (561, '新巴尔虎右旗', 183, 0);
INSERT INTO `tb_area` VALUES (562, '满洲里市', 183, 0);
INSERT INTO `tb_area` VALUES (563, '牙克石市', 183, 0);
INSERT INTO `tb_area` VALUES (564, '扎兰屯市', 183, 0);
INSERT INTO `tb_area` VALUES (565, '额尔古纳市', 183, 0);
INSERT INTO `tb_area` VALUES (566, '根河市', 183, 0);
INSERT INTO `tb_area` VALUES (567, '九江市', 58, 1);
INSERT INTO `tb_area` VALUES (568, '漳州市', 23, 1);
INSERT INTO `tb_area` VALUES (569, '安庆市', 18, 1);
INSERT INTO `tb_area` VALUES (570, '衢州市', 13, 1);
INSERT INTO `tb_area` VALUES (571, '铁岭市', 6, 1);
INSERT INTO `tb_area` VALUES (572, '镇江市', 11, 1);
INSERT INTO `tb_area` VALUES (573, '大兴安岭地区', 9, 1);
INSERT INTO `tb_area` VALUES (574, '云南省', 0, 1);
INSERT INTO `tb_area` VALUES (575, '淄博市', 127, 1);
INSERT INTO `tb_area` VALUES (576, '桥东区', 270, 0);
INSERT INTO `tb_area` VALUES (577, '桥西区', 270, 0);
INSERT INTO `tb_area` VALUES (578, '宣化区', 270, 0);
INSERT INTO `tb_area` VALUES (579, '下花园区', 270, 0);
INSERT INTO `tb_area` VALUES (580, '万全区', 270, 0);
INSERT INTO `tb_area` VALUES (581, '崇礼区', 270, 0);
INSERT INTO `tb_area` VALUES (582, '张北县', 270, 0);
INSERT INTO `tb_area` VALUES (583, '康保县', 270, 0);
INSERT INTO `tb_area` VALUES (584, '沽源县', 270, 0);
INSERT INTO `tb_area` VALUES (585, '尚义县', 270, 0);
INSERT INTO `tb_area` VALUES (586, '蔚县', 270, 0);
INSERT INTO `tb_area` VALUES (587, '阳原县', 270, 0);
INSERT INTO `tb_area` VALUES (588, '怀安县', 270, 0);
INSERT INTO `tb_area` VALUES (589, '怀来县', 270, 0);
INSERT INTO `tb_area` VALUES (590, '涿鹿县', 270, 0);
INSERT INTO `tb_area` VALUES (591, '赤城县', 270, 0);
INSERT INTO `tb_area` VALUES (592, '张家口市高新技术产业开发区', 270, 0);
INSERT INTO `tb_area` VALUES (593, '张家口市察北管理区', 270, 0);
INSERT INTO `tb_area` VALUES (594, '张家口市塞北管理区', 270, 0);
INSERT INTO `tb_area` VALUES (595, '萨尔图区', 269, 0);
INSERT INTO `tb_area` VALUES (596, '龙凤区', 269, 0);
INSERT INTO `tb_area` VALUES (597, '让胡路区', 269, 0);
INSERT INTO `tb_area` VALUES (598, '红岗区', 269, 0);
INSERT INTO `tb_area` VALUES (599, '大同区', 269, 0);
INSERT INTO `tb_area` VALUES (600, '肇州县', 269, 0);
INSERT INTO `tb_area` VALUES (601, '肇源县', 269, 0);
INSERT INTO `tb_area` VALUES (602, '林甸县', 269, 0);
INSERT INTO `tb_area` VALUES (603, '杜尔伯特蒙古族自治县', 269, 0);
INSERT INTO `tb_area` VALUES (604, '大庆高新技术产业开发区', 269, 0);
INSERT INTO `tb_area` VALUES (605, '天宁区', 268, 0);
INSERT INTO `tb_area` VALUES (606, '钟楼区', 268, 0);
INSERT INTO `tb_area` VALUES (607, '新北区', 268, 0);
INSERT INTO `tb_area` VALUES (608, '武进区', 268, 0);
INSERT INTO `tb_area` VALUES (609, '金坛区', 268, 0);
INSERT INTO `tb_area` VALUES (610, '溧阳市', 268, 0);
INSERT INTO `tb_area` VALUES (611, '东昌区', 267, 0);
INSERT INTO `tb_area` VALUES (612, '二道江区', 267, 0);
INSERT INTO `tb_area` VALUES (613, '通化县', 267, 0);
INSERT INTO `tb_area` VALUES (614, '辉南县', 267, 0);
INSERT INTO `tb_area` VALUES (615, '柳河县', 267, 0);
INSERT INTO `tb_area` VALUES (616, '梅河口市', 267, 0);
INSERT INTO `tb_area` VALUES (617, '集安市', 267, 0);
INSERT INTO `tb_area` VALUES (618, '郑州市', 182, 1);
INSERT INTO `tb_area` VALUES (619, '新余市', 58, 1);
INSERT INTO `tb_area` VALUES (620, '南平市', 23, 1);
INSERT INTO `tb_area` VALUES (621, '黄山市', 18, 1);
INSERT INTO `tb_area` VALUES (622, '舟山市', 13, 1);
INSERT INTO `tb_area` VALUES (623, '朝阳市', 6, 1);
INSERT INTO `tb_area` VALUES (624, '泰州市', 11, 1);
INSERT INTO `tb_area` VALUES (625, '西藏自治区', 0, 1);
INSERT INTO `tb_area` VALUES (626, '枣庄市', 127, 1);
INSERT INTO `tb_area` VALUES (627, '平山区', 266, 0);
INSERT INTO `tb_area` VALUES (628, '溪湖区', 266, 0);
INSERT INTO `tb_area` VALUES (629, '明山区', 266, 0);
INSERT INTO `tb_area` VALUES (630, '南芬区', 266, 0);
INSERT INTO `tb_area` VALUES (631, '本溪满族自治县', 266, 0);
INSERT INTO `tb_area` VALUES (632, '桓仁满族自治县', 266, 0);
INSERT INTO `tb_area` VALUES (633, '上城区', 265, 0);
INSERT INTO `tb_area` VALUES (634, '下城区', 265, 0);
INSERT INTO `tb_area` VALUES (635, '江干区', 265, 0);
INSERT INTO `tb_area` VALUES (636, '拱墅区', 265, 0);
INSERT INTO `tb_area` VALUES (637, '西湖区', 265, 0);
INSERT INTO `tb_area` VALUES (638, '滨江区', 265, 0);
INSERT INTO `tb_area` VALUES (639, '萧山区', 265, 0);
INSERT INTO `tb_area` VALUES (640, '余杭区', 265, 0);
INSERT INTO `tb_area` VALUES (641, '富阳区', 265, 0);
INSERT INTO `tb_area` VALUES (642, '临安区', 265, 0);
INSERT INTO `tb_area` VALUES (643, '桐庐县', 265, 0);
INSERT INTO `tb_area` VALUES (644, '淳安县', 265, 0);
INSERT INTO `tb_area` VALUES (645, '建德市', 265, 0);
INSERT INTO `tb_area` VALUES (646, '瑶海区', 221, 0);
INSERT INTO `tb_area` VALUES (647, '庐阳区', 221, 0);
INSERT INTO `tb_area` VALUES (648, '蜀山区', 221, 0);
INSERT INTO `tb_area` VALUES (649, '包河区', 221, 0);
INSERT INTO `tb_area` VALUES (650, '长丰县', 221, 0);
INSERT INTO `tb_area` VALUES (651, '肥东县', 221, 0);
INSERT INTO `tb_area` VALUES (652, '肥西县', 221, 0);
INSERT INTO `tb_area` VALUES (653, '庐江县', 221, 0);
INSERT INTO `tb_area` VALUES (654, '合肥高新技术产业开发区', 221, 0);
INSERT INTO `tb_area` VALUES (655, '合肥经济技术开发区', 221, 0);
INSERT INTO `tb_area` VALUES (656, '合肥新站高新技术产业开发区', 221, 0);
INSERT INTO `tb_area` VALUES (657, '巢湖市', 221, 0);
INSERT INTO `tb_area` VALUES (658, '尖山区', 216, 0);
INSERT INTO `tb_area` VALUES (659, '岭东区', 216, 0);
INSERT INTO `tb_area` VALUES (660, '四方台区', 216, 0);
INSERT INTO `tb_area` VALUES (661, '宝山区', 216, 0);
INSERT INTO `tb_area` VALUES (662, '集贤县', 216, 0);
INSERT INTO `tb_area` VALUES (663, '友谊县', 216, 0);
INSERT INTO `tb_area` VALUES (664, '宝清县', 216, 0);
INSERT INTO `tb_area` VALUES (665, '饶河县', 216, 0);
INSERT INTO `tb_area` VALUES (666, '开封市', 182, 1);
INSERT INTO `tb_area` VALUES (667, '鹰潭市', 58, 1);
INSERT INTO `tb_area` VALUES (668, '龙岩市', 23, 1);
INSERT INTO `tb_area` VALUES (669, '滁州市', 18, 1);
INSERT INTO `tb_area` VALUES (670, '台州市', 13, 1);
INSERT INTO `tb_area` VALUES (671, '葫芦岛市', 6, 1);
INSERT INTO `tb_area` VALUES (672, '宿迁市', 11, 1);
INSERT INTO `tb_area` VALUES (673, '陕西省', 0, 1);
INSERT INTO `tb_area` VALUES (674, '东营市', 127, 1);
INSERT INTO `tb_area` VALUES (675, '临河区', 219, 0);
INSERT INTO `tb_area` VALUES (676, '五原县', 219, 0);
INSERT INTO `tb_area` VALUES (677, '磴口县', 219, 0);
INSERT INTO `tb_area` VALUES (678, '乌拉特前旗', 219, 0);
INSERT INTO `tb_area` VALUES (679, '乌拉特中旗', 219, 0);
INSERT INTO `tb_area` VALUES (680, '乌拉特后旗', 219, 0);
INSERT INTO `tb_area` VALUES (681, '杭锦后旗', 219, 0);
INSERT INTO `tb_area` VALUES (682, '双桥区', 326, 0);
INSERT INTO `tb_area` VALUES (683, '双滦区', 326, 0);
INSERT INTO `tb_area` VALUES (684, '鹰手营子矿区', 326, 0);
INSERT INTO `tb_area` VALUES (685, '承德县', 326, 0);
INSERT INTO `tb_area` VALUES (686, '兴隆县', 326, 0);
INSERT INTO `tb_area` VALUES (687, '滦平县', 326, 0);
INSERT INTO `tb_area` VALUES (688, '隆化县', 326, 0);
INSERT INTO `tb_area` VALUES (689, '丰宁满族自治县', 326, 0);
INSERT INTO `tb_area` VALUES (690, '宽城满族自治县', 326, 0);
INSERT INTO `tb_area` VALUES (691, '围场满族蒙古族自治县', 326, 0);
INSERT INTO `tb_area` VALUES (692, '承德高新技术产业开发区', 326, 0);
INSERT INTO `tb_area` VALUES (693, '平泉市', 326, 0);
INSERT INTO `tb_area` VALUES (694, '洛阳市', 182, 1);
INSERT INTO `tb_area` VALUES (695, '赣州市', 58, 1);
INSERT INTO `tb_area` VALUES (696, '宁德市', 23, 1);
INSERT INTO `tb_area` VALUES (697, '阜阳市', 18, 1);
INSERT INTO `tb_area` VALUES (698, '丽水市', 13, 1);
INSERT INTO `tb_area` VALUES (699, '甘肃省', 0, 1);
INSERT INTO `tb_area` VALUES (700, '烟台市', 127, 1);
INSERT INTO `tb_area` VALUES (701, '武汉市', 218, 1);
INSERT INTO `tb_area` VALUES (702, '伊春区', 325, 0);
INSERT INTO `tb_area` VALUES (703, '南岔区', 325, 0);
INSERT INTO `tb_area` VALUES (704, '友好区', 325, 0);
INSERT INTO `tb_area` VALUES (705, '西林区', 325, 0);
INSERT INTO `tb_area` VALUES (706, '翠峦区', 325, 0);
INSERT INTO `tb_area` VALUES (707, '新青区', 325, 0);
INSERT INTO `tb_area` VALUES (708, '美溪区', 325, 0);
INSERT INTO `tb_area` VALUES (709, '金山屯区', 325, 0);
INSERT INTO `tb_area` VALUES (710, '五营区', 325, 0);
INSERT INTO `tb_area` VALUES (711, '乌马河区', 325, 0);
INSERT INTO `tb_area` VALUES (712, '汤旺河区', 325, 0);
INSERT INTO `tb_area` VALUES (713, '带岭区', 325, 0);
INSERT INTO `tb_area` VALUES (714, '乌伊岭区', 325, 0);
INSERT INTO `tb_area` VALUES (715, '红星区', 325, 0);
INSERT INTO `tb_area` VALUES (716, '上甘岭区', 325, 0);
INSERT INTO `tb_area` VALUES (717, '嘉荫县', 325, 0);
INSERT INTO `tb_area` VALUES (718, '铁力市', 325, 0);
INSERT INTO `tb_area` VALUES (719, '虎丘区', 324, 0);
INSERT INTO `tb_area` VALUES (720, '吴中区', 324, 0);
INSERT INTO `tb_area` VALUES (721, '相城区', 324, 0);
INSERT INTO `tb_area` VALUES (722, '姑苏区', 324, 0);
INSERT INTO `tb_area` VALUES (723, '吴江区', 324, 0);
INSERT INTO `tb_area` VALUES (724, '苏州工业园区', 324, 0);
INSERT INTO `tb_area` VALUES (725, '常熟市', 324, 0);
INSERT INTO `tb_area` VALUES (726, '张家港市', 324, 0);
INSERT INTO `tb_area` VALUES (727, '昆山市', 324, 0);
INSERT INTO `tb_area` VALUES (728, '太仓市', 324, 0);
INSERT INTO `tb_area` VALUES (729, '新华区', 370, 0);
INSERT INTO `tb_area` VALUES (730, '运河区', 370, 0);
INSERT INTO `tb_area` VALUES (731, '沧县', 370, 0);
INSERT INTO `tb_area` VALUES (732, '青县', 370, 0);
INSERT INTO `tb_area` VALUES (733, '东光县', 370, 0);
INSERT INTO `tb_area` VALUES (734, '海兴县', 370, 0);
INSERT INTO `tb_area` VALUES (735, '盐山县', 370, 0);
INSERT INTO `tb_area` VALUES (736, '肃宁县', 370, 0);
INSERT INTO `tb_area` VALUES (737, '南皮县', 370, 0);
INSERT INTO `tb_area` VALUES (738, '吴桥县', 370, 0);
INSERT INTO `tb_area` VALUES (739, '献县', 370, 0);
INSERT INTO `tb_area` VALUES (740, '孟村回族自治县', 370, 0);
INSERT INTO `tb_area` VALUES (741, '河北沧州经济开发区', 370, 0);
INSERT INTO `tb_area` VALUES (742, '沧州高新技术产业开发区', 370, 0);
INSERT INTO `tb_area` VALUES (743, '沧州渤海新区', 370, 0);
INSERT INTO `tb_area` VALUES (744, '泊头市', 370, 0);
INSERT INTO `tb_area` VALUES (745, '任丘市', 370, 0);
INSERT INTO `tb_area` VALUES (746, '黄骅市', 370, 0);
INSERT INTO `tb_area` VALUES (747, '河间市', 370, 0);
INSERT INTO `tb_area` VALUES (748, '向阳区', 369, 0);
INSERT INTO `tb_area` VALUES (749, '前进区', 369, 0);
INSERT INTO `tb_area` VALUES (750, '东风区', 369, 0);
INSERT INTO `tb_area` VALUES (751, '郊区', 369, 0);
INSERT INTO `tb_area` VALUES (752, '桦南县', 369, 0);
INSERT INTO `tb_area` VALUES (753, '桦川县', 369, 0);
INSERT INTO `tb_area` VALUES (754, '汤原县', 369, 0);
INSERT INTO `tb_area` VALUES (755, '同江市', 369, 0);
INSERT INTO `tb_area` VALUES (756, '富锦市', 369, 0);
INSERT INTO `tb_area` VALUES (757, '抚远市', 369, 0);
INSERT INTO `tb_area` VALUES (758, '平顶山市', 182, 1);
INSERT INTO `tb_area` VALUES (759, '吉安市', 58, 1);
INSERT INTO `tb_area` VALUES (760, '宿州市', 18, 1);
INSERT INTO `tb_area` VALUES (761, '青海省', 0, 1);
INSERT INTO `tb_area` VALUES (762, '潍坊市', 127, 1);
INSERT INTO `tb_area` VALUES (763, '黄石市', 218, 1);
INSERT INTO `tb_area` VALUES (764, '崇川区', 368, 0);
INSERT INTO `tb_area` VALUES (765, '港闸区', 368, 0);
INSERT INTO `tb_area` VALUES (766, '通州区', 368, 0);
INSERT INTO `tb_area` VALUES (767, '如东县', 368, 0);
INSERT INTO `tb_area` VALUES (768, '南通经济技术开发区', 368, 0);
INSERT INTO `tb_area` VALUES (769, '启东市', 368, 0);
INSERT INTO `tb_area` VALUES (770, '如皋市', 368, 0);
INSERT INTO `tb_area` VALUES (771, '海门市', 368, 0);
INSERT INTO `tb_area` VALUES (772, '海安市', 368, 0);
INSERT INTO `tb_area` VALUES (773, '宁江区', 367, 0);
INSERT INTO `tb_area` VALUES (774, '前郭尔罗斯蒙古族自治县', 367, 0);
INSERT INTO `tb_area` VALUES (775, '长岭县', 367, 0);
INSERT INTO `tb_area` VALUES (776, '乾安县', 367, 0);
INSERT INTO `tb_area` VALUES (777, '吉林松原经济开发区', 367, 0);
INSERT INTO `tb_area` VALUES (778, '扶余市', 367, 0);
INSERT INTO `tb_area` VALUES (779, '古塔区', 366, 0);
INSERT INTO `tb_area` VALUES (780, '凌河区', 366, 0);
INSERT INTO `tb_area` VALUES (781, '太和区', 366, 0);
INSERT INTO `tb_area` VALUES (782, '黑山县', 366, 0);
INSERT INTO `tb_area` VALUES (783, '义县', 366, 0);
INSERT INTO `tb_area` VALUES (784, '凌海市', 366, 0);
INSERT INTO `tb_area` VALUES (785, '北镇市', 366, 0);
INSERT INTO `tb_area` VALUES (786, '安阳市', 182, 1);
INSERT INTO `tb_area` VALUES (787, '宜春市', 58, 1);
INSERT INTO `tb_area` VALUES (788, '六安市', 18, 1);
INSERT INTO `tb_area` VALUES (789, '宁夏回族自治区', 0, 1);
INSERT INTO `tb_area` VALUES (790, '安次区', 431, 0);
INSERT INTO `tb_area` VALUES (791, '广阳区', 431, 0);
INSERT INTO `tb_area` VALUES (792, '固安县', 431, 0);
INSERT INTO `tb_area` VALUES (793, '永清县', 431, 0);
INSERT INTO `tb_area` VALUES (794, '香河县', 431, 0);
INSERT INTO `tb_area` VALUES (795, '大城县', 431, 0);
INSERT INTO `tb_area` VALUES (796, '文安县', 431, 0);
INSERT INTO `tb_area` VALUES (797, '大厂回族自治县', 431, 0);
INSERT INTO `tb_area` VALUES (798, '廊坊经济技术开发区', 431, 0);
INSERT INTO `tb_area` VALUES (799, '霸州市', 431, 0);
INSERT INTO `tb_area` VALUES (800, '三河市', 431, 0);
INSERT INTO `tb_area` VALUES (801, '新兴区', 430, 0);
INSERT INTO `tb_area` VALUES (802, '桃山区', 430, 0);
INSERT INTO `tb_area` VALUES (803, '茄子河区', 430, 0);
INSERT INTO `tb_area` VALUES (804, '勃利县', 430, 0);
INSERT INTO `tb_area` VALUES (805, '连云区', 429, 0);
INSERT INTO `tb_area` VALUES (806, '海州区', 429, 0);
INSERT INTO `tb_area` VALUES (807, '赣榆区', 429, 0);
INSERT INTO `tb_area` VALUES (808, '东海县', 429, 0);
INSERT INTO `tb_area` VALUES (809, '灌云县', 429, 0);
INSERT INTO `tb_area` VALUES (810, '灌南县', 429, 0);
INSERT INTO `tb_area` VALUES (811, '连云港经济技术开发区', 429, 0);
INSERT INTO `tb_area` VALUES (812, '连云港高新技术产业开发区', 429, 0);
INSERT INTO `tb_area` VALUES (813, '桃城区', 463, 0);
INSERT INTO `tb_area` VALUES (814, '冀州区', 463, 0);
INSERT INTO `tb_area` VALUES (815, '枣强县', 463, 0);
INSERT INTO `tb_area` VALUES (816, '武邑县', 463, 0);
INSERT INTO `tb_area` VALUES (817, '武强县', 463, 0);
INSERT INTO `tb_area` VALUES (818, '饶阳县', 463, 0);
INSERT INTO `tb_area` VALUES (819, '安平县', 463, 0);
INSERT INTO `tb_area` VALUES (820, '故城县', 463, 0);
INSERT INTO `tb_area` VALUES (821, '景县', 463, 0);
INSERT INTO `tb_area` VALUES (822, '阜城县', 463, 0);
INSERT INTO `tb_area` VALUES (823, '河北衡水高新技术产业开发区', 463, 0);
INSERT INTO `tb_area` VALUES (824, '衡水滨湖新区', 463, 0);
INSERT INTO `tb_area` VALUES (825, '深州市', 463, 0);
INSERT INTO `tb_area` VALUES (826, '济宁市', 127, 1);
INSERT INTO `tb_area` VALUES (827, '十堰市', 218, 1);
INSERT INTO `tb_area` VALUES (828, '鹤壁市', 182, 1);
INSERT INTO `tb_area` VALUES (829, '抚州市', 58, 1);
INSERT INTO `tb_area` VALUES (830, '亳州市', 18, 1);
INSERT INTO `tb_area` VALUES (831, '新疆维吾尔自治区', 0, 1);
INSERT INTO `tb_area` VALUES (832, '榆次区', 220, 0);
INSERT INTO `tb_area` VALUES (833, '榆社县', 220, 0);
INSERT INTO `tb_area` VALUES (834, '左权县', 220, 0);
INSERT INTO `tb_area` VALUES (835, '和顺县', 220, 0);
INSERT INTO `tb_area` VALUES (836, '昔阳县', 220, 0);
INSERT INTO `tb_area` VALUES (837, '寿阳县', 220, 0);
INSERT INTO `tb_area` VALUES (838, '太谷县', 220, 0);
INSERT INTO `tb_area` VALUES (839, '祁县', 220, 0);
INSERT INTO `tb_area` VALUES (840, '平遥县', 220, 0);
INSERT INTO `tb_area` VALUES (841, '灵石县', 220, 0);
INSERT INTO `tb_area` VALUES (842, '介休市', 220, 0);
INSERT INTO `tb_area` VALUES (843, '东安区', 462, 0);
INSERT INTO `tb_area` VALUES (844, '阳明区', 462, 0);
INSERT INTO `tb_area` VALUES (845, '爱民区', 462, 0);
INSERT INTO `tb_area` VALUES (846, '西安区', 462, 0);
INSERT INTO `tb_area` VALUES (847, '林口县', 462, 0);
INSERT INTO `tb_area` VALUES (848, '牡丹江经济技术开发区', 462, 0);
INSERT INTO `tb_area` VALUES (849, '绥芬河市', 462, 0);
INSERT INTO `tb_area` VALUES (850, '海林市', 462, 0);
INSERT INTO `tb_area` VALUES (851, '宁安市', 462, 0);
INSERT INTO `tb_area` VALUES (852, '穆棱市', 462, 0);
INSERT INTO `tb_area` VALUES (853, '东宁市', 462, 0);
INSERT INTO `tb_area` VALUES (854, '淮安区', 461, 0);
INSERT INTO `tb_area` VALUES (855, '淮阴区', 461, 0);
INSERT INTO `tb_area` VALUES (856, '清江浦区', 461, 0);
INSERT INTO `tb_area` VALUES (857, '洪泽区', 461, 0);
INSERT INTO `tb_area` VALUES (858, '涟水县', 461, 0);
INSERT INTO `tb_area` VALUES (859, '盱眙县', 461, 0);
INSERT INTO `tb_area` VALUES (860, '金湖县', 461, 0);
INSERT INTO `tb_area` VALUES (861, '淮安经济技术开发区', 461, 0);
INSERT INTO `tb_area` VALUES (862, '延吉市', 460, 0);
INSERT INTO `tb_area` VALUES (863, '图们市', 460, 0);
INSERT INTO `tb_area` VALUES (864, '敦化市', 460, 0);
INSERT INTO `tb_area` VALUES (865, '珲春市', 460, 0);
INSERT INTO `tb_area` VALUES (866, '龙井市', 460, 0);
INSERT INTO `tb_area` VALUES (867, '和龙市', 460, 0);
INSERT INTO `tb_area` VALUES (868, '汪清县', 460, 0);
INSERT INTO `tb_area` VALUES (869, '安图县', 460, 0);
INSERT INTO `tb_area` VALUES (870, '泰安市', 127, 1);
INSERT INTO `tb_area` VALUES (871, '宜昌市', 218, 1);
INSERT INTO `tb_area` VALUES (872, '新乡市', 182, 1);
INSERT INTO `tb_area` VALUES (873, '上饶市', 58, 1);
INSERT INTO `tb_area` VALUES (874, '池州市', 18, 1);
INSERT INTO `tb_area` VALUES (875, '爱辉区', 512, 0);
INSERT INTO `tb_area` VALUES (876, '嫩江县', 512, 0);
INSERT INTO `tb_area` VALUES (877, '逊克县', 512, 0);
INSERT INTO `tb_area` VALUES (878, '孙吴县', 512, 0);
INSERT INTO `tb_area` VALUES (879, '北安市', 512, 0);
INSERT INTO `tb_area` VALUES (880, '五大连池市', 512, 0);
INSERT INTO `tb_area` VALUES (881, '亭湖区', 511, 0);
INSERT INTO `tb_area` VALUES (882, '盐都区', 511, 0);
INSERT INTO `tb_area` VALUES (883, '大丰区', 511, 0);
INSERT INTO `tb_area` VALUES (884, '响水县', 511, 0);
INSERT INTO `tb_area` VALUES (885, '滨海县', 511, 0);
INSERT INTO `tb_area` VALUES (886, '阜宁县', 511, 0);
INSERT INTO `tb_area` VALUES (887, '射阳县', 511, 0);
INSERT INTO `tb_area` VALUES (888, '建湖县', 511, 0);
INSERT INTO `tb_area` VALUES (889, '盐城经济技术开发区', 511, 0);
INSERT INTO `tb_area` VALUES (890, '东台市', 511, 0);
INSERT INTO `tb_area` VALUES (891, '白塔区', 510, 0);
INSERT INTO `tb_area` VALUES (892, '文圣区', 510, 0);
INSERT INTO `tb_area` VALUES (893, '宏伟区', 510, 0);
INSERT INTO `tb_area` VALUES (894, '弓长岭区', 510, 0);
INSERT INTO `tb_area` VALUES (895, '太子河区', 510, 0);
INSERT INTO `tb_area` VALUES (896, '辽阳县', 510, 0);
INSERT INTO `tb_area` VALUES (897, '灯塔市', 510, 0);
INSERT INTO `tb_area` VALUES (898, '北林区', 543, 0);
INSERT INTO `tb_area` VALUES (899, '望奎县', 543, 0);
INSERT INTO `tb_area` VALUES (900, '兰西县', 543, 0);
INSERT INTO `tb_area` VALUES (901, '青冈县', 543, 0);
INSERT INTO `tb_area` VALUES (902, '庆安县', 543, 0);
INSERT INTO `tb_area` VALUES (903, '明水县', 543, 0);
INSERT INTO `tb_area` VALUES (904, '绥棱县', 543, 0);
INSERT INTO `tb_area` VALUES (905, '安达市', 543, 0);
INSERT INTO `tb_area` VALUES (906, '肇东市', 543, 0);
INSERT INTO `tb_area` VALUES (907, '海伦市', 543, 0);
INSERT INTO `tb_area` VALUES (908, '威海市', 127, 1);
INSERT INTO `tb_area` VALUES (909, '襄阳市', 218, 1);
INSERT INTO `tb_area` VALUES (910, '焦作市', 182, 1);
INSERT INTO `tb_area` VALUES (911, '宣城市', 18, 1);
INSERT INTO `tb_area` VALUES (912, '双台子区', 541, 0);
INSERT INTO `tb_area` VALUES (913, '兴隆台区', 541, 0);
INSERT INTO `tb_area` VALUES (914, '大洼区', 541, 0);
INSERT INTO `tb_area` VALUES (915, '盘山县', 541, 0);
INSERT INTO `tb_area` VALUES (916, '漠河市', 573, 0);
INSERT INTO `tb_area` VALUES (917, '呼玛县', 573, 0);
INSERT INTO `tb_area` VALUES (918, '塔河县', 573, 0);
INSERT INTO `tb_area` VALUES (919, '加格达奇区', 573, 0);
INSERT INTO `tb_area` VALUES (920, '松岭区', 573, 0);
INSERT INTO `tb_area` VALUES (921, '新林区', 573, 0);
INSERT INTO `tb_area` VALUES (922, '呼中区', 573, 0);
INSERT INTO `tb_area` VALUES (923, '京口区', 572, 0);
INSERT INTO `tb_area` VALUES (924, '润州区', 572, 0);
INSERT INTO `tb_area` VALUES (925, '丹徒区', 572, 0);
INSERT INTO `tb_area` VALUES (926, '镇江新区', 572, 0);
INSERT INTO `tb_area` VALUES (927, '丹阳市', 572, 0);
INSERT INTO `tb_area` VALUES (928, '扬中市', 572, 0);
INSERT INTO `tb_area` VALUES (929, '句容市', 572, 0);
INSERT INTO `tb_area` VALUES (930, '日照市', 127, 1);
INSERT INTO `tb_area` VALUES (931, '鄂州市', 218, 1);
INSERT INTO `tb_area` VALUES (932, '濮阳市', 182, 1);
INSERT INTO `tb_area` VALUES (933, '银州区', 571, 0);
INSERT INTO `tb_area` VALUES (934, '清河区', 571, 0);
INSERT INTO `tb_area` VALUES (935, '铁岭县', 571, 0);
INSERT INTO `tb_area` VALUES (936, '西丰县', 571, 0);
INSERT INTO `tb_area` VALUES (937, '昌图县', 571, 0);
INSERT INTO `tb_area` VALUES (938, '调兵山市', 571, 0);
INSERT INTO `tb_area` VALUES (939, '开原市', 571, 0);
INSERT INTO `tb_area` VALUES (940, '柯城区', 570, 0);
INSERT INTO `tb_area` VALUES (941, '衢江区', 570, 0);
INSERT INTO `tb_area` VALUES (942, '常山县', 570, 0);
INSERT INTO `tb_area` VALUES (943, '开化县', 570, 0);
INSERT INTO `tb_area` VALUES (944, '龙游县', 570, 0);
INSERT INTO `tb_area` VALUES (945, '江山市', 570, 0);
INSERT INTO `tb_area` VALUES (946, '海陵区', 624, 0);
INSERT INTO `tb_area` VALUES (947, '高港区', 624, 0);
INSERT INTO `tb_area` VALUES (948, '姜堰区', 624, 0);
INSERT INTO `tb_area` VALUES (949, '泰州医药高新技术产业开发区', 624, 0);
INSERT INTO `tb_area` VALUES (950, '兴化市', 624, 0);
INSERT INTO `tb_area` VALUES (951, '靖江市', 624, 0);
INSERT INTO `tb_area` VALUES (952, '泰兴市', 624, 0);
INSERT INTO `tb_area` VALUES (953, '双塔区', 623, 0);
INSERT INTO `tb_area` VALUES (954, '龙城区', 623, 0);
INSERT INTO `tb_area` VALUES (955, '朝阳县', 623, 0);
INSERT INTO `tb_area` VALUES (956, '建平县', 623, 0);
INSERT INTO `tb_area` VALUES (957, '喀喇沁左翼蒙古族自治县', 623, 0);
INSERT INTO `tb_area` VALUES (958, '北票市', 623, 0);
INSERT INTO `tb_area` VALUES (959, '凌源市', 623, 0);
INSERT INTO `tb_area` VALUES (960, '莱芜市', 127, 1);
INSERT INTO `tb_area` VALUES (961, '荆门市', 218, 1);
INSERT INTO `tb_area` VALUES (962, '许昌市', 182, 1);
INSERT INTO `tb_area` VALUES (963, '定海区', 622, 0);
INSERT INTO `tb_area` VALUES (964, '普陀区', 622, 0);
INSERT INTO `tb_area` VALUES (965, '岱山县', 622, 0);
INSERT INTO `tb_area` VALUES (966, '嵊泗县', 622, 0);
INSERT INTO `tb_area` VALUES (967, '屯溪区', 621, 0);
INSERT INTO `tb_area` VALUES (968, '黄山区', 621, 0);
INSERT INTO `tb_area` VALUES (969, '徽州区', 621, 0);
INSERT INTO `tb_area` VALUES (970, '歙县', 621, 0);
INSERT INTO `tb_area` VALUES (971, '休宁县', 621, 0);
INSERT INTO `tb_area` VALUES (972, '黟县', 621, 0);
INSERT INTO `tb_area` VALUES (973, '祁门县', 621, 0);
INSERT INTO `tb_area` VALUES (974, '宿城区', 672, 0);
INSERT INTO `tb_area` VALUES (975, '宿豫区', 672, 0);
INSERT INTO `tb_area` VALUES (976, '沭阳县', 672, 0);
INSERT INTO `tb_area` VALUES (977, '泗阳县', 672, 0);
INSERT INTO `tb_area` VALUES (978, '泗洪县', 672, 0);
INSERT INTO `tb_area` VALUES (979, '宿迁经济技术开发区', 672, 0);
INSERT INTO `tb_area` VALUES (980, '临沂市', 127, 1);
INSERT INTO `tb_area` VALUES (981, '孝感市', 218, 1);
INSERT INTO `tb_area` VALUES (982, '漯河市', 182, 1);
INSERT INTO `tb_area` VALUES (983, '连山区', 671, 0);
INSERT INTO `tb_area` VALUES (984, '龙港区', 671, 0);
INSERT INTO `tb_area` VALUES (985, '南票区', 671, 0);
INSERT INTO `tb_area` VALUES (986, '绥中县', 671, 0);
INSERT INTO `tb_area` VALUES (987, '建昌县', 671, 0);
INSERT INTO `tb_area` VALUES (988, '兴城市', 671, 0);
INSERT INTO `tb_area` VALUES (989, '椒江区', 670, 0);
INSERT INTO `tb_area` VALUES (990, '黄岩区', 670, 0);
INSERT INTO `tb_area` VALUES (991, '路桥区', 670, 0);
INSERT INTO `tb_area` VALUES (992, '三门县', 670, 0);
INSERT INTO `tb_area` VALUES (993, '天台县', 670, 0);
INSERT INTO `tb_area` VALUES (994, '仙居县', 670, 0);
INSERT INTO `tb_area` VALUES (995, '温岭市', 670, 0);
INSERT INTO `tb_area` VALUES (996, '临海市', 670, 0);
INSERT INTO `tb_area` VALUES (997, '玉环市', 670, 0);
INSERT INTO `tb_area` VALUES (998, '莲都区', 698, 0);
INSERT INTO `tb_area` VALUES (999, '青田县', 698, 0);
INSERT INTO `tb_area` VALUES (1000, '缙云县', 698, 0);
INSERT INTO `tb_area` VALUES (1001, '遂昌县', 698, 0);
INSERT INTO `tb_area` VALUES (1002, '松阳县', 698, 0);
INSERT INTO `tb_area` VALUES (1003, '云和县', 698, 0);
INSERT INTO `tb_area` VALUES (1004, '庆元县', 698, 0);
INSERT INTO `tb_area` VALUES (1005, '景宁畲族自治县', 698, 0);
INSERT INTO `tb_area` VALUES (1006, '龙泉市', 698, 0);
INSERT INTO `tb_area` VALUES (1007, '颍州区', 697, 0);
INSERT INTO `tb_area` VALUES (1008, '颍东区', 697, 0);
INSERT INTO `tb_area` VALUES (1009, '颍泉区', 697, 0);
INSERT INTO `tb_area` VALUES (1010, '临泉县', 697, 0);
INSERT INTO `tb_area` VALUES (1011, '太和县', 697, 0);
INSERT INTO `tb_area` VALUES (1012, '阜南县', 697, 0);
INSERT INTO `tb_area` VALUES (1013, '颍上县', 697, 0);
INSERT INTO `tb_area` VALUES (1014, '阜阳合肥现代产业园区', 697, 0);
INSERT INTO `tb_area` VALUES (1015, '阜阳经济技术开发区', 697, 0);
INSERT INTO `tb_area` VALUES (1016, '界首市', 697, 0);
INSERT INTO `tb_area` VALUES (1017, '德州市', 127, 1);
INSERT INTO `tb_area` VALUES (1018, '荆州市', 218, 1);
INSERT INTO `tb_area` VALUES (1019, '三门峡市', 182, 1);
INSERT INTO `tb_area` VALUES (1020, '蕉城区', 696, 0);
INSERT INTO `tb_area` VALUES (1021, '霞浦县', 696, 0);
INSERT INTO `tb_area` VALUES (1022, '古田县', 696, 0);
INSERT INTO `tb_area` VALUES (1023, '屏南县', 696, 0);
INSERT INTO `tb_area` VALUES (1024, '寿宁县', 696, 0);
INSERT INTO `tb_area` VALUES (1025, '周宁县', 696, 0);
INSERT INTO `tb_area` VALUES (1026, '柘荣县', 696, 0);
INSERT INTO `tb_area` VALUES (1027, '福安市', 696, 0);
INSERT INTO `tb_area` VALUES (1028, '福鼎市', 696, 0);
INSERT INTO `tb_area` VALUES (1029, '章贡区', 695, 0);
INSERT INTO `tb_area` VALUES (1030, '南康区', 695, 0);
INSERT INTO `tb_area` VALUES (1031, '赣县区', 695, 0);
INSERT INTO `tb_area` VALUES (1032, '信丰县', 695, 0);
INSERT INTO `tb_area` VALUES (1033, '大余县', 695, 0);
INSERT INTO `tb_area` VALUES (1034, '上犹县', 695, 0);
INSERT INTO `tb_area` VALUES (1035, '崇义县', 695, 0);
INSERT INTO `tb_area` VALUES (1036, '安远县', 695, 0);
INSERT INTO `tb_area` VALUES (1037, '龙南县', 695, 0);
INSERT INTO `tb_area` VALUES (1038, '定南县', 695, 0);
INSERT INTO `tb_area` VALUES (1039, '全南县', 695, 0);
INSERT INTO `tb_area` VALUES (1040, '宁都县', 695, 0);
INSERT INTO `tb_area` VALUES (1041, '于都县', 695, 0);
INSERT INTO `tb_area` VALUES (1042, '兴国县', 695, 0);
INSERT INTO `tb_area` VALUES (1043, '会昌县', 695, 0);
INSERT INTO `tb_area` VALUES (1044, '寻乌县', 695, 0);
INSERT INTO `tb_area` VALUES (1045, '石城县', 695, 0);
INSERT INTO `tb_area` VALUES (1046, '瑞金市', 695, 0);
INSERT INTO `tb_area` VALUES (1047, '埇桥区', 760, 0);
INSERT INTO `tb_area` VALUES (1048, '砀山县', 760, 0);
INSERT INTO `tb_area` VALUES (1049, '萧县', 760, 0);
INSERT INTO `tb_area` VALUES (1050, '灵璧县', 760, 0);
INSERT INTO `tb_area` VALUES (1051, '泗县', 760, 0);
INSERT INTO `tb_area` VALUES (1052, '宿州马鞍山现代产业园区', 760, 0);
INSERT INTO `tb_area` VALUES (1053, '宿州经济技术开发区', 760, 0);
INSERT INTO `tb_area` VALUES (1054, '聊城市', 127, 1);
INSERT INTO `tb_area` VALUES (1055, '黄冈市', 218, 1);
INSERT INTO `tb_area` VALUES (1056, '南阳市', 182, 1);
INSERT INTO `tb_area` VALUES (1057, '新华区', 758, 0);
INSERT INTO `tb_area` VALUES (1058, '卫东区', 758, 0);
INSERT INTO `tb_area` VALUES (1059, '石龙区', 758, 0);
INSERT INTO `tb_area` VALUES (1060, '湛河区', 758, 0);
INSERT INTO `tb_area` VALUES (1061, '宝丰县', 758, 0);
INSERT INTO `tb_area` VALUES (1062, '叶县', 758, 0);
INSERT INTO `tb_area` VALUES (1063, '鲁山县', 758, 0);
INSERT INTO `tb_area` VALUES (1064, '郏县', 758, 0);
INSERT INTO `tb_area` VALUES (1065, '平顶山高新技术产业开发区', 758, 0);
INSERT INTO `tb_area` VALUES (1066, '平顶山市新城区', 758, 0);
INSERT INTO `tb_area` VALUES (1067, '舞钢市', 758, 0);
INSERT INTO `tb_area` VALUES (1068, '汝州市', 758, 0);
INSERT INTO `tb_area` VALUES (1069, '金安区', 788, 0);
INSERT INTO `tb_area` VALUES (1070, '裕安区', 788, 0);
INSERT INTO `tb_area` VALUES (1071, '叶集区', 788, 0);
INSERT INTO `tb_area` VALUES (1072, '霍邱县', 788, 0);
INSERT INTO `tb_area` VALUES (1073, '舒城县', 788, 0);
INSERT INTO `tb_area` VALUES (1074, '金寨县', 788, 0);
INSERT INTO `tb_area` VALUES (1075, '霍山县', 788, 0);
INSERT INTO `tb_area` VALUES (1076, '袁州区', 787, 0);
INSERT INTO `tb_area` VALUES (1077, '奉新县', 787, 0);
INSERT INTO `tb_area` VALUES (1078, '万载县', 787, 0);
INSERT INTO `tb_area` VALUES (1079, '上高县', 787, 0);
INSERT INTO `tb_area` VALUES (1080, '宜丰县', 787, 0);
INSERT INTO `tb_area` VALUES (1081, '靖安县', 787, 0);
INSERT INTO `tb_area` VALUES (1082, '铜鼓县', 787, 0);
INSERT INTO `tb_area` VALUES (1083, '丰城市', 787, 0);
INSERT INTO `tb_area` VALUES (1084, '樟树市', 787, 0);
INSERT INTO `tb_area` VALUES (1085, '高安市', 787, 0);
INSERT INTO `tb_area` VALUES (1086, '滨州市', 127, 1);
INSERT INTO `tb_area` VALUES (1087, '咸宁市', 218, 1);
INSERT INTO `tb_area` VALUES (1088, '商丘市', 182, 1);
INSERT INTO `tb_area` VALUES (1089, '吉州区', 759, 0);
INSERT INTO `tb_area` VALUES (1090, '青原区', 759, 0);
INSERT INTO `tb_area` VALUES (1091, '吉安县', 759, 0);
INSERT INTO `tb_area` VALUES (1092, '吉水县', 759, 0);
INSERT INTO `tb_area` VALUES (1093, '峡江县', 759, 0);
INSERT INTO `tb_area` VALUES (1094, '新干县', 759, 0);
INSERT INTO `tb_area` VALUES (1095, '永丰县', 759, 0);
INSERT INTO `tb_area` VALUES (1096, '泰和县', 759, 0);
INSERT INTO `tb_area` VALUES (1097, '遂川县', 759, 0);
INSERT INTO `tb_area` VALUES (1098, '万安县', 759, 0);
INSERT INTO `tb_area` VALUES (1099, '安福县', 759, 0);
INSERT INTO `tb_area` VALUES (1100, '永新县', 759, 0);
INSERT INTO `tb_area` VALUES (1101, '井冈山市', 759, 0);
INSERT INTO `tb_area` VALUES (1102, '文峰区', 786, 0);
INSERT INTO `tb_area` VALUES (1103, '北关区', 786, 0);
INSERT INTO `tb_area` VALUES (1104, '殷都区', 786, 0);
INSERT INTO `tb_area` VALUES (1105, '龙安区', 786, 0);
INSERT INTO `tb_area` VALUES (1106, '安阳县', 786, 0);
INSERT INTO `tb_area` VALUES (1107, '汤阴县', 786, 0);
INSERT INTO `tb_area` VALUES (1108, '滑县', 786, 0);
INSERT INTO `tb_area` VALUES (1109, '内黄县', 786, 0);
INSERT INTO `tb_area` VALUES (1110, '安阳高新技术产业开发区', 786, 0);
INSERT INTO `tb_area` VALUES (1111, '林州市', 786, 0);
INSERT INTO `tb_area` VALUES (1112, '黄石港区', 763, 0);
INSERT INTO `tb_area` VALUES (1113, '西塞山区', 763, 0);
INSERT INTO `tb_area` VALUES (1114, '下陆区', 763, 0);
INSERT INTO `tb_area` VALUES (1115, '铁山区', 763, 0);
INSERT INTO `tb_area` VALUES (1116, '阳新县', 763, 0);
INSERT INTO `tb_area` VALUES (1117, '大冶市', 763, 0);
INSERT INTO `tb_area` VALUES (1118, '谯城区', 830, 0);
INSERT INTO `tb_area` VALUES (1119, '涡阳县', 830, 0);
INSERT INTO `tb_area` VALUES (1120, '蒙城县', 830, 0);
INSERT INTO `tb_area` VALUES (1121, '利辛县', 830, 0);
INSERT INTO `tb_area` VALUES (1122, '菏泽市', 127, 1);
INSERT INTO `tb_area` VALUES (1123, '随州市', 218, 1);
INSERT INTO `tb_area` VALUES (1124, '信阳市', 182, 1);
INSERT INTO `tb_area` VALUES (1125, '临川区', 829, 0);
INSERT INTO `tb_area` VALUES (1126, '东乡区', 829, 0);
INSERT INTO `tb_area` VALUES (1127, '南城县', 829, 0);
INSERT INTO `tb_area` VALUES (1128, '黎川县', 829, 0);
INSERT INTO `tb_area` VALUES (1129, '南丰县', 829, 0);
INSERT INTO `tb_area` VALUES (1130, '崇仁县', 829, 0);
INSERT INTO `tb_area` VALUES (1131, '乐安县', 829, 0);
INSERT INTO `tb_area` VALUES (1132, '宜黄县', 829, 0);
INSERT INTO `tb_area` VALUES (1133, '金溪县', 829, 0);
INSERT INTO `tb_area` VALUES (1134, '资溪县', 829, 0);
INSERT INTO `tb_area` VALUES (1135, '广昌县', 829, 0);
INSERT INTO `tb_area` VALUES (1136, '鹤山区', 828, 0);
INSERT INTO `tb_area` VALUES (1137, '山城区', 828, 0);
INSERT INTO `tb_area` VALUES (1138, '淇滨区', 828, 0);
INSERT INTO `tb_area` VALUES (1139, '浚县', 828, 0);
INSERT INTO `tb_area` VALUES (1140, '淇县', 828, 0);
INSERT INTO `tb_area` VALUES (1141, '鹤壁经济技术开发区', 828, 0);
INSERT INTO `tb_area` VALUES (1142, '恩施土家族苗族自治州', 218, 1);
INSERT INTO `tb_area` VALUES (1143, '周口市', 182, 1);
INSERT INTO `tb_area` VALUES (1144, '省直辖县级行政区划', 218, 1);
INSERT INTO `tb_area` VALUES (1145, '贵池区', 874, 0);
INSERT INTO `tb_area` VALUES (1146, '东至县', 874, 0);
INSERT INTO `tb_area` VALUES (1147, '石台县', 874, 0);
INSERT INTO `tb_area` VALUES (1148, '青阳县', 874, 0);
INSERT INTO `tb_area` VALUES (1149, '茅箭区', 827, 0);
INSERT INTO `tb_area` VALUES (1150, '张湾区', 827, 0);
INSERT INTO `tb_area` VALUES (1151, '郧阳区', 827, 0);
INSERT INTO `tb_area` VALUES (1152, '郧西县', 827, 0);
INSERT INTO `tb_area` VALUES (1153, '竹山县', 827, 0);
INSERT INTO `tb_area` VALUES (1154, '竹溪县', 827, 0);
INSERT INTO `tb_area` VALUES (1155, '房县', 827, 0);
INSERT INTO `tb_area` VALUES (1156, '丹江口市', 827, 0);
INSERT INTO `tb_area` VALUES (1157, '信州区', 873, 0);
INSERT INTO `tb_area` VALUES (1158, '广丰区', 873, 0);
INSERT INTO `tb_area` VALUES (1159, '上饶县', 873, 0);
INSERT INTO `tb_area` VALUES (1160, '玉山县', 873, 0);
INSERT INTO `tb_area` VALUES (1161, '铅山县', 873, 0);
INSERT INTO `tb_area` VALUES (1162, '横峰县', 873, 0);
INSERT INTO `tb_area` VALUES (1163, '弋阳县', 873, 0);
INSERT INTO `tb_area` VALUES (1164, '余干县', 873, 0);
INSERT INTO `tb_area` VALUES (1165, '鄱阳县', 873, 0);
INSERT INTO `tb_area` VALUES (1166, '万年县', 873, 0);
INSERT INTO `tb_area` VALUES (1167, '婺源县', 873, 0);
INSERT INTO `tb_area` VALUES (1168, '德兴市', 873, 0);
INSERT INTO `tb_area` VALUES (1169, '红旗区', 872, 0);
INSERT INTO `tb_area` VALUES (1170, '卫滨区', 872, 0);
INSERT INTO `tb_area` VALUES (1171, '凤泉区', 872, 0);
INSERT INTO `tb_area` VALUES (1172, '牧野区', 872, 0);
INSERT INTO `tb_area` VALUES (1173, '新乡县', 872, 0);
INSERT INTO `tb_area` VALUES (1174, '获嘉县', 872, 0);
INSERT INTO `tb_area` VALUES (1175, '原阳县', 872, 0);
INSERT INTO `tb_area` VALUES (1176, '延津县', 872, 0);
INSERT INTO `tb_area` VALUES (1177, '封丘县', 872, 0);
INSERT INTO `tb_area` VALUES (1178, '长垣县', 872, 0);
INSERT INTO `tb_area` VALUES (1179, '新乡高新技术产业开发区', 872, 0);
INSERT INTO `tb_area` VALUES (1180, '新乡经济技术开发区', 872, 0);
INSERT INTO `tb_area` VALUES (1181, '新乡市平原城乡一体化示范区', 872, 0);
INSERT INTO `tb_area` VALUES (1182, '卫辉市', 872, 0);
INSERT INTO `tb_area` VALUES (1183, '辉县市', 872, 0);
INSERT INTO `tb_area` VALUES (1184, '西陵区', 871, 0);
INSERT INTO `tb_area` VALUES (1185, '伍家岗区', 871, 0);
INSERT INTO `tb_area` VALUES (1186, '点军区', 871, 0);
INSERT INTO `tb_area` VALUES (1187, '猇亭区', 871, 0);
INSERT INTO `tb_area` VALUES (1188, '夷陵区', 871, 0);
INSERT INTO `tb_area` VALUES (1189, '远安县', 871, 0);
INSERT INTO `tb_area` VALUES (1190, '兴山县', 871, 0);
INSERT INTO `tb_area` VALUES (1191, '秭归县', 871, 0);
INSERT INTO `tb_area` VALUES (1192, '长阳土家族自治县', 871, 0);
INSERT INTO `tb_area` VALUES (1193, '五峰土家族自治县', 871, 0);
INSERT INTO `tb_area` VALUES (1194, '宜都市', 871, 0);
INSERT INTO `tb_area` VALUES (1195, '当阳市', 871, 0);
INSERT INTO `tb_area` VALUES (1196, '枝江市', 871, 0);
INSERT INTO `tb_area` VALUES (1197, '驻马店市', 182, 1);
INSERT INTO `tb_area` VALUES (1198, '宣州区', 911, 0);
INSERT INTO `tb_area` VALUES (1199, '郎溪县', 911, 0);
INSERT INTO `tb_area` VALUES (1200, '广德县', 911, 0);
INSERT INTO `tb_area` VALUES (1201, '泾县', 911, 0);
INSERT INTO `tb_area` VALUES (1202, '绩溪县', 911, 0);
INSERT INTO `tb_area` VALUES (1203, '旌德县', 911, 0);
INSERT INTO `tb_area` VALUES (1204, '宣城市经济开发区', 911, 0);
INSERT INTO `tb_area` VALUES (1205, '宁国市', 911, 0);
INSERT INTO `tb_area` VALUES (1206, '解放区', 910, 0);
INSERT INTO `tb_area` VALUES (1207, '中站区', 910, 0);
INSERT INTO `tb_area` VALUES (1208, '马村区', 910, 0);
INSERT INTO `tb_area` VALUES (1209, '山阳区', 910, 0);
INSERT INTO `tb_area` VALUES (1210, '修武县', 910, 0);
INSERT INTO `tb_area` VALUES (1211, '博爱县', 910, 0);
INSERT INTO `tb_area` VALUES (1212, '武陟县', 910, 0);
INSERT INTO `tb_area` VALUES (1213, '温县', 910, 0);
INSERT INTO `tb_area` VALUES (1214, '焦作城乡一体化示范区', 910, 0);
INSERT INTO `tb_area` VALUES (1215, '沁阳市', 910, 0);
INSERT INTO `tb_area` VALUES (1216, '孟州市', 910, 0);
INSERT INTO `tb_area` VALUES (1217, '省直辖县级行政区划', 182, 1);
INSERT INTO `tb_area` VALUES (1218, '襄城区', 909, 0);
INSERT INTO `tb_area` VALUES (1219, '樊城区', 909, 0);
INSERT INTO `tb_area` VALUES (1220, '襄州区', 909, 0);
INSERT INTO `tb_area` VALUES (1221, '南漳县', 909, 0);
INSERT INTO `tb_area` VALUES (1222, '谷城县', 909, 0);
INSERT INTO `tb_area` VALUES (1223, '保康县', 909, 0);
INSERT INTO `tb_area` VALUES (1224, '老河口市', 909, 0);
INSERT INTO `tb_area` VALUES (1225, '枣阳市', 909, 0);
INSERT INTO `tb_area` VALUES (1226, '宜城市', 909, 0);
INSERT INTO `tb_area` VALUES (1227, '梁子湖区', 931, 0);
INSERT INTO `tb_area` VALUES (1228, '华容区', 931, 0);
INSERT INTO `tb_area` VALUES (1229, '鄂城区', 931, 0);
INSERT INTO `tb_area` VALUES (1230, '东港区', 930, 0);
INSERT INTO `tb_area` VALUES (1231, '岚山区', 930, 0);
INSERT INTO `tb_area` VALUES (1232, '五莲县', 930, 0);
INSERT INTO `tb_area` VALUES (1233, '莒县', 930, 0);
INSERT INTO `tb_area` VALUES (1234, '日照经济技术开发区', 930, 0);
INSERT INTO `tb_area` VALUES (1235, '环翠区', 908, 0);
INSERT INTO `tb_area` VALUES (1236, '文登区', 908, 0);
INSERT INTO `tb_area` VALUES (1237, '威海火炬高技术产业开发区', 908, 0);
INSERT INTO `tb_area` VALUES (1238, '威海经济技术开发区', 908, 0);
INSERT INTO `tb_area` VALUES (1239, '威海临港经济技术开发区', 908, 0);
INSERT INTO `tb_area` VALUES (1240, '荣成市', 908, 0);
INSERT INTO `tb_area` VALUES (1241, '乳山市', 908, 0);
INSERT INTO `tb_area` VALUES (1242, '魏都区', 962, 0);
INSERT INTO `tb_area` VALUES (1243, '建安区', 962, 0);
INSERT INTO `tb_area` VALUES (1244, '鄢陵县', 962, 0);
INSERT INTO `tb_area` VALUES (1245, '襄城县', 962, 0);
INSERT INTO `tb_area` VALUES (1246, '许昌经济技术开发区', 962, 0);
INSERT INTO `tb_area` VALUES (1247, '禹州市', 962, 0);
INSERT INTO `tb_area` VALUES (1248, '长葛市', 962, 0);
INSERT INTO `tb_area` VALUES (1249, '东宝区', 961, 0);
INSERT INTO `tb_area` VALUES (1250, '掇刀区', 961, 0);
INSERT INTO `tb_area` VALUES (1251, '沙洋县', 961, 0);
INSERT INTO `tb_area` VALUES (1252, '钟祥市', 961, 0);
INSERT INTO `tb_area` VALUES (1253, '京山市', 961, 0);
INSERT INTO `tb_area` VALUES (1254, '华龙区', 932, 0);
INSERT INTO `tb_area` VALUES (1255, '清丰县', 932, 0);
INSERT INTO `tb_area` VALUES (1256, '南乐县', 932, 0);
INSERT INTO `tb_area` VALUES (1257, '范县', 932, 0);
INSERT INTO `tb_area` VALUES (1258, '台前县', 932, 0);
INSERT INTO `tb_area` VALUES (1259, '濮阳县', 932, 0);
INSERT INTO `tb_area` VALUES (1260, '河南濮阳工业园区', 932, 0);
INSERT INTO `tb_area` VALUES (1261, '濮阳经济技术开发区', 932, 0);
INSERT INTO `tb_area` VALUES (1262, '莱城区', 960, 0);
INSERT INTO `tb_area` VALUES (1263, '钢城区', 960, 0);
INSERT INTO `tb_area` VALUES (1264, '源汇区', 982, 0);
INSERT INTO `tb_area` VALUES (1265, '郾城区', 982, 0);
INSERT INTO `tb_area` VALUES (1266, '召陵区', 982, 0);
INSERT INTO `tb_area` VALUES (1267, '舞阳县', 982, 0);
INSERT INTO `tb_area` VALUES (1268, '临颍县', 982, 0);
INSERT INTO `tb_area` VALUES (1269, '漯河经济技术开发区', 982, 0);
INSERT INTO `tb_area` VALUES (1270, '孝南区', 981, 0);
INSERT INTO `tb_area` VALUES (1271, '孝昌县', 981, 0);
INSERT INTO `tb_area` VALUES (1272, '大悟县', 981, 0);
INSERT INTO `tb_area` VALUES (1273, '云梦县', 981, 0);
INSERT INTO `tb_area` VALUES (1274, '应城市', 981, 0);
INSERT INTO `tb_area` VALUES (1275, '安陆市', 981, 0);
INSERT INTO `tb_area` VALUES (1276, '汉川市', 981, 0);
INSERT INTO `tb_area` VALUES (1277, '兰山区', 980, 0);
INSERT INTO `tb_area` VALUES (1278, '罗庄区', 980, 0);
INSERT INTO `tb_area` VALUES (1279, '河东区', 980, 0);
INSERT INTO `tb_area` VALUES (1280, '沂南县', 980, 0);
INSERT INTO `tb_area` VALUES (1281, '郯城县', 980, 0);
INSERT INTO `tb_area` VALUES (1282, '沂水县', 980, 0);
INSERT INTO `tb_area` VALUES (1283, '兰陵县', 980, 0);
INSERT INTO `tb_area` VALUES (1284, '费县', 980, 0);
INSERT INTO `tb_area` VALUES (1285, '平邑县', 980, 0);
INSERT INTO `tb_area` VALUES (1286, '莒南县', 980, 0);
INSERT INTO `tb_area` VALUES (1287, '蒙阴县', 980, 0);
INSERT INTO `tb_area` VALUES (1288, '临沭县', 980, 0);
INSERT INTO `tb_area` VALUES (1289, '临沂高新技术产业开发区', 980, 0);
INSERT INTO `tb_area` VALUES (1290, '临沂经济技术开发区', 980, 0);
INSERT INTO `tb_area` VALUES (1291, '临沂临港经济开发区', 980, 0);
INSERT INTO `tb_area` VALUES (1292, '泰山区', 870, 0);
INSERT INTO `tb_area` VALUES (1293, '岱岳区', 870, 0);
INSERT INTO `tb_area` VALUES (1294, '宁阳县', 870, 0);
INSERT INTO `tb_area` VALUES (1295, '东平县', 870, 0);
INSERT INTO `tb_area` VALUES (1296, '新泰市', 870, 0);
INSERT INTO `tb_area` VALUES (1297, '肥城市', 870, 0);
INSERT INTO `tb_area` VALUES (1298, '湖滨区', 1019, 0);
INSERT INTO `tb_area` VALUES (1299, '陕州区', 1019, 0);
INSERT INTO `tb_area` VALUES (1300, '渑池县', 1019, 0);
INSERT INTO `tb_area` VALUES (1301, '卢氏县', 1019, 0);
INSERT INTO `tb_area` VALUES (1302, '河南三门峡经济开发区', 1019, 0);
INSERT INTO `tb_area` VALUES (1303, '义马市', 1019, 0);
INSERT INTO `tb_area` VALUES (1304, '灵宝市', 1019, 0);
INSERT INTO `tb_area` VALUES (1305, '沙市区', 1018, 0);
INSERT INTO `tb_area` VALUES (1306, '荆州区', 1018, 0);
INSERT INTO `tb_area` VALUES (1307, '公安县', 1018, 0);
INSERT INTO `tb_area` VALUES (1308, '监利县', 1018, 0);
INSERT INTO `tb_area` VALUES (1309, '江陵县', 1018, 0);
INSERT INTO `tb_area` VALUES (1310, '荆州经济技术开发区', 1018, 0);
INSERT INTO `tb_area` VALUES (1311, '石首市', 1018, 0);
INSERT INTO `tb_area` VALUES (1312, '洪湖市', 1018, 0);
INSERT INTO `tb_area` VALUES (1313, '松滋市', 1018, 0);
INSERT INTO `tb_area` VALUES (1314, '德城区', 1017, 0);
INSERT INTO `tb_area` VALUES (1315, '陵城区', 1017, 0);
INSERT INTO `tb_area` VALUES (1316, '宁津县', 1017, 0);
INSERT INTO `tb_area` VALUES (1317, '庆云县', 1017, 0);
INSERT INTO `tb_area` VALUES (1318, '临邑县', 1017, 0);
INSERT INTO `tb_area` VALUES (1319, '齐河县', 1017, 0);
INSERT INTO `tb_area` VALUES (1320, '平原县', 1017, 0);
INSERT INTO `tb_area` VALUES (1321, '夏津县', 1017, 0);
INSERT INTO `tb_area` VALUES (1322, '武城县', 1017, 0);
INSERT INTO `tb_area` VALUES (1323, '德州经济技术开发区', 1017, 0);
INSERT INTO `tb_area` VALUES (1324, '德州运河经济开发区', 1017, 0);
INSERT INTO `tb_area` VALUES (1325, '乐陵市', 1017, 0);
INSERT INTO `tb_area` VALUES (1326, '禹城市', 1017, 0);
INSERT INTO `tb_area` VALUES (1327, '宛城区', 1056, 0);
INSERT INTO `tb_area` VALUES (1328, '卧龙区', 1056, 0);
INSERT INTO `tb_area` VALUES (1329, '南召县', 1056, 0);
INSERT INTO `tb_area` VALUES (1330, '方城县', 1056, 0);
INSERT INTO `tb_area` VALUES (1331, '西峡县', 1056, 0);
INSERT INTO `tb_area` VALUES (1332, '镇平县', 1056, 0);
INSERT INTO `tb_area` VALUES (1333, '内乡县', 1056, 0);
INSERT INTO `tb_area` VALUES (1334, '淅川县', 1056, 0);
INSERT INTO `tb_area` VALUES (1335, '社旗县', 1056, 0);
INSERT INTO `tb_area` VALUES (1336, '唐河县', 1056, 0);
INSERT INTO `tb_area` VALUES (1337, '新野县', 1056, 0);
INSERT INTO `tb_area` VALUES (1338, '桐柏县', 1056, 0);
INSERT INTO `tb_area` VALUES (1339, '南阳高新技术产业开发区', 1056, 0);
INSERT INTO `tb_area` VALUES (1340, '南阳市城乡一体化示范区', 1056, 0);
INSERT INTO `tb_area` VALUES (1341, '邓州市', 1056, 0);
INSERT INTO `tb_area` VALUES (1342, '黄州区', 1055, 0);
INSERT INTO `tb_area` VALUES (1343, '团风县', 1055, 0);
INSERT INTO `tb_area` VALUES (1344, '红安县', 1055, 0);
INSERT INTO `tb_area` VALUES (1345, '罗田县', 1055, 0);
INSERT INTO `tb_area` VALUES (1346, '英山县', 1055, 0);
INSERT INTO `tb_area` VALUES (1347, '浠水县', 1055, 0);
INSERT INTO `tb_area` VALUES (1348, '蕲春县', 1055, 0);
INSERT INTO `tb_area` VALUES (1349, '黄梅县', 1055, 0);
INSERT INTO `tb_area` VALUES (1350, '龙感湖管理区', 1055, 0);
INSERT INTO `tb_area` VALUES (1351, '麻城市', 1055, 0);
INSERT INTO `tb_area` VALUES (1352, '武穴市', 1055, 0);
INSERT INTO `tb_area` VALUES (1353, '东昌府区', 1054, 0);
INSERT INTO `tb_area` VALUES (1354, '阳谷县', 1054, 0);
INSERT INTO `tb_area` VALUES (1355, '莘县', 1054, 0);
INSERT INTO `tb_area` VALUES (1356, '茌平县', 1054, 0);
INSERT INTO `tb_area` VALUES (1357, '东阿县', 1054, 0);
INSERT INTO `tb_area` VALUES (1358, '冠县', 1054, 0);
INSERT INTO `tb_area` VALUES (1359, '高唐县', 1054, 0);
INSERT INTO `tb_area` VALUES (1360, '临清市', 1054, 0);
INSERT INTO `tb_area` VALUES (1361, '梁园区', 1088, 0);
INSERT INTO `tb_area` VALUES (1362, '睢阳区', 1088, 0);
INSERT INTO `tb_area` VALUES (1363, '民权县', 1088, 0);
INSERT INTO `tb_area` VALUES (1364, '睢县', 1088, 0);
INSERT INTO `tb_area` VALUES (1365, '宁陵县', 1088, 0);
INSERT INTO `tb_area` VALUES (1366, '柘城县', 1088, 0);
INSERT INTO `tb_area` VALUES (1367, '虞城县', 1088, 0);
INSERT INTO `tb_area` VALUES (1368, '夏邑县', 1088, 0);
INSERT INTO `tb_area` VALUES (1369, '豫东综合物流产业聚集区', 1088, 0);
INSERT INTO `tb_area` VALUES (1370, '河南商丘经济开发区', 1088, 0);
INSERT INTO `tb_area` VALUES (1371, '永城市', 1088, 0);
INSERT INTO `tb_area` VALUES (1372, '咸安区', 1087, 0);
INSERT INTO `tb_area` VALUES (1373, '嘉鱼县', 1087, 0);
INSERT INTO `tb_area` VALUES (1374, '通城县', 1087, 0);
INSERT INTO `tb_area` VALUES (1375, '崇阳县', 1087, 0);
INSERT INTO `tb_area` VALUES (1376, '通山县', 1087, 0);
INSERT INTO `tb_area` VALUES (1377, '赤壁市', 1087, 0);
INSERT INTO `tb_area` VALUES (1378, '滨城区', 1086, 0);
INSERT INTO `tb_area` VALUES (1379, '沾化区', 1086, 0);
INSERT INTO `tb_area` VALUES (1380, '惠民县', 1086, 0);
INSERT INTO `tb_area` VALUES (1381, '阳信县', 1086, 0);
INSERT INTO `tb_area` VALUES (1382, '无棣县', 1086, 0);
INSERT INTO `tb_area` VALUES (1383, '博兴县', 1086, 0);
INSERT INTO `tb_area` VALUES (1384, '邹平市', 1086, 0);
INSERT INTO `tb_area` VALUES (1385, '浉河区', 1124, 0);
INSERT INTO `tb_area` VALUES (1386, '平桥区', 1124, 0);
INSERT INTO `tb_area` VALUES (1387, '罗山县', 1124, 0);
INSERT INTO `tb_area` VALUES (1388, '光山县', 1124, 0);
INSERT INTO `tb_area` VALUES (1389, '新县', 1124, 0);
INSERT INTO `tb_area` VALUES (1390, '商城县', 1124, 0);
INSERT INTO `tb_area` VALUES (1391, '固始县', 1124, 0);
INSERT INTO `tb_area` VALUES (1392, '潢川县', 1124, 0);
INSERT INTO `tb_area` VALUES (1393, '淮滨县', 1124, 0);
INSERT INTO `tb_area` VALUES (1394, '息县', 1124, 0);
INSERT INTO `tb_area` VALUES (1395, '信阳高新技术产业开发区', 1124, 0);
INSERT INTO `tb_area` VALUES (1396, '曾都区', 1123, 0);
INSERT INTO `tb_area` VALUES (1397, '随县', 1123, 0);
INSERT INTO `tb_area` VALUES (1398, '广水市', 1123, 0);
INSERT INTO `tb_area` VALUES (1399, '川汇区', 1143, 0);
INSERT INTO `tb_area` VALUES (1400, '扶沟县', 1143, 0);
INSERT INTO `tb_area` VALUES (1401, '西华县', 1143, 0);
INSERT INTO `tb_area` VALUES (1402, '商水县', 1143, 0);
INSERT INTO `tb_area` VALUES (1403, '沈丘县', 1143, 0);
INSERT INTO `tb_area` VALUES (1404, '郸城县', 1143, 0);
INSERT INTO `tb_area` VALUES (1405, '淮阳县', 1143, 0);
INSERT INTO `tb_area` VALUES (1406, '太康县', 1143, 0);
INSERT INTO `tb_area` VALUES (1407, '鹿邑县', 1143, 0);
INSERT INTO `tb_area` VALUES (1408, '河南周口经济开发区', 1143, 0);
INSERT INTO `tb_area` VALUES (1409, '项城市', 1143, 0);
INSERT INTO `tb_area` VALUES (1410, '乌鲁木齐市', 831, 1);
INSERT INTO `tb_area` VALUES (1411, '恩施市', 1142, 0);
INSERT INTO `tb_area` VALUES (1412, '利川市', 1142, 0);
INSERT INTO `tb_area` VALUES (1413, '建始县', 1142, 0);
INSERT INTO `tb_area` VALUES (1414, '巴东县', 1142, 0);
INSERT INTO `tb_area` VALUES (1415, '宣恩县', 1142, 0);
INSERT INTO `tb_area` VALUES (1416, '咸丰县', 1142, 0);
INSERT INTO `tb_area` VALUES (1417, '来凤县', 1142, 0);
INSERT INTO `tb_area` VALUES (1418, '鹤峰县', 1142, 0);
INSERT INTO `tb_area` VALUES (1419, '牡丹区', 1122, 0);
INSERT INTO `tb_area` VALUES (1420, '定陶区', 1122, 0);
INSERT INTO `tb_area` VALUES (1421, '曹县', 1122, 0);
INSERT INTO `tb_area` VALUES (1422, '单县', 1122, 0);
INSERT INTO `tb_area` VALUES (1423, '成武县', 1122, 0);
INSERT INTO `tb_area` VALUES (1424, '巨野县', 1122, 0);
INSERT INTO `tb_area` VALUES (1425, '郓城县', 1122, 0);
INSERT INTO `tb_area` VALUES (1426, '鄄城县', 1122, 0);
INSERT INTO `tb_area` VALUES (1427, '东明县', 1122, 0);
INSERT INTO `tb_area` VALUES (1428, '菏泽经济技术开发区', 1122, 0);
INSERT INTO `tb_area` VALUES (1429, '菏泽高新技术开发区', 1122, 0);
INSERT INTO `tb_area` VALUES (1430, '任城区', 826, 0);
INSERT INTO `tb_area` VALUES (1431, '兖州区', 826, 0);
INSERT INTO `tb_area` VALUES (1432, '微山县', 826, 0);
INSERT INTO `tb_area` VALUES (1433, '鱼台县', 826, 0);
INSERT INTO `tb_area` VALUES (1434, '金乡县', 826, 0);
INSERT INTO `tb_area` VALUES (1435, '嘉祥县', 826, 0);
INSERT INTO `tb_area` VALUES (1436, '汶上县', 826, 0);
INSERT INTO `tb_area` VALUES (1437, '泗水县', 826, 0);
INSERT INTO `tb_area` VALUES (1438, '梁山县', 826, 0);
INSERT INTO `tb_area` VALUES (1439, '济宁高新技术产业开发区', 826, 0);
INSERT INTO `tb_area` VALUES (1440, '曲阜市', 826, 0);
INSERT INTO `tb_area` VALUES (1441, '邹城市', 826, 0);
INSERT INTO `tb_area` VALUES (1442, '克拉玛依市', 831, 1);
INSERT INTO `tb_area` VALUES (1443, '驿城区', 1197, 0);
INSERT INTO `tb_area` VALUES (1444, '西平县', 1197, 0);
INSERT INTO `tb_area` VALUES (1445, '上蔡县', 1197, 0);
INSERT INTO `tb_area` VALUES (1446, '平舆县', 1197, 0);
INSERT INTO `tb_area` VALUES (1447, '正阳县', 1197, 0);
INSERT INTO `tb_area` VALUES (1448, '确山县', 1197, 0);
INSERT INTO `tb_area` VALUES (1449, '泌阳县', 1197, 0);
INSERT INTO `tb_area` VALUES (1450, '汝南县', 1197, 0);
INSERT INTO `tb_area` VALUES (1451, '遂平县', 1197, 0);
INSERT INTO `tb_area` VALUES (1452, '新蔡县', 1197, 0);
INSERT INTO `tb_area` VALUES (1453, '河南驻马店经济开发区', 1197, 0);
INSERT INTO `tb_area` VALUES (1454, '仙桃市', 1144, 0);
INSERT INTO `tb_area` VALUES (1455, '潜江市', 1144, 0);
INSERT INTO `tb_area` VALUES (1456, '天门市', 1144, 0);
INSERT INTO `tb_area` VALUES (1457, '神农架林区', 1144, 0);
INSERT INTO `tb_area` VALUES (1458, '济源市', 1217, 0);
INSERT INTO `tb_area` VALUES (1459, '吐鲁番市', 831, 1);
INSERT INTO `tb_area` VALUES (1460, '银川市', 789, 1);
INSERT INTO `tb_area` VALUES (1461, '潍城区', 762, 0);
INSERT INTO `tb_area` VALUES (1462, '寒亭区', 762, 0);
INSERT INTO `tb_area` VALUES (1463, '坊子区', 762, 0);
INSERT INTO `tb_area` VALUES (1464, '奎文区', 762, 0);
INSERT INTO `tb_area` VALUES (1465, '临朐县', 762, 0);
INSERT INTO `tb_area` VALUES (1466, '昌乐县', 762, 0);
INSERT INTO `tb_area` VALUES (1467, '潍坊滨海经济技术开发区', 762, 0);
INSERT INTO `tb_area` VALUES (1468, '青州市', 762, 0);
INSERT INTO `tb_area` VALUES (1469, '诸城市', 762, 0);
INSERT INTO `tb_area` VALUES (1470, '寿光市', 762, 0);
INSERT INTO `tb_area` VALUES (1471, '安丘市', 762, 0);
INSERT INTO `tb_area` VALUES (1472, '高密市', 762, 0);
INSERT INTO `tb_area` VALUES (1473, '昌邑市', 762, 0);
INSERT INTO `tb_area` VALUES (1474, '江岸区', 701, 0);
INSERT INTO `tb_area` VALUES (1475, '江汉区', 701, 0);
INSERT INTO `tb_area` VALUES (1476, '硚口区', 701, 0);
INSERT INTO `tb_area` VALUES (1477, '汉阳区', 701, 0);
INSERT INTO `tb_area` VALUES (1478, '武昌区', 701, 0);
INSERT INTO `tb_area` VALUES (1479, '青山区', 701, 0);
INSERT INTO `tb_area` VALUES (1480, '洪山区', 701, 0);
INSERT INTO `tb_area` VALUES (1481, '东西湖区', 701, 0);
INSERT INTO `tb_area` VALUES (1482, '汉南区', 701, 0);
INSERT INTO `tb_area` VALUES (1483, '蔡甸区', 701, 0);
INSERT INTO `tb_area` VALUES (1484, '江夏区', 701, 0);
INSERT INTO `tb_area` VALUES (1485, '黄陂区', 701, 0);
INSERT INTO `tb_area` VALUES (1486, '新洲区', 701, 0);
INSERT INTO `tb_area` VALUES (1487, '哈密市', 831, 1);
INSERT INTO `tb_area` VALUES (1488, '石嘴山市', 789, 1);
INSERT INTO `tb_area` VALUES (1489, '西宁市', 761, 1);
INSERT INTO `tb_area` VALUES (1490, '芝罘区', 700, 0);
INSERT INTO `tb_area` VALUES (1491, '福山区', 700, 0);
INSERT INTO `tb_area` VALUES (1492, '牟平区', 700, 0);
INSERT INTO `tb_area` VALUES (1493, '莱山区', 700, 0);
INSERT INTO `tb_area` VALUES (1494, '长岛县', 700, 0);
INSERT INTO `tb_area` VALUES (1495, '烟台高新技术产业开发区', 700, 0);
INSERT INTO `tb_area` VALUES (1496, '烟台经济技术开发区', 700, 0);
INSERT INTO `tb_area` VALUES (1497, '龙口市', 700, 0);
INSERT INTO `tb_area` VALUES (1498, '莱阳市', 700, 0);
INSERT INTO `tb_area` VALUES (1499, '莱州市', 700, 0);
INSERT INTO `tb_area` VALUES (1500, '蓬莱市', 700, 0);
INSERT INTO `tb_area` VALUES (1501, '招远市', 700, 0);
INSERT INTO `tb_area` VALUES (1502, '栖霞市', 700, 0);
INSERT INTO `tb_area` VALUES (1503, '海阳市', 700, 0);
INSERT INTO `tb_area` VALUES (1504, '老城区', 694, 0);
INSERT INTO `tb_area` VALUES (1505, '西工区', 694, 0);
INSERT INTO `tb_area` VALUES (1506, '瀍河回族区', 694, 0);
INSERT INTO `tb_area` VALUES (1507, '涧西区', 694, 0);
INSERT INTO `tb_area` VALUES (1508, '吉利区', 694, 0);
INSERT INTO `tb_area` VALUES (1509, '洛龙区', 694, 0);
INSERT INTO `tb_area` VALUES (1510, '孟津县', 694, 0);
INSERT INTO `tb_area` VALUES (1511, '新安县', 694, 0);
INSERT INTO `tb_area` VALUES (1512, '栾川县', 694, 0);
INSERT INTO `tb_area` VALUES (1513, '嵩县', 694, 0);
INSERT INTO `tb_area` VALUES (1514, '汝阳县', 694, 0);
INSERT INTO `tb_area` VALUES (1515, '宜阳县', 694, 0);
INSERT INTO `tb_area` VALUES (1516, '洛宁县', 694, 0);
INSERT INTO `tb_area` VALUES (1517, '伊川县', 694, 0);
INSERT INTO `tb_area` VALUES (1518, '洛阳高新技术产业开发区', 694, 0);
INSERT INTO `tb_area` VALUES (1519, '偃师市', 694, 0);
INSERT INTO `tb_area` VALUES (1520, '东营区', 674, 0);
INSERT INTO `tb_area` VALUES (1521, '河口区', 674, 0);
INSERT INTO `tb_area` VALUES (1522, '垦利区', 674, 0);
INSERT INTO `tb_area` VALUES (1523, '利津县', 674, 0);
INSERT INTO `tb_area` VALUES (1524, '广饶县', 674, 0);
INSERT INTO `tb_area` VALUES (1525, '东营经济技术开发区', 674, 0);
INSERT INTO `tb_area` VALUES (1526, '东营港经济开发区', 674, 0);
INSERT INTO `tb_area` VALUES (1527, '昌吉回族自治州', 831, 1);
INSERT INTO `tb_area` VALUES (1528, '吴忠市', 789, 1);
INSERT INTO `tb_area` VALUES (1529, '海东市', 761, 1);
INSERT INTO `tb_area` VALUES (1530, '琅琊区', 669, 0);
INSERT INTO `tb_area` VALUES (1531, '南谯区', 669, 0);
INSERT INTO `tb_area` VALUES (1532, '来安县', 669, 0);
INSERT INTO `tb_area` VALUES (1533, '全椒县', 669, 0);
INSERT INTO `tb_area` VALUES (1534, '定远县', 669, 0);
INSERT INTO `tb_area` VALUES (1535, '凤阳县', 669, 0);
INSERT INTO `tb_area` VALUES (1536, '苏滁现代产业园', 669, 0);
INSERT INTO `tb_area` VALUES (1537, '滁州经济技术开发区', 669, 0);
INSERT INTO `tb_area` VALUES (1538, '天长市', 669, 0);
INSERT INTO `tb_area` VALUES (1539, '明光市', 669, 0);
INSERT INTO `tb_area` VALUES (1540, '广陵区', 542, 0);
INSERT INTO `tb_area` VALUES (1541, '邗江区', 542, 0);
INSERT INTO `tb_area` VALUES (1542, '江都区', 542, 0);
INSERT INTO `tb_area` VALUES (1543, '宝应县', 542, 0);
INSERT INTO `tb_area` VALUES (1544, '扬州经济技术开发区', 542, 0);
INSERT INTO `tb_area` VALUES (1545, '仪征市', 542, 0);
INSERT INTO `tb_area` VALUES (1546, '高邮市', 542, 0);
INSERT INTO `tb_area` VALUES (1547, '新罗区', 668, 0);
INSERT INTO `tb_area` VALUES (1548, '永定区', 668, 0);
INSERT INTO `tb_area` VALUES (1549, '长汀县', 668, 0);
INSERT INTO `tb_area` VALUES (1550, '上杭县', 668, 0);
INSERT INTO `tb_area` VALUES (1551, '武平县', 668, 0);
INSERT INTO `tb_area` VALUES (1552, '连城县', 668, 0);
INSERT INTO `tb_area` VALUES (1553, '漳平市', 668, 0);
INSERT INTO `tb_area` VALUES (1554, '兰州市', 699, 1);
INSERT INTO `tb_area` VALUES (1555, '博尔塔拉蒙古自治州', 831, 1);
INSERT INTO `tb_area` VALUES (1556, '固原市', 789, 1);
INSERT INTO `tb_area` VALUES (1557, '海北藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1558, '西安市', 673, 1);
INSERT INTO `tb_area` VALUES (1559, '月湖区', 667, 0);
INSERT INTO `tb_area` VALUES (1560, '余江区', 667, 0);
INSERT INTO `tb_area` VALUES (1561, '贵溪市', 667, 0);
INSERT INTO `tb_area` VALUES (1562, '龙亭区', 666, 0);
INSERT INTO `tb_area` VALUES (1563, '顺河回族区', 666, 0);
INSERT INTO `tb_area` VALUES (1564, '鼓楼区', 666, 0);
INSERT INTO `tb_area` VALUES (1565, '禹王台区', 666, 0);
INSERT INTO `tb_area` VALUES (1566, '祥符区', 666, 0);
INSERT INTO `tb_area` VALUES (1567, '杞县', 666, 0);
INSERT INTO `tb_area` VALUES (1568, '通许县', 666, 0);
INSERT INTO `tb_area` VALUES (1569, '尉氏县', 666, 0);
INSERT INTO `tb_area` VALUES (1570, '兰考县', 666, 0);
INSERT INTO `tb_area` VALUES (1571, '市中区', 626, 0);
INSERT INTO `tb_area` VALUES (1572, '薛城区', 626, 0);
INSERT INTO `tb_area` VALUES (1573, '峄城区', 626, 0);
INSERT INTO `tb_area` VALUES (1574, '台儿庄区', 626, 0);
INSERT INTO `tb_area` VALUES (1575, '山亭区', 626, 0);
INSERT INTO `tb_area` VALUES (1576, '滕州市', 626, 0);
INSERT INTO `tb_area` VALUES (1577, '嘉峪关市', 699, 1);
INSERT INTO `tb_area` VALUES (1578, '巴音郭楞蒙古自治州', 831, 1);
INSERT INTO `tb_area` VALUES (1579, '中卫市', 789, 1);
INSERT INTO `tb_area` VALUES (1580, '黄南藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1581, '延平区', 620, 0);
INSERT INTO `tb_area` VALUES (1582, '建阳区', 620, 0);
INSERT INTO `tb_area` VALUES (1583, '顺昌县', 620, 0);
INSERT INTO `tb_area` VALUES (1584, '浦城县', 620, 0);
INSERT INTO `tb_area` VALUES (1585, '光泽县', 620, 0);
INSERT INTO `tb_area` VALUES (1586, '松溪县', 620, 0);
INSERT INTO `tb_area` VALUES (1587, '政和县', 620, 0);
INSERT INTO `tb_area` VALUES (1588, '邵武市', 620, 0);
INSERT INTO `tb_area` VALUES (1589, '武夷山市', 620, 0);
INSERT INTO `tb_area` VALUES (1590, '建瓯市', 620, 0);
INSERT INTO `tb_area` VALUES (1591, '渝水区', 619, 0);
INSERT INTO `tb_area` VALUES (1592, '分宜县', 619, 0);
INSERT INTO `tb_area` VALUES (1593, '中原区', 618, 0);
INSERT INTO `tb_area` VALUES (1594, '二七区', 618, 0);
INSERT INTO `tb_area` VALUES (1595, '管城回族区', 618, 0);
INSERT INTO `tb_area` VALUES (1596, '金水区', 618, 0);
INSERT INTO `tb_area` VALUES (1597, '上街区', 618, 0);
INSERT INTO `tb_area` VALUES (1598, '惠济区', 618, 0);
INSERT INTO `tb_area` VALUES (1599, '中牟县', 618, 0);
INSERT INTO `tb_area` VALUES (1600, '郑州经济技术开发区', 618, 0);
INSERT INTO `tb_area` VALUES (1601, '郑州高新技术产业开发区', 618, 0);
INSERT INTO `tb_area` VALUES (1602, '郑州航空港经济综合实验区', 618, 0);
INSERT INTO `tb_area` VALUES (1603, '巩义市', 618, 0);
INSERT INTO `tb_area` VALUES (1604, '荥阳市', 618, 0);
INSERT INTO `tb_area` VALUES (1605, '新密市', 618, 0);
INSERT INTO `tb_area` VALUES (1606, '新郑市', 618, 0);
INSERT INTO `tb_area` VALUES (1607, '登封市', 618, 0);
INSERT INTO `tb_area` VALUES (1608, '淄川区', 575, 0);
INSERT INTO `tb_area` VALUES (1609, '张店区', 575, 0);
INSERT INTO `tb_area` VALUES (1610, '博山区', 575, 0);
INSERT INTO `tb_area` VALUES (1611, '临淄区', 575, 0);
INSERT INTO `tb_area` VALUES (1612, '周村区', 575, 0);
INSERT INTO `tb_area` VALUES (1613, '桓台县', 575, 0);
INSERT INTO `tb_area` VALUES (1614, '高青县', 575, 0);
INSERT INTO `tb_area` VALUES (1615, '沂源县', 575, 0);
INSERT INTO `tb_area` VALUES (1616, '铜川市', 673, 1);
INSERT INTO `tb_area` VALUES (1617, '拉萨市', 625, 1);
INSERT INTO `tb_area` VALUES (1618, '金昌市', 699, 1);
INSERT INTO `tb_area` VALUES (1619, '阿克苏地区', 831, 1);
INSERT INTO `tb_area` VALUES (1620, '迎江区', 569, 0);
INSERT INTO `tb_area` VALUES (1621, '大观区', 569, 0);
INSERT INTO `tb_area` VALUES (1622, '宜秀区', 569, 0);
INSERT INTO `tb_area` VALUES (1623, '怀宁县', 569, 0);
INSERT INTO `tb_area` VALUES (1624, '太湖县', 569, 0);
INSERT INTO `tb_area` VALUES (1625, '宿松县', 569, 0);
INSERT INTO `tb_area` VALUES (1626, '望江县', 569, 0);
INSERT INTO `tb_area` VALUES (1627, '岳西县', 569, 0);
INSERT INTO `tb_area` VALUES (1628, '安徽安庆经济开发区', 569, 0);
INSERT INTO `tb_area` VALUES (1629, '桐城市', 569, 0);
INSERT INTO `tb_area` VALUES (1630, '潜山市', 569, 0);
INSERT INTO `tb_area` VALUES (1631, '芗城区', 568, 0);
INSERT INTO `tb_area` VALUES (1632, '龙文区', 568, 0);
INSERT INTO `tb_area` VALUES (1633, '云霄县', 568, 0);
INSERT INTO `tb_area` VALUES (1634, '漳浦县', 568, 0);
INSERT INTO `tb_area` VALUES (1635, '诏安县', 568, 0);
INSERT INTO `tb_area` VALUES (1636, '长泰县', 568, 0);
INSERT INTO `tb_area` VALUES (1637, '东山县', 568, 0);
INSERT INTO `tb_area` VALUES (1638, '南靖县', 568, 0);
INSERT INTO `tb_area` VALUES (1639, '平和县', 568, 0);
INSERT INTO `tb_area` VALUES (1640, '华安县', 568, 0);
INSERT INTO `tb_area` VALUES (1641, '龙海市', 568, 0);
INSERT INTO `tb_area` VALUES (1642, '濂溪区', 567, 0);
INSERT INTO `tb_area` VALUES (1643, '浔阳区', 567, 0);
INSERT INTO `tb_area` VALUES (1644, '柴桑区', 567, 0);
INSERT INTO `tb_area` VALUES (1645, '武宁县', 567, 0);
INSERT INTO `tb_area` VALUES (1646, '修水县', 567, 0);
INSERT INTO `tb_area` VALUES (1647, '永修县', 567, 0);
INSERT INTO `tb_area` VALUES (1648, '德安县', 567, 0);
INSERT INTO `tb_area` VALUES (1649, '都昌县', 567, 0);
INSERT INTO `tb_area` VALUES (1650, '湖口县', 567, 0);
INSERT INTO `tb_area` VALUES (1651, '彭泽县', 567, 0);
INSERT INTO `tb_area` VALUES (1652, '瑞昌市', 567, 0);
INSERT INTO `tb_area` VALUES (1653, '共青城市', 567, 0);
INSERT INTO `tb_area` VALUES (1654, '庐山市', 567, 0);
INSERT INTO `tb_area` VALUES (1655, '海南藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1656, '宝鸡市', 673, 1);
INSERT INTO `tb_area` VALUES (1657, '日喀则市', 625, 1);
INSERT INTO `tb_area` VALUES (1658, '白银市', 699, 1);
INSERT INTO `tb_area` VALUES (1659, '克孜勒苏柯尔克孜自治州', 831, 1);
INSERT INTO `tb_area` VALUES (1660, '昆明市', 574, 1);
INSERT INTO `tb_area` VALUES (1661, '市南区', 545, 0);
INSERT INTO `tb_area` VALUES (1662, '市北区', 545, 0);
INSERT INTO `tb_area` VALUES (1663, '黄岛区', 545, 0);
INSERT INTO `tb_area` VALUES (1664, '崂山区', 545, 0);
INSERT INTO `tb_area` VALUES (1665, '李沧区', 545, 0);
INSERT INTO `tb_area` VALUES (1666, '城阳区', 545, 0);
INSERT INTO `tb_area` VALUES (1667, '即墨区', 545, 0);
INSERT INTO `tb_area` VALUES (1668, '青岛高新技术产业开发区', 545, 0);
INSERT INTO `tb_area` VALUES (1669, '胶州市', 545, 0);
INSERT INTO `tb_area` VALUES (1670, '平度市', 545, 0);
INSERT INTO `tb_area` VALUES (1671, '莱西市', 545, 0);
INSERT INTO `tb_area` VALUES (1672, '婺城区', 540, 0);
INSERT INTO `tb_area` VALUES (1673, '金东区', 540, 0);
INSERT INTO `tb_area` VALUES (1674, '武义县', 540, 0);
INSERT INTO `tb_area` VALUES (1675, '浦江县', 540, 0);
INSERT INTO `tb_area` VALUES (1676, '磐安县', 540, 0);
INSERT INTO `tb_area` VALUES (1677, '兰溪市', 540, 0);
INSERT INTO `tb_area` VALUES (1678, '义乌市', 540, 0);
INSERT INTO `tb_area` VALUES (1679, '东阳市', 540, 0);
INSERT INTO `tb_area` VALUES (1680, '永康市', 540, 0);
INSERT INTO `tb_area` VALUES (1681, '铜官区', 539, 0);
INSERT INTO `tb_area` VALUES (1682, '义安区', 539, 0);
INSERT INTO `tb_area` VALUES (1683, '郊区', 539, 0);
INSERT INTO `tb_area` VALUES (1684, '枞阳县', 539, 0);
INSERT INTO `tb_area` VALUES (1685, '果洛藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1686, '咸阳市', 673, 1);
INSERT INTO `tb_area` VALUES (1687, '昌都市', 625, 1);
INSERT INTO `tb_area` VALUES (1688, '天水市', 699, 1);
INSERT INTO `tb_area` VALUES (1689, '喀什地区', 831, 1);
INSERT INTO `tb_area` VALUES (1690, '曲靖市', 574, 1);
INSERT INTO `tb_area` VALUES (1691, '贵阳市', 544, 1);
INSERT INTO `tb_area` VALUES (1692, '鲤城区', 538, 0);
INSERT INTO `tb_area` VALUES (1693, '丰泽区', 538, 0);
INSERT INTO `tb_area` VALUES (1694, '洛江区', 538, 0);
INSERT INTO `tb_area` VALUES (1695, '泉港区', 538, 0);
INSERT INTO `tb_area` VALUES (1696, '惠安县', 538, 0);
INSERT INTO `tb_area` VALUES (1697, '安溪县', 538, 0);
INSERT INTO `tb_area` VALUES (1698, '永春县', 538, 0);
INSERT INTO `tb_area` VALUES (1699, '德化县', 538, 0);
INSERT INTO `tb_area` VALUES (1700, '石狮市', 538, 0);
INSERT INTO `tb_area` VALUES (1701, '晋江市', 538, 0);
INSERT INTO `tb_area` VALUES (1702, '南安市', 538, 0);
INSERT INTO `tb_area` VALUES (1703, '天山区', 1410, 0);
INSERT INTO `tb_area` VALUES (1704, '沙依巴克区', 1410, 0);
INSERT INTO `tb_area` VALUES (1705, '新市区', 1410, 0);
INSERT INTO `tb_area` VALUES (1706, '水磨沟区', 1410, 0);
INSERT INTO `tb_area` VALUES (1707, '头屯河区', 1410, 0);
INSERT INTO `tb_area` VALUES (1708, '达坂城区', 1410, 0);
INSERT INTO `tb_area` VALUES (1709, '米东区', 1410, 0);
INSERT INTO `tb_area` VALUES (1710, '乌鲁木齐县', 1410, 0);
INSERT INTO `tb_area` VALUES (1711, '乌鲁木齐经济技术开发区', 1410, 0);
INSERT INTO `tb_area` VALUES (1712, '乌鲁木齐高新技术产业开发区', 1410, 0);
INSERT INTO `tb_area` VALUES (1713, '安源区', 537, 0);
INSERT INTO `tb_area` VALUES (1714, '湘东区', 537, 0);
INSERT INTO `tb_area` VALUES (1715, '莲花县', 537, 0);
INSERT INTO `tb_area` VALUES (1716, '上栗县', 537, 0);
INSERT INTO `tb_area` VALUES (1717, '芦溪县', 537, 0);
INSERT INTO `tb_area` VALUES (1718, '历下区', 514, 0);
INSERT INTO `tb_area` VALUES (1719, '市中区', 514, 0);
INSERT INTO `tb_area` VALUES (1720, '槐荫区', 514, 0);
INSERT INTO `tb_area` VALUES (1721, '天桥区', 514, 0);
INSERT INTO `tb_area` VALUES (1722, '历城区', 514, 0);
INSERT INTO `tb_area` VALUES (1723, '长清区', 514, 0);
INSERT INTO `tb_area` VALUES (1724, '章丘区', 514, 0);
INSERT INTO `tb_area` VALUES (1725, '济阳区', 514, 0);
INSERT INTO `tb_area` VALUES (1726, '平阴县', 514, 0);
INSERT INTO `tb_area` VALUES (1727, '商河县', 514, 0);
INSERT INTO `tb_area` VALUES (1728, '济南高新技术产业开发区', 514, 0);
INSERT INTO `tb_area` VALUES (1729, '玉树藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1730, '渭南市', 673, 1);
INSERT INTO `tb_area` VALUES (1731, '林芝市', 625, 1);
INSERT INTO `tb_area` VALUES (1732, '武威市', 699, 1);
INSERT INTO `tb_area` VALUES (1733, '和田地区', 831, 1);
INSERT INTO `tb_area` VALUES (1734, '玉溪市', 574, 1);
INSERT INTO `tb_area` VALUES (1735, '六盘水市', 544, 1);
INSERT INTO `tb_area` VALUES (1736, '独山子区', 1442, 0);
INSERT INTO `tb_area` VALUES (1737, '克拉玛依区', 1442, 0);
INSERT INTO `tb_area` VALUES (1738, '白碱滩区', 1442, 0);
INSERT INTO `tb_area` VALUES (1739, '乌尔禾区', 1442, 0);
INSERT INTO `tb_area` VALUES (1740, '越城区', 509, 0);
INSERT INTO `tb_area` VALUES (1741, '柯桥区', 509, 0);
INSERT INTO `tb_area` VALUES (1742, '上虞区', 509, 0);
INSERT INTO `tb_area` VALUES (1743, '新昌县', 509, 0);
INSERT INTO `tb_area` VALUES (1744, '诸暨市', 509, 0);
INSERT INTO `tb_area` VALUES (1745, '嵊州市', 509, 0);
INSERT INTO `tb_area` VALUES (1746, '杜集区', 508, 0);
INSERT INTO `tb_area` VALUES (1747, '相山区', 508, 0);
INSERT INTO `tb_area` VALUES (1748, '烈山区', 508, 0);
INSERT INTO `tb_area` VALUES (1749, '濉溪县', 508, 0);
INSERT INTO `tb_area` VALUES (1750, '海西蒙古族藏族自治州', 761, 1);
INSERT INTO `tb_area` VALUES (1751, '延安市', 673, 1);
INSERT INTO `tb_area` VALUES (1752, '山南市', 625, 1);
INSERT INTO `tb_area` VALUES (1753, '张掖市', 699, 1);
INSERT INTO `tb_area` VALUES (1754, '伊犁哈萨克自治州', 831, 1);
INSERT INTO `tb_area` VALUES (1755, '保山市', 574, 1);
INSERT INTO `tb_area` VALUES (1756, '遵义市', 544, 1);
INSERT INTO `tb_area` VALUES (1757, '成都市', 513, 1);
INSERT INTO `tb_area` VALUES (1758, '兴庆区', 1460, 0);
INSERT INTO `tb_area` VALUES (1759, '西夏区', 1460, 0);
INSERT INTO `tb_area` VALUES (1760, '金凤区', 1460, 0);
INSERT INTO `tb_area` VALUES (1761, '永宁县', 1460, 0);
INSERT INTO `tb_area` VALUES (1762, '贺兰县', 1460, 0);
INSERT INTO `tb_area` VALUES (1763, '灵武市', 1460, 0);
INSERT INTO `tb_area` VALUES (1764, '高昌区', 1459, 0);
INSERT INTO `tb_area` VALUES (1765, '鄯善县', 1459, 0);
INSERT INTO `tb_area` VALUES (1766, '托克逊县', 1459, 0);
INSERT INTO `tb_area` VALUES (1767, '梅列区', 507, 0);
INSERT INTO `tb_area` VALUES (1768, '三元区', 507, 0);
INSERT INTO `tb_area` VALUES (1769, '明溪县', 507, 0);
INSERT INTO `tb_area` VALUES (1770, '清流县', 507, 0);
INSERT INTO `tb_area` VALUES (1771, '宁化县', 507, 0);
INSERT INTO `tb_area` VALUES (1772, '大田县', 507, 0);
INSERT INTO `tb_area` VALUES (1773, '尤溪县', 507, 0);
INSERT INTO `tb_area` VALUES (1774, '沙县', 507, 0);
INSERT INTO `tb_area` VALUES (1775, '将乐县', 507, 0);
INSERT INTO `tb_area` VALUES (1776, '泰宁县', 507, 0);
INSERT INTO `tb_area` VALUES (1777, '建宁县', 507, 0);
INSERT INTO `tb_area` VALUES (1778, '永安市', 507, 0);
INSERT INTO `tb_area` VALUES (1779, '昌江区', 506, 0);
INSERT INTO `tb_area` VALUES (1780, '珠山区', 506, 0);
INSERT INTO `tb_area` VALUES (1781, '浮梁县', 506, 0);
INSERT INTO `tb_area` VALUES (1782, '乐平市', 506, 0);
INSERT INTO `tb_area` VALUES (1783, '汉中市', 673, 1);
INSERT INTO `tb_area` VALUES (1784, '那曲市', 625, 1);
INSERT INTO `tb_area` VALUES (1785, '平凉市', 699, 1);
INSERT INTO `tb_area` VALUES (1786, '塔城地区', 831, 1);
INSERT INTO `tb_area` VALUES (1787, '昭通市', 574, 1);
INSERT INTO `tb_area` VALUES (1788, '安顺市', 544, 1);
INSERT INTO `tb_area` VALUES (1789, '城东区', 1489, 0);
INSERT INTO `tb_area` VALUES (1790, '城中区', 1489, 0);
INSERT INTO `tb_area` VALUES (1791, '城西区', 1489, 0);
INSERT INTO `tb_area` VALUES (1792, '城北区', 1489, 0);
INSERT INTO `tb_area` VALUES (1793, '大通回族土族自治县', 1489, 0);
INSERT INTO `tb_area` VALUES (1794, '湟中县', 1489, 0);
INSERT INTO `tb_area` VALUES (1795, '湟源县', 1489, 0);
INSERT INTO `tb_area` VALUES (1796, '大武口区', 1488, 0);
INSERT INTO `tb_area` VALUES (1797, '惠农区', 1488, 0);
INSERT INTO `tb_area` VALUES (1798, '平罗县', 1488, 0);
INSERT INTO `tb_area` VALUES (1799, '伊州区', 1487, 0);
INSERT INTO `tb_area` VALUES (1800, '巴里坤哈萨克自治县', 1487, 0);
INSERT INTO `tb_area` VALUES (1801, '伊吾县', 1487, 0);
INSERT INTO `tb_area` VALUES (1802, '自贡市', 513, 1);
INSERT INTO `tb_area` VALUES (1803, '榆林市', 673, 1);
INSERT INTO `tb_area` VALUES (1804, '阿里地区', 625, 1);
INSERT INTO `tb_area` VALUES (1805, '酒泉市', 699, 1);
INSERT INTO `tb_area` VALUES (1806, '阿勒泰地区', 831, 1);
INSERT INTO `tb_area` VALUES (1807, '丽江市', 574, 1);
INSERT INTO `tb_area` VALUES (1808, '毕节市', 544, 1);
INSERT INTO `tb_area` VALUES (1809, '城关区', 1554, 0);
INSERT INTO `tb_area` VALUES (1810, '七里河区', 1554, 0);
INSERT INTO `tb_area` VALUES (1811, '西固区', 1554, 0);
INSERT INTO `tb_area` VALUES (1812, '安宁区', 1554, 0);
INSERT INTO `tb_area` VALUES (1813, '红古区', 1554, 0);
INSERT INTO `tb_area` VALUES (1814, '永登县', 1554, 0);
INSERT INTO `tb_area` VALUES (1815, '皋兰县', 1554, 0);
INSERT INTO `tb_area` VALUES (1816, '榆中县', 1554, 0);
INSERT INTO `tb_area` VALUES (1817, '兰州新区', 1554, 0);
INSERT INTO `tb_area` VALUES (1818, '乐都区', 1529, 0);
INSERT INTO `tb_area` VALUES (1819, '平安区', 1529, 0);
INSERT INTO `tb_area` VALUES (1820, '民和回族土族自治县', 1529, 0);
INSERT INTO `tb_area` VALUES (1821, '互助土族自治县', 1529, 0);
INSERT INTO `tb_area` VALUES (1822, '化隆回族自治县', 1529, 0);
INSERT INTO `tb_area` VALUES (1823, '循化撒拉族自治县', 1529, 0);
INSERT INTO `tb_area` VALUES (1824, '利通区', 1528, 0);
INSERT INTO `tb_area` VALUES (1825, '红寺堡区', 1528, 0);
INSERT INTO `tb_area` VALUES (1826, '盐池县', 1528, 0);
INSERT INTO `tb_area` VALUES (1827, '同心县', 1528, 0);
INSERT INTO `tb_area` VALUES (1828, '青铜峡市', 1528, 0);
INSERT INTO `tb_area` VALUES (1829, '昌吉市', 1527, 0);
INSERT INTO `tb_area` VALUES (1830, '阜康市', 1527, 0);
INSERT INTO `tb_area` VALUES (1831, '呼图壁县', 1527, 0);
INSERT INTO `tb_area` VALUES (1832, '玛纳斯县', 1527, 0);
INSERT INTO `tb_area` VALUES (1833, '奇台县', 1527, 0);
INSERT INTO `tb_area` VALUES (1834, '吉木萨尔县', 1527, 0);
INSERT INTO `tb_area` VALUES (1835, '木垒哈萨克自治县', 1527, 0);
INSERT INTO `tb_area` VALUES (1836, '市辖区', 464, 1);
INSERT INTO `tb_area` VALUES (1837, '攀枝花市', 513, 1);
INSERT INTO `tb_area` VALUES (1838, '安康市', 673, 1);
INSERT INTO `tb_area` VALUES (1839, '庆阳市', 699, 1);
INSERT INTO `tb_area` VALUES (1840, '自治区直辖县级行政区划', 831, 1);
INSERT INTO `tb_area` VALUES (1841, '普洱市', 574, 1);
INSERT INTO `tb_area` VALUES (1842, '铜仁市', 544, 1);
INSERT INTO `tb_area` VALUES (1843, '市辖区', 1577, 0);
INSERT INTO `tb_area` VALUES (1844, '新城区', 1558, 0);
INSERT INTO `tb_area` VALUES (1845, '碑林区', 1558, 0);
INSERT INTO `tb_area` VALUES (1846, '莲湖区', 1558, 0);
INSERT INTO `tb_area` VALUES (1847, '灞桥区', 1558, 0);
INSERT INTO `tb_area` VALUES (1848, '未央区', 1558, 0);
INSERT INTO `tb_area` VALUES (1849, '雁塔区', 1558, 0);
INSERT INTO `tb_area` VALUES (1850, '阎良区', 1558, 0);
INSERT INTO `tb_area` VALUES (1851, '临潼区', 1558, 0);
INSERT INTO `tb_area` VALUES (1852, '长安区', 1558, 0);
INSERT INTO `tb_area` VALUES (1853, '高陵区', 1558, 0);
INSERT INTO `tb_area` VALUES (1854, '鄠邑区', 1558, 0);
INSERT INTO `tb_area` VALUES (1855, '蓝田县', 1558, 0);
INSERT INTO `tb_area` VALUES (1856, '周至县', 1558, 0);
INSERT INTO `tb_area` VALUES (1857, '门源回族自治县', 1557, 0);
INSERT INTO `tb_area` VALUES (1858, '祁连县', 1557, 0);
INSERT INTO `tb_area` VALUES (1859, '海晏县', 1557, 0);
INSERT INTO `tb_area` VALUES (1860, '刚察县', 1557, 0);
INSERT INTO `tb_area` VALUES (1861, '县', 464, 1);
INSERT INTO `tb_area` VALUES (1862, '泸州市', 513, 1);
INSERT INTO `tb_area` VALUES (1863, '商洛市', 673, 1);
INSERT INTO `tb_area` VALUES (1864, '定西市', 699, 1);
INSERT INTO `tb_area` VALUES (1865, '临沧市', 574, 1);
INSERT INTO `tb_area` VALUES (1866, '黔西南布依族苗族自治州', 544, 1);
INSERT INTO `tb_area` VALUES (1867, '金川区', 1618, 0);
INSERT INTO `tb_area` VALUES (1868, '永昌县', 1618, 0);
INSERT INTO `tb_area` VALUES (1869, '原州区', 1556, 0);
INSERT INTO `tb_area` VALUES (1870, '西吉县', 1556, 0);
INSERT INTO `tb_area` VALUES (1871, '隆德县', 1556, 0);
INSERT INTO `tb_area` VALUES (1872, '泾源县', 1556, 0);
INSERT INTO `tb_area` VALUES (1873, '彭阳县', 1556, 0);
INSERT INTO `tb_area` VALUES (1874, '城关区', 1617, 0);
INSERT INTO `tb_area` VALUES (1875, '堆龙德庆区', 1617, 0);
INSERT INTO `tb_area` VALUES (1876, '达孜区', 1617, 0);
INSERT INTO `tb_area` VALUES (1877, '林周县', 1617, 0);
INSERT INTO `tb_area` VALUES (1878, '当雄县', 1617, 0);
INSERT INTO `tb_area` VALUES (1879, '尼木县', 1617, 0);
INSERT INTO `tb_area` VALUES (1880, '曲水县', 1617, 0);
INSERT INTO `tb_area` VALUES (1881, '墨竹工卡县', 1617, 0);
INSERT INTO `tb_area` VALUES (1882, '格尔木藏青工业园区', 1617, 0);
INSERT INTO `tb_area` VALUES (1883, '拉萨经济技术开发区', 1617, 0);
INSERT INTO `tb_area` VALUES (1884, '西藏文化旅游创意园区', 1617, 0);
INSERT INTO `tb_area` VALUES (1885, '达孜工业园区', 1617, 0);
INSERT INTO `tb_area` VALUES (1886, '王益区', 1616, 0);
INSERT INTO `tb_area` VALUES (1887, '印台区', 1616, 0);
INSERT INTO `tb_area` VALUES (1888, '耀州区', 1616, 0);
INSERT INTO `tb_area` VALUES (1889, '宜君县', 1616, 0);
INSERT INTO `tb_area` VALUES (1890, '同仁县', 1580, 0);
INSERT INTO `tb_area` VALUES (1891, '尖扎县', 1580, 0);
INSERT INTO `tb_area` VALUES (1892, '泽库县', 1580, 0);
INSERT INTO `tb_area` VALUES (1893, '河南蒙古族自治县', 1580, 0);
INSERT INTO `tb_area` VALUES (1894, '德阳市', 513, 1);
INSERT INTO `tb_area` VALUES (1895, '陇南市', 699, 1);
INSERT INTO `tb_area` VALUES (1896, '楚雄彝族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (1897, '黔东南苗族侗族自治州', 544, 1);
INSERT INTO `tb_area` VALUES (1898, '白银区', 1658, 0);
INSERT INTO `tb_area` VALUES (1899, '平川区', 1658, 0);
INSERT INTO `tb_area` VALUES (1900, '靖远县', 1658, 0);
INSERT INTO `tb_area` VALUES (1901, '会宁县', 1658, 0);
INSERT INTO `tb_area` VALUES (1902, '景泰县', 1658, 0);
INSERT INTO `tb_area` VALUES (1903, '桑珠孜区', 1657, 0);
INSERT INTO `tb_area` VALUES (1904, '南木林县', 1657, 0);
INSERT INTO `tb_area` VALUES (1905, '江孜县', 1657, 0);
INSERT INTO `tb_area` VALUES (1906, '定日县', 1657, 0);
INSERT INTO `tb_area` VALUES (1907, '萨迦县', 1657, 0);
INSERT INTO `tb_area` VALUES (1908, '拉孜县', 1657, 0);
INSERT INTO `tb_area` VALUES (1909, '昂仁县', 1657, 0);
INSERT INTO `tb_area` VALUES (1910, '谢通门县', 1657, 0);
INSERT INTO `tb_area` VALUES (1911, '白朗县', 1657, 0);
INSERT INTO `tb_area` VALUES (1912, '仁布县', 1657, 0);
INSERT INTO `tb_area` VALUES (1913, '康马县', 1657, 0);
INSERT INTO `tb_area` VALUES (1914, '定结县', 1657, 0);
INSERT INTO `tb_area` VALUES (1915, '仲巴县', 1657, 0);
INSERT INTO `tb_area` VALUES (1916, '亚东县', 1657, 0);
INSERT INTO `tb_area` VALUES (1917, '吉隆县', 1657, 0);
INSERT INTO `tb_area` VALUES (1918, '聂拉木县', 1657, 0);
INSERT INTO `tb_area` VALUES (1919, '萨嘎县', 1657, 0);
INSERT INTO `tb_area` VALUES (1920, '岗巴县', 1657, 0);
INSERT INTO `tb_area` VALUES (1921, '渭滨区', 1656, 0);
INSERT INTO `tb_area` VALUES (1922, '金台区', 1656, 0);
INSERT INTO `tb_area` VALUES (1923, '陈仓区', 1656, 0);
INSERT INTO `tb_area` VALUES (1924, '凤翔县', 1656, 0);
INSERT INTO `tb_area` VALUES (1925, '岐山县', 1656, 0);
INSERT INTO `tb_area` VALUES (1926, '扶风县', 1656, 0);
INSERT INTO `tb_area` VALUES (1927, '眉县', 1656, 0);
INSERT INTO `tb_area` VALUES (1928, '陇县', 1656, 0);
INSERT INTO `tb_area` VALUES (1929, '千阳县', 1656, 0);
INSERT INTO `tb_area` VALUES (1930, '麟游县', 1656, 0);
INSERT INTO `tb_area` VALUES (1931, '凤县', 1656, 0);
INSERT INTO `tb_area` VALUES (1932, '太白县', 1656, 0);
INSERT INTO `tb_area` VALUES (1933, '绵阳市', 513, 1);
INSERT INTO `tb_area` VALUES (1934, '临夏回族自治州', 699, 1);
INSERT INTO `tb_area` VALUES (1935, '红河哈尼族彝族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (1936, '黔南布依族苗族自治州', 544, 1);
INSERT INTO `tb_area` VALUES (1937, '共和县', 1655, 0);
INSERT INTO `tb_area` VALUES (1938, '同德县', 1655, 0);
INSERT INTO `tb_area` VALUES (1939, '贵德县', 1655, 0);
INSERT INTO `tb_area` VALUES (1940, '兴海县', 1655, 0);
INSERT INTO `tb_area` VALUES (1941, '贵南县', 1655, 0);
INSERT INTO `tb_area` VALUES (1942, '秦州区', 1688, 0);
INSERT INTO `tb_area` VALUES (1943, '麦积区', 1688, 0);
INSERT INTO `tb_area` VALUES (1944, '清水县', 1688, 0);
INSERT INTO `tb_area` VALUES (1945, '秦安县', 1688, 0);
INSERT INTO `tb_area` VALUES (1946, '甘谷县', 1688, 0);
INSERT INTO `tb_area` VALUES (1947, '武山县', 1688, 0);
INSERT INTO `tb_area` VALUES (1948, '张家川回族自治县', 1688, 0);
INSERT INTO `tb_area` VALUES (1949, '卡若区', 1687, 0);
INSERT INTO `tb_area` VALUES (1950, '江达县', 1687, 0);
INSERT INTO `tb_area` VALUES (1951, '贡觉县', 1687, 0);
INSERT INTO `tb_area` VALUES (1952, '类乌齐县', 1687, 0);
INSERT INTO `tb_area` VALUES (1953, '丁青县', 1687, 0);
INSERT INTO `tb_area` VALUES (1954, '察雅县', 1687, 0);
INSERT INTO `tb_area` VALUES (1955, '八宿县', 1687, 0);
INSERT INTO `tb_area` VALUES (1956, '左贡县', 1687, 0);
INSERT INTO `tb_area` VALUES (1957, '芒康县', 1687, 0);
INSERT INTO `tb_area` VALUES (1958, '洛隆县', 1687, 0);
INSERT INTO `tb_area` VALUES (1959, '边坝县', 1687, 0);
INSERT INTO `tb_area` VALUES (1960, '秦都区', 1686, 0);
INSERT INTO `tb_area` VALUES (1961, '杨陵区', 1686, 0);
INSERT INTO `tb_area` VALUES (1962, '渭城区', 1686, 0);
INSERT INTO `tb_area` VALUES (1963, '三原县', 1686, 0);
INSERT INTO `tb_area` VALUES (1964, '泾阳县', 1686, 0);
INSERT INTO `tb_area` VALUES (1965, '乾县', 1686, 0);
INSERT INTO `tb_area` VALUES (1966, '礼泉县', 1686, 0);
INSERT INTO `tb_area` VALUES (1967, '永寿县', 1686, 0);
INSERT INTO `tb_area` VALUES (1968, '长武县', 1686, 0);
INSERT INTO `tb_area` VALUES (1969, '旬邑县', 1686, 0);
INSERT INTO `tb_area` VALUES (1970, '淳化县', 1686, 0);
INSERT INTO `tb_area` VALUES (1971, '武功县', 1686, 0);
INSERT INTO `tb_area` VALUES (1972, '兴平市', 1686, 0);
INSERT INTO `tb_area` VALUES (1973, '彬州市', 1686, 0);
INSERT INTO `tb_area` VALUES (1974, '玛沁县', 1685, 0);
INSERT INTO `tb_area` VALUES (1975, '班玛县', 1685, 0);
INSERT INTO `tb_area` VALUES (1976, '甘德县', 1685, 0);
INSERT INTO `tb_area` VALUES (1977, '达日县', 1685, 0);
INSERT INTO `tb_area` VALUES (1978, '久治县', 1685, 0);
INSERT INTO `tb_area` VALUES (1979, '玛多县', 1685, 0);
INSERT INTO `tb_area` VALUES (1980, '广元市', 513, 1);
INSERT INTO `tb_area` VALUES (1981, '甘南藏族自治州', 699, 1);
INSERT INTO `tb_area` VALUES (1982, '文山壮族苗族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (1983, '凉州区', 1732, 0);
INSERT INTO `tb_area` VALUES (1984, '民勤县', 1732, 0);
INSERT INTO `tb_area` VALUES (1985, '古浪县', 1732, 0);
INSERT INTO `tb_area` VALUES (1986, '天祝藏族自治县', 1732, 0);
INSERT INTO `tb_area` VALUES (1987, '巴宜区', 1731, 0);
INSERT INTO `tb_area` VALUES (1988, '工布江达县', 1731, 0);
INSERT INTO `tb_area` VALUES (1989, '米林县', 1731, 0);
INSERT INTO `tb_area` VALUES (1990, '墨脱县', 1731, 0);
INSERT INTO `tb_area` VALUES (1991, '波密县', 1731, 0);
INSERT INTO `tb_area` VALUES (1992, '察隅县', 1731, 0);
INSERT INTO `tb_area` VALUES (1993, '朗县', 1731, 0);
INSERT INTO `tb_area` VALUES (1994, '临渭区', 1730, 0);
INSERT INTO `tb_area` VALUES (1995, '华州区', 1730, 0);
INSERT INTO `tb_area` VALUES (1996, '潼关县', 1730, 0);
INSERT INTO `tb_area` VALUES (1997, '大荔县', 1730, 0);
INSERT INTO `tb_area` VALUES (1998, '合阳县', 1730, 0);
INSERT INTO `tb_area` VALUES (1999, '澄城县', 1730, 0);
INSERT INTO `tb_area` VALUES (2000, '蒲城县', 1730, 0);
INSERT INTO `tb_area` VALUES (2001, '白水县', 1730, 0);
INSERT INTO `tb_area` VALUES (2002, '富平县', 1730, 0);
INSERT INTO `tb_area` VALUES (2003, '韩城市', 1730, 0);
INSERT INTO `tb_area` VALUES (2004, '华阴市', 1730, 0);
INSERT INTO `tb_area` VALUES (2005, '遂宁市', 513, 1);
INSERT INTO `tb_area` VALUES (2006, '西双版纳傣族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (2007, '玉树市', 1729, 0);
INSERT INTO `tb_area` VALUES (2008, '杂多县', 1729, 0);
INSERT INTO `tb_area` VALUES (2009, '称多县', 1729, 0);
INSERT INTO `tb_area` VALUES (2010, '治多县', 1729, 0);
INSERT INTO `tb_area` VALUES (2011, '囊谦县', 1729, 0);
INSERT INTO `tb_area` VALUES (2012, '曲麻莱县', 1729, 0);
INSERT INTO `tb_area` VALUES (2013, '甘州区', 1753, 0);
INSERT INTO `tb_area` VALUES (2014, '肃南裕固族自治县', 1753, 0);
INSERT INTO `tb_area` VALUES (2015, '民乐县', 1753, 0);
INSERT INTO `tb_area` VALUES (2016, '临泽县', 1753, 0);
INSERT INTO `tb_area` VALUES (2017, '高台县', 1753, 0);
INSERT INTO `tb_area` VALUES (2018, '山丹县', 1753, 0);
INSERT INTO `tb_area` VALUES (2019, '乃东区', 1752, 0);
INSERT INTO `tb_area` VALUES (2020, '扎囊县', 1752, 0);
INSERT INTO `tb_area` VALUES (2021, '贡嘎县', 1752, 0);
INSERT INTO `tb_area` VALUES (2022, '桑日县', 1752, 0);
INSERT INTO `tb_area` VALUES (2023, '琼结县', 1752, 0);
INSERT INTO `tb_area` VALUES (2024, '曲松县', 1752, 0);
INSERT INTO `tb_area` VALUES (2025, '措美县', 1752, 0);
INSERT INTO `tb_area` VALUES (2026, '洛扎县', 1752, 0);
INSERT INTO `tb_area` VALUES (2027, '加查县', 1752, 0);
INSERT INTO `tb_area` VALUES (2028, '隆子县', 1752, 0);
INSERT INTO `tb_area` VALUES (2029, '错那县', 1752, 0);
INSERT INTO `tb_area` VALUES (2030, '浪卡子县', 1752, 0);
INSERT INTO `tb_area` VALUES (2031, '宝塔区', 1751, 0);
INSERT INTO `tb_area` VALUES (2032, '安塞区', 1751, 0);
INSERT INTO `tb_area` VALUES (2033, '延长县', 1751, 0);
INSERT INTO `tb_area` VALUES (2034, '延川县', 1751, 0);
INSERT INTO `tb_area` VALUES (2035, '子长县', 1751, 0);
INSERT INTO `tb_area` VALUES (2036, '志丹县', 1751, 0);
INSERT INTO `tb_area` VALUES (2037, '吴起县', 1751, 0);
INSERT INTO `tb_area` VALUES (2038, '甘泉县', 1751, 0);
INSERT INTO `tb_area` VALUES (2039, '富县', 1751, 0);
INSERT INTO `tb_area` VALUES (2040, '洛川县', 1751, 0);
INSERT INTO `tb_area` VALUES (2041, '宜川县', 1751, 0);
INSERT INTO `tb_area` VALUES (2042, '黄龙县', 1751, 0);
INSERT INTO `tb_area` VALUES (2043, '黄陵县', 1751, 0);
INSERT INTO `tb_area` VALUES (2044, '格尔木市', 1750, 0);
INSERT INTO `tb_area` VALUES (2045, '德令哈市', 1750, 0);
INSERT INTO `tb_area` VALUES (2046, '茫崖市', 1750, 0);
INSERT INTO `tb_area` VALUES (2047, '乌兰县', 1750, 0);
INSERT INTO `tb_area` VALUES (2048, '都兰县', 1750, 0);
INSERT INTO `tb_area` VALUES (2049, '天峻县', 1750, 0);
INSERT INTO `tb_area` VALUES (2050, '大柴旦行政委员会', 1750, 0);
INSERT INTO `tb_area` VALUES (2051, '内江市', 513, 1);
INSERT INTO `tb_area` VALUES (2052, '大理白族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (2053, '崆峒区', 1785, 0);
INSERT INTO `tb_area` VALUES (2054, '泾川县', 1785, 0);
INSERT INTO `tb_area` VALUES (2055, '灵台县', 1785, 0);
INSERT INTO `tb_area` VALUES (2056, '崇信县', 1785, 0);
INSERT INTO `tb_area` VALUES (2057, '庄浪县', 1785, 0);
INSERT INTO `tb_area` VALUES (2058, '静宁县', 1785, 0);
INSERT INTO `tb_area` VALUES (2059, '华亭市', 1785, 0);
INSERT INTO `tb_area` VALUES (2060, '色尼区', 1784, 0);
INSERT INTO `tb_area` VALUES (2061, '嘉黎县', 1784, 0);
INSERT INTO `tb_area` VALUES (2062, '比如县', 1784, 0);
INSERT INTO `tb_area` VALUES (2063, '聂荣县', 1784, 0);
INSERT INTO `tb_area` VALUES (2064, '安多县', 1784, 0);
INSERT INTO `tb_area` VALUES (2065, '申扎县', 1784, 0);
INSERT INTO `tb_area` VALUES (2066, '索县', 1784, 0);
INSERT INTO `tb_area` VALUES (2067, '班戈县', 1784, 0);
INSERT INTO `tb_area` VALUES (2068, '巴青县', 1784, 0);
INSERT INTO `tb_area` VALUES (2069, '尼玛县', 1784, 0);
INSERT INTO `tb_area` VALUES (2070, '双湖县', 1784, 0);
INSERT INTO `tb_area` VALUES (2071, '汉台区', 1783, 0);
INSERT INTO `tb_area` VALUES (2072, '南郑区', 1783, 0);
INSERT INTO `tb_area` VALUES (2073, '城固县', 1783, 0);
INSERT INTO `tb_area` VALUES (2074, '洋县', 1783, 0);
INSERT INTO `tb_area` VALUES (2075, '西乡县', 1783, 0);
INSERT INTO `tb_area` VALUES (2076, '勉县', 1783, 0);
INSERT INTO `tb_area` VALUES (2077, '宁强县', 1783, 0);
INSERT INTO `tb_area` VALUES (2078, '略阳县', 1783, 0);
INSERT INTO `tb_area` VALUES (2079, '镇巴县', 1783, 0);
INSERT INTO `tb_area` VALUES (2080, '留坝县', 1783, 0);
INSERT INTO `tb_area` VALUES (2081, '佛坪县', 1783, 0);
INSERT INTO `tb_area` VALUES (2082, '乐山市', 513, 1);
INSERT INTO `tb_area` VALUES (2083, '德宏傣族景颇族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (2084, '南充市', 513, 1);
INSERT INTO `tb_area` VALUES (2085, '怒江傈僳族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (2086, '眉山市', 513, 1);
INSERT INTO `tb_area` VALUES (2087, '迪庆藏族自治州', 574, 1);
INSERT INTO `tb_area` VALUES (2088, '宜宾市', 513, 1);
INSERT INTO `tb_area` VALUES (2089, '广安市', 513, 1);
INSERT INTO `tb_area` VALUES (2090, '达州市', 513, 1);
INSERT INTO `tb_area` VALUES (2091, '雅安市', 513, 1);
INSERT INTO `tb_area` VALUES (2092, '巴中市', 513, 1);
INSERT INTO `tb_area` VALUES (2093, '资阳市', 513, 1);
INSERT INTO `tb_area` VALUES (2094, '阿坝藏族羌族自治州', 513, 1);
INSERT INTO `tb_area` VALUES (2095, '甘孜藏族自治州', 513, 1);
INSERT INTO `tb_area` VALUES (2096, '凉山彝族自治州', 513, 1);
INSERT INTO `tb_area` VALUES (2097, '锦江区', 1757, 0);
INSERT INTO `tb_area` VALUES (2098, '青羊区', 1757, 0);
INSERT INTO `tb_area` VALUES (2099, '金牛区', 1757, 0);
INSERT INTO `tb_area` VALUES (2100, '武侯区', 1757, 0);
INSERT INTO `tb_area` VALUES (2101, '成华区', 1757, 0);
INSERT INTO `tb_area` VALUES (2102, '龙泉驿区', 1757, 0);
INSERT INTO `tb_area` VALUES (2103, '青白江区', 1757, 0);
INSERT INTO `tb_area` VALUES (2104, '新都区', 1757, 0);
INSERT INTO `tb_area` VALUES (2105, '温江区', 1757, 0);
INSERT INTO `tb_area` VALUES (2106, '双流区', 1757, 0);
INSERT INTO `tb_area` VALUES (2107, '郫都区', 1757, 0);
INSERT INTO `tb_area` VALUES (2108, '金堂县', 1757, 0);
INSERT INTO `tb_area` VALUES (2109, '大邑县', 1757, 0);
INSERT INTO `tb_area` VALUES (2110, '蒲江县', 1757, 0);
INSERT INTO `tb_area` VALUES (2111, '新津县', 1757, 0);
INSERT INTO `tb_area` VALUES (2112, '都江堰市', 1757, 0);
INSERT INTO `tb_area` VALUES (2113, '彭州市', 1757, 0);
INSERT INTO `tb_area` VALUES (2114, '邛崃市', 1757, 0);
INSERT INTO `tb_area` VALUES (2115, '崇州市', 1757, 0);
INSERT INTO `tb_area` VALUES (2116, '简阳市', 1757, 0);
INSERT INTO `tb_area` VALUES (2117, '西峰区', 1839, 0);
INSERT INTO `tb_area` VALUES (2118, '庆城县', 1839, 0);
INSERT INTO `tb_area` VALUES (2119, '环县', 1839, 0);
INSERT INTO `tb_area` VALUES (2120, '华池县', 1839, 0);
INSERT INTO `tb_area` VALUES (2121, '合水县', 1839, 0);
INSERT INTO `tb_area` VALUES (2122, '正宁县', 1839, 0);
INSERT INTO `tb_area` VALUES (2123, '宁县', 1839, 0);
INSERT INTO `tb_area` VALUES (2124, '镇原县', 1839, 0);
INSERT INTO `tb_area` VALUES (2125, '普兰县', 1804, 0);
INSERT INTO `tb_area` VALUES (2126, '札达县', 1804, 0);
INSERT INTO `tb_area` VALUES (2127, '噶尔县', 1804, 0);
INSERT INTO `tb_area` VALUES (2128, '日土县', 1804, 0);
INSERT INTO `tb_area` VALUES (2129, '革吉县', 1804, 0);
INSERT INTO `tb_area` VALUES (2130, '改则县', 1804, 0);
INSERT INTO `tb_area` VALUES (2131, '措勤县', 1804, 0);
INSERT INTO `tb_area` VALUES (2132, '安定区', 1864, 0);
INSERT INTO `tb_area` VALUES (2133, '通渭县', 1864, 0);
INSERT INTO `tb_area` VALUES (2134, '陇西县', 1864, 0);
INSERT INTO `tb_area` VALUES (2135, '渭源县', 1864, 0);
INSERT INTO `tb_area` VALUES (2136, '临洮县', 1864, 0);
INSERT INTO `tb_area` VALUES (2137, '漳县', 1864, 0);
INSERT INTO `tb_area` VALUES (2138, '岷县', 1864, 0);
INSERT INTO `tb_area` VALUES (2139, '汉滨区', 1838, 0);
INSERT INTO `tb_area` VALUES (2140, '汉阴县', 1838, 0);
INSERT INTO `tb_area` VALUES (2141, '石泉县', 1838, 0);
INSERT INTO `tb_area` VALUES (2142, '宁陕县', 1838, 0);
INSERT INTO `tb_area` VALUES (2143, '紫阳县', 1838, 0);
INSERT INTO `tb_area` VALUES (2144, '岚皋县', 1838, 0);
INSERT INTO `tb_area` VALUES (2145, '平利县', 1838, 0);
INSERT INTO `tb_area` VALUES (2146, '镇坪县', 1838, 0);
INSERT INTO `tb_area` VALUES (2147, '旬阳县', 1838, 0);
INSERT INTO `tb_area` VALUES (2148, '白河县', 1838, 0);
INSERT INTO `tb_area` VALUES (2149, '商州区', 1863, 0);
INSERT INTO `tb_area` VALUES (2150, '洛南县', 1863, 0);
INSERT INTO `tb_area` VALUES (2151, '丹凤县', 1863, 0);
INSERT INTO `tb_area` VALUES (2152, '商南县', 1863, 0);
INSERT INTO `tb_area` VALUES (2153, '山阳县', 1863, 0);
INSERT INTO `tb_area` VALUES (2154, '镇安县', 1863, 0);
INSERT INTO `tb_area` VALUES (2155, '柞水县', 1863, 0);
INSERT INTO `tb_area` VALUES (2156, '江阳区', 1862, 0);
INSERT INTO `tb_area` VALUES (2157, '纳溪区', 1862, 0);
INSERT INTO `tb_area` VALUES (2158, '龙马潭区', 1862, 0);
INSERT INTO `tb_area` VALUES (2159, '泸县', 1862, 0);
INSERT INTO `tb_area` VALUES (2160, '合江县', 1862, 0);
INSERT INTO `tb_area` VALUES (2161, '叙永县', 1862, 0);
INSERT INTO `tb_area` VALUES (2162, '古蔺县', 1862, 0);
INSERT INTO `tb_area` VALUES (2163, '榆阳区', 1803, 0);
INSERT INTO `tb_area` VALUES (2164, '横山区', 1803, 0);
INSERT INTO `tb_area` VALUES (2165, '府谷县', 1803, 0);
INSERT INTO `tb_area` VALUES (2166, '靖边县', 1803, 0);
INSERT INTO `tb_area` VALUES (2167, '定边县', 1803, 0);
INSERT INTO `tb_area` VALUES (2168, '绥德县', 1803, 0);
INSERT INTO `tb_area` VALUES (2169, '米脂县', 1803, 0);
INSERT INTO `tb_area` VALUES (2170, '佳县', 1803, 0);
INSERT INTO `tb_area` VALUES (2171, '吴堡县', 1803, 0);
INSERT INTO `tb_area` VALUES (2172, '清涧县', 1803, 0);
INSERT INTO `tb_area` VALUES (2173, '子洲县', 1803, 0);
INSERT INTO `tb_area` VALUES (2174, '神木市', 1803, 0);
INSERT INTO `tb_area` VALUES (2175, '城口县', 1861, 0);
INSERT INTO `tb_area` VALUES (2176, '丰都县', 1861, 0);
INSERT INTO `tb_area` VALUES (2177, '垫江县', 1861, 0);
INSERT INTO `tb_area` VALUES (2178, '忠县', 1861, 0);
INSERT INTO `tb_area` VALUES (2179, '云阳县', 1861, 0);
INSERT INTO `tb_area` VALUES (2180, '奉节县', 1861, 0);
INSERT INTO `tb_area` VALUES (2181, '巫山县', 1861, 0);
INSERT INTO `tb_area` VALUES (2182, '巫溪县', 1861, 0);
INSERT INTO `tb_area` VALUES (2183, '石柱土家族自治县', 1861, 0);
INSERT INTO `tb_area` VALUES (2184, '秀山土家族苗族自治县', 1861, 0);
INSERT INTO `tb_area` VALUES (2185, '酉阳土家族苗族自治县', 1861, 0);
INSERT INTO `tb_area` VALUES (2186, '彭水苗族土家族自治县', 1861, 0);
INSERT INTO `tb_area` VALUES (2187, '碧江区', 1842, 0);
INSERT INTO `tb_area` VALUES (2188, '万山区', 1842, 0);
INSERT INTO `tb_area` VALUES (2189, '江口县', 1842, 0);
INSERT INTO `tb_area` VALUES (2190, '玉屏侗族自治县', 1842, 0);
INSERT INTO `tb_area` VALUES (2191, '石阡县', 1842, 0);
INSERT INTO `tb_area` VALUES (2192, '思南县', 1842, 0);
INSERT INTO `tb_area` VALUES (2193, '印江土家族苗族自治县', 1842, 0);
INSERT INTO `tb_area` VALUES (2194, '德江县', 1842, 0);
INSERT INTO `tb_area` VALUES (2195, '沿河土家族自治县', 1842, 0);
INSERT INTO `tb_area` VALUES (2196, '松桃苗族自治县', 1842, 0);
INSERT INTO `tb_area` VALUES (2197, '肃州区', 1805, 0);
INSERT INTO `tb_area` VALUES (2198, '金塔县', 1805, 0);
INSERT INTO `tb_area` VALUES (2199, '瓜州县', 1805, 0);
INSERT INTO `tb_area` VALUES (2200, '肃北蒙古族自治县', 1805, 0);
INSERT INTO `tb_area` VALUES (2201, '阿克塞哈萨克族自治县', 1805, 0);
INSERT INTO `tb_area` VALUES (2202, '玉门市', 1805, 0);
INSERT INTO `tb_area` VALUES (2203, '敦煌市', 1805, 0);
INSERT INTO `tb_area` VALUES (2204, '自流井区', 1802, 0);
INSERT INTO `tb_area` VALUES (2205, '贡井区', 1802, 0);
INSERT INTO `tb_area` VALUES (2206, '大安区', 1802, 0);
INSERT INTO `tb_area` VALUES (2207, '沿滩区', 1802, 0);
INSERT INTO `tb_area` VALUES (2208, '荣县', 1802, 0);
INSERT INTO `tb_area` VALUES (2209, '富顺县', 1802, 0);
INSERT INTO `tb_area` VALUES (2210, '武都区', 1895, 0);
INSERT INTO `tb_area` VALUES (2211, '成县', 1895, 0);
INSERT INTO `tb_area` VALUES (2212, '文县', 1895, 0);
INSERT INTO `tb_area` VALUES (2213, '宕昌县', 1895, 0);
INSERT INTO `tb_area` VALUES (2214, '康县', 1895, 0);
INSERT INTO `tb_area` VALUES (2215, '西和县', 1895, 0);
INSERT INTO `tb_area` VALUES (2216, '礼县', 1895, 0);
INSERT INTO `tb_area` VALUES (2217, '徽县', 1895, 0);
INSERT INTO `tb_area` VALUES (2218, '两当县', 1895, 0);
INSERT INTO `tb_area` VALUES (2219, '东区', 1837, 0);
INSERT INTO `tb_area` VALUES (2220, '西区', 1837, 0);
INSERT INTO `tb_area` VALUES (2221, '仁和区', 1837, 0);
INSERT INTO `tb_area` VALUES (2222, '米易县', 1837, 0);
INSERT INTO `tb_area` VALUES (2223, '盐边县', 1837, 0);
INSERT INTO `tb_area` VALUES (2224, '旌阳区', 1894, 0);
INSERT INTO `tb_area` VALUES (2225, '罗江区', 1894, 0);
INSERT INTO `tb_area` VALUES (2226, '中江县', 1894, 0);
INSERT INTO `tb_area` VALUES (2227, '广汉市', 1894, 0);
INSERT INTO `tb_area` VALUES (2228, '什邡市', 1894, 0);
INSERT INTO `tb_area` VALUES (2229, '绵竹市', 1894, 0);
INSERT INTO `tb_area` VALUES (2230, '兴义市', 1866, 0);
INSERT INTO `tb_area` VALUES (2231, '兴仁市', 1866, 0);
INSERT INTO `tb_area` VALUES (2232, '普安县', 1866, 0);
INSERT INTO `tb_area` VALUES (2233, '晴隆县', 1866, 0);
INSERT INTO `tb_area` VALUES (2234, '贞丰县', 1866, 0);
INSERT INTO `tb_area` VALUES (2235, '望谟县', 1866, 0);
INSERT INTO `tb_area` VALUES (2236, '册亨县', 1866, 0);
INSERT INTO `tb_area` VALUES (2237, '安龙县', 1866, 0);
INSERT INTO `tb_area` VALUES (2238, '临夏市', 1934, 0);
INSERT INTO `tb_area` VALUES (2239, '临夏县', 1934, 0);
INSERT INTO `tb_area` VALUES (2240, '康乐县', 1934, 0);
INSERT INTO `tb_area` VALUES (2241, '永靖县', 1934, 0);
INSERT INTO `tb_area` VALUES (2242, '广河县', 1934, 0);
INSERT INTO `tb_area` VALUES (2243, '和政县', 1934, 0);
INSERT INTO `tb_area` VALUES (2244, '东乡族自治县', 1934, 0);
INSERT INTO `tb_area` VALUES (2245, '积石山保安族东乡族撒拉族自治县', 1934, 0);
INSERT INTO `tb_area` VALUES (2246, '涪城区', 1933, 0);
INSERT INTO `tb_area` VALUES (2247, '游仙区', 1933, 0);
INSERT INTO `tb_area` VALUES (2248, '安州区', 1933, 0);
INSERT INTO `tb_area` VALUES (2249, '三台县', 1933, 0);
INSERT INTO `tb_area` VALUES (2250, '盐亭县', 1933, 0);
INSERT INTO `tb_area` VALUES (2251, '梓潼县', 1933, 0);
INSERT INTO `tb_area` VALUES (2252, '北川羌族自治县', 1933, 0);
INSERT INTO `tb_area` VALUES (2253, '平武县', 1933, 0);
INSERT INTO `tb_area` VALUES (2254, '江油市', 1933, 0);
INSERT INTO `tb_area` VALUES (2255, '凯里市', 1897, 0);
INSERT INTO `tb_area` VALUES (2256, '黄平县', 1897, 0);
INSERT INTO `tb_area` VALUES (2257, '施秉县', 1897, 0);
INSERT INTO `tb_area` VALUES (2258, '三穗县', 1897, 0);
INSERT INTO `tb_area` VALUES (2259, '镇远县', 1897, 0);
INSERT INTO `tb_area` VALUES (2260, '岑巩县', 1897, 0);
INSERT INTO `tb_area` VALUES (2261, '天柱县', 1897, 0);
INSERT INTO `tb_area` VALUES (2262, '锦屏县', 1897, 0);
INSERT INTO `tb_area` VALUES (2263, '剑河县', 1897, 0);
INSERT INTO `tb_area` VALUES (2264, '台江县', 1897, 0);
INSERT INTO `tb_area` VALUES (2265, '黎平县', 1897, 0);
INSERT INTO `tb_area` VALUES (2266, '榕江县', 1897, 0);
INSERT INTO `tb_area` VALUES (2267, '从江县', 1897, 0);
INSERT INTO `tb_area` VALUES (2268, '雷山县', 1897, 0);
INSERT INTO `tb_area` VALUES (2269, '麻江县', 1897, 0);
INSERT INTO `tb_area` VALUES (2270, '丹寨县', 1897, 0);
INSERT INTO `tb_area` VALUES (2271, '楚雄市', 1896, 0);
INSERT INTO `tb_area` VALUES (2272, '双柏县', 1896, 0);
INSERT INTO `tb_area` VALUES (2273, '牟定县', 1896, 0);
INSERT INTO `tb_area` VALUES (2274, '南华县', 1896, 0);
INSERT INTO `tb_area` VALUES (2275, '姚安县', 1896, 0);
INSERT INTO `tb_area` VALUES (2276, '大姚县', 1896, 0);
INSERT INTO `tb_area` VALUES (2277, '永仁县', 1896, 0);
INSERT INTO `tb_area` VALUES (2278, '元谋县', 1896, 0);
INSERT INTO `tb_area` VALUES (2279, '武定县', 1896, 0);
INSERT INTO `tb_area` VALUES (2280, '禄丰县', 1896, 0);
INSERT INTO `tb_area` VALUES (2281, '临翔区', 1865, 0);
INSERT INTO `tb_area` VALUES (2282, '凤庆县', 1865, 0);
INSERT INTO `tb_area` VALUES (2283, '云县', 1865, 0);
INSERT INTO `tb_area` VALUES (2284, '永德县', 1865, 0);
INSERT INTO `tb_area` VALUES (2285, '镇康县', 1865, 0);
INSERT INTO `tb_area` VALUES (2286, '双江拉祜族佤族布朗族傣族自治县', 1865, 0);
INSERT INTO `tb_area` VALUES (2287, '耿马傣族佤族自治县', 1865, 0);
INSERT INTO `tb_area` VALUES (2288, '沧源佤族自治县', 1865, 0);
INSERT INTO `tb_area` VALUES (2289, '合作市', 1981, 0);
INSERT INTO `tb_area` VALUES (2290, '临潭县', 1981, 0);
INSERT INTO `tb_area` VALUES (2291, '卓尼县', 1981, 0);
INSERT INTO `tb_area` VALUES (2292, '舟曲县', 1981, 0);
INSERT INTO `tb_area` VALUES (2293, '迭部县', 1981, 0);
INSERT INTO `tb_area` VALUES (2294, '玛曲县', 1981, 0);
INSERT INTO `tb_area` VALUES (2295, '碌曲县', 1981, 0);
INSERT INTO `tb_area` VALUES (2296, '夏河县', 1981, 0);
INSERT INTO `tb_area` VALUES (2297, '利州区', 1980, 0);
INSERT INTO `tb_area` VALUES (2298, '昭化区', 1980, 0);
INSERT INTO `tb_area` VALUES (2299, '朝天区', 1980, 0);
INSERT INTO `tb_area` VALUES (2300, '旺苍县', 1980, 0);
INSERT INTO `tb_area` VALUES (2301, '青川县', 1980, 0);
INSERT INTO `tb_area` VALUES (2302, '剑阁县', 1980, 0);
INSERT INTO `tb_area` VALUES (2303, '苍溪县', 1980, 0);
INSERT INTO `tb_area` VALUES (2304, '都匀市', 1936, 0);
INSERT INTO `tb_area` VALUES (2305, '福泉市', 1936, 0);
INSERT INTO `tb_area` VALUES (2306, '荔波县', 1936, 0);
INSERT INTO `tb_area` VALUES (2307, '贵定县', 1936, 0);
INSERT INTO `tb_area` VALUES (2308, '瓮安县', 1936, 0);
INSERT INTO `tb_area` VALUES (2309, '独山县', 1936, 0);
INSERT INTO `tb_area` VALUES (2310, '平塘县', 1936, 0);
INSERT INTO `tb_area` VALUES (2311, '罗甸县', 1936, 0);
INSERT INTO `tb_area` VALUES (2312, '长顺县', 1936, 0);
INSERT INTO `tb_area` VALUES (2313, '龙里县', 1936, 0);
INSERT INTO `tb_area` VALUES (2314, '惠水县', 1936, 0);
INSERT INTO `tb_area` VALUES (2315, '三都水族自治县', 1936, 0);
INSERT INTO `tb_area` VALUES (2316, '船山区', 2005, 0);
INSERT INTO `tb_area` VALUES (2317, '安居区', 2005, 0);
INSERT INTO `tb_area` VALUES (2318, '蓬溪县', 2005, 0);
INSERT INTO `tb_area` VALUES (2319, '射洪县', 2005, 0);
INSERT INTO `tb_area` VALUES (2320, '大英县', 2005, 0);
INSERT INTO `tb_area` VALUES (2321, '文山市', 1982, 0);
INSERT INTO `tb_area` VALUES (2322, '砚山县', 1982, 0);
INSERT INTO `tb_area` VALUES (2323, '西畴县', 1982, 0);
INSERT INTO `tb_area` VALUES (2324, '麻栗坡县', 1982, 0);
INSERT INTO `tb_area` VALUES (2325, '马关县', 1982, 0);
INSERT INTO `tb_area` VALUES (2326, '丘北县', 1982, 0);
INSERT INTO `tb_area` VALUES (2327, '广南县', 1982, 0);
INSERT INTO `tb_area` VALUES (2328, '富宁县', 1982, 0);
INSERT INTO `tb_area` VALUES (2329, '个旧市', 1935, 0);
INSERT INTO `tb_area` VALUES (2330, '开远市', 1935, 0);
INSERT INTO `tb_area` VALUES (2331, '蒙自市', 1935, 0);
INSERT INTO `tb_area` VALUES (2332, '弥勒市', 1935, 0);
INSERT INTO `tb_area` VALUES (2333, '屏边苗族自治县', 1935, 0);
INSERT INTO `tb_area` VALUES (2334, '建水县', 1935, 0);
INSERT INTO `tb_area` VALUES (2335, '石屏县', 1935, 0);
INSERT INTO `tb_area` VALUES (2336, '泸西县', 1935, 0);
INSERT INTO `tb_area` VALUES (2337, '元阳县', 1935, 0);
INSERT INTO `tb_area` VALUES (2338, '红河县', 1935, 0);
INSERT INTO `tb_area` VALUES (2339, '金平苗族瑶族傣族自治县', 1935, 0);
INSERT INTO `tb_area` VALUES (2340, '绿春县', 1935, 0);
INSERT INTO `tb_area` VALUES (2341, '河口瑶族自治县', 1935, 0);
INSERT INTO `tb_area` VALUES (2342, '思茅区', 1841, 0);
INSERT INTO `tb_area` VALUES (2343, '宁洱哈尼族彝族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2344, '墨江哈尼族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2345, '景东彝族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2346, '景谷傣族彝族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2347, '镇沅彝族哈尼族拉祜族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2348, '江城哈尼族彝族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2349, '孟连傣族拉祜族佤族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2350, '澜沧拉祜族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2351, '西盟佤族自治县', 1841, 0);
INSERT INTO `tb_area` VALUES (2352, '石河子市', 1840, 0);
INSERT INTO `tb_area` VALUES (2353, '阿拉尔市', 1840, 0);
INSERT INTO `tb_area` VALUES (2354, '图木舒克市', 1840, 0);
INSERT INTO `tb_area` VALUES (2355, '五家渠市', 1840, 0);
INSERT INTO `tb_area` VALUES (2356, '铁门关市', 1840, 0);
INSERT INTO `tb_area` VALUES (2357, '市中区', 2051, 0);
INSERT INTO `tb_area` VALUES (2358, '东兴区', 2051, 0);
INSERT INTO `tb_area` VALUES (2359, '威远县', 2051, 0);
INSERT INTO `tb_area` VALUES (2360, '资中县', 2051, 0);
INSERT INTO `tb_area` VALUES (2361, '内江经济开发区', 2051, 0);
INSERT INTO `tb_area` VALUES (2362, '隆昌市', 2051, 0);
INSERT INTO `tb_area` VALUES (2363, '景洪市', 2006, 0);
INSERT INTO `tb_area` VALUES (2364, '勐海县', 2006, 0);
INSERT INTO `tb_area` VALUES (2365, '勐腊县', 2006, 0);
INSERT INTO `tb_area` VALUES (2366, '万州区', 1836, 0);
INSERT INTO `tb_area` VALUES (2367, '涪陵区', 1836, 0);
INSERT INTO `tb_area` VALUES (2368, '渝中区', 1836, 0);
INSERT INTO `tb_area` VALUES (2369, '大渡口区', 1836, 0);
INSERT INTO `tb_area` VALUES (2370, '江北区', 1836, 0);
INSERT INTO `tb_area` VALUES (2371, '沙坪坝区', 1836, 0);
INSERT INTO `tb_area` VALUES (2372, '九龙坡区', 1836, 0);
INSERT INTO `tb_area` VALUES (2373, '南岸区', 1836, 0);
INSERT INTO `tb_area` VALUES (2374, '北碚区', 1836, 0);
INSERT INTO `tb_area` VALUES (2375, '綦江区', 1836, 0);
INSERT INTO `tb_area` VALUES (2376, '大足区', 1836, 0);
INSERT INTO `tb_area` VALUES (2377, '渝北区', 1836, 0);
INSERT INTO `tb_area` VALUES (2378, '巴南区', 1836, 0);
INSERT INTO `tb_area` VALUES (2379, '黔江区', 1836, 0);
INSERT INTO `tb_area` VALUES (2380, '长寿区', 1836, 0);
INSERT INTO `tb_area` VALUES (2381, '江津区', 1836, 0);
INSERT INTO `tb_area` VALUES (2382, '合川区', 1836, 0);
INSERT INTO `tb_area` VALUES (2383, '永川区', 1836, 0);
INSERT INTO `tb_area` VALUES (2384, '南川区', 1836, 0);
INSERT INTO `tb_area` VALUES (2385, '璧山区', 1836, 0);
INSERT INTO `tb_area` VALUES (2386, '铜梁区', 1836, 0);
INSERT INTO `tb_area` VALUES (2387, '潼南区', 1836, 0);
INSERT INTO `tb_area` VALUES (2388, '荣昌区', 1836, 0);
INSERT INTO `tb_area` VALUES (2389, '开州区', 1836, 0);
INSERT INTO `tb_area` VALUES (2390, '梁平区', 1836, 0);
INSERT INTO `tb_area` VALUES (2391, '武隆区', 1836, 0);
INSERT INTO `tb_area` VALUES (2392, '西昌市', 2096, 0);
INSERT INTO `tb_area` VALUES (2393, '木里藏族自治县', 2096, 0);
INSERT INTO `tb_area` VALUES (2394, '盐源县', 2096, 0);
INSERT INTO `tb_area` VALUES (2395, '德昌县', 2096, 0);
INSERT INTO `tb_area` VALUES (2396, '会理县', 2096, 0);
INSERT INTO `tb_area` VALUES (2397, '会东县', 2096, 0);
INSERT INTO `tb_area` VALUES (2398, '宁南县', 2096, 0);
INSERT INTO `tb_area` VALUES (2399, '普格县', 2096, 0);
INSERT INTO `tb_area` VALUES (2400, '布拖县', 2096, 0);
INSERT INTO `tb_area` VALUES (2401, '金阳县', 2096, 0);
INSERT INTO `tb_area` VALUES (2402, '昭觉县', 2096, 0);
INSERT INTO `tb_area` VALUES (2403, '喜德县', 2096, 0);
INSERT INTO `tb_area` VALUES (2404, '冕宁县', 2096, 0);
INSERT INTO `tb_area` VALUES (2405, '越西县', 2096, 0);
INSERT INTO `tb_area` VALUES (2406, '甘洛县', 2096, 0);
INSERT INTO `tb_area` VALUES (2407, '美姑县', 2096, 0);
INSERT INTO `tb_area` VALUES (2408, '雷波县', 2096, 0);
INSERT INTO `tb_area` VALUES (2409, '康定市', 2095, 0);
INSERT INTO `tb_area` VALUES (2410, '泸定县', 2095, 0);
INSERT INTO `tb_area` VALUES (2411, '丹巴县', 2095, 0);
INSERT INTO `tb_area` VALUES (2412, '九龙县', 2095, 0);
INSERT INTO `tb_area` VALUES (2413, '雅江县', 2095, 0);
INSERT INTO `tb_area` VALUES (2414, '道孚县', 2095, 0);
INSERT INTO `tb_area` VALUES (2415, '炉霍县', 2095, 0);
INSERT INTO `tb_area` VALUES (2416, '甘孜县', 2095, 0);
INSERT INTO `tb_area` VALUES (2417, '新龙县', 2095, 0);
INSERT INTO `tb_area` VALUES (2418, '德格县', 2095, 0);
INSERT INTO `tb_area` VALUES (2419, '白玉县', 2095, 0);
INSERT INTO `tb_area` VALUES (2420, '石渠县', 2095, 0);
INSERT INTO `tb_area` VALUES (2421, '色达县', 2095, 0);
INSERT INTO `tb_area` VALUES (2422, '理塘县', 2095, 0);
INSERT INTO `tb_area` VALUES (2423, '巴塘县', 2095, 0);
INSERT INTO `tb_area` VALUES (2424, '乡城县', 2095, 0);
INSERT INTO `tb_area` VALUES (2425, '稻城县', 2095, 0);
INSERT INTO `tb_area` VALUES (2426, '得荣县', 2095, 0);
INSERT INTO `tb_area` VALUES (2427, '雁江区', 2093, 0);
INSERT INTO `tb_area` VALUES (2428, '安岳县', 2093, 0);
INSERT INTO `tb_area` VALUES (2429, '乐至县', 2093, 0);
INSERT INTO `tb_area` VALUES (2430, '巴州区', 2092, 0);
INSERT INTO `tb_area` VALUES (2431, '恩阳区', 2092, 0);
INSERT INTO `tb_area` VALUES (2432, '通江县', 2092, 0);
INSERT INTO `tb_area` VALUES (2433, '南江县', 2092, 0);
INSERT INTO `tb_area` VALUES (2434, '平昌县', 2092, 0);
INSERT INTO `tb_area` VALUES (2435, '巴中经济开发区', 2092, 0);
INSERT INTO `tb_area` VALUES (2436, '雨城区', 2091, 0);
INSERT INTO `tb_area` VALUES (2437, '名山区', 2091, 0);
INSERT INTO `tb_area` VALUES (2438, '荥经县', 2091, 0);
INSERT INTO `tb_area` VALUES (2439, '汉源县', 2091, 0);
INSERT INTO `tb_area` VALUES (2440, '石棉县', 2091, 0);
INSERT INTO `tb_area` VALUES (2441, '天全县', 2091, 0);
INSERT INTO `tb_area` VALUES (2442, '芦山县', 2091, 0);
INSERT INTO `tb_area` VALUES (2443, '宝兴县', 2091, 0);
INSERT INTO `tb_area` VALUES (2444, '马尔康市', 2094, 0);
INSERT INTO `tb_area` VALUES (2445, '汶川县', 2094, 0);
INSERT INTO `tb_area` VALUES (2446, '理县', 2094, 0);
INSERT INTO `tb_area` VALUES (2447, '茂县', 2094, 0);
INSERT INTO `tb_area` VALUES (2448, '松潘县', 2094, 0);
INSERT INTO `tb_area` VALUES (2449, '九寨沟县', 2094, 0);
INSERT INTO `tb_area` VALUES (2450, '金川县', 2094, 0);
INSERT INTO `tb_area` VALUES (2451, '小金县', 2094, 0);
INSERT INTO `tb_area` VALUES (2452, '黑水县', 2094, 0);
INSERT INTO `tb_area` VALUES (2453, '壤塘县', 2094, 0);
INSERT INTO `tb_area` VALUES (2454, '阿坝县', 2094, 0);
INSERT INTO `tb_area` VALUES (2455, '若尔盖县', 2094, 0);
INSERT INTO `tb_area` VALUES (2456, '红原县', 2094, 0);
INSERT INTO `tb_area` VALUES (2457, '通川区', 2090, 0);
INSERT INTO `tb_area` VALUES (2458, '达川区', 2090, 0);
INSERT INTO `tb_area` VALUES (2459, '宣汉县', 2090, 0);
INSERT INTO `tb_area` VALUES (2460, '开江县', 2090, 0);
INSERT INTO `tb_area` VALUES (2461, '大竹县', 2090, 0);
INSERT INTO `tb_area` VALUES (2462, '渠县', 2090, 0);
INSERT INTO `tb_area` VALUES (2463, '达州经济开发区', 2090, 0);
INSERT INTO `tb_area` VALUES (2464, '万源市', 2090, 0);
INSERT INTO `tb_area` VALUES (2465, '广安区', 2089, 0);
INSERT INTO `tb_area` VALUES (2466, '前锋区', 2089, 0);
INSERT INTO `tb_area` VALUES (2467, '岳池县', 2089, 0);
INSERT INTO `tb_area` VALUES (2468, '武胜县', 2089, 0);
INSERT INTO `tb_area` VALUES (2469, '邻水县', 2089, 0);
INSERT INTO `tb_area` VALUES (2470, '华蓥市', 2089, 0);
INSERT INTO `tb_area` VALUES (2471, '翠屏区', 2088, 0);
INSERT INTO `tb_area` VALUES (2472, '南溪区', 2088, 0);
INSERT INTO `tb_area` VALUES (2473, '叙州区', 2088, 0);
INSERT INTO `tb_area` VALUES (2474, '江安县', 2088, 0);
INSERT INTO `tb_area` VALUES (2475, '长宁县', 2088, 0);
INSERT INTO `tb_area` VALUES (2476, '高县', 2088, 0);
INSERT INTO `tb_area` VALUES (2477, '珙县', 2088, 0);
INSERT INTO `tb_area` VALUES (2478, '筠连县', 2088, 0);
INSERT INTO `tb_area` VALUES (2479, '兴文县', 2088, 0);
INSERT INTO `tb_area` VALUES (2480, '屏山县', 2088, 0);
INSERT INTO `tb_area` VALUES (2481, '香格里拉市', 2087, 0);
INSERT INTO `tb_area` VALUES (2482, '德钦县', 2087, 0);
INSERT INTO `tb_area` VALUES (2483, '维西傈僳族自治县', 2087, 0);
INSERT INTO `tb_area` VALUES (2484, '东坡区', 2086, 0);
INSERT INTO `tb_area` VALUES (2485, '彭山区', 2086, 0);
INSERT INTO `tb_area` VALUES (2486, '仁寿县', 2086, 0);
INSERT INTO `tb_area` VALUES (2487, '洪雅县', 2086, 0);
INSERT INTO `tb_area` VALUES (2488, '丹棱县', 2086, 0);
INSERT INTO `tb_area` VALUES (2489, '青神县', 2086, 0);
INSERT INTO `tb_area` VALUES (2490, '泸水市', 2085, 0);
INSERT INTO `tb_area` VALUES (2491, '福贡县', 2085, 0);
INSERT INTO `tb_area` VALUES (2492, '贡山独龙族怒族自治县', 2085, 0);
INSERT INTO `tb_area` VALUES (2493, '兰坪白族普米族自治县', 2085, 0);
INSERT INTO `tb_area` VALUES (2494, '顺庆区', 2084, 0);
INSERT INTO `tb_area` VALUES (2495, '高坪区', 2084, 0);
INSERT INTO `tb_area` VALUES (2496, '嘉陵区', 2084, 0);
INSERT INTO `tb_area` VALUES (2497, '南部县', 2084, 0);
INSERT INTO `tb_area` VALUES (2498, '营山县', 2084, 0);
INSERT INTO `tb_area` VALUES (2499, '蓬安县', 2084, 0);
INSERT INTO `tb_area` VALUES (2500, '仪陇县', 2084, 0);
INSERT INTO `tb_area` VALUES (2501, '西充县', 2084, 0);
INSERT INTO `tb_area` VALUES (2502, '阆中市', 2084, 0);
INSERT INTO `tb_area` VALUES (2503, '瑞丽市', 2083, 0);
INSERT INTO `tb_area` VALUES (2504, '芒市', 2083, 0);
INSERT INTO `tb_area` VALUES (2505, '梁河县', 2083, 0);
INSERT INTO `tb_area` VALUES (2506, '盈江县', 2083, 0);
INSERT INTO `tb_area` VALUES (2507, '陇川县', 2083, 0);
INSERT INTO `tb_area` VALUES (2508, '市中区', 2082, 0);
INSERT INTO `tb_area` VALUES (2509, '沙湾区', 2082, 0);
INSERT INTO `tb_area` VALUES (2510, '五通桥区', 2082, 0);
INSERT INTO `tb_area` VALUES (2511, '金口河区', 2082, 0);
INSERT INTO `tb_area` VALUES (2512, '犍为县', 2082, 0);
INSERT INTO `tb_area` VALUES (2513, '井研县', 2082, 0);
INSERT INTO `tb_area` VALUES (2514, '夹江县', 2082, 0);
INSERT INTO `tb_area` VALUES (2515, '沐川县', 2082, 0);
INSERT INTO `tb_area` VALUES (2516, '峨边彝族自治县', 2082, 0);
INSERT INTO `tb_area` VALUES (2517, '马边彝族自治县', 2082, 0);
INSERT INTO `tb_area` VALUES (2518, '峨眉山市', 2082, 0);
INSERT INTO `tb_area` VALUES (2519, '大理市', 2052, 0);
INSERT INTO `tb_area` VALUES (2520, '漾濞彝族自治县', 2052, 0);
INSERT INTO `tb_area` VALUES (2521, '祥云县', 2052, 0);
INSERT INTO `tb_area` VALUES (2522, '宾川县', 2052, 0);
INSERT INTO `tb_area` VALUES (2523, '弥渡县', 2052, 0);
INSERT INTO `tb_area` VALUES (2524, '南涧彝族自治县', 2052, 0);
INSERT INTO `tb_area` VALUES (2525, '巍山彝族回族自治县', 2052, 0);
INSERT INTO `tb_area` VALUES (2526, '永平县', 2052, 0);
INSERT INTO `tb_area` VALUES (2527, '云龙县', 2052, 0);
INSERT INTO `tb_area` VALUES (2528, '洱源县', 2052, 0);
INSERT INTO `tb_area` VALUES (2529, '剑川县', 2052, 0);
INSERT INTO `tb_area` VALUES (2530, '鹤庆县', 2052, 0);
INSERT INTO `tb_area` VALUES (2531, '七星关区', 1808, 0);
INSERT INTO `tb_area` VALUES (2532, '大方县', 1808, 0);
INSERT INTO `tb_area` VALUES (2533, '黔西县', 1808, 0);
INSERT INTO `tb_area` VALUES (2534, '金沙县', 1808, 0);
INSERT INTO `tb_area` VALUES (2535, '织金县', 1808, 0);
INSERT INTO `tb_area` VALUES (2536, '纳雍县', 1808, 0);
INSERT INTO `tb_area` VALUES (2537, '威宁彝族回族苗族自治县', 1808, 0);
INSERT INTO `tb_area` VALUES (2538, '赫章县', 1808, 0);
INSERT INTO `tb_area` VALUES (2539, '古城区', 1807, 0);
INSERT INTO `tb_area` VALUES (2540, '玉龙纳西族自治县', 1807, 0);
INSERT INTO `tb_area` VALUES (2541, '永胜县', 1807, 0);
INSERT INTO `tb_area` VALUES (2542, '华坪县', 1807, 0);
INSERT INTO `tb_area` VALUES (2543, '宁蒗彝族自治县', 1807, 0);
INSERT INTO `tb_area` VALUES (2544, '阿勒泰市', 1806, 0);
INSERT INTO `tb_area` VALUES (2545, '布尔津县', 1806, 0);
INSERT INTO `tb_area` VALUES (2546, '富蕴县', 1806, 0);
INSERT INTO `tb_area` VALUES (2547, '福海县', 1806, 0);
INSERT INTO `tb_area` VALUES (2548, '哈巴河县', 1806, 0);
INSERT INTO `tb_area` VALUES (2549, '青河县', 1806, 0);
INSERT INTO `tb_area` VALUES (2550, '吉木乃县', 1806, 0);
INSERT INTO `tb_area` VALUES (2551, '西秀区', 1788, 0);
INSERT INTO `tb_area` VALUES (2552, '平坝区', 1788, 0);
INSERT INTO `tb_area` VALUES (2553, '普定县', 1788, 0);
INSERT INTO `tb_area` VALUES (2554, '镇宁布依族苗族自治县', 1788, 0);
INSERT INTO `tb_area` VALUES (2555, '关岭布依族苗族自治县', 1788, 0);
INSERT INTO `tb_area` VALUES (2556, '紫云苗族布依族自治县', 1788, 0);
INSERT INTO `tb_area` VALUES (2557, '昭阳区', 1787, 0);
INSERT INTO `tb_area` VALUES (2558, '鲁甸县', 1787, 0);
INSERT INTO `tb_area` VALUES (2559, '巧家县', 1787, 0);
INSERT INTO `tb_area` VALUES (2560, '盐津县', 1787, 0);
INSERT INTO `tb_area` VALUES (2561, '大关县', 1787, 0);
INSERT INTO `tb_area` VALUES (2562, '永善县', 1787, 0);
INSERT INTO `tb_area` VALUES (2563, '绥江县', 1787, 0);
INSERT INTO `tb_area` VALUES (2564, '镇雄县', 1787, 0);
INSERT INTO `tb_area` VALUES (2565, '彝良县', 1787, 0);
INSERT INTO `tb_area` VALUES (2566, '威信县', 1787, 0);
INSERT INTO `tb_area` VALUES (2567, '水富市', 1787, 0);
INSERT INTO `tb_area` VALUES (2568, '塔城市', 1786, 0);
INSERT INTO `tb_area` VALUES (2569, '乌苏市', 1786, 0);
INSERT INTO `tb_area` VALUES (2570, '额敏县', 1786, 0);
INSERT INTO `tb_area` VALUES (2571, '沙湾县', 1786, 0);
INSERT INTO `tb_area` VALUES (2572, '托里县', 1786, 0);
INSERT INTO `tb_area` VALUES (2573, '裕民县', 1786, 0);
INSERT INTO `tb_area` VALUES (2574, '和布克赛尔蒙古自治县', 1786, 0);
INSERT INTO `tb_area` VALUES (2575, '红花岗区', 1756, 0);
INSERT INTO `tb_area` VALUES (2576, '汇川区', 1756, 0);
INSERT INTO `tb_area` VALUES (2577, '播州区', 1756, 0);
INSERT INTO `tb_area` VALUES (2578, '桐梓县', 1756, 0);
INSERT INTO `tb_area` VALUES (2579, '绥阳县', 1756, 0);
INSERT INTO `tb_area` VALUES (2580, '正安县', 1756, 0);
INSERT INTO `tb_area` VALUES (2581, '道真仡佬族苗族自治县', 1756, 0);
INSERT INTO `tb_area` VALUES (2582, '务川仡佬族苗族自治县', 1756, 0);
INSERT INTO `tb_area` VALUES (2583, '凤冈县', 1756, 0);
INSERT INTO `tb_area` VALUES (2584, '湄潭县', 1756, 0);
INSERT INTO `tb_area` VALUES (2585, '余庆县', 1756, 0);
INSERT INTO `tb_area` VALUES (2586, '习水县', 1756, 0);
INSERT INTO `tb_area` VALUES (2587, '赤水市', 1756, 0);
INSERT INTO `tb_area` VALUES (2588, '仁怀市', 1756, 0);
INSERT INTO `tb_area` VALUES (2589, '隆阳区', 1755, 0);
INSERT INTO `tb_area` VALUES (2590, '施甸县', 1755, 0);
INSERT INTO `tb_area` VALUES (2591, '龙陵县', 1755, 0);
INSERT INTO `tb_area` VALUES (2592, '昌宁县', 1755, 0);
INSERT INTO `tb_area` VALUES (2593, '腾冲市', 1755, 0);
INSERT INTO `tb_area` VALUES (2594, '伊宁市', 1754, 0);
INSERT INTO `tb_area` VALUES (2595, '奎屯市', 1754, 0);
INSERT INTO `tb_area` VALUES (2596, '霍尔果斯市', 1754, 0);
INSERT INTO `tb_area` VALUES (2597, '伊宁县', 1754, 0);
INSERT INTO `tb_area` VALUES (2598, '察布查尔锡伯自治县', 1754, 0);
INSERT INTO `tb_area` VALUES (2599, '霍城县', 1754, 0);
INSERT INTO `tb_area` VALUES (2600, '巩留县', 1754, 0);
INSERT INTO `tb_area` VALUES (2601, '新源县', 1754, 0);
INSERT INTO `tb_area` VALUES (2602, '昭苏县', 1754, 0);
INSERT INTO `tb_area` VALUES (2603, '特克斯县', 1754, 0);
INSERT INTO `tb_area` VALUES (2604, '尼勒克县', 1754, 0);
INSERT INTO `tb_area` VALUES (2605, '钟山区', 1735, 0);
INSERT INTO `tb_area` VALUES (2606, '六枝特区', 1735, 0);
INSERT INTO `tb_area` VALUES (2607, '水城县', 1735, 0);
INSERT INTO `tb_area` VALUES (2608, '盘州市', 1735, 0);
INSERT INTO `tb_area` VALUES (2609, '红塔区', 1734, 0);
INSERT INTO `tb_area` VALUES (2610, '江川区', 1734, 0);
INSERT INTO `tb_area` VALUES (2611, '澄江县', 1734, 0);
INSERT INTO `tb_area` VALUES (2612, '通海县', 1734, 0);
INSERT INTO `tb_area` VALUES (2613, '华宁县', 1734, 0);
INSERT INTO `tb_area` VALUES (2614, '易门县', 1734, 0);
INSERT INTO `tb_area` VALUES (2615, '峨山彝族自治县', 1734, 0);
INSERT INTO `tb_area` VALUES (2616, '新平彝族傣族自治县', 1734, 0);
INSERT INTO `tb_area` VALUES (2617, '元江哈尼族彝族傣族自治县', 1734, 0);
INSERT INTO `tb_area` VALUES (2618, '和田市', 1733, 0);
INSERT INTO `tb_area` VALUES (2619, '和田县', 1733, 0);
INSERT INTO `tb_area` VALUES (2620, '墨玉县', 1733, 0);
INSERT INTO `tb_area` VALUES (2621, '皮山县', 1733, 0);
INSERT INTO `tb_area` VALUES (2622, '洛浦县', 1733, 0);
INSERT INTO `tb_area` VALUES (2623, '策勒县', 1733, 0);
INSERT INTO `tb_area` VALUES (2624, '于田县', 1733, 0);
INSERT INTO `tb_area` VALUES (2625, '民丰县', 1733, 0);
INSERT INTO `tb_area` VALUES (2626, '南明区', 1691, 0);
INSERT INTO `tb_area` VALUES (2627, '云岩区', 1691, 0);
INSERT INTO `tb_area` VALUES (2628, '花溪区', 1691, 0);
INSERT INTO `tb_area` VALUES (2629, '乌当区', 1691, 0);
INSERT INTO `tb_area` VALUES (2630, '白云区', 1691, 0);
INSERT INTO `tb_area` VALUES (2631, '观山湖区', 1691, 0);
INSERT INTO `tb_area` VALUES (2632, '开阳县', 1691, 0);
INSERT INTO `tb_area` VALUES (2633, '息烽县', 1691, 0);
INSERT INTO `tb_area` VALUES (2634, '修文县', 1691, 0);
INSERT INTO `tb_area` VALUES (2635, '清镇市', 1691, 0);
INSERT INTO `tb_area` VALUES (2636, '麒麟区', 1690, 0);
INSERT INTO `tb_area` VALUES (2637, '沾益区', 1690, 0);
INSERT INTO `tb_area` VALUES (2638, '马龙区', 1690, 0);
INSERT INTO `tb_area` VALUES (2639, '陆良县', 1690, 0);
INSERT INTO `tb_area` VALUES (2640, '师宗县', 1690, 0);
INSERT INTO `tb_area` VALUES (2641, '罗平县', 1690, 0);
INSERT INTO `tb_area` VALUES (2642, '富源县', 1690, 0);
INSERT INTO `tb_area` VALUES (2643, '会泽县', 1690, 0);
INSERT INTO `tb_area` VALUES (2644, '宣威市', 1690, 0);
INSERT INTO `tb_area` VALUES (2645, '喀什市', 1689, 0);
INSERT INTO `tb_area` VALUES (2646, '疏附县', 1689, 0);
INSERT INTO `tb_area` VALUES (2647, '疏勒县', 1689, 0);
INSERT INTO `tb_area` VALUES (2648, '英吉沙县', 1689, 0);
INSERT INTO `tb_area` VALUES (2649, '泽普县', 1689, 0);
INSERT INTO `tb_area` VALUES (2650, '莎车县', 1689, 0);
INSERT INTO `tb_area` VALUES (2651, '叶城县', 1689, 0);
INSERT INTO `tb_area` VALUES (2652, '麦盖提县', 1689, 0);
INSERT INTO `tb_area` VALUES (2653, '岳普湖县', 1689, 0);
INSERT INTO `tb_area` VALUES (2654, '伽师县', 1689, 0);
INSERT INTO `tb_area` VALUES (2655, '巴楚县', 1689, 0);
INSERT INTO `tb_area` VALUES (2656, '塔什库尔干塔吉克自治县', 1689, 0);
INSERT INTO `tb_area` VALUES (2657, '五华区', 1660, 0);
INSERT INTO `tb_area` VALUES (2658, '盘龙区', 1660, 0);
INSERT INTO `tb_area` VALUES (2659, '官渡区', 1660, 0);
INSERT INTO `tb_area` VALUES (2660, '西山区', 1660, 0);
INSERT INTO `tb_area` VALUES (2661, '东川区', 1660, 0);
INSERT INTO `tb_area` VALUES (2662, '呈贡区', 1660, 0);
INSERT INTO `tb_area` VALUES (2663, '晋宁区', 1660, 0);
INSERT INTO `tb_area` VALUES (2664, '富民县', 1660, 0);
INSERT INTO `tb_area` VALUES (2665, '宜良县', 1660, 0);
INSERT INTO `tb_area` VALUES (2666, '石林彝族自治县', 1660, 0);
INSERT INTO `tb_area` VALUES (2667, '嵩明县', 1660, 0);
INSERT INTO `tb_area` VALUES (2668, '禄劝彝族苗族自治县', 1660, 0);
INSERT INTO `tb_area` VALUES (2669, '寻甸回族彝族自治县', 1660, 0);
INSERT INTO `tb_area` VALUES (2670, '安宁市', 1660, 0);
INSERT INTO `tb_area` VALUES (2671, '阿图什市', 1659, 0);
INSERT INTO `tb_area` VALUES (2672, '阿克陶县', 1659, 0);
INSERT INTO `tb_area` VALUES (2673, '阿合奇县', 1659, 0);
INSERT INTO `tb_area` VALUES (2674, '乌恰县', 1659, 0);
INSERT INTO `tb_area` VALUES (2675, '阿克苏市', 1619, 0);
INSERT INTO `tb_area` VALUES (2676, '温宿县', 1619, 0);
INSERT INTO `tb_area` VALUES (2677, '库车县', 1619, 0);
INSERT INTO `tb_area` VALUES (2678, '沙雅县', 1619, 0);
INSERT INTO `tb_area` VALUES (2679, '新和县', 1619, 0);
INSERT INTO `tb_area` VALUES (2680, '拜城县', 1619, 0);
INSERT INTO `tb_area` VALUES (2681, '乌什县', 1619, 0);
INSERT INTO `tb_area` VALUES (2682, '阿瓦提县', 1619, 0);
INSERT INTO `tb_area` VALUES (2683, '柯坪县', 1619, 0);
INSERT INTO `tb_area` VALUES (2684, '沙坡头区', 1579, 0);
INSERT INTO `tb_area` VALUES (2685, '中宁县', 1579, 0);
INSERT INTO `tb_area` VALUES (2686, '海原县', 1579, 0);
INSERT INTO `tb_area` VALUES (2687, '库尔勒市', 1578, 0);
INSERT INTO `tb_area` VALUES (2688, '轮台县', 1578, 0);
INSERT INTO `tb_area` VALUES (2689, '尉犁县', 1578, 0);
INSERT INTO `tb_area` VALUES (2690, '若羌县', 1578, 0);
INSERT INTO `tb_area` VALUES (2691, '且末县', 1578, 0);
INSERT INTO `tb_area` VALUES (2692, '焉耆回族自治县', 1578, 0);
INSERT INTO `tb_area` VALUES (2693, '和静县', 1578, 0);
INSERT INTO `tb_area` VALUES (2694, '和硕县', 1578, 0);
INSERT INTO `tb_area` VALUES (2695, '博湖县', 1578, 0);
INSERT INTO `tb_area` VALUES (2696, '库尔勒经济技术开发区', 1578, 0);
INSERT INTO `tb_area` VALUES (2697, '博乐市', 1555, 0);
INSERT INTO `tb_area` VALUES (2698, '阿拉山口市', 1555, 0);
INSERT INTO `tb_area` VALUES (2699, '精河县', 1555, 0);
INSERT INTO `tb_area` VALUES (2700, '温泉县', 1555, 0);
INSERT INTO `tb_area` VALUES (2701, '海州区', 459, 0);
INSERT INTO `tb_area` VALUES (2702, '新邱区', 459, 0);
INSERT INTO `tb_area` VALUES (2703, '太平区', 459, 0);
INSERT INTO `tb_area` VALUES (2704, '清河门区', 459, 0);
INSERT INTO `tb_area` VALUES (2705, '细河区', 459, 0);
INSERT INTO `tb_area` VALUES (2706, '阜新蒙古族自治县', 459, 0);
INSERT INTO `tb_area` VALUES (2707, '彰武县', 459, 0);
INSERT INTO `tb_area` VALUES (2708, '吴兴区', 458, 0);
INSERT INTO `tb_area` VALUES (2709, '南浔区', 458, 0);
INSERT INTO `tb_area` VALUES (2710, '德清县', 458, 0);
INSERT INTO `tb_area` VALUES (2711, '长兴县', 458, 0);
INSERT INTO `tb_area` VALUES (2712, '安吉县', 458, 0);
INSERT INTO `tb_area` VALUES (2713, '花山区', 457, 0);
INSERT INTO `tb_area` VALUES (2714, '雨山区', 457, 0);
INSERT INTO `tb_area` VALUES (2715, '博望区', 457, 0);
INSERT INTO `tb_area` VALUES (2716, '当涂县', 457, 0);
INSERT INTO `tb_area` VALUES (2717, '含山县', 457, 0);
INSERT INTO `tb_area` VALUES (2718, '和县', 457, 0);
INSERT INTO `tb_area` VALUES (2719, '城厢区', 456, 0);
INSERT INTO `tb_area` VALUES (2720, '涵江区', 456, 0);
INSERT INTO `tb_area` VALUES (2721, '荔城区', 456, 0);
INSERT INTO `tb_area` VALUES (2722, '秀屿区', 456, 0);
INSERT INTO `tb_area` VALUES (2723, '仙游县', 456, 0);
INSERT INTO `tb_area` VALUES (2724, '大通区', 425, 0);
INSERT INTO `tb_area` VALUES (2725, '田家庵区', 425, 0);
INSERT INTO `tb_area` VALUES (2726, '谢家集区', 425, 0);
INSERT INTO `tb_area` VALUES (2727, '八公山区', 425, 0);
INSERT INTO `tb_area` VALUES (2728, '潘集区', 425, 0);
INSERT INTO `tb_area` VALUES (2729, '凤台县', 425, 0);
INSERT INTO `tb_area` VALUES (2730, '寿县', 425, 0);
INSERT INTO `tb_area` VALUES (2731, '思明区', 424, 0);
INSERT INTO `tb_area` VALUES (2732, '海沧区', 424, 0);
INSERT INTO `tb_area` VALUES (2733, '湖里区', 424, 0);
INSERT INTO `tb_area` VALUES (2734, '集美区', 424, 0);
INSERT INTO `tb_area` VALUES (2735, '同安区', 424, 0);
INSERT INTO `tb_area` VALUES (2736, '翔安区', 424, 0);
INSERT INTO `tb_area` VALUES (2737, '尧都区', 373, 0);
INSERT INTO `tb_area` VALUES (2738, '曲沃县', 373, 0);
INSERT INTO `tb_area` VALUES (2739, '翼城县', 373, 0);
INSERT INTO `tb_area` VALUES (2740, '襄汾县', 373, 0);
INSERT INTO `tb_area` VALUES (2741, '洪洞县', 373, 0);
INSERT INTO `tb_area` VALUES (2742, '古县', 373, 0);
INSERT INTO `tb_area` VALUES (2743, '安泽县', 373, 0);
INSERT INTO `tb_area` VALUES (2744, '浮山县', 373, 0);
INSERT INTO `tb_area` VALUES (2745, '吉县', 373, 0);
INSERT INTO `tb_area` VALUES (2746, '乡宁县', 373, 0);
INSERT INTO `tb_area` VALUES (2747, '大宁县', 373, 0);
INSERT INTO `tb_area` VALUES (2748, '隰县', 373, 0);
INSERT INTO `tb_area` VALUES (2749, '永和县', 373, 0);
INSERT INTO `tb_area` VALUES (2750, '蒲县', 373, 0);
INSERT INTO `tb_area` VALUES (2751, '汾西县', 373, 0);
INSERT INTO `tb_area` VALUES (2752, '侯马市', 373, 0);
INSERT INTO `tb_area` VALUES (2753, '霍州市', 373, 0);
INSERT INTO `tb_area` VALUES (2754, '东湖区', 455, 0);
INSERT INTO `tb_area` VALUES (2755, '西湖区', 455, 0);
INSERT INTO `tb_area` VALUES (2756, '青云谱区', 455, 0);
INSERT INTO `tb_area` VALUES (2757, '湾里区', 455, 0);
INSERT INTO `tb_area` VALUES (2758, '青山湖区', 455, 0);
INSERT INTO `tb_area` VALUES (2759, '新建区', 455, 0);
INSERT INTO `tb_area` VALUES (2760, '南昌县', 455, 0);
INSERT INTO `tb_area` VALUES (2761, '安义县', 455, 0);
INSERT INTO `tb_area` VALUES (2762, '进贤县', 455, 0);
INSERT INTO `tb_area` VALUES (2763, '离石区', 434, 0);
INSERT INTO `tb_area` VALUES (2764, '文水县', 434, 0);
INSERT INTO `tb_area` VALUES (2765, '交城县', 434, 0);
INSERT INTO `tb_area` VALUES (2766, '兴县', 434, 0);
INSERT INTO `tb_area` VALUES (2767, '临县', 434, 0);
INSERT INTO `tb_area` VALUES (2768, '柳林县', 434, 0);
INSERT INTO `tb_area` VALUES (2769, '石楼县', 434, 0);
INSERT INTO `tb_area` VALUES (2770, '岚县', 434, 0);
INSERT INTO `tb_area` VALUES (2771, '方山县', 434, 0);
INSERT INTO `tb_area` VALUES (2772, '中阳县', 434, 0);
INSERT INTO `tb_area` VALUES (2773, '交口县', 434, 0);
INSERT INTO `tb_area` VALUES (2774, '孝义市', 434, 0);
INSERT INTO `tb_area` VALUES (2775, '汾阳市', 434, 0);
INSERT INTO `tb_area` VALUES (2776, '二连浩特市', 372, 0);
INSERT INTO `tb_area` VALUES (2777, '锡林浩特市', 372, 0);
INSERT INTO `tb_area` VALUES (2778, '阿巴嘎旗', 372, 0);
INSERT INTO `tb_area` VALUES (2779, '苏尼特左旗', 372, 0);
INSERT INTO `tb_area` VALUES (2780, '苏尼特右旗', 372, 0);
INSERT INTO `tb_area` VALUES (2781, '东乌珠穆沁旗', 372, 0);
INSERT INTO `tb_area` VALUES (2782, '西乌珠穆沁旗', 372, 0);
INSERT INTO `tb_area` VALUES (2783, '太仆寺旗', 372, 0);
INSERT INTO `tb_area` VALUES (2784, '镶黄旗', 372, 0);
INSERT INTO `tb_area` VALUES (2785, '正镶白旗', 372, 0);
INSERT INTO `tb_area` VALUES (2786, '正蓝旗', 372, 0);
INSERT INTO `tb_area` VALUES (2787, '多伦县', 372, 0);
INSERT INTO `tb_area` VALUES (2788, '乌拉盖管委会', 372, 0);
INSERT INTO `tb_area` VALUES (2789, '龙子湖区', 364, 0);
INSERT INTO `tb_area` VALUES (2790, '蚌山区', 364, 0);
INSERT INTO `tb_area` VALUES (2791, '禹会区', 364, 0);
INSERT INTO `tb_area` VALUES (2792, '淮上区', 364, 0);
INSERT INTO `tb_area` VALUES (2793, '怀远县', 364, 0);
INSERT INTO `tb_area` VALUES (2794, '五河县', 364, 0);
INSERT INTO `tb_area` VALUES (2795, '固镇县', 364, 0);
INSERT INTO `tb_area` VALUES (2796, '蚌埠市高新技术开发区', 364, 0);
INSERT INTO `tb_area` VALUES (2797, '蚌埠市经济开发区', 364, 0);
INSERT INTO `tb_area` VALUES (2798, '阿拉善左旗', 433, 0);
INSERT INTO `tb_area` VALUES (2799, '阿拉善右旗', 433, 0);
INSERT INTO `tb_area` VALUES (2800, '额济纳旗', 433, 0);
INSERT INTO `tb_area` VALUES (2801, '内蒙古阿拉善经济开发区', 433, 0);
INSERT INTO `tb_area` VALUES (2802, '洮北区', 428, 0);
INSERT INTO `tb_area` VALUES (2803, '镇赉县', 428, 0);
INSERT INTO `tb_area` VALUES (2804, '通榆县', 428, 0);
INSERT INTO `tb_area` VALUES (2805, '吉林白城经济开发区', 428, 0);
INSERT INTO `tb_area` VALUES (2806, '洮南市', 428, 0);
INSERT INTO `tb_area` VALUES (2807, '大安市', 428, 0);
INSERT INTO `tb_area` VALUES (2808, '站前区', 427, 0);
INSERT INTO `tb_area` VALUES (2809, '西市区', 427, 0);
INSERT INTO `tb_area` VALUES (2810, '鲅鱼圈区', 427, 0);
INSERT INTO `tb_area` VALUES (2811, '老边区', 427, 0);
INSERT INTO `tb_area` VALUES (2812, '盖州市', 427, 0);
INSERT INTO `tb_area` VALUES (2813, '大石桥市', 427, 0);
INSERT INTO `tb_area` VALUES (2814, '南湖区', 426, 0);
INSERT INTO `tb_area` VALUES (2815, '秀洲区', 426, 0);
INSERT INTO `tb_area` VALUES (2816, '嘉善县', 426, 0);
INSERT INTO `tb_area` VALUES (2817, '海盐县', 426, 0);
INSERT INTO `tb_area` VALUES (2818, '海宁市', 426, 0);
INSERT INTO `tb_area` VALUES (2819, '平湖市', 426, 0);
INSERT INTO `tb_area` VALUES (2820, '桐乡市', 426, 0);
INSERT INTO `tb_area` VALUES (2821, '海口市', 432, 1);
INSERT INTO `tb_area` VALUES (2822, '鼓楼区', 363, 0);
INSERT INTO `tb_area` VALUES (2823, '台江区', 363, 0);
INSERT INTO `tb_area` VALUES (2824, '仓山区', 363, 0);
INSERT INTO `tb_area` VALUES (2825, '马尾区', 363, 0);
INSERT INTO `tb_area` VALUES (2826, '晋安区', 363, 0);
INSERT INTO `tb_area` VALUES (2827, '长乐区', 363, 0);
INSERT INTO `tb_area` VALUES (2828, '闽侯县', 363, 0);
INSERT INTO `tb_area` VALUES (2829, '连江县', 363, 0);
INSERT INTO `tb_area` VALUES (2830, '罗源县', 363, 0);
INSERT INTO `tb_area` VALUES (2831, '闽清县', 363, 0);
INSERT INTO `tb_area` VALUES (2832, '永泰县', 363, 0);
INSERT INTO `tb_area` VALUES (2833, '平潭县', 363, 0);
INSERT INTO `tb_area` VALUES (2834, '福清市', 363, 0);
INSERT INTO `tb_area` VALUES (2835, '三亚市', 432, 1);
INSERT INTO `tb_area` VALUES (2836, '海曙区', 321, 0);
INSERT INTO `tb_area` VALUES (2837, '江北区', 321, 0);
INSERT INTO `tb_area` VALUES (2838, '北仑区', 321, 0);
INSERT INTO `tb_area` VALUES (2839, '镇海区', 321, 0);
INSERT INTO `tb_area` VALUES (2840, '鄞州区', 321, 0);
INSERT INTO `tb_area` VALUES (2841, '奉化区', 321, 0);
INSERT INTO `tb_area` VALUES (2842, '象山县', 321, 0);
INSERT INTO `tb_area` VALUES (2843, '宁海县', 321, 0);
INSERT INTO `tb_area` VALUES (2844, '余姚市', 321, 0);
INSERT INTO `tb_area` VALUES (2845, '慈溪市', 321, 0);
INSERT INTO `tb_area` VALUES (2846, '三沙市', 432, 1);
INSERT INTO `tb_area` VALUES (2847, '忻府区', 329, 0);
INSERT INTO `tb_area` VALUES (2848, '定襄县', 329, 0);
INSERT INTO `tb_area` VALUES (2849, '五台县', 329, 0);
INSERT INTO `tb_area` VALUES (2850, '代县', 329, 0);
INSERT INTO `tb_area` VALUES (2851, '繁峙县', 329, 0);
INSERT INTO `tb_area` VALUES (2852, '宁武县', 329, 0);
INSERT INTO `tb_area` VALUES (2853, '静乐县', 329, 0);
INSERT INTO `tb_area` VALUES (2854, '神池县', 329, 0);
INSERT INTO `tb_area` VALUES (2855, '五寨县', 329, 0);
INSERT INTO `tb_area` VALUES (2856, '岢岚县', 329, 0);
INSERT INTO `tb_area` VALUES (2857, '河曲县', 329, 0);
INSERT INTO `tb_area` VALUES (2858, '保德县', 329, 0);
INSERT INTO `tb_area` VALUES (2859, '偏关县', 329, 0);
INSERT INTO `tb_area` VALUES (2860, '五台山风景名胜区', 329, 0);
INSERT INTO `tb_area` VALUES (2861, '原平市', 329, 0);
INSERT INTO `tb_area` VALUES (2862, '乌兰浩特市', 328, 0);
INSERT INTO `tb_area` VALUES (2863, '阿尔山市', 328, 0);
INSERT INTO `tb_area` VALUES (2864, '科尔沁右翼前旗', 328, 0);
INSERT INTO `tb_area` VALUES (2865, '科尔沁右翼中旗', 328, 0);
INSERT INTO `tb_area` VALUES (2866, '扎赉特旗', 328, 0);
INSERT INTO `tb_area` VALUES (2867, '突泉县', 328, 0);
INSERT INTO `tb_area` VALUES (2868, '浑江区', 323, 0);
INSERT INTO `tb_area` VALUES (2869, '江源区', 323, 0);
INSERT INTO `tb_area` VALUES (2870, '抚松县', 323, 0);
INSERT INTO `tb_area` VALUES (2871, '靖宇县', 323, 0);
INSERT INTO `tb_area` VALUES (2872, '长白朝鲜族自治县', 323, 0);
INSERT INTO `tb_area` VALUES (2873, '临江市', 323, 0);
INSERT INTO `tb_area` VALUES (2874, '元宝区', 322, 0);
INSERT INTO `tb_area` VALUES (2875, '振兴区', 322, 0);
INSERT INTO `tb_area` VALUES (2876, '振安区', 322, 0);
INSERT INTO `tb_area` VALUES (2877, '宽甸满族自治县', 322, 0);
INSERT INTO `tb_area` VALUES (2878, '东港市', 322, 0);
INSERT INTO `tb_area` VALUES (2879, '凤城市', 322, 0);
INSERT INTO `tb_area` VALUES (2880, '儋州市', 432, 1);
INSERT INTO `tb_area` VALUES (2881, '南宁市', 371, 1);
INSERT INTO `tb_area` VALUES (2882, '广州市', 327, 1);
INSERT INTO `tb_area` VALUES (2883, '镜湖区', 320, 0);
INSERT INTO `tb_area` VALUES (2884, '弋江区', 320, 0);
INSERT INTO `tb_area` VALUES (2885, '鸠江区', 320, 0);
INSERT INTO `tb_area` VALUES (2886, '三山区', 320, 0);
INSERT INTO `tb_area` VALUES (2887, '芜湖县', 320, 0);
INSERT INTO `tb_area` VALUES (2888, '繁昌县', 320, 0);
INSERT INTO `tb_area` VALUES (2889, '南陵县', 320, 0);
INSERT INTO `tb_area` VALUES (2890, '无为县', 320, 0);
INSERT INTO `tb_area` VALUES (2891, '芜湖经济技术开发区', 320, 0);
INSERT INTO `tb_area` VALUES (2892, '安徽芜湖长江大桥经济开发区', 320, 0);
INSERT INTO `tb_area` VALUES (2893, '鹿城区', 365, 0);
INSERT INTO `tb_area` VALUES (2894, '龙湾区', 365, 0);
INSERT INTO `tb_area` VALUES (2895, '瓯海区', 365, 0);
INSERT INTO `tb_area` VALUES (2896, '洞头区', 365, 0);
INSERT INTO `tb_area` VALUES (2897, '永嘉县', 365, 0);
INSERT INTO `tb_area` VALUES (2898, '平阳县', 365, 0);
INSERT INTO `tb_area` VALUES (2899, '苍南县', 365, 0);
INSERT INTO `tb_area` VALUES (2900, '文成县', 365, 0);
INSERT INTO `tb_area` VALUES (2901, '泰顺县', 365, 0);
INSERT INTO `tb_area` VALUES (2902, '温州经济技术开发区', 365, 0);
INSERT INTO `tb_area` VALUES (2903, '瑞安市', 365, 0);
INSERT INTO `tb_area` VALUES (2904, '乐清市', 365, 0);
INSERT INTO `tb_area` VALUES (2905, '省直辖县级行政区划', 432, 1);
INSERT INTO `tb_area` VALUES (2906, '柳州市', 371, 1);
INSERT INTO `tb_area` VALUES (2907, '韶关市', 327, 1);
INSERT INTO `tb_area` VALUES (2908, '盐湖区', 273, 0);
INSERT INTO `tb_area` VALUES (2909, '临猗县', 273, 0);
INSERT INTO `tb_area` VALUES (2910, '万荣县', 273, 0);
INSERT INTO `tb_area` VALUES (2911, '闻喜县', 273, 0);
INSERT INTO `tb_area` VALUES (2912, '稷山县', 273, 0);
INSERT INTO `tb_area` VALUES (2913, '新绛县', 273, 0);
INSERT INTO `tb_area` VALUES (2914, '绛县', 273, 0);
INSERT INTO `tb_area` VALUES (2915, '垣曲县', 273, 0);
INSERT INTO `tb_area` VALUES (2916, '夏县', 273, 0);
INSERT INTO `tb_area` VALUES (2917, '平陆县', 273, 0);
INSERT INTO `tb_area` VALUES (2918, '芮城县', 273, 0);
INSERT INTO `tb_area` VALUES (2919, '永济市', 273, 0);
INSERT INTO `tb_area` VALUES (2920, '河津市', 273, 0);
INSERT INTO `tb_area` VALUES (2921, '集宁区', 272, 0);
INSERT INTO `tb_area` VALUES (2922, '卓资县', 272, 0);
INSERT INTO `tb_area` VALUES (2923, '化德县', 272, 0);
INSERT INTO `tb_area` VALUES (2924, '商都县', 272, 0);
INSERT INTO `tb_area` VALUES (2925, '兴和县', 272, 0);
INSERT INTO `tb_area` VALUES (2926, '凉城县', 272, 0);
INSERT INTO `tb_area` VALUES (2927, '察哈尔右翼前旗', 272, 0);
INSERT INTO `tb_area` VALUES (2928, '察哈尔右翼中旗', 272, 0);
INSERT INTO `tb_area` VALUES (2929, '察哈尔右翼后旗', 272, 0);
INSERT INTO `tb_area` VALUES (2930, '四子王旗', 272, 0);
INSERT INTO `tb_area` VALUES (2931, '丰镇市', 272, 0);
INSERT INTO `tb_area` VALUES (2932, '秀英区', 2821, 0);
INSERT INTO `tb_area` VALUES (2933, '龙华区', 2821, 0);
INSERT INTO `tb_area` VALUES (2934, '琼山区', 2821, 0);
INSERT INTO `tb_area` VALUES (2935, '美兰区', 2821, 0);
INSERT INTO `tb_area` VALUES (2936, '海棠区', 2835, 0);
INSERT INTO `tb_area` VALUES (2937, '吉阳区', 2835, 0);
INSERT INTO `tb_area` VALUES (2938, '天涯区', 2835, 0);
INSERT INTO `tb_area` VALUES (2939, '崖州区', 2835, 0);
INSERT INTO `tb_area` VALUES (2940, '桂林市', 371, 1);
INSERT INTO `tb_area` VALUES (2941, '深圳市', 327, 1);
INSERT INTO `tb_area` VALUES (2942, '西沙群岛', 2846, 0);
INSERT INTO `tb_area` VALUES (2943, '南沙群岛', 2846, 0);
INSERT INTO `tb_area` VALUES (2944, '中沙群岛的岛礁及其海域', 2846, 0);
INSERT INTO `tb_area` VALUES (2945, '长沙市', 271, 1);
INSERT INTO `tb_area` VALUES (2946, '梧州市', 371, 1);
INSERT INTO `tb_area` VALUES (2947, '珠海市', 327, 1);
INSERT INTO `tb_area` VALUES (2948, '荔湾区', 2882, 0);
INSERT INTO `tb_area` VALUES (2949, '越秀区', 2882, 0);
INSERT INTO `tb_area` VALUES (2950, '海珠区', 2882, 0);
INSERT INTO `tb_area` VALUES (2951, '天河区', 2882, 0);
INSERT INTO `tb_area` VALUES (2952, '白云区', 2882, 0);
INSERT INTO `tb_area` VALUES (2953, '黄埔区', 2882, 0);
INSERT INTO `tb_area` VALUES (2954, '番禺区', 2882, 0);
INSERT INTO `tb_area` VALUES (2955, '花都区', 2882, 0);
INSERT INTO `tb_area` VALUES (2956, '南沙区', 2882, 0);
INSERT INTO `tb_area` VALUES (2957, '从化区', 2882, 0);
INSERT INTO `tb_area` VALUES (2958, '增城区', 2882, 0);
INSERT INTO `tb_area` VALUES (2959, '兴宁区', 2881, 0);
INSERT INTO `tb_area` VALUES (2960, '青秀区', 2881, 0);
INSERT INTO `tb_area` VALUES (2961, '江南区', 2881, 0);
INSERT INTO `tb_area` VALUES (2962, '西乡塘区', 2881, 0);
INSERT INTO `tb_area` VALUES (2963, '良庆区', 2881, 0);
INSERT INTO `tb_area` VALUES (2964, '邕宁区', 2881, 0);
INSERT INTO `tb_area` VALUES (2965, '武鸣区', 2881, 0);
INSERT INTO `tb_area` VALUES (2966, '隆安县', 2881, 0);
INSERT INTO `tb_area` VALUES (2967, '马山县', 2881, 0);
INSERT INTO `tb_area` VALUES (2968, '上林县', 2881, 0);
INSERT INTO `tb_area` VALUES (2969, '宾阳县', 2881, 0);
INSERT INTO `tb_area` VALUES (2970, '横县', 2881, 0);
INSERT INTO `tb_area` VALUES (2971, '株洲市', 271, 1);
INSERT INTO `tb_area` VALUES (2972, '北海市', 371, 1);
INSERT INTO `tb_area` VALUES (2973, '汕头市', 327, 1);
INSERT INTO `tb_area` VALUES (2974, '武江区', 2907, 0);
INSERT INTO `tb_area` VALUES (2975, '浈江区', 2907, 0);
INSERT INTO `tb_area` VALUES (2976, '曲江区', 2907, 0);
INSERT INTO `tb_area` VALUES (2977, '始兴县', 2907, 0);
INSERT INTO `tb_area` VALUES (2978, '仁化县', 2907, 0);
INSERT INTO `tb_area` VALUES (2979, '翁源县', 2907, 0);
INSERT INTO `tb_area` VALUES (2980, '乳源瑶族自治县', 2907, 0);
INSERT INTO `tb_area` VALUES (2981, '新丰县', 2907, 0);
INSERT INTO `tb_area` VALUES (2982, '乐昌市', 2907, 0);
INSERT INTO `tb_area` VALUES (2983, '南雄市', 2907, 0);
INSERT INTO `tb_area` VALUES (2984, '城中区', 2906, 0);
INSERT INTO `tb_area` VALUES (2985, '鱼峰区', 2906, 0);
INSERT INTO `tb_area` VALUES (2986, '柳南区', 2906, 0);
INSERT INTO `tb_area` VALUES (2987, '柳北区', 2906, 0);
INSERT INTO `tb_area` VALUES (2988, '柳江区', 2906, 0);
INSERT INTO `tb_area` VALUES (2989, '柳城县', 2906, 0);
INSERT INTO `tb_area` VALUES (2990, '鹿寨县', 2906, 0);
INSERT INTO `tb_area` VALUES (2991, '融安县', 2906, 0);
INSERT INTO `tb_area` VALUES (2992, '融水苗族自治县', 2906, 0);
INSERT INTO `tb_area` VALUES (2993, '三江侗族自治县', 2906, 0);
INSERT INTO `tb_area` VALUES (2994, '五指山市', 2905, 0);
INSERT INTO `tb_area` VALUES (2995, '琼海市', 2905, 0);
INSERT INTO `tb_area` VALUES (2996, '文昌市', 2905, 0);
INSERT INTO `tb_area` VALUES (2997, '万宁市', 2905, 0);
INSERT INTO `tb_area` VALUES (2998, '东方市', 2905, 0);
INSERT INTO `tb_area` VALUES (2999, '定安县', 2905, 0);
INSERT INTO `tb_area` VALUES (3000, '屯昌县', 2905, 0);
INSERT INTO `tb_area` VALUES (3001, '澄迈县', 2905, 0);
INSERT INTO `tb_area` VALUES (3002, '临高县', 2905, 0);
INSERT INTO `tb_area` VALUES (3003, '白沙黎族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3004, '昌江黎族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3005, '乐东黎族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3006, '陵水黎族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3007, '保亭黎族苗族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3008, '琼中黎族苗族自治县', 2905, 0);
INSERT INTO `tb_area` VALUES (3009, '湘潭市', 271, 1);
INSERT INTO `tb_area` VALUES (3010, '防城港市', 371, 1);
INSERT INTO `tb_area` VALUES (3011, '佛山市', 327, 1);
INSERT INTO `tb_area` VALUES (3012, '秀峰区', 2940, 0);
INSERT INTO `tb_area` VALUES (3013, '叠彩区', 2940, 0);
INSERT INTO `tb_area` VALUES (3014, '象山区', 2940, 0);
INSERT INTO `tb_area` VALUES (3015, '七星区', 2940, 0);
INSERT INTO `tb_area` VALUES (3016, '雁山区', 2940, 0);
INSERT INTO `tb_area` VALUES (3017, '临桂区', 2940, 0);
INSERT INTO `tb_area` VALUES (3018, '阳朔县', 2940, 0);
INSERT INTO `tb_area` VALUES (3019, '灵川县', 2940, 0);
INSERT INTO `tb_area` VALUES (3020, '全州县', 2940, 0);
INSERT INTO `tb_area` VALUES (3021, '兴安县', 2940, 0);
INSERT INTO `tb_area` VALUES (3022, '永福县', 2940, 0);
INSERT INTO `tb_area` VALUES (3023, '灌阳县', 2940, 0);
INSERT INTO `tb_area` VALUES (3024, '龙胜各族自治县', 2940, 0);
INSERT INTO `tb_area` VALUES (3025, '资源县', 2940, 0);
INSERT INTO `tb_area` VALUES (3026, '平乐县', 2940, 0);
INSERT INTO `tb_area` VALUES (3027, '恭城瑶族自治县', 2940, 0);
INSERT INTO `tb_area` VALUES (3028, '荔浦市', 2940, 0);
INSERT INTO `tb_area` VALUES (3029, '芙蓉区', 2945, 0);
INSERT INTO `tb_area` VALUES (3030, '天心区', 2945, 0);
INSERT INTO `tb_area` VALUES (3031, '岳麓区', 2945, 0);
INSERT INTO `tb_area` VALUES (3032, '开福区', 2945, 0);
INSERT INTO `tb_area` VALUES (3033, '雨花区', 2945, 0);
INSERT INTO `tb_area` VALUES (3034, '望城区', 2945, 0);
INSERT INTO `tb_area` VALUES (3035, '长沙县', 2945, 0);
INSERT INTO `tb_area` VALUES (3036, '浏阳市', 2945, 0);
INSERT INTO `tb_area` VALUES (3037, '宁乡市', 2945, 0);
INSERT INTO `tb_area` VALUES (3038, '罗湖区', 2941, 0);
INSERT INTO `tb_area` VALUES (3039, '福田区', 2941, 0);
INSERT INTO `tb_area` VALUES (3040, '南山区', 2941, 0);
INSERT INTO `tb_area` VALUES (3041, '宝安区', 2941, 0);
INSERT INTO `tb_area` VALUES (3042, '龙岗区', 2941, 0);
INSERT INTO `tb_area` VALUES (3043, '盐田区', 2941, 0);
INSERT INTO `tb_area` VALUES (3044, '龙华区', 2941, 0);
INSERT INTO `tb_area` VALUES (3045, '坪山区', 2941, 0);
INSERT INTO `tb_area` VALUES (3046, '光明区', 2941, 0);
INSERT INTO `tb_area` VALUES (3047, '衡阳市', 271, 1);
INSERT INTO `tb_area` VALUES (3048, '钦州市', 371, 1);
INSERT INTO `tb_area` VALUES (3049, '江门市', 327, 1);
INSERT INTO `tb_area` VALUES (3050, '荷塘区', 2971, 0);
INSERT INTO `tb_area` VALUES (3051, '芦淞区', 2971, 0);
INSERT INTO `tb_area` VALUES (3052, '石峰区', 2971, 0);
INSERT INTO `tb_area` VALUES (3053, '天元区', 2971, 0);
INSERT INTO `tb_area` VALUES (3054, '渌口区', 2971, 0);
INSERT INTO `tb_area` VALUES (3055, '攸县', 2971, 0);
INSERT INTO `tb_area` VALUES (3056, '茶陵县', 2971, 0);
INSERT INTO `tb_area` VALUES (3057, '炎陵县', 2971, 0);
INSERT INTO `tb_area` VALUES (3058, '云龙示范区', 2971, 0);
INSERT INTO `tb_area` VALUES (3059, '醴陵市', 2971, 0);
INSERT INTO `tb_area` VALUES (3060, '万秀区', 2946, 0);
INSERT INTO `tb_area` VALUES (3061, '长洲区', 2946, 0);
INSERT INTO `tb_area` VALUES (3062, '龙圩区', 2946, 0);
INSERT INTO `tb_area` VALUES (3063, '苍梧县', 2946, 0);
INSERT INTO `tb_area` VALUES (3064, '藤县', 2946, 0);
INSERT INTO `tb_area` VALUES (3065, '蒙山县', 2946, 0);
INSERT INTO `tb_area` VALUES (3066, '岑溪市', 2946, 0);
INSERT INTO `tb_area` VALUES (3067, '香洲区', 2947, 0);
INSERT INTO `tb_area` VALUES (3068, '斗门区', 2947, 0);
INSERT INTO `tb_area` VALUES (3069, '金湾区', 2947, 0);
INSERT INTO `tb_area` VALUES (3070, '邵阳市', 271, 1);
INSERT INTO `tb_area` VALUES (3071, '贵港市', 371, 1);
INSERT INTO `tb_area` VALUES (3072, '湛江市', 327, 1);
INSERT INTO `tb_area` VALUES (3073, '海城区', 2972, 0);
INSERT INTO `tb_area` VALUES (3074, '银海区', 2972, 0);
INSERT INTO `tb_area` VALUES (3075, '铁山港区', 2972, 0);
INSERT INTO `tb_area` VALUES (3076, '合浦县', 2972, 0);
INSERT INTO `tb_area` VALUES (3077, '雨湖区', 3009, 0);
INSERT INTO `tb_area` VALUES (3078, '岳塘区', 3009, 0);
INSERT INTO `tb_area` VALUES (3079, '湘潭县', 3009, 0);
INSERT INTO `tb_area` VALUES (3080, '湖南湘潭高新技术产业园区', 3009, 0);
INSERT INTO `tb_area` VALUES (3081, '湘潭昭山示范区', 3009, 0);
INSERT INTO `tb_area` VALUES (3082, '湘潭九华示范区', 3009, 0);
INSERT INTO `tb_area` VALUES (3083, '湘乡市', 3009, 0);
INSERT INTO `tb_area` VALUES (3084, '韶山市', 3009, 0);
INSERT INTO `tb_area` VALUES (3085, '龙湖区', 2973, 0);
INSERT INTO `tb_area` VALUES (3086, '金平区', 2973, 0);
INSERT INTO `tb_area` VALUES (3087, '濠江区', 2973, 0);
INSERT INTO `tb_area` VALUES (3088, '潮阳区', 2973, 0);
INSERT INTO `tb_area` VALUES (3089, '潮南区', 2973, 0);
INSERT INTO `tb_area` VALUES (3090, '澄海区', 2973, 0);
INSERT INTO `tb_area` VALUES (3091, '南澳县', 2973, 0);
INSERT INTO `tb_area` VALUES (3092, '岳阳市', 271, 1);
INSERT INTO `tb_area` VALUES (3093, '玉林市', 371, 1);
INSERT INTO `tb_area` VALUES (3094, '茂名市', 327, 1);
INSERT INTO `tb_area` VALUES (3095, '港口区', 3010, 0);
INSERT INTO `tb_area` VALUES (3096, '防城区', 3010, 0);
INSERT INTO `tb_area` VALUES (3097, '上思县', 3010, 0);
INSERT INTO `tb_area` VALUES (3098, '东兴市', 3010, 0);
INSERT INTO `tb_area` VALUES (3099, '珠晖区', 3047, 0);
INSERT INTO `tb_area` VALUES (3100, '雁峰区', 3047, 0);
INSERT INTO `tb_area` VALUES (3101, '石鼓区', 3047, 0);
INSERT INTO `tb_area` VALUES (3102, '蒸湘区', 3047, 0);
INSERT INTO `tb_area` VALUES (3103, '南岳区', 3047, 0);
INSERT INTO `tb_area` VALUES (3104, '衡阳县', 3047, 0);
INSERT INTO `tb_area` VALUES (3105, '衡南县', 3047, 0);
INSERT INTO `tb_area` VALUES (3106, '衡山县', 3047, 0);
INSERT INTO `tb_area` VALUES (3107, '衡东县', 3047, 0);
INSERT INTO `tb_area` VALUES (3108, '祁东县', 3047, 0);
INSERT INTO `tb_area` VALUES (3109, '衡阳综合保税区', 3047, 0);
INSERT INTO `tb_area` VALUES (3110, '湖南衡阳高新技术产业园区', 3047, 0);
INSERT INTO `tb_area` VALUES (3111, '湖南衡阳松木经济开发区', 3047, 0);
INSERT INTO `tb_area` VALUES (3112, '耒阳市', 3047, 0);
INSERT INTO `tb_area` VALUES (3113, '常宁市', 3047, 0);
INSERT INTO `tb_area` VALUES (3114, '禅城区', 3011, 0);
INSERT INTO `tb_area` VALUES (3115, '南海区', 3011, 0);
INSERT INTO `tb_area` VALUES (3116, '顺德区', 3011, 0);
INSERT INTO `tb_area` VALUES (3117, '三水区', 3011, 0);
INSERT INTO `tb_area` VALUES (3118, '高明区', 3011, 0);
INSERT INTO `tb_area` VALUES (3119, '常德市', 271, 1);
INSERT INTO `tb_area` VALUES (3120, '百色市', 371, 1);
INSERT INTO `tb_area` VALUES (3121, '肇庆市', 327, 1);
INSERT INTO `tb_area` VALUES (3122, '钦南区', 3048, 0);
INSERT INTO `tb_area` VALUES (3123, '钦北区', 3048, 0);
INSERT INTO `tb_area` VALUES (3124, '灵山县', 3048, 0);
INSERT INTO `tb_area` VALUES (3125, '浦北县', 3048, 0);
INSERT INTO `tb_area` VALUES (3126, '双清区', 3070, 0);
INSERT INTO `tb_area` VALUES (3127, '大祥区', 3070, 0);
INSERT INTO `tb_area` VALUES (3128, '北塔区', 3070, 0);
INSERT INTO `tb_area` VALUES (3129, '邵东县', 3070, 0);
INSERT INTO `tb_area` VALUES (3130, '新邵县', 3070, 0);
INSERT INTO `tb_area` VALUES (3131, '邵阳县', 3070, 0);
INSERT INTO `tb_area` VALUES (3132, '隆回县', 3070, 0);
INSERT INTO `tb_area` VALUES (3133, '洞口县', 3070, 0);
INSERT INTO `tb_area` VALUES (3134, '绥宁县', 3070, 0);
INSERT INTO `tb_area` VALUES (3135, '新宁县', 3070, 0);
INSERT INTO `tb_area` VALUES (3136, '城步苗族自治县', 3070, 0);
INSERT INTO `tb_area` VALUES (3137, '武冈市', 3070, 0);
INSERT INTO `tb_area` VALUES (3138, '蓬江区', 3049, 0);
INSERT INTO `tb_area` VALUES (3139, '江海区', 3049, 0);
INSERT INTO `tb_area` VALUES (3140, '新会区', 3049, 0);
INSERT INTO `tb_area` VALUES (3141, '台山市', 3049, 0);
INSERT INTO `tb_area` VALUES (3142, '开平市', 3049, 0);
INSERT INTO `tb_area` VALUES (3143, '鹤山市', 3049, 0);
INSERT INTO `tb_area` VALUES (3144, '恩平市', 3049, 0);
INSERT INTO `tb_area` VALUES (3145, '张家界市', 271, 1);
INSERT INTO `tb_area` VALUES (3146, '贺州市', 371, 1);
INSERT INTO `tb_area` VALUES (3147, '惠州市', 327, 1);
INSERT INTO `tb_area` VALUES (3148, '港北区', 3071, 0);
INSERT INTO `tb_area` VALUES (3149, '港南区', 3071, 0);
INSERT INTO `tb_area` VALUES (3150, '覃塘区', 3071, 0);
INSERT INTO `tb_area` VALUES (3151, '平南县', 3071, 0);
INSERT INTO `tb_area` VALUES (3152, '桂平市', 3071, 0);
INSERT INTO `tb_area` VALUES (3153, '岳阳楼区', 3092, 0);
INSERT INTO `tb_area` VALUES (3154, '云溪区', 3092, 0);
INSERT INTO `tb_area` VALUES (3155, '君山区', 3092, 0);
INSERT INTO `tb_area` VALUES (3156, '岳阳县', 3092, 0);
INSERT INTO `tb_area` VALUES (3157, '华容县', 3092, 0);
INSERT INTO `tb_area` VALUES (3158, '湘阴县', 3092, 0);
INSERT INTO `tb_area` VALUES (3159, '平江县', 3092, 0);
INSERT INTO `tb_area` VALUES (3160, '岳阳市屈原管理区', 3092, 0);
INSERT INTO `tb_area` VALUES (3161, '汨罗市', 3092, 0);
INSERT INTO `tb_area` VALUES (3162, '临湘市', 3092, 0);
INSERT INTO `tb_area` VALUES (3163, '赤坎区', 3072, 0);
INSERT INTO `tb_area` VALUES (3164, '霞山区', 3072, 0);
INSERT INTO `tb_area` VALUES (3165, '坡头区', 3072, 0);
INSERT INTO `tb_area` VALUES (3166, '麻章区', 3072, 0);
INSERT INTO `tb_area` VALUES (3167, '遂溪县', 3072, 0);
INSERT INTO `tb_area` VALUES (3168, '徐闻县', 3072, 0);
INSERT INTO `tb_area` VALUES (3169, '廉江市', 3072, 0);
INSERT INTO `tb_area` VALUES (3170, '雷州市', 3072, 0);
INSERT INTO `tb_area` VALUES (3171, '吴川市', 3072, 0);
INSERT INTO `tb_area` VALUES (3172, '益阳市', 271, 1);
INSERT INTO `tb_area` VALUES (3173, '河池市', 371, 1);
INSERT INTO `tb_area` VALUES (3174, '梅州市', 327, 1);
INSERT INTO `tb_area` VALUES (3175, '玉州区', 3093, 0);
INSERT INTO `tb_area` VALUES (3176, '福绵区', 3093, 0);
INSERT INTO `tb_area` VALUES (3177, '容县', 3093, 0);
INSERT INTO `tb_area` VALUES (3178, '陆川县', 3093, 0);
INSERT INTO `tb_area` VALUES (3179, '博白县', 3093, 0);
INSERT INTO `tb_area` VALUES (3180, '兴业县', 3093, 0);
INSERT INTO `tb_area` VALUES (3181, '北流市', 3093, 0);
INSERT INTO `tb_area` VALUES (3182, '武陵区', 3119, 0);
INSERT INTO `tb_area` VALUES (3183, '鼎城区', 3119, 0);
INSERT INTO `tb_area` VALUES (3184, '安乡县', 3119, 0);
INSERT INTO `tb_area` VALUES (3185, '汉寿县', 3119, 0);
INSERT INTO `tb_area` VALUES (3186, '澧县', 3119, 0);
INSERT INTO `tb_area` VALUES (3187, '临澧县', 3119, 0);
INSERT INTO `tb_area` VALUES (3188, '桃源县', 3119, 0);
INSERT INTO `tb_area` VALUES (3189, '石门县', 3119, 0);
INSERT INTO `tb_area` VALUES (3190, '常德市西洞庭管理区', 3119, 0);
INSERT INTO `tb_area` VALUES (3191, '津市市', 3119, 0);
INSERT INTO `tb_area` VALUES (3192, '茂南区', 3094, 0);
INSERT INTO `tb_area` VALUES (3193, '电白区', 3094, 0);
INSERT INTO `tb_area` VALUES (3194, '高州市', 3094, 0);
INSERT INTO `tb_area` VALUES (3195, '化州市', 3094, 0);
INSERT INTO `tb_area` VALUES (3196, '信宜市', 3094, 0);
INSERT INTO `tb_area` VALUES (3197, '郴州市', 271, 1);
INSERT INTO `tb_area` VALUES (3198, '来宾市', 371, 1);
INSERT INTO `tb_area` VALUES (3199, '汕尾市', 327, 1);
INSERT INTO `tb_area` VALUES (3200, '右江区', 3120, 0);
INSERT INTO `tb_area` VALUES (3201, '田阳县', 3120, 0);
INSERT INTO `tb_area` VALUES (3202, '田东县', 3120, 0);
INSERT INTO `tb_area` VALUES (3203, '平果县', 3120, 0);
INSERT INTO `tb_area` VALUES (3204, '德保县', 3120, 0);
INSERT INTO `tb_area` VALUES (3205, '那坡县', 3120, 0);
INSERT INTO `tb_area` VALUES (3206, '凌云县', 3120, 0);
INSERT INTO `tb_area` VALUES (3207, '乐业县', 3120, 0);
INSERT INTO `tb_area` VALUES (3208, '田林县', 3120, 0);
INSERT INTO `tb_area` VALUES (3209, '西林县', 3120, 0);
INSERT INTO `tb_area` VALUES (3210, '隆林各族自治县', 3120, 0);
INSERT INTO `tb_area` VALUES (3211, '靖西市', 3120, 0);
INSERT INTO `tb_area` VALUES (3212, '永定区', 3145, 0);
INSERT INTO `tb_area` VALUES (3213, '武陵源区', 3145, 0);
INSERT INTO `tb_area` VALUES (3214, '慈利县', 3145, 0);
INSERT INTO `tb_area` VALUES (3215, '桑植县', 3145, 0);
INSERT INTO `tb_area` VALUES (3216, '端州区', 3121, 0);
INSERT INTO `tb_area` VALUES (3217, '鼎湖区', 3121, 0);
INSERT INTO `tb_area` VALUES (3218, '高要区', 3121, 0);
INSERT INTO `tb_area` VALUES (3219, '广宁县', 3121, 0);
INSERT INTO `tb_area` VALUES (3220, '怀集县', 3121, 0);
INSERT INTO `tb_area` VALUES (3221, '封开县', 3121, 0);
INSERT INTO `tb_area` VALUES (3222, '德庆县', 3121, 0);
INSERT INTO `tb_area` VALUES (3223, '四会市', 3121, 0);
INSERT INTO `tb_area` VALUES (3224, '永州市', 271, 1);
INSERT INTO `tb_area` VALUES (3225, '崇左市', 371, 1);
INSERT INTO `tb_area` VALUES (3226, '河源市', 327, 1);
INSERT INTO `tb_area` VALUES (3227, '八步区', 3146, 0);
INSERT INTO `tb_area` VALUES (3228, '平桂区', 3146, 0);
INSERT INTO `tb_area` VALUES (3229, '昭平县', 3146, 0);
INSERT INTO `tb_area` VALUES (3230, '钟山县', 3146, 0);
INSERT INTO `tb_area` VALUES (3231, '富川瑶族自治县', 3146, 0);
INSERT INTO `tb_area` VALUES (3232, '资阳区', 3172, 0);
INSERT INTO `tb_area` VALUES (3233, '赫山区', 3172, 0);
INSERT INTO `tb_area` VALUES (3234, '南县', 3172, 0);
INSERT INTO `tb_area` VALUES (3235, '桃江县', 3172, 0);
INSERT INTO `tb_area` VALUES (3236, '安化县', 3172, 0);
INSERT INTO `tb_area` VALUES (3237, '益阳市大通湖管理区', 3172, 0);
INSERT INTO `tb_area` VALUES (3238, '湖南益阳高新技术产业园区', 3172, 0);
INSERT INTO `tb_area` VALUES (3239, '沅江市', 3172, 0);
INSERT INTO `tb_area` VALUES (3240, '惠城区', 3147, 0);
INSERT INTO `tb_area` VALUES (3241, '惠阳区', 3147, 0);
INSERT INTO `tb_area` VALUES (3242, '博罗县', 3147, 0);
INSERT INTO `tb_area` VALUES (3243, '惠东县', 3147, 0);
INSERT INTO `tb_area` VALUES (3244, '龙门县', 3147, 0);
INSERT INTO `tb_area` VALUES (3245, '怀化市', 271, 1);
INSERT INTO `tb_area` VALUES (3246, '金城江区', 3173, 0);
INSERT INTO `tb_area` VALUES (3247, '宜州区', 3173, 0);
INSERT INTO `tb_area` VALUES (3248, '南丹县', 3173, 0);
INSERT INTO `tb_area` VALUES (3249, '天峨县', 3173, 0);
INSERT INTO `tb_area` VALUES (3250, '凤山县', 3173, 0);
INSERT INTO `tb_area` VALUES (3251, '东兰县', 3173, 0);
INSERT INTO `tb_area` VALUES (3252, '罗城仫佬族自治县', 3173, 0);
INSERT INTO `tb_area` VALUES (3253, '环江毛南族自治县', 3173, 0);
INSERT INTO `tb_area` VALUES (3254, '巴马瑶族自治县', 3173, 0);
INSERT INTO `tb_area` VALUES (3255, '都安瑶族自治县', 3173, 0);
INSERT INTO `tb_area` VALUES (3256, '大化瑶族自治县', 3173, 0);
INSERT INTO `tb_area` VALUES (3257, '北湖区', 3197, 0);
INSERT INTO `tb_area` VALUES (3258, '苏仙区', 3197, 0);
INSERT INTO `tb_area` VALUES (3259, '桂阳县', 3197, 0);
INSERT INTO `tb_area` VALUES (3260, '宜章县', 3197, 0);
INSERT INTO `tb_area` VALUES (3261, '永兴县', 3197, 0);
INSERT INTO `tb_area` VALUES (3262, '嘉禾县', 3197, 0);
INSERT INTO `tb_area` VALUES (3263, '临武县', 3197, 0);
INSERT INTO `tb_area` VALUES (3264, '汝城县', 3197, 0);
INSERT INTO `tb_area` VALUES (3265, '桂东县', 3197, 0);
INSERT INTO `tb_area` VALUES (3266, '安仁县', 3197, 0);
INSERT INTO `tb_area` VALUES (3267, '资兴市', 3197, 0);
INSERT INTO `tb_area` VALUES (3268, '梅江区', 3174, 0);
INSERT INTO `tb_area` VALUES (3269, '梅县区', 3174, 0);
INSERT INTO `tb_area` VALUES (3270, '大埔县', 3174, 0);
INSERT INTO `tb_area` VALUES (3271, '丰顺县', 3174, 0);
INSERT INTO `tb_area` VALUES (3272, '五华县', 3174, 0);
INSERT INTO `tb_area` VALUES (3273, '平远县', 3174, 0);
INSERT INTO `tb_area` VALUES (3274, '蕉岭县', 3174, 0);
INSERT INTO `tb_area` VALUES (3275, '兴宁市', 3174, 0);
INSERT INTO `tb_area` VALUES (3276, '阳江市', 327, 1);
INSERT INTO `tb_area` VALUES (3277, '娄底市', 271, 1);
INSERT INTO `tb_area` VALUES (3278, '兴宾区', 3198, 0);
INSERT INTO `tb_area` VALUES (3279, '忻城县', 3198, 0);
INSERT INTO `tb_area` VALUES (3280, '象州县', 3198, 0);
INSERT INTO `tb_area` VALUES (3281, '武宣县', 3198, 0);
INSERT INTO `tb_area` VALUES (3282, '金秀瑶族自治县', 3198, 0);
INSERT INTO `tb_area` VALUES (3283, '合山市', 3198, 0);
INSERT INTO `tb_area` VALUES (3284, '零陵区', 3224, 0);
INSERT INTO `tb_area` VALUES (3285, '冷水滩区', 3224, 0);
INSERT INTO `tb_area` VALUES (3286, '祁阳县', 3224, 0);
INSERT INTO `tb_area` VALUES (3287, '东安县', 3224, 0);
INSERT INTO `tb_area` VALUES (3288, '双牌县', 3224, 0);
INSERT INTO `tb_area` VALUES (3289, '道县', 3224, 0);
INSERT INTO `tb_area` VALUES (3290, '江永县', 3224, 0);
INSERT INTO `tb_area` VALUES (3291, '宁远县', 3224, 0);
INSERT INTO `tb_area` VALUES (3292, '蓝山县', 3224, 0);
INSERT INTO `tb_area` VALUES (3293, '新田县', 3224, 0);
INSERT INTO `tb_area` VALUES (3294, '江华瑶族自治县', 3224, 0);
INSERT INTO `tb_area` VALUES (3295, '永州经济技术开发区', 3224, 0);
INSERT INTO `tb_area` VALUES (3296, '永州市金洞管理区', 3224, 0);
INSERT INTO `tb_area` VALUES (3297, '永州市回龙圩管理区', 3224, 0);
INSERT INTO `tb_area` VALUES (3298, '城区', 3199, 0);
INSERT INTO `tb_area` VALUES (3299, '海丰县', 3199, 0);
INSERT INTO `tb_area` VALUES (3300, '陆河县', 3199, 0);
INSERT INTO `tb_area` VALUES (3301, '陆丰市', 3199, 0);
INSERT INTO `tb_area` VALUES (3302, '清远市', 327, 1);
INSERT INTO `tb_area` VALUES (3303, '湘西土家族苗族自治州', 271, 1);
INSERT INTO `tb_area` VALUES (3304, '江州区', 3225, 0);
INSERT INTO `tb_area` VALUES (3305, '扶绥县', 3225, 0);
INSERT INTO `tb_area` VALUES (3306, '宁明县', 3225, 0);
INSERT INTO `tb_area` VALUES (3307, '龙州县', 3225, 0);
INSERT INTO `tb_area` VALUES (3308, '大新县', 3225, 0);
INSERT INTO `tb_area` VALUES (3309, '天等县', 3225, 0);
INSERT INTO `tb_area` VALUES (3310, '凭祥市', 3225, 0);
INSERT INTO `tb_area` VALUES (3311, '鹤城区', 3245, 0);
INSERT INTO `tb_area` VALUES (3312, '中方县', 3245, 0);
INSERT INTO `tb_area` VALUES (3313, '沅陵县', 3245, 0);
INSERT INTO `tb_area` VALUES (3314, '辰溪县', 3245, 0);
INSERT INTO `tb_area` VALUES (3315, '溆浦县', 3245, 0);
INSERT INTO `tb_area` VALUES (3316, '会同县', 3245, 0);
INSERT INTO `tb_area` VALUES (3317, '麻阳苗族自治县', 3245, 0);
INSERT INTO `tb_area` VALUES (3318, '新晃侗族自治县', 3245, 0);
INSERT INTO `tb_area` VALUES (3319, '芷江侗族自治县', 3245, 0);
INSERT INTO `tb_area` VALUES (3320, '靖州苗族侗族自治县', 3245, 0);
INSERT INTO `tb_area` VALUES (3321, '通道侗族自治县', 3245, 0);
INSERT INTO `tb_area` VALUES (3322, '怀化市洪江管理区', 3245, 0);
INSERT INTO `tb_area` VALUES (3323, '洪江市', 3245, 0);
INSERT INTO `tb_area` VALUES (3324, '源城区', 3226, 0);
INSERT INTO `tb_area` VALUES (3325, '紫金县', 3226, 0);
INSERT INTO `tb_area` VALUES (3326, '龙川县', 3226, 0);
INSERT INTO `tb_area` VALUES (3327, '连平县', 3226, 0);
INSERT INTO `tb_area` VALUES (3328, '和平县', 3226, 0);
INSERT INTO `tb_area` VALUES (3329, '东源县', 3226, 0);
INSERT INTO `tb_area` VALUES (3330, '东莞市', 327, 1);
INSERT INTO `tb_area` VALUES (3331, '娄星区', 3277, 0);
INSERT INTO `tb_area` VALUES (3332, '双峰县', 3277, 0);
INSERT INTO `tb_area` VALUES (3333, '新化县', 3277, 0);
INSERT INTO `tb_area` VALUES (3334, '冷水江市', 3277, 0);
INSERT INTO `tb_area` VALUES (3335, '涟源市', 3277, 0);
INSERT INTO `tb_area` VALUES (3336, '江城区', 3276, 0);
INSERT INTO `tb_area` VALUES (3337, '阳东区', 3276, 0);
INSERT INTO `tb_area` VALUES (3338, '阳西县', 3276, 0);
INSERT INTO `tb_area` VALUES (3339, '阳春市', 3276, 0);
INSERT INTO `tb_area` VALUES (3340, '中山市', 327, 1);
INSERT INTO `tb_area` VALUES (3341, '吉首市', 3303, 0);
INSERT INTO `tb_area` VALUES (3342, '泸溪县', 3303, 0);
INSERT INTO `tb_area` VALUES (3343, '凤凰县', 3303, 0);
INSERT INTO `tb_area` VALUES (3344, '花垣县', 3303, 0);
INSERT INTO `tb_area` VALUES (3345, '保靖县', 3303, 0);
INSERT INTO `tb_area` VALUES (3346, '古丈县', 3303, 0);
INSERT INTO `tb_area` VALUES (3347, '永顺县', 3303, 0);
INSERT INTO `tb_area` VALUES (3348, '龙山县', 3303, 0);
INSERT INTO `tb_area` VALUES (3349, '湖南吉首经济开发区', 3303, 0);
INSERT INTO `tb_area` VALUES (3350, '湖南永顺经济开发区', 3303, 0);
INSERT INTO `tb_area` VALUES (3351, '清城区', 3302, 0);
INSERT INTO `tb_area` VALUES (3352, '清新区', 3302, 0);
INSERT INTO `tb_area` VALUES (3353, '佛冈县', 3302, 0);
INSERT INTO `tb_area` VALUES (3354, '阳山县', 3302, 0);
INSERT INTO `tb_area` VALUES (3355, '连山壮族瑶族自治县', 3302, 0);
INSERT INTO `tb_area` VALUES (3356, '连南瑶族自治县', 3302, 0);
INSERT INTO `tb_area` VALUES (3357, '英德市', 3302, 0);
INSERT INTO `tb_area` VALUES (3358, '连州市', 3302, 0);
INSERT INTO `tb_area` VALUES (3359, '潮州市', 327, 1);
INSERT INTO `tb_area` VALUES (3360, '揭阳市', 327, 1);
INSERT INTO `tb_area` VALUES (3361, '云浮市', 327, 1);
INSERT INTO `tb_area` VALUES (3362, '湘桥区', 3359, 0);
INSERT INTO `tb_area` VALUES (3363, '潮安区', 3359, 0);
INSERT INTO `tb_area` VALUES (3364, '饶平县', 3359, 0);
INSERT INTO `tb_area` VALUES (3365, '榕城区', 3360, 0);
INSERT INTO `tb_area` VALUES (3366, '揭东区', 3360, 0);
INSERT INTO `tb_area` VALUES (3367, '揭西县', 3360, 0);
INSERT INTO `tb_area` VALUES (3368, '惠来县', 3360, 0);
INSERT INTO `tb_area` VALUES (3369, '普宁市', 3360, 0);
INSERT INTO `tb_area` VALUES (3370, '云城区', 3361, 0);
INSERT INTO `tb_area` VALUES (3371, '云安区', 3361, 0);
INSERT INTO `tb_area` VALUES (3372, '新兴县', 3361, 0);
INSERT INTO `tb_area` VALUES (3373, '郁南县', 3361, 0);
INSERT INTO `tb_area` VALUES (3374, '罗定市', 3361, 0);

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
-- Table structure for tb_progress
-- ----------------------------
DROP TABLE IF EXISTS `tb_progress`;
CREATE TABLE `tb_progress`  (
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
  `Desccription` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述',
  `AdminType` int(11) NULL DEFAULT NULL COMMENT '管理员类型（0表示超级管理员，1表示普通用户）',
  `Avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '头像',
  `Status` int(11) NULL DEFAULT NULL COMMENT '状态(0表示停用，1表示启用)',
  `CompanyID` int(11) NULL DEFAULT NULL COMMENT '属于哪个公司',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES (1, 'superadmin', 'superadmin', 'pbkdf2:sha256:50000$TjUAzjO2$207c0f3dfed3314e11aff166d6ce48d4ce6e100233229af5f294e65741fe3ac5', '122@qq.com', '1110', '超级管理员', 0, NULL, 1, 0);

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


-- 2019-10-09 添加

CREATE TABLE `csms`.`tb_user_pro`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `uid` int(0) NULL COMMENT '用户ID',
  `pid` int(0) NULL COMMENT '项目ID',
  PRIMARY KEY (`id`),
  CONSTRAINT `user_project` FOREIGN KEY (`uid`) REFERENCES `csms`.`tb_user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_per` FOREIGN KEY (`pid`) REFERENCES `csms`.`tb_project` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE `csms`.`tb_user`
ADD COLUMN `permission` int(11) NULL DEFAULT 1 COMMENT '权限标志位' AFTER `CompanyID`;

ALTER TABLE `csms`.`tb_project`
ADD COLUMN `subcompany` varchar(2048) NULL DEFAULT '[]' COMMENT '分包企业' AFTER `TotalMonth`;


CREATE TABLE `csms`.`tb_bank`  (
  `id` int(0) NOT NULL,
  `name` varchar(255) NULL COMMENT '银行名称',
  `description` varchar(255) NULL COMMENT '银行描述',
  PRIMARY KEY (`id`)
);

-- 已同步到my-aliyun

--2019-10-13

ALTER TABLE `csms`.`tb_company`
ADD COLUMN `OtherInfo` varchar(4096) NULL COMMENT '其他信息' AFTER `url`;

ALTER TABLE `csms`.`tb_company`
MODIFY COLUMN `Phone` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '联系方式' AFTER `Address`;

ALTER TABLE `csms`.`tb_guarantee`
MODIFY COLUMN `Kind` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '保函格式' AFTER `Amount`,
ADD COLUMN `Address` varchar(4096) NULL COMMENT '工程所在地' AFTER `GuaCompany`;


-- 2019-10-14
ALTER TABLE `csms`.`tb_project`
ADD COLUMN `Bank` int(255) NULL COMMENT '银行' AFTER `subcompany`;

ALTER TABLE `csms`.`tb_project`
CHANGE COLUMN `subcompany` `SubCompany` varchar(2048) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '[]' COMMENT '分包企业' AFTER `TotalMonth`;

ALTER TABLE `csms`.`tb_progress`
ADD COLUMN `Connect` varchar(4096) NULL COMMENT '月联系人' AFTER `month`;

ALTER TABLE `csms`.`tb_project`
ADD COLUMN `Account` varchar(255) NULL COMMENT '银行卡账号' AFTER `Bank`;

ALTER TABLE `csms`.`tb_bank`
MODIFY COLUMN `id` int(11) NOT NULL AUTO_INCREMENT FIRST;

ALTER TABLE `csms`.`tb_progress`
ADD COLUMN `Workers` int(255) NULL DEFAULT 0 COMMENT '用工人数' AFTER `Connect`,
ADD COLUMN `ShouldIssues` varchar(255) NULL DEFAULT 0 COMMENT '应发放数' AFTER `Workers`,
ADD COLUMN `RealIssues` varchar(255) NULL DEFAULT 0 COMMENT '实际发放数' AFTER `ShouldIssues`,
ADD COLUMN `Payment` varchar(255) NULL DEFAULT 0 COMMENT '支付款项' AFTER `RealIssues`,
ADD COLUMN `Overdraft` varchar(255) NULL DEFAULT 0 COMMENT '欠款' AFTER `Payment`,
ADD COLUMN `TotalSalary` varchar(255) NULL DEFAULT 0 COMMENT '总工资' AFTER `Overdraft`;

--2019-10-19

ALTER TABLE `csms`.`tb_wage`
MODIFY COLUMN `RPay` float(20, 2) NULL DEFAULT NULL COMMENT '实际到账金额' AFTER `WTime`,
ADD COLUMN `ActualPay` varchar(255) NULL COMMENT '实际支付金额' AFTER `month`;

ALTER TABLE `csms`.`tb_wage`
MODIFY COLUMN `ActualPay` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT 0 COMMENT '实际支付金额' AFTER `month`;

ALTER TABLE `csms`.`tb_wage`
ADD COLUMN `Receipt` varchar(255) NULL COMMENT '银行回单' AFTER `ActualPay`;


-- 2019-10-20

ALTER TABLE `csms`.`tb_guarantee`
ADD COLUMN `CreateUser` int(255) NULL DEFAULT 1 COMMENT '创建人' AFTER `Address`,
ADD CONSTRAINT `create_user_id` FOREIGN KEY (`CreateUser`) REFERENCES `csms`.`tb_user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

alter table tb_guarantee convert to character set utf8;
alter database csms character set utf8;

ALTER TABLE `csms`.`tb_guarantee`
MODIFY COLUMN `Bene` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '受益人' AFTER `Margin`;

-- 删除公司项目索引

ALTER TABLE `csms`.`tb_guarantee`
MODIFY COLUMN `Description` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述' AFTER `DID`;

ALTER TABLE `csms`.`tb_guarantee`
MODIFY COLUMN `CompanyID` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司名称' AFTER `ID`;


ALTER TABLE `csms`.`tb_cguarantee`
MODIFY COLUMN `GID` int(11) UNSIGNED NULL DEFAULT 00000000000 COMMENT '保函ID' AFTER `Pimg`;

-- 2019-10-22
ALTER TABLE `csms`.`tb_laborinfo`
ADD COLUMN `SubCompany` int(255) NULL DEFAULT 0 COMMENT '分包公司ID' AFTER `isFeeStand`;

ALTER TABLE `csms`.`tb_laborinfo`
MODIFY COLUMN `Train` int(255) NULL DEFAULT 0 COMMENT '是否培训如果培训则上传图片' AFTER `Political`;

-- 2019-10-23

ALTER TABLE `csms`.`tb_laborinfo`
DROP COLUMN `UserID`,
ADD COLUMN `UserID` int(11) NULL DEFAULT 1 COMMENT '用户ID' AFTER `SubCompany`;

ALTER TABLE `csms`.`tb_laborinfo`
MODIFY COLUMN `BadRecord` varchar(4096) NULL DEFAULT 0 COMMENT '不良记录' AFTER `Remark`;

ALTER TABLE `csms`.`tb_laborinfo`
ADD COLUMN `TrainPic` varchar(4096) NULL COMMENT '培训图片' AFTER `UserID`;

-- 已同步到阿里云


--2019-11-10
ALTER TABLE `csms`.`tb_progress`
ADD COLUMN `Punches` int(255) NULL DEFAULT 0 COMMENT '打卡数' AFTER `TotalSalary`;


-- 2019-11-12
ALTER TABLE `csms`.`tb_attendance`
ADD COLUMN `aminpos` varchar(255) NULL COMMENT '上午进场' AFTER `day`,
ADD COLUMN `amoutpos` varchar(255) NULL COMMENT '上午出场' AFTER `aminpos`,
ADD COLUMN `pminpos` varchar(255) NULL COMMENT '下午进场' AFTER `amoutpos`,
ADD COLUMN `pmoutpos` varchar(255) NULL COMMENT '下午出场' AFTER `pminpos`;

-- 2019-11-19
CREATE TABLE `csms`.`tb_question`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) NULL COMMENT '问题',
  `answer` varchar(4096) NULL COMMENT '答案',
  `type` int(255) NULL COMMENT '问题类型',
  PRIMARY KEY (`id`)
);

ALTER TABLE `csms`.`tb_question`
MODIFY COLUMN `type` int(255) NULL DEFAULT NULL COMMENT '问题类型(类型从1开始)' AFTER `answer`,
ADD COLUMN `createtime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间' AFTER `type`,
ADD COLUMN `updatetime` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '修改时间' AFTER `createtime`,
ADD COLUMN `updateuser` int(255) NULL COMMENT '修改用户' AFTER `updatetime`;

ALTER TABLE `csms`.`tb_question`
CHANGE COLUMN `question` `Name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '问题' AFTER `id`,
CHANGE COLUMN `answer` `Answer` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '答案' AFTER `Name`,
CHANGE COLUMN `type` `Type` int(255) NULL DEFAULT NULL COMMENT '问题类型(类型从1开始)' AFTER `Answer`,
CHANGE COLUMN `updateuser` `Creator` int(255) NULL DEFAULT NULL COMMENT '修改用户' AFTER `updatetime`;

SET FOREIGN_KEY_CHECKS = 1;

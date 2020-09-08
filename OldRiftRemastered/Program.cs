using Fantome.Libraries.League.Helpers.Structures;
using Fantome.Libraries.League.Helpers.Structures.BucketGrid;
using Fantome.Libraries.League.IO.MapGeometry;
using Fantome.Libraries.League.IO.OBJ;
using Fantome.Libraries.League.IO.WorldGeometry;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Fantome.Libraries.League.Tests
{
    class Program
    {
        static void Main(string[] args)
        {
            OldRiftRemastered2();
        }

        static void OldRiftRemastered2()
        {
            MapGeometry mgeo = new MapGeometry(@"K:\Riot Games\LeagueofLegendsRAW\LeagueofLegendsRAW\Maps\Shipping\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo");
            mgeo.Models.Clear();

            //ModelsForOldRift

            //Layer 1
            OBJFile object1 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room1.obj");
            OBJFile object2 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room2.obj");
            OBJFile object3 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room3.obj");
            OBJFile object4 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room4.obj");
            OBJFile object5 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room5.obj");
            OBJFile object6 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room6.obj");
            OBJFile object7 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room7.obj");
            OBJFile object8 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room8.obj");
            OBJFile object9 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room9.obj");
            OBJFile object10 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room10.obj");
            OBJFile object11 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room11.obj");
            OBJFile object12 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room12.obj");
            OBJFile object13 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room13.obj");
            OBJFile object14 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room14.obj");
            OBJFile object15 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room15.obj");
            OBJFile object16 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room16.obj"); //Chaos_dirt Lanes
            OBJFile object17 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room17.obj");
            OBJFile object18 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room18.obj");
            OBJFile object19 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room19.obj");
            OBJFile object20 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room20.obj");
            OBJFile object21 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room21.obj");
            OBJFile object22 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room22.obj");
            OBJFile object23 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room23.obj");
            OBJFile object24 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room24.obj");
            OBJFile object25 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room25.obj");
            OBJFile object26 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room26.obj");
            OBJFile object27 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room27.obj");
            OBJFile object28 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room28.obj");
            OBJFile object29 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room29.obj");
            OBJFile object30 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room30.obj");
            OBJFile object31 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room31.obj");
            OBJFile object32 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room32.obj");
            OBJFile object33 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room33.obj");
            OBJFile object34 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room34.obj");
            OBJFile object35 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room35.obj");
            OBJFile object36 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room36.obj");
            OBJFile object37 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room37.obj");
            OBJFile object38 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room38.obj");
            OBJFile object39 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room39.obj");
            OBJFile object40 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room40.obj");
            OBJFile object41 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room41.obj");
            OBJFile object42 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room42.obj");
            OBJFile object43 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room43.obj");
            OBJFile object44 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room44.obj");
            OBJFile object45 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room45.obj");
            OBJFile object46 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room46.obj");
            OBJFile object47 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room47.obj");
            OBJFile object48 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room48.obj");
            OBJFile object49 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room49.obj");
            OBJFile object50 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room50.obj"); //SR_Lane_Tile
            OBJFile object51 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room51.obj");
            OBJFile object52 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room52.obj");
            OBJFile object53 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room53.obj");
            OBJFile object54 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room54.obj");
            OBJFile object55 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room55.obj");
            OBJFile object56 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room56.obj");
            OBJFile object57 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room57.obj");
            OBJFile object58 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room58.obj");
            OBJFile object59 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room59.obj");
            OBJFile object60 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room60.obj");
            OBJFile object61 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room61.obj");
            OBJFile object62 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room62.obj");
            OBJFile object63 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room63.obj"); //chaos_dirt River
            OBJFile object64 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room64.obj");
            OBJFile object65 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room65.obj");
            OBJFile object66 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room66.obj");
            OBJFile object67 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room67.obj"); //order_tile_floor Base
            OBJFile object68 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room68.obj");
            OBJFile object69 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room69.obj");
            OBJFile object70 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room70.obj");
            OBJFile object71 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room71.obj");
            OBJFile object72 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room72.obj");
            OBJFile object73 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room73.obj");
            OBJFile object74 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room74.obj");
            OBJFile object75 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room75.obj");
            OBJFile object76 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room76.obj");
            OBJFile object77 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room77.obj");
            OBJFile object78 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room78.obj");
            OBJFile object79 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room79.obj");
            OBJFile object80 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room80.obj");
            OBJFile object81 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room81.obj");
            OBJFile object82 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room82.obj");
            OBJFile object83 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room83.obj");
            OBJFile object84 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room84.obj");
            OBJFile object85 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room85.obj");
            OBJFile object86 = new OBJFile(@"D:\TODO2020\LolFileDownloader\live\lol_game_client\0.0.0.200\LEVELS\Map1\Scene\NVR_OBJ_output_Wooxy\room86.obj");


            //NewInstancesForOldRift
            AddModel(object1, "MapGeo_Instance_0");
            AddModel2(object2, "MapGeo_Instance_1");
            AddModel3(object3, "MapGeo_Instance_2");
            AddModel4(object4, "MapGeo_Instance_3");
            AddModel5(object5, "MapGeo_Instance_4");
            AddModel6(object6, "MapGeo_Instance_5");
            AddModel7(object7, "MapGeo_Instance_6");
            AddModel8(object8, "MapGeo_Instance_7");
            AddModel9(object9, "MapGeo_Instance_8");
            AddModel10(object10, "MapGeo_Instance_9");
            AddModel11(object11, "MapGeo_Instance_10");
            AddModel12(object12, "MapGeo_Instance_11");
            AddModel13(object13, "MapGeo_Instance_12");
            AddModel14(object14, "MapGeo_Instance_13");
            AddModel15(object15, "MapGeo_Instance_14");
            AddModel16(object16, "MapGeo_Instance_15");
            AddModel17(object17, "MapGeo_Instance_16");
            AddModel18(object18, "MapGeo_Instance_17");
            AddModel19(object19, "MapGeo_Instance_18");
            AddModel20(object20, "MapGeo_Instance_19");
            AddModel21(object21, "MapGeo_Instance_20");
            AddModel22(object22, "MapGeo_Instance_21");
            AddModel23(object23, "MapGeo_Instance_22");
            AddModel24(object24, "MapGeo_Instance_23");
            AddModel25(object25, "MapGeo_Instance_24");
            AddModel26(object26, "MapGeo_Instance_25");
            AddModel27(object27, "MapGeo_Instance_26");
            AddModel28(object28, "MapGeo_Instance_27");
            AddModel29(object29, "MapGeo_Instance_28");
            AddModel30(object30, "MapGeo_Instance_29");
            AddModel31(object31, "MapGeo_Instance_30");
            AddModel32(object32, "MapGeo_Instance_31");
            AddModel33(object33, "MapGeo_Instance_32");
            AddModel34(object34, "MapGeo_Instance_33");
            AddModel35(object35, "MapGeo_Instance_34");
            AddModel36(object36, "MapGeo_Instance_35");
            AddModel37(object37, "MapGeo_Instance_36");
            AddModel38(object38, "MapGeo_Instance_37");
            AddModel39(object39, "MapGeo_Instance_38");
            AddModel40(object40, "MapGeo_Instance_39");
            AddModel41(object41, "MapGeo_Instance_40");
            AddModel42(object42, "MapGeo_Instance_41");
            AddModel43(object43, "MapGeo_Instance_42");
            AddModel44(object44, "MapGeo_Instance_43");
            AddModel45(object45, "MapGeo_Instance_44");
            AddModel46(object46, "MapGeo_Instance_45");
            AddModel47(object47, "MapGeo_Instance_46");
            AddModel48(object48, "MapGeo_Instance_47");
            AddModel49(object49, "MapGeo_Instance_48");
            AddModel50(object50, "MapGeo_Instance_49");
            AddModel51(object51, "MapGeo_Instance_50");
            AddModel52(object52, "MapGeo_Instance_51");
            AddModel53(object53, "MapGeo_Instance_52");
            AddModel54(object54, "MapGeo_Instance_53");
            AddModel55(object55, "MapGeo_Instance_54");
            AddModel56(object56, "MapGeo_Instance_55");
            AddModel57(object57, "MapGeo_Instance_56");
            AddModel58(object58, "MapGeo_Instance_57");
            AddModel59(object59, "MapGeo_Instance_58");
            AddModel60(object60, "MapGeo_Instance_59");
            AddModel61(object61, "MapGeo_Instance_60");
            AddModel62(object62, "MapGeo_Instance_61");
            AddModel63(object63, "MapGeo_Instance_62");
            AddModel64(object64, "MapGeo_Instance_63");
            AddModel65(object65, "MapGeo_Instance_64");
            AddModel66(object66, "MapGeo_Instance_65");
            AddModel67(object67, "MapGeo_Instance_66");
            AddModel68(object68, "MapGeo_Instance_67");
            AddModel69(object69, "MapGeo_Instance_68");
            AddModel70(object70, "MapGeo_Instance_69");
            AddModel71(object71, "MapGeo_Instance_70");
            AddModel72(object72, "MapGeo_Instance_71");
            AddModel73(object73, "MapGeo_Instance_72");
            AddModel74(object74, "MapGeo_Instance_73");
            AddModel75(object75, "MapGeo_Instance_74");
            AddModel76(object76, "MapGeo_Instance_75");
            AddModel77(object77, "MapGeo_Instance_76");
            AddModel78(object78, "MapGeo_Instance_77");
            AddModel79(object79, "MapGeo_Instance_78");
            AddModel80(object80, "MapGeo_Instance_79");
            AddModel81(object81, "MapGeo_Instance_80");
            AddModel82(object82, "MapGeo_Instance_81");
            AddModel83(object83, "MapGeo_Instance_82");
            AddModel84(object84, "MapGeo_Instance_83");
            AddModel85(object85, "MapGeo_Instance_84");
            AddModel86(object86, "MapGeo_Instance_85");

            //Write the new Mapgeo File
            mgeo.Write(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo", 11);

            //Layer 1 (Base Layer)
            void AddModel(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room1", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel2(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room2", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel3(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room3", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel4(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room4", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel5(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room5", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel6(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room6", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel7(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room7", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel8(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room8", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel9(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room9", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel10(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room10", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel11(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room11", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                
                mgeo.AddModel(object3);
            }
            void AddModel12(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room12", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel13(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room13", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel14(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room14", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel15(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room15", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel16(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room16", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel17(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room17", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel18(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room18", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel19(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room19", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel20(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room20", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel21(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room21", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel22(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room22", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel23(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room23", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel24(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room24", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel25(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room25", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel26(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room26", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel27(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room27", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel28(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room28", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel29(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room29", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel30(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room30", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel31(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room31", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel32(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room32", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel33(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room33", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel34(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room34", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel35(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room35", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel36(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room36", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel37(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room37", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel38(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room38", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel39(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room39", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel40(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room40", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel41(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room41", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel42(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room42", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel43(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room43", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel44(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room44", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel45(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room45", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel46(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room46", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel47(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room47", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel48(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room48", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel49(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room49", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel50(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room50", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel51(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room51", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel52(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room52", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel53(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room53", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel54(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room54", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel55(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room55", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel56(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room56", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel57(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room57", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel58(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room58", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel59(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room59", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel60(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room60", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel61(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room61", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel62(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room62", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel63(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room63", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel64(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room64", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel65(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room65", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel66(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room66", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel67(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room67", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel68(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room68", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel69(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room69", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel70(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room70", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel71(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room71", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel72(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room72", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel73(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room73", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel74(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room74", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel75(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room75", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel76(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room76", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel77(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room77", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel78(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room78", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel79(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room79", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel80(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room80", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel81(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room81", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel82(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room82", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object2);
            }
            void AddModel83(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room83", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel84(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room84", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel85(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room85", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }
            void AddModel86(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room86", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(object3);
            }


        }

    }
}

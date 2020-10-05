using Fantome.Libraries.League.Helpers.Structures;
using Fantome.Libraries.League.Helpers.Structures.BucketGrid;
using Fantome.Libraries.League.IO.MapGeometry;
using Fantome.Libraries.League.IO.OBJ;
using Fantome.Libraries.League.IO.WorldGeometry;
using ImageMagick;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using SharpGLTF.Geometry.VertexTypes;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace OldRiftRemastered
{
    class Program
    {
        static void Main(string[] args)
        {
          
            Sandbox();
        }

        static void OldRiftRemastered2()
        {
            MapGeometry mgeo = new MapGeometry(@"K:\Riot Games\LeagueofLegendsRAW\LeagueofLegendsRAW\Maps\Shipping\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo");
            mgeo.Models.Clear();

            //ModelsForOldRift

            //Layer 1 (Right now only "All Layers" for testing map)
            OBJFile object1 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room1.obj");
            OBJFile object2 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room2.obj");
            OBJFile object3 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room3.obj");
            OBJFile object4 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room4.obj");
            OBJFile object5 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room5.obj");
            OBJFile object6 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room6.obj");
            OBJFile object7 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room7.obj");
            OBJFile object8 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room8.obj");
            OBJFile object9 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room9.obj");
            OBJFile object10 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room10.obj");
            OBJFile object11 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room11.obj");
            OBJFile object12 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room12.obj");
            OBJFile object13 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room13.obj");
            OBJFile object14 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room14.obj");
            OBJFile object15 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room15.obj");
          //  OBJFile object16 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room16.obj"); //Chaos_dirt Lanes + Jungle
            OBJFile object17 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room17.obj");
            OBJFile object18 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room18.obj");
            OBJFile object19 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room19.obj");
            OBJFile object20 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room20.obj");
            OBJFile object21 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room21.obj");
            OBJFile object22 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room22.obj");
            OBJFile object23 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room23.obj");
            OBJFile object24 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room24.obj");
            OBJFile object25 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room25.obj");
            OBJFile object26 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room26.obj");
            OBJFile object27 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room27.obj");
            OBJFile object28 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room28.obj");
            OBJFile object29 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room29.obj");
            OBJFile object30 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room30.obj");
            OBJFile object31 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room31.obj");
            OBJFile object32 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room32.obj");
            OBJFile object33 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room33.obj");
            OBJFile object34 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room34.obj");
            OBJFile object35 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room35.obj");
            OBJFile object36 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room36.obj");
            OBJFile object37 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room37.obj");
            OBJFile object38 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room38.obj");
            OBJFile object39 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room39.obj");
            OBJFile object40 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room40.obj");
            OBJFile object41 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room41.obj");
            OBJFile object42 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room42.obj");
            OBJFile object43 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room43.obj");
            OBJFile object44 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room44.obj");
            OBJFile object45 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room45.obj");
            OBJFile object46 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room46.obj");
            OBJFile object47 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room47.obj");
            OBJFile object48 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room48.obj");
            OBJFile object49 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room49.obj");
           // OBJFile object50 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room50.obj"); //SR_Lane_Tile Lane
            OBJFile object51 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room51.obj");
            OBJFile object52 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room52.obj");
            OBJFile object53 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room53.obj");
            OBJFile object54 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room54.obj");
            OBJFile object55 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room55.obj");
            OBJFile object56 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room56.obj");
            OBJFile object57 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room57.obj");
            OBJFile object58 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room58.obj");
            OBJFile object59 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room59.obj");
            OBJFile object60 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room60.obj");
            OBJFile object61 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room61.obj");
            OBJFile object62 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room62.obj");
            OBJFile object63 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room63.obj"); //chaos_dirt River
            OBJFile object64 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room64.obj");
            OBJFile object65 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room65.obj");
            OBJFile object66 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room66.obj");
          //  OBJFile object67 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room67.obj"); //order_tile_floor Base
            OBJFile object68 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room68.obj");
            OBJFile object69 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room69.obj");
            OBJFile object70 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room70.obj");
            OBJFile object71 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room71.obj");
            OBJFile object72 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room72.obj");
            OBJFile object73 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room73.obj");
            OBJFile object74 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room74.obj");
            OBJFile object75 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room75.obj");
            OBJFile object76 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room76.obj");
            OBJFile object77 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room77.obj");
            OBJFile object78 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room78.obj");
            OBJFile object79 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room79.obj");
            OBJFile object80 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room80.obj");
            OBJFile object81 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room81.obj");
            OBJFile object82 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room82.obj");
            OBJFile object83 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room83.obj");
            OBJFile object84 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room84.obj");
            OBJFile object85 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room85.obj");
            OBJFile object86 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\room86.obj");

            //BakedTerrain
            OBJFile object87 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain1.obj");
            OBJFile object88 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain2.obj");
            OBJFile object89 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain3.obj");
            OBJFile object90 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain4.obj");
            OBJFile object91 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain5.obj");
            OBJFile object92 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain6.obj");
            OBJFile object93 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain7.obj");
            OBJFile object94 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain8.obj");
            OBJFile object95 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain9.obj");
            OBJFile object96 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain10.obj");
            OBJFile object97 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain11.obj");
            OBJFile object98 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain12.obj");
            OBJFile object99 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain13.obj");
            OBJFile object100 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain14.obj");
            OBJFile object101 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain15.obj");
            OBJFile object102 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain16.obj");
            OBJFile object103 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain17.obj");
            OBJFile object104 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain18.obj");
            OBJFile object105 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain19.obj");
            OBJFile object106 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain20.obj");
            OBJFile object107 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain21.obj");
            OBJFile object108 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain22.obj");
            OBJFile object109 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain23.obj");
            OBJFile object110 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain24.obj");
            OBJFile object111 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain25.obj");
            OBJFile object112 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain26.obj");
            OBJFile object113 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain27.obj");
            OBJFile object114 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain28.obj");
            OBJFile object115 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain29.obj");
            OBJFile object116 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain30.obj");
            OBJFile object117 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain31.obj");
            OBJFile object118 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain32.obj");
            OBJFile object119 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain33.obj");
            OBJFile object120 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain34.obj");
            OBJFile object121 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain35.obj");
            OBJFile object122 = new OBJFile(@"K:\Riot Games\LeagueSkins\OldSummonersRiftRemastered2\Models\terrain36.obj");

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
           // AddModel16(object16, "MapGeo_Instance_15");
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
           // AddModel50(object50, "MapGeo_Instance_49");
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
           // AddModel67(object67, "MapGeo_Instance_66");
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

            //BakedTerrain
            
            AddModel87(object87, "MapGeo_Instance_86");
            AddModel88(object88, "MapGeo_Instance_87");
            AddModel89(object89, "MapGeo_Instance_88");
            AddModel90(object90, "MapGeo_Instance_89");
            AddModel91(object91, "MapGeo_Instance_90");
            AddModel92(object92, "MapGeo_Instance_91");
            AddModel93(object93, "MapGeo_Instance_92");
            AddModel94(object94, "MapGeo_Instance_93");
            AddModel95(object95, "MapGeo_Instance_94");
            AddModel96(object96, "MapGeo_Instance_95");
            AddModel97(object97, "MapGeo_Instance_96");
            AddModel98(object98, "MapGeo_Instance_97");
            AddModel99(object99, "MapGeo_Instance_98");
            AddModel100(object100, "MapGeo_Instance_99");
            AddModel101(object101, "MapGeo_Instance_100");
            AddModel102(object102, "MapGeo_Instance_101");
            AddModel103(object103, "MapGeo_Instance_102");
            AddModel104(object104, "MapGeo_Instance_103");
            AddModel105(object105, "MapGeo_Instance_104");
            AddModel106(object106, "MapGeo_Instance_105");
            AddModel107(object107, "MapGeo_Instance_106");
            AddModel108(object108, "MapGeo_Instance_107");
            AddModel109(object109, "MapGeo_Instance_108");
            AddModel110(object110, "MapGeo_Instance_109");
            AddModel111(object111, "MapGeo_Instance_110");
            AddModel112(object112, "MapGeo_Instance_111");
            AddModel113(object113, "MapGeo_Instance_112");
            AddModel114(object114, "MapGeo_Instance_113");
            AddModel115(object115, "MapGeo_Instance_114");
            AddModel116(object116, "MapGeo_Instance_115");
            AddModel117(object117, "MapGeo_Instance_116");
            AddModel118(object118, "MapGeo_Instance_117");
            AddModel119(object119, "MapGeo_Instance_118");
            AddModel120(object120, "MapGeo_Instance_119");
            AddModel121(object121, "MapGeo_Instance_120");
            AddModel122(object122, "MapGeo_Instance_121");

            //Write the new Mapgeo File. Current Version is 11
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
            //void AddModel16(OBJFile obj, string name)
            //{
            //    (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            //    MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room16", 0, (uint)indices.Count, 0, (uint)vertices.Count);
            //    MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            //    mgeo.AddModel(object3);
            //}
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
            //void AddModel50(OBJFile obj, string name)
            //{
            //    (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            //    MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room50", 0, (uint)indices.Count, 0, (uint)vertices.Count);
            //    MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            //    mgeo.AddModel(object2);
            //}
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
            //void AddModel67(OBJFile obj, string name)
            //{
            //    (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            //    MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/room67", 0, (uint)indices.Count, 0, (uint)vertices.Count);
            //    MapGeometryModel object2 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
            //    mgeo.AddModel(object2);
            //}
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

            //Terrain
            void AddModel87(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked1", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked1.tga"; //testing tga files instead of dds
               // BakedTexture = (1);
                mgeo.AddModel(object3);
            }
            void AddModel88(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked2", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked2.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel89(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked3", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked3.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel90(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked4", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked4.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel91(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked5", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked5.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel92(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked6", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked6.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel93(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked7", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked7.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel94(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked8", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked8.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel95(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked9", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked9.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel96(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked10", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked10.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel97(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked11", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked11.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel98(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked12", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked12.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel99(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked13", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked13.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel100(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked14", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked14.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel101(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked15", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked15.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel102(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked16", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked16.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel103(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked17", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked17.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel104(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked18", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked18.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel105(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked19", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked19.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel106(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked20", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked20.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel107(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked21", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked21.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel108(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked22", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked22.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel109(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked23", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked23.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel110(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked24", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked24.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel111(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked25", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked25.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel112(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked26", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked26.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel113(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked27", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked27.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel114(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked28", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked28.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel115(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked29", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked29.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel116(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked30", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked30.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel117(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked31", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked31.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel118(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked32", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked32.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel119(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked33", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked33.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel120(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked34", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked34.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel121(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked35", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked35.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }
            void AddModel122(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/OldRift/Materials/Default/old_rift_baked36", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel object3 = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                //object3.BakedPaintTexture = "Maps/Kitpieces/Baked/Baked36.tga"; //testing tga files instead of dds
                mgeo.AddModel(object3);
            }


            
            //Layer 2 = Fire (Infernal)
            //Layer 3 = Earth (Mountain)
            //Layer 4 = Water (Ocean)
            //Layer 5 = Wind (Cloud)

        }
        
        static void Sandbox()
        {
        MapGeometry mgeo = new MapGeometry(@"K:\Riot Games\LeagueofLegendsRAW\LeagueofLegendsRAW\Maps\Shipping\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo");
        mgeo.Models.Clear();

        OBJFile sandbox = new OBJFile(@"K:\Riot Games\LeagueSkins\DefaultTestMap\Models\testmap.obj");
        OBJFile decal = new OBJFile(@"K:\Riot Games\LeagueSkins\DefaultTestMap\Models\decal.obj");

        AddModel(sandbox, "MapGeo_Instance_0");
        AddModel2(decal, "MapGeo_Instance_1");

        //Write the new Mapgeo File. Current Version is 11
            mgeo.Write(@"K:\Riot Games\LeagueSkins\DefaultTestMap\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo", 11);

            
            void AddModel(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/SRX/Materials/Default/Sandbox", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel sandbox = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                sandbox.SeparatePointLight = new Vector3(1, 1, 1); //Unknown what it does.
                mgeo.AddModel(sandbox);
            }
            void AddModel2(OBJFile obj, string name)
            {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                MapGeometrySubmesh submesh = new MapGeometrySubmesh("Maps/KitPieces/SRX/Materials/Default/Decal", 0, (uint)indices.Count, 0, (uint)vertices.Count);
                MapGeometryModel decal = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);
                mgeo.AddModel(decal);
            }
        }

        static void HalloweenRift()
        {

        }

    }
}

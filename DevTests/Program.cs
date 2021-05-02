using System;
using System.Collections.Generic;
using System.IO;
using Aspose;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using LeagueToolkit.Converters;
using LeagueToolkit.IO.OBJ;
using LeagueToolkit.IO.WorldGeometry;
using LeagueToolkit.IO.MapGeometry;
using SharpGLTF.Schema2;
using SharpGLTF.Geometry;
using LeagueToolkit.IO.SimpleSkinFile;
using LeagueToolkit.IO.MapParticles;
using LeagueToolkit.IO.PropertyBin;
using LeagueToolkit.IO.ObjectConfig;
using System.Linq;

namespace DevTests
{
    class Program
    {
        

        static void Main(string[] args)
        {
           
            
            
            ObjectConfigFile testfile = new ObjectConfigFile(@"K:\Riot Games\LeagueSkins\BildgewaterRift\Map11LEVELS\Levels\map11\scene\CFG\objectcfg_srx.cfg");
            var list = testfile.Objects.ToList();
            string liststring = list.ToString();
            testfile.Write(@"K:\Riot Games\LeagueSkins\BildgewaterRift\Map11LEVELS\Levels\map11\scene\CFG\objectcfg_srx2.cfg");
            
        }

        
    }
}

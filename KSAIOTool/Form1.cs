using DarkUI.Forms;
using System;
using System.IO;
using LeagueToolkit;
using System.Windows.Forms;
using DarkUI.Controls;
using DarkUI.Collections;

using Fantome.Libraries.League.IO.MapGeometry;
using System.Linq;
using Fantome.Libraries.League.IO.OBJ;
using System.Collections.Generic;
using System.Text;
using ObjLoader.Loader.Common;
using ObjLoader.Loader.Data;
using System.Text.RegularExpressions;
using System.Reflection;
using System.Linq.Expressions;
using ImageMagick;
using System.Globalization;
using Accessibility;

namespace KSAIOTool
{
    public partial class Form1 : DarkForm
    {
        public Form1()
        {
            InitializeComponent();
            
        }

        //Open/Save Dialog
        FolderBrowserDialog obj_d = new FolderBrowserDialog();
        SaveFileDialog mapgeo = new SaveFileDialog();
        SaveFileDialog mapgeomat = new SaveFileDialog();
        SaveFileDialog python = new SaveFileDialog();
        int number = 1;
        
        
       


        //Map Stuff
        MapGeometry CleanedMapFile = new MapGeometry("MapFile/base_srx.mapgeo");

        private void Form1_Load(object sender, EventArgs e)
        {
            //Github update feature comes here.
        }

        

        

        private void darkButton1_Click(object sender, EventArgs e)
        {
            
            if (obj_d.ShowDialog() == DialogResult.OK)
            {
                
                darkTextBox1.Text = obj_d.SelectedPath;
            }
            System.IO.DirectoryInfo di = new DirectoryInfo("material_output");

             foreach (FileInfo file in di.GetFiles())
             {
                 file.Delete(); 
             }
             foreach (DirectoryInfo dir in di.GetDirectories())
             {
                 dir.Delete(true); 
             }
        }

        private void darkTextBox1_TextChanged(object sender, EventArgs e) //Textbox usage to convert files to mapgeo and it shows how much files will be loaded
        {
            //Model Bulk Loading
            var fileCount = (from file in Directory.EnumerateFiles(darkTextBox1.Text, "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            int OBJsToCreate = fileCount + 1;
            OBJFile[] OBJs = new OBJFile[OBJsToCreate];
            darkTextBox3.Text = fileCount.ToString();
            
            if(OBJsToCreate is 1)
            {
            darkTextBox4.AppendText($"{darkTextBox3.Text} file is loaded");
            darkTextBox4.AppendText(Environment.NewLine);
            }
            else
            {
            darkTextBox4.AppendText($"{darkTextBox3.Text} files are loaded");
            darkTextBox4.AppendText(Environment.NewLine);
            }

            //Check for Layers
            //var BasePath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/1_Base", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            //var InfernalPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/2_Infernal", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            //var MountainPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/3_Mountain", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            //var OceanPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/4_Ocean", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            //var CloudPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/5_Cloud", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();

            //Base
            //darkTextBox13.AppendText(BasePath.ToString());
            //Infernal
            //darkTextBox14.AppendText(InfernalPath.ToString());
            //Mountain
            //darkTextBox15.AppendText(MountainPath.ToString());
            //Ocean
            //darkTextBox16.AppendText(OceanPath.ToString());
            //Cloud
            //darkTextBox17.AppendText(CloudPath.ToString());

            //How many layers we have
            int LayerCount = 0;
            if(darkTextBox13.TextLength > 1 )
            {
                LayerCount++;
            }
            if(darkTextBox14.TextLength > 1 )
            {
                LayerCount++;
            }
            if(darkTextBox15.TextLength > 1 )
            {
                LayerCount++;;
            }
            if(darkTextBox16.TextLength > 1 )
            {
                LayerCount++;
            }
            if(darkTextBox17.TextLength > 1 )
            {
                LayerCount++;
            }
            darkTextBox12.AppendText(LayerCount.ToString());
            
        }

        public static void AddModel(OBJFile obj,  string name, string path, MapGeometry mgeo, int i, TextBox darkTextBox1, TextBox darkTextBox5_TextChanged, CheckBox darkCheckBox1, ProgressBar progressBar1, ComboBox lightmode)
        {
            progressBar1.Value = 0;
            if(darkCheckBox1.Checked) //If AllLayers button is checked load AllLayers if not use Layer 1
            {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.AllLayers);

            progressBar1.Value = 20;

            //Fix for big models that league can't handle.
            List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();

            
            //Porting material file to league format
            StringBuilder mtl = new StringBuilder();
            string number = $"{i}";
            string readfile = File.ReadLines($@"{darkTextBox1.Text}\room{i}.mtl").Skip(12).Take(1).First();
            progressBar1.Value = 40;

            //Get texture name without extension
            string replace = readfile.Replace("\\\\", " \\\\ ");
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            string text = gettexturename.Replace(".dds", "");
            string texturename = text;
            string Map = darkTextBox5_TextChanged.Text;
            var Mapname = Map.Replace(' ', '_');

            //Light Changes
            string Light = lightmode.SelectedItem.ToString();
            

            progressBar1.Value = 60;
            

            // " is replaced by *
            // { is replaced by (
            // } is replaced by )

            //Will be replaced later
            
            if (readfile.IsNullOrEmpty())
            {
                mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}* = StaticMaterialDef (");
                mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}*");
                mtl.AppendLine("        type: u32 = 0");
                mtl.AppendLine("        defaultTechnique: string = *normal*");
                mtl.AppendLine("        samplerValues: list[embed] = (");
                mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                mtl.AppendLine("                addressW: u32 = 1");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("        paramValues: list[embed] = (");
                mtl.AppendLine("            StaticMaterialShaderParamDef (");
                mtl.AppendLine("                name: string = *AlphaTestValue*");
                mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("        shaderMacros: map[string,string] = (");
                if(Light == "1")
                    {
                mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                    }
                    else
                    {
                        
                    }
                mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                mtl.AppendLine("        )");
                mtl.AppendLine("        techniques: list[embed] = (");
                mtl.AppendLine("            StaticMaterialTechniqueDef (");
                mtl.AppendLine("                name: string = *normal*");
                mtl.AppendLine("                passes: list[embed] = (");
                mtl.AppendLine("                    StaticMaterialPassDef (");
                mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                mtl.AppendLine("                        blendEnable: bool = true");
                mtl.AppendLine("                        cullEnable: bool = false");
                mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                mtl.AppendLine("                    )");
                mtl.AppendLine("                )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("    )");

                
                
                mtl.Replace('*','"');
                mtl.Replace('(', '{');
                mtl.Replace(')', '}');
                Directory.CreateDirectory("material_output");
                File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
            }
            else
            {
                mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}* = StaticMaterialDef (");
                mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}*");
                mtl.AppendLine("        type: u32 = 0");
                mtl.AppendLine("        defaultTechnique: string = *normal*");
                mtl.AppendLine("        samplerValues: list[embed] = (");
                mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                mtl.AppendLine("                addressW: u32 = 1");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("        paramValues: list[embed] = (");
                mtl.AppendLine("            StaticMaterialShaderParamDef (");
                mtl.AppendLine("                name: string = *AlphaTestValue*");
                mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("        shaderMacros: map[string,string] = (");
                    if(Light == "1")
                    {
                mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                    }
                    else
                    {
                        
                    }
                mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                mtl.AppendLine("        )");
                mtl.AppendLine("        techniques: list[embed] = (");
                mtl.AppendLine("            StaticMaterialTechniqueDef (");
                mtl.AppendLine("                name: string = *normal*");
                mtl.AppendLine("                passes: list[embed] = (");
                mtl.AppendLine("                    StaticMaterialPassDef (");
                mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                mtl.AppendLine("                        blendEnable: bool = true");
                mtl.AppendLine("                        cullEnable: bool = false");
                mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                mtl.AppendLine("                    )");
                mtl.AppendLine("                )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("    )");

                
                //Fixes the format
                mtl.Replace('*','"');
                mtl.Replace('(', '{');
                mtl.Replace(')', '}');
                Directory.CreateDirectory("material_output");
                File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                
                
                
            }

            progressBar1.Value = 80;

            if (vertices.Count > 30000 & indices.Count > 27000)
            {
                
                Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                Console.WriteLine($"Vertices:{vertices.Count}");
                Console.WriteLine($"Indices:{indices.Count}");
                mgeo.Models.Remove(room);
                Console.WriteLine($"Ignored: {room.Name}");
                Console.WriteLine("_________________________________________________________________________________");
                
                
                
                //Writes Temporary a log file into a specific folder
                StringBuilder sb = new StringBuilder();
                
                //Set Max values for vertices and indices
                int vtmax = 30000;
                int idmax = 27000;
                //Log Formatting
                sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                
                //Addeds DateTime to filename
                int Day = DateTime.Now.Day;
                int Month = DateTime.Now.Month;
                int Year = DateTime.Now.Year;
                int Hour = DateTime.Now.Hour;
                int Minute = DateTime.Now.Minute;
                int Second = DateTime.Now.Second;
                string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                
                Directory.CreateDirectory("logs");
                File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                
                sb.Clear();

            }
            else
            {
                Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                Console.WriteLine($"Vertices:{vertices.Count}");
                Console.WriteLine($"Indices:{indices.Count}");
                Console.WriteLine("_________________________________________________________________________________");
                
                
            }
            mgeo.AddModel(room);

            progressBar1.Value = 90;


            }
            
            else
            {
                if(path.Contains("_base"))
                {
                   (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                   MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
                   MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer1);
                   
                   progressBar1.Value = 20;
                   
                   //Fix for big models that league can't handle.
                   List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();
                   
                   
                   //Porting material file to league format
                   StringBuilder mtl = new StringBuilder();
                   string number = $"{i}";
                   string readfile = File.ReadLines($@"{darkTextBox1.Text}\1_Base\room{i}.mtl").Skip(12).Take(1).First();
                   progressBar1.Value = 40;
                   
                   //Get texture name without extension
                   string replace = readfile.Replace("\\\\", " \\\\ ");
                   var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                   string text = gettexturename.Replace(".dds", "");
                   string texturename = text;
                   string Map = darkTextBox5_TextChanged.Text;
                   var Mapname = Map.Replace(' ', '_');
                   
                   //Light Changes
                   string Light = lightmode.SelectedItem.ToString();
                   
                   
                   progressBar1.Value = 60;
                   
                   
                   // " is replaced by *
                   // { is replaced by (
                   // } is replaced by )
                   
                   //Will be replaced later
                   
                   if (readfile.IsNullOrEmpty())
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_base* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_base*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                       if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                   }
                   else
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_base* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_base*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                           if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       //Fixes the format
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                       
                       
                       
                   }
                   
                   progressBar1.Value = 80;
                   
                   if (vertices.Count > 30000 & indices.Count > 27000)
                   {
                       
                       Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       mgeo.Models.Remove(room);
                       Console.WriteLine($"Ignored: {room.Name}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                       
                       //Writes Temporary a log file into a specific folder
                       StringBuilder sb = new StringBuilder();
                       
                       //Set Max values for vertices and indices
                       int vtmax = 30000;
                       int idmax = 27000;
                       //Log Formatting
                       sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                       
                       //Addeds DateTime to filename
                       int Day = DateTime.Now.Day;
                       int Month = DateTime.Now.Month;
                       int Year = DateTime.Now.Year;
                       int Hour = DateTime.Now.Hour;
                       int Minute = DateTime.Now.Minute;
                       int Second = DateTime.Now.Second;
                       string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                       
                       Directory.CreateDirectory("logs");
                       File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                       
                       sb.Clear();
                   
                   }
                   else
                   {
                       Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                   }
                   mgeo.AddModel(room);
                   
                   progressBar1.Value = 90;
                   }
                if(name.Contains("_infernal"))
                {
                   (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                   MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
                   MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer2);
                   
                   progressBar1.Value = 20;
                   
                   //Fix for big models that league can't handle.
                   List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();
                   
                   
                   //Porting material file to league format
                   StringBuilder mtl = new StringBuilder();
                   string number = $"{i}";
                   string readfile = File.ReadLines($@"{darkTextBox1.Text}\2_Infernal\room{i}.mtl").Skip(12).Take(1).First();
                   progressBar1.Value = 40;
                   
                   //Get texture name without extension
                   string replace = readfile.Replace("\\\\", " \\\\ ");
                   var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                   string text = gettexturename.Replace(".dds", "");
                   string texturename = text;
                   string Map = darkTextBox5_TextChanged.Text;
                   var Mapname = Map.Replace(' ', '_');
                   
                   //Light Changes
                   string Light = lightmode.SelectedItem.ToString();
                   
                   
                   progressBar1.Value = 60;
                   
                   
                   // " is replaced by *
                   // { is replaced by (
                   // } is replaced by )
                   
                   //Will be replaced later
                   
                   if (readfile.IsNullOrEmpty())
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_infernal* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_infernal*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                       if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                   }
                   else
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_infernal* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_infernal*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                           if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       //Fixes the format
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                       
                       
                       
                   }
                   
                   progressBar1.Value = 80;
                   
                   if (vertices.Count > 30000 & indices.Count > 27000)
                   {
                       
                       Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       mgeo.Models.Remove(room);
                       Console.WriteLine($"Ignored: {room.Name}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                       
                       //Writes Temporary a log file into a specific folder
                       StringBuilder sb = new StringBuilder();
                       
                       //Set Max values for vertices and indices
                       int vtmax = 30000;
                       int idmax = 27000;
                       //Log Formatting
                       sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                       
                       //Addeds DateTime to filename
                       int Day = DateTime.Now.Day;
                       int Month = DateTime.Now.Month;
                       int Year = DateTime.Now.Year;
                       int Hour = DateTime.Now.Hour;
                       int Minute = DateTime.Now.Minute;
                       int Second = DateTime.Now.Second;
                       string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                       
                       Directory.CreateDirectory("logs");
                       File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                       
                       sb.Clear();
                   
                   }
                   else
                   {
                       Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                   }
                   mgeo.AddModel(room);
                   
                   progressBar1.Value = 90;
                }
                if(name.Contains("_mountain"))
                {
                   (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                   MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
                   MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer3);
                   
                   progressBar1.Value = 20;
                   
                   //Fix for big models that league can't handle.
                   List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();
                   
                   
                   //Porting material file to league format
                   StringBuilder mtl = new StringBuilder();
                   string number = $"{i}";
                   string readfile = File.ReadLines($@"{darkTextBox1.Text}\3_Mountain\room{i}.mtl").Skip(12).Take(1).First();
                   progressBar1.Value = 40;
                   
                   //Get texture name without extension
                   string replace = readfile.Replace("\\\\", " \\\\ ");
                   var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                   string text = gettexturename.Replace(".dds", "");
                   string texturename = text;
                   string Map = darkTextBox5_TextChanged.Text;
                   var Mapname = Map.Replace(' ', '_');
                   
                   //Light Changes
                   string Light = lightmode.SelectedItem.ToString();
                   
                   
                   progressBar1.Value = 60;
                   
                   
                   // " is replaced by *
                   // { is replaced by (
                   // } is replaced by )
                   
                   //Will be replaced later
                   
                   if (readfile.IsNullOrEmpty())
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_mountain* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_mountain*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                       if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                   }
                   else
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_mountain* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_mountain*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                           if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       //Fixes the format
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                       
                       
                       
                   }
                   
                   progressBar1.Value = 80;
                   
                   if (vertices.Count > 30000 & indices.Count > 27000)
                   {
                       
                       Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       mgeo.Models.Remove(room);
                       Console.WriteLine($"Ignored: {room.Name}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                       
                       //Writes Temporary a log file into a specific folder
                       StringBuilder sb = new StringBuilder();
                       
                       //Set Max values for vertices and indices
                       int vtmax = 30000;
                       int idmax = 27000;
                       //Log Formatting
                       sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                       
                       //Addeds DateTime to filename
                       int Day = DateTime.Now.Day;
                       int Month = DateTime.Now.Month;
                       int Year = DateTime.Now.Year;
                       int Hour = DateTime.Now.Hour;
                       int Minute = DateTime.Now.Minute;
                       int Second = DateTime.Now.Second;
                       string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                       
                       Directory.CreateDirectory("logs");
                       File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                       
                       sb.Clear();
                   
                   }
                   else
                   {
                       Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                   }
                   mgeo.AddModel(room);
                   
                   progressBar1.Value = 90;
                }
                if(name.Contains("_cloud"))
                {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                   MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
                   MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer4);
                   
                   progressBar1.Value = 20;
                   
                   //Fix for big models that league can't handle.
                   List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();
                   
                   
                   //Porting material file to league format
                   StringBuilder mtl = new StringBuilder();
                   string number = $"{i}";
                   string readfile = File.ReadLines($@"{darkTextBox1.Text}\4_Cloud\room{i}.mtl").Skip(12).Take(1).First();
                   progressBar1.Value = 40;
                   
                   //Get texture name without extension
                   string replace = readfile.Replace("\\\\", " \\\\ ");
                   var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                   string text = gettexturename.Replace(".dds", "");
                   string texturename = text;
                   string Map = darkTextBox5_TextChanged.Text;
                   var Mapname = Map.Replace(' ', '_');
                   
                   //Light Changes
                   string Light = lightmode.SelectedItem.ToString();
                   
                   
                   progressBar1.Value = 60;
                   
                   
                   // " is replaced by *
                   // { is replaced by (
                   // } is replaced by )
                   
                   //Will be replaced later
                   
                   if (readfile.IsNullOrEmpty())
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_cloud* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_cloud*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                       if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                   }
                   else
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_cloud* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_cloud*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                           if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       //Fixes the format
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                       
                       
                       
                   }
                   
                   progressBar1.Value = 80;
                   
                   if (vertices.Count > 30000 & indices.Count > 27000)
                   {
                       
                       Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       mgeo.Models.Remove(room);
                       Console.WriteLine($"Ignored: {room.Name}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                       
                       //Writes Temporary a log file into a specific folder
                       StringBuilder sb = new StringBuilder();
                       
                       //Set Max values for vertices and indices
                       int vtmax = 30000;
                       int idmax = 27000;
                       //Log Formatting
                       sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                       
                       //Addeds DateTime to filename
                       int Day = DateTime.Now.Day;
                       int Month = DateTime.Now.Month;
                       int Year = DateTime.Now.Year;
                       int Hour = DateTime.Now.Hour;
                       int Minute = DateTime.Now.Minute;
                       int Second = DateTime.Now.Second;
                       string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                       
                       Directory.CreateDirectory("logs");
                       File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                       
                       sb.Clear();
                   
                   }
                   else
                   {
                       Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                   }
                   mgeo.AddModel(room);
                   
                   progressBar1.Value = 90;
                }
                if(name.Contains("_ocean"))
                {
                (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
                   MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
                   MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer5);
                   
                   progressBar1.Value = 20;
                   
                   //Fix for big models that league can't handle.
                   List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();
                   
                   
                   //Porting material file to league format
                   StringBuilder mtl = new StringBuilder();
                   string number = $"{i}";
                   string readfile = File.ReadLines($@"{darkTextBox1.Text}\5_Ocean\room{i}.mtl").Skip(12).Take(1).First();
                   progressBar1.Value = 40;
                   
                   //Get texture name without extension
                   string replace = readfile.Replace("\\\\", " \\\\ ");
                   var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
                   string text = gettexturename.Replace(".dds", "");
                   string texturename = text;
                   string Map = darkTextBox5_TextChanged.Text;
                   var Mapname = Map.Replace(' ', '_');
                   
                   //Light Changes
                   string Light = lightmode.SelectedItem.ToString();
                   
                   
                   progressBar1.Value = 60;
                   
                   
                   // " is replaced by *
                   // { is replaced by (
                   // } is replaced by )
                   
                   //Will be replaced later
                   
                   if (readfile.IsNullOrEmpty())
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_ocean* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_ocean*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Shared/Materials/white.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                       if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                   }
                   else
                   {
                       mtl.AppendLine($"*Maps/KitPieces/Summoners_Rift/Materials/room{i}_ocean* = StaticMaterialDef (");
                       mtl.AppendLine($"        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room{i}_ocean*");
                       mtl.AppendLine("        type: u32 = 0");
                       mtl.AppendLine("        defaultTechnique: string = *normal*");
                       mtl.AppendLine("        samplerValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderSamplerDef (");
                       mtl.AppendLine("                samplerName: string = *DiffuseTexture*");
                       mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/{Mapname}/{texturename}.dds*");
                       mtl.AppendLine("                addressW: u32 = 1");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        paramValues: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialShaderParamDef (");
                       mtl.AppendLine("                name: string = *AlphaTestValue*");
                       mtl.AppendLine("                value: vec4 = ( 0.300000012, 0, 0, 0 )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        shaderMacros: map[string,string] = (");
                           if(Light == "1")
                           {
                       mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
                           }
                           else
                           {
                               
                           }
                       mtl.AppendLine("            *DISABLE_DEPTH_FOG* = *1*");
                       mtl.AppendLine("            *PREMULTIPLIED_ALPHA* = *1*");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("        techniques: list[embed] = (");
                       mtl.AppendLine("            StaticMaterialTechniqueDef (");
                       mtl.AppendLine("                name: string = *normal*");
                       mtl.AppendLine("                passes: list[embed] = (");
                       mtl.AppendLine("                    StaticMaterialPassDef (");
                       mtl.AppendLine("                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*");
                       mtl.AppendLine("                        blendEnable: bool = true");
                       mtl.AppendLine("                        cullEnable: bool = false");
                       mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                       mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                       mtl.AppendLine("                    )");
                       mtl.AppendLine("                )");
                       mtl.AppendLine("            )");
                       mtl.AppendLine("        )");
                       mtl.AppendLine("    )");
                   
                       
                       //Fixes the format
                       mtl.Replace('*','"');
                       mtl.Replace('(', '{');
                       mtl.Replace(')', '}');
                       Directory.CreateDirectory("material_output");
                       File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                       
                       
                       
                   }
                   
                   progressBar1.Value = 80;
                   
                   if (vertices.Count > 30000 & indices.Count > 27000)
                   {
                       
                       Console.WriteLine($"{room.Name} is too big for Leauge and need to be splitted into smaller parts.");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       mgeo.Models.Remove(room);
                       Console.WriteLine($"Ignored: {room.Name}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                       
                       //Writes Temporary a log file into a specific folder
                       StringBuilder sb = new StringBuilder();
                       
                       //Set Max values for vertices and indices
                       int vtmax = 30000;
                       int idmax = 27000;
                       //Log Formatting
                       sb.AppendLine($"room{i}.obj -> {room.Name} | Vertices:{vertices.Count} > {vtmax}, Indices:{indices.Count} > {idmax}");
                       
                       //Addeds DateTime to filename
                       int Day = DateTime.Now.Day;
                       int Month = DateTime.Now.Month;
                       int Year = DateTime.Now.Year;
                       int Hour = DateTime.Now.Hour;
                       int Minute = DateTime.Now.Minute;
                       int Second = DateTime.Now.Second;
                       string Time = $"{Day}_{Month}_{Year}_{Hour}_{Minute}";
                       
                       Directory.CreateDirectory("logs");
                       File.AppendAllText(@"logs\"+$"{Time}_map_log.txt", sb.ToString());
                       
                       sb.Clear();
                   
                   }
                   else
                   {
                       Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                       Console.WriteLine($"Vertices:{vertices.Count}");
                       Console.WriteLine($"Indices:{indices.Count}");
                       Console.WriteLine("_________________________________________________________________________________");
                       
                       
                   }
                   mgeo.AddModel(room);
                   
                   progressBar1.Value = 90;
                }
            }
            progressBar1.Value = 100;


        }

        
        

        private void darkTextBox4_TextChanged(object sender, EventArgs e, StringBuilder sb)
        {
            string consoletext = sb.ToString();
            darkTextBox1.AppendText(consoletext);
        }

        private void darkTextBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void darkTextBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void darkButton2_Click_1(object sender, EventArgs e)
        {
            mapgeo.Filter = "League MapGeometryFile (*.mapgeo)| *.mapgeo";
            if(darkTextBox1.Text == string.Empty)
            {
                this.darkTextBox4.Clear();
                darkTextBox4.AppendText("No files are selected! Mapgeo will not be created!");
                
            }
            else
            {
            
                if (mapgeo.ShowDialog() == DialogResult.OK)
                {
                    //Model Bulk Loading
                    var fileCount = (from file in Directory.EnumerateFiles(darkTextBox1.Text, "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
                    var BasePath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/1_Base", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
                    var InfernalPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/2_Infernal", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
                    var MountainPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/3_Mountain", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
                    var OceanPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/4_Ocean", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
                    var CloudPath = (from file in Directory.EnumerateFiles(darkTextBox1.Text + "/5_Cloud", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();

                    int OBJsToCreate = fileCount + 5;
                    OBJFile[] OBJs = new OBJFile[OBJsToCreate];
                    darkTextBox3.Text = OBJsToCreate.ToString();
                    
                    
                    for (int i = 1; i < OBJsToCreate; i++)
                    {
                        try
                        {
                            OBJs[i] = new OBJFile($"{darkTextBox1.Text}" + $"room{i}.obj");
                            
                            
                            AddModel(OBJs[i], $"MapGeo_Instance_{i}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}", CleanedMapFile, i, darkTextBox1, darkTextBox5, darkCheckBox1, progressBar1, lightmode);
                            
                        }
                        
                    catch(FileNotFoundException ex)
                        {
                            MessageBox.Show($"room{i} is missing and will be ignored!", "Error: File Missing", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            
                        }
                       
                    }
                    string namemapgeo = mapgeo.FileName;
                    string materialname = namemapgeo.Replace(".mapgeo", ".materials.bin");
                    string pathmapgeo = Path.GetFullPath(namemapgeo);
                    string pathmapgeomat = Path.GetFullPath(materialname);
                    string filenamemgeo = Path.GetFileName(namemapgeo);
                    string filenamemat = Path.GetFileName(materialname);
                    
                    string correctpathmat = pathmapgeomat.Replace(@"\\", @"/");
                    CleanedMapFile.Write(pathmapgeo, 11);

                    //Material Properties
                    string newmtl = File.ReadAllText(@"material_output\"+"material.py");
                    string originalmtl = File.ReadAllText("MapFile/base_srx.materials");
                    string originalmtl2 = originalmtl.Replace("Replaceme", newmtl);
                    


                    //NewStringBuilder for Sun Properties

                    StringBuilder sunprop = new StringBuilder();

                    sunprop.Clear();
                    sunprop.AppendLine($"sunColor: vec4 = ( {suncolorR.Text}, {suncolorG.Text}, {suncolorB.Text}, {suncolorA.Text} )");
                    sunprop.AppendLine($"                sunDirection: vec3 = ( {sundirectionX.Text}, {sundirectionY.Text}, {sundirectionZ.Text} )");
                    sunprop.AppendLine($"                skyLightColor: vec4 = ( {skylightcolorR.Text}, {skylightcolorG.Text}, {skylightcolorB.Text}, {skylightcolorA.Text} )");
                    sunprop.AppendLine($"                groundColor: vec4 = ( {groundcolorR.Text}, {groundcolorG.Text}, {groundcolorB.Text}, {groundcolorA.Text} )");
                    sunprop.AppendLine($"                lightMapColorScale: f32 = {lightmapcolorscaletext.Text}");
                    sunprop.AppendLine($"                fogEnabled: bool = {fogcombobox.SelectedItem}");
                    sunprop.AppendLine($"                fogStartAndEnd: vec2 = ( {fogstarttext.Text}, {fogendtext.Text} )");

                    
                    sunprop.Replace('(', '{');
                    sunprop.Replace(')', '}');

                    

                    File.AppendAllText(@"material_output\"+"sunprop.py", sunprop.ToString());
                    string sunprops = File.ReadAllText(@"material_output/"+"sunprop.py");
                    
                    

                    File.WriteAllText(@$"material_output\output_new.py", originalmtl2);
                    string rewrite = File.ReadAllText(@$"material_output\output_new.py");
                    string originalmtl3 = rewrite.Replace("Fixme", sunprops);
                    File.WriteAllText(@$"material_output\output_new.py", originalmtl3);

                    string pymtl = File.ReadAllText(@$"material_output\output_new.py");

                    var binfile = System.Diagnostics.Process.Start("Executive/txt2ritobin.exe", $"material_output/output_new.py material_output/output_new.bin");
                    
                    binfile.WaitForExit();
                    File.Move("material_output/output_new.bin", pathmapgeomat);
                    
                    darkTextBox4.AppendText($"{filenamemgeo} exported");
                    darkTextBox4.AppendText(Environment.NewLine);
                    darkTextBox4.AppendText($"{filenamemat} exported");
                    darkTextBox4.AppendText(Environment.NewLine);
                    
                }
                

            }
            
        }

        private void darkCheckBox1_CheckedChanged(object sender, EventArgs e)
        {
           
        }

        private void progressBar1_Click(object sender, EventArgs e)
        {

        }

        private void darkDropdownList1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() != System.Windows.Forms.DialogResult.Cancel)
            {
                button1.BackColor = colorDialog1.Color;
                //Convert RGBA 0-255 to 0-1

                //Red
                var RedSunColor = button1.BackColor.R;
                var RedSunColor01 = RedSunColor / 255.0;

                //Green
                var GreenSunColor = button1.BackColor.G;
                var GreenSunColor01 = GreenSunColor / 255.0;
                //Blue
                var BlueSunColor = button1.BackColor.B;
                var BlueSunColor01 = BlueSunColor / 255.0;
                //Alpha
                var AlphaSunColor = button1.BackColor.A;
                var AlphaSunColor01 = AlphaSunColor / 255.0;

                suncolorR.Text = RedSunColor01.ToString();
                suncolorG.Text = GreenSunColor01.ToString();
                suncolorB.Text = BlueSunColor01.ToString();
                suncolorA.Text = AlphaSunColor01.ToString();
            }
            
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() != System.Windows.Forms.DialogResult.Cancel)
            {
                button2.BackColor = colorDialog1.Color;

                //Convert RGBA 0-255 to 0-1

                //Red
                var RedSkyColor = button2.BackColor.R;
                var RedSkyColor01 = RedSkyColor / 255.0;

                //Green
                var GreenSkyColor = button2.BackColor.G;
                var GreenSkyColor01 = GreenSkyColor / 255.0;
                //Blue
                var BlueSkyColor = button2.BackColor.B;
                var BlueSkyColor01 = BlueSkyColor / 255.0;
                //Alpha
                var AlphaSkyColor = button2.BackColor.A;
                var AlphaSkyColor01 = AlphaSkyColor / 255.0;

                skylightcolorR.Text = RedSkyColor01.ToString();
                skylightcolorG.Text = GreenSkyColor01.ToString();
                skylightcolorB.Text = BlueSkyColor01.ToString();
                skylightcolorA.Text = AlphaSkyColor01.ToString();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() != System.Windows.Forms.DialogResult.Cancel)
            {
                button3.BackColor = colorDialog1.Color;

                //Convert RGBA 0-255 to 0-1

                //Red
                var RedGroundColor = button3.BackColor.R;
                var RedGroundColor01 = RedGroundColor / 255.0;

                //Green
                var GreenGroundColor = button3.BackColor.G;
                var GreenGroundColor01 = GreenGroundColor / 255.0;
                //Blue
                var BlueGroundColor = button3.BackColor.B;
                var BlueGroundColor01 = BlueGroundColor / 255.0;
                //Alpha
                var AlphaGroundColor = button3.BackColor.A;
                var AlphaGroundColor01 = AlphaGroundColor / 255.0;

                skylightcolorR.Text = RedGroundColor01.ToString();
                skylightcolorG.Text = GreenGroundColor01.ToString();
                skylightcolorB.Text = BlueGroundColor01.ToString();
                skylightcolorA.Text = AlphaGroundColor01.ToString();
            }
        }

        private void lightmode_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void fogcombobox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void darkButton3_Click(object sender, EventArgs e)
        {

        }

        private void darkButton5_Click(object sender, EventArgs e)
        {

        }

        private void darkTextBox11_TextChanged(object sender, EventArgs e)
        {
           
           
        }

        private void darkTextBox7_TextChanged(object sender, EventArgs e)
        {

        }

        private void darkTextBox8_TextChanged(object sender, EventArgs e)
        {

        }

        private void darkTextBox9_TextChanged(object sender, EventArgs e)
        {

        }

        private void darkTextBox10_TextChanged(object sender, EventArgs e)
        {

        }

        private int a = 0;

        private void darkButton5_Click_1(object sender, EventArgs e)
        {
            

            darkTextBox11.ResetText();

            string MapParticleName = darkTextBox7.Text.ToString() + "_";
            string ParticleRoot = darkTextBox8.Text.ToString();
            string transformation = darkTextBox9.Text.ToString();
            string prefabname = darkTextBox10.Text.ToString() + "_";
            string eyecandy = darkCheckBox2.CheckState.ToString();
            if(eyecandy.Contains("Checked"))
            {
            darkTextBox11.AppendText($"*{MapParticleName + a}* = MapParticle (");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                system: link = *{ParticleRoot}*");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                eyeCandy: bool = true");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                transform: mtx44 = (");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    1, 0, 0, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    0, 1, 0, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    0, 0, 1, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                    {transformation}, 1");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                )");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                name: string = *{prefabname + a}*");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                0xccf79327: u8 = 1");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("            )");
            }

            else
            {
            darkTextBox11.AppendText($"*{MapParticleName + a}* = MapParticle (");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                system: link = *{ParticleRoot}*");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                eyeCandy: bool = false");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                transform: mtx44 = (");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    1, 0, 0, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    0, 1, 0, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                    0, 0, 1, 0");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                    {transformation}, 1");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                )");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText($"                name: string = *{prefabname + a}*");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("                0xccf79327: u8 = 1");
            darkTextBox11.AppendText(Environment.NewLine);
            darkTextBox11.AppendText("            )");
            }
            
            
        }

        private void darkButton6_Click(object sender, EventArgs e)
        {
           a++;
           string num = a.ToString();
            string MapParticleName = darkTextBox7.Text.ToString() + "_";
            string ParticleRoot = darkTextBox8.Text.ToString();
            string transformation = darkTextBox9.Text.ToString();
            string prefabname = darkTextBox10.Text.ToString() + "_";
            string eyecandy = darkCheckBox2.CheckState.ToString();
            if(eyecandy.Contains("Checked"))
            {
            darkTextBox6.AppendText($"*{MapParticleName + num}* = MapParticle (");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                system: link = *{ParticleRoot}*");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                eyeCandy: bool = true");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                transform: mtx44 = (");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    1, 0, 0, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    0, 1, 0, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    0, 0, 1, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                    {transformation}, 1");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                )");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                name: string = *{prefabname + num}*");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                0xccf79327: u8 = 1");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("            )");
            darkTextBox6.AppendText(Environment.NewLine);
            }

            else
            {
            darkTextBox6.AppendText($"*{MapParticleName + num}* = MapParticle (");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                system: link = *{ParticleRoot}*");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                eyeCandy: bool = false");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                transform: mtx44 = (");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    1, 0, 0, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    0, 1, 0, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                    0, 0, 1, 0");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                    {transformation}, 1");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                )");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText($"                name: string = *{prefabname + num}*");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("                0xccf79327: u8 = 1");
            darkTextBox6.AppendText(Environment.NewLine);
            darkTextBox6.AppendText("            )");
            darkTextBox6.AppendText(Environment.NewLine);
            }

           
        }

        private void darkButton7_Click(object sender, EventArgs e)
        {
            python.Filter = "Python file (*.py)|*.py";
            if (python.ShowDialog() == DialogResult.OK)
            {
                
                TextWriter writer = new StreamWriter(Path.GetFullPath(python.FileName));
                var TextBox6 = darkTextBox6.Text;
                writer.Write(TextBox6);
                writer.Close();
                
                string text = File.ReadAllText(Path.GetFullPath(python.FileName));
                text = text.Replace("(", "{");
                text = text.Replace(")", "}");
                text = text.Replace('*', '"');

                File.WriteAllText(Path.GetFullPath(python.FileName), text);
                
            }
        }

        private void darkButton8_Click(object sender, EventArgs e)
        {
            darkTextBox6.ResetText();
            a = 0;
        }
    }
}

﻿using Fantome.Libraries.League.Helpers.Structures;
using Fantome.Libraries.League.Helpers.Structures.BucketGrid;
using Fantome.Libraries.League.IO.MapGeometry;
using Fantome.Libraries.League.IO.OBJ;
using Fantome.Libraries.League.IO.BIN;
using Fantome.Libraries.League.IO.WorldGeometry;
using ImageMagick;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using SharpGLTF.Geometry.VertexTypes;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using SharpGLTF.Schema2;
using Fantome.Libraries.League.IO.NVR;
using Fantome.Libraries.League.IO.SimpleSkinFile;
using System.Numerics;
using static System.Net.Mime.MediaTypeNames;
using Microsoft.VisualBasic.CompilerServices;
using Fantome.Libraries.League.Converters;
using Newtonsoft.Json.Linq;
using System.Runtime.InteropServices;
using System.Text;
using Microsoft.VisualBasic.FileIO;
using System.ComponentModel.DataAnnotations;
using System.Threading;
using Fantome.Libraries.League.IO.MapParticles;
using System.Runtime.Intrinsics.X86;
using Fantome.Libraries.League.IO.MaterialLibrary;
using ObjLoader;
using Fantome.Libraries.League.Helpers;
using ObjLoader.Loader.Data;
using ObjLoader.Loader.Data.VertexData;
using ObjLoader.Loader.Common;

namespace KSMapCreator
{
    class Program
    {
        

        static void Main(string[] args)
        {
            //Deletes existing material file.
            if(File.Exists(@"material_output\material.py"))
            {
                File.Delete(@"material_output\material.py");
            }
          
            string MapMgeoPath = "MapFile/base_srx.mapgeo";
            MapGeometry MapMgeo = new MapGeometry(MapMgeoPath);
            MapMgeo.Models.Clear();
            BildgeWaterRift(MapMgeo);
            

        }

        static void BildgeWaterRift(MapGeometry mgeo)
        {
            
            //Model Bulk Loading
            var fileCount = (from file in Directory.EnumerateFiles(@"K:\Riot Games\LeagueSkins\BildgewaterRift\3dmodelsnewnew", "*.obj", System.IO.SearchOption.AllDirectories) select file).Count();
            int OBJsToCreate = fileCount + 1;
            OBJFile[] OBJs = new OBJFile[OBJsToCreate];
            
            
            
            for (int i = 1; i < OBJsToCreate; i++)
            {
                
                OBJs[i] = new OBJFile($@"K:\Riot Games\LeagueSkins\BildgewaterRift\3dmodelsnewnew\room{i}.obj");
                
                int j = i;
                AddModel(OBJs[i], $"MapGeo_Instance_{i}", $"Maps/KitPieces/Summoners_Rift/Materials/room{i}", mgeo, i, j);

               
            }
            mgeo.Write(@"K:\Riot Games\LeagueSkins\BildgewaterRift\Map11\data\maps\mapgeometry\sr\base_srx.mapgeo", 11);
        }



        static void AddModel(OBJFile obj,  string name, string path, MapGeometry mgeo, int i, int j)
        {
            (List<ushort> indices, List<MapGeometryVertex> vertices) = obj.GetMGEOData();
            MapGeometrySubmesh submesh = new MapGeometrySubmesh(path, 0, (uint)indices.Count, 0, (uint)vertices.Count);
            MapGeometryModel room = new MapGeometryModel(name, vertices, indices, new List<MapGeometrySubmesh>() { submesh }, MapGeometryLayer.Layer1);
            //Fix for big models that league can't handle.
            List<MapGeometryModel> mgeoModels = new List<MapGeometryModel>();


            //Porting material file to league format
           
            
                
            StringBuilder mtl = new StringBuilder();
            string number = $"{i}";
            string readfile = File.ReadLines($@"K:\Riot Games\LeagueSkins\BildgewaterRift\3dmodelsnewnew\room{i}.mtl").Skip(12).Take(1).First();
            string replace = readfile.Replace("\\\\", " \\\\ ");
            
            var gettexturename = string.Join(" ", replace.Split().Reverse().Take(1).Reverse());
            


            
            string text = gettexturename.Replace(".dds", "");
            string texturename = text;

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
                mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
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
                mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                mtl.AppendLine("                    )");
                mtl.AppendLine("                )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("    )");

                
                
            
                Directory.CreateDirectory("material_output");
                File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
                //Console.Write(mtl.ToString());
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
                mtl.AppendLine($"                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/{texturename}.dds*");
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
                mtl.AppendLine("            *NO_BAKED_LIGHTING* = *1*");
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
                mtl.AppendLine("                        dstColorBlendFactor: u32 = 7");
                mtl.AppendLine("                        dstAlphaBlendFactor: u32 = 7");
                mtl.AppendLine("                    )");
                mtl.AppendLine("                )");
                mtl.AppendLine("            )");
                mtl.AppendLine("        )");
                mtl.AppendLine("    )");

                
                
                //Console.Write(mtl.ToString());
                Directory.CreateDirectory("material_output");
                File.AppendAllText(@"material_output\"+"material.py", mtl.ToString());
            }

            

                
               


            if (vertices.Count > 30000 & indices.Count > 27000)
            {
                /*MapGeometryModel newMgeoMesh = new MapGeometryModel();
                foreach (var vert in vertices)
                {
                    MapGeometryVertex newMgeoVertex = new MapGeometryVertex();
                    newMgeoVertex.Position = vert.Position;
                    newMgeoVertex.DiffuseUV = vert.DiffuseUV;
                    newMgeoMesh.Vertices.Add(newMgeoVertex);
                }
                foreach (var index in indices)
                newMgeoMesh.Indices.Add(index);
                mgeoModels.Add(newMgeoMesh);*/ //should work now
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
                
                //Addeds DateTime to file name
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

                /*room.Indices.AddRange(room.Indices);
                UInt32 mgeoCount = 1;
                while (room.Indices.Count > 0)
                {
                    MapGeometryModel newMgeoMesh = new MapGeometryModel();
                    // Keeps the indices we can keep :D
                    UInt32 count = 0;
                    List<UInt32> keptIndices = new List<UInt32>();
                    bool tooManyIndices = false;
                    while (count < (room.Indices.Count / (double)3))
                    {
                        //Code on here cause out of range exception. IDK why
                        if (room.Indices[3 * room.Indices.Count] <= mgeoCount * 30000 && room.Indices[3 * indices.Count + 1] <= mgeoCount * 30000 && room.Indices[3 * room.Indices.Count + 2] <= mgeoCount * 30000)
                        {
                           

                            if (keptIndices.Count <= 27000)
                            {
                                tooManyIndices = true;
                                count = (uint)(room.Indices.Count / (double)3);
                            }
                            else
                            {
                                keptIndices.Add(room.Indices[3 * room.Indices.Count]);
                                keptIndices.Add(room.Indices[3 * room.Indices.Count + 1]);
                                keptIndices.Add(room.Indices[3 * room.Indices.Count + 2]);
                                room.Indices.RemoveRange(3 * room.Indices.Count, 3);
                            }
                        }
                        else
                            count += 1;
                    }
                    foreach (var vert in vertices)
                    {
                        MapGeometryVertex newMgeoVertex = new MapGeometryVertex();
                        newMgeoVertex.Position = vert.Position; //problably got all positions
                        newMgeoVertex.DiffuseUV = vert.DiffuseUV;
                        newMgeoMesh.Vertices.Add(newMgeoVertex);
                    }
                    //Check what vertex to keep depending on the index we put
                    List<UInt32> sortedIndices = new List<UInt32>();
                    sortedIndices.AddRange(keptIndices);
                    sortedIndices.Sort();
                    Int32 previousIndex = -1;
                    for (var p = 0; i <= sortedIndices.Count - 1; i++)
                    {
                        if ((sortedIndices[i] - previousIndex) > 1)
                        {

                            UInt32 verticesToRemove = (uint)(sortedIndices[i] - previousIndex - 1);
                            // Removing vertices
                            newMgeoMesh.Vertices.RemoveRange(previousIndex + 1, (int)verticesToRemove);
                            NewMethod(keptIndices, sortedIndices, p, verticesToRemove);
                            for (j = i; j <= sortedIndices.Count - 1; j++)
                                // Adjusting sorted indices
                                sortedIndices[j] = sortedIndices[j] - verticesToRemove;
                        }
                        previousIndex = (int)sortedIndices[i];
                    }
                    if (newMgeoMesh.Vertices.Count > previousIndex + 1)
                        newMgeoMesh.Vertices.RemoveRange(previousIndex + 1, newMgeoMesh.Vertices.Count - previousIndex - 1);
                    foreach (var index in keptIndices)
                        newMgeoMesh.Indices.Add((ushort)index);
                    mgeo.AddModel(newMgeoMesh);
                    if (!tooManyIndices)
                        mgeoCount += 1;
                }*/
                Console.WriteLine($"OBJ to MAPGEO Convert: room{i}.obj -> {room.Name}");
                Console.WriteLine($"Vertices:{vertices.Count}");
                Console.WriteLine($"Indices:{indices.Count}");
                Console.WriteLine("_________________________________________________________________________________");
              //Console.WriteLine(mgeoCount.ToString(""));
                
            }
            mgeo.AddModel(room);


            //mtl to league material format.

           
            
            
                }
            /*private static void NewMethod(List<uint> keptIndices, List<uint> sortedIndices, int p, uint verticesToRemove)
            {
                for (var j = 0; j <= keptIndices.Count - 1; j++)
                {
                    if (keptIndices[j] >= sortedIndices[p])
                        keptIndices[j] = keptIndices[j] - verticesToRemove;
                }
            }*/
        }
    } 

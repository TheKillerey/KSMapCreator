*Maps/KitPieces/Summoners_Rift/Materials/room1* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room1*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_e.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room2* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room2*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_d.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room3* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room3*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_c.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room4* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room4*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room5* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room5*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room6* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room6*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_f.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room7* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room7*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_g.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room8* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room8*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_h.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room9* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room9*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_i.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room10* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room10*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_j.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room11* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room11*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_o.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room12* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room12*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_n.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room13* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room13*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_m.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room14* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room14*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_l.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room15* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room15*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_k.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room16* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room16*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_p.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room17* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room17*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_q.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room18* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room18*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_r.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room19* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room19*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_s.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room20* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room20*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_t.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room21* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room21*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_y.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room22* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room22*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_x.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room23* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room23*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_w.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room24* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room24*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_v.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room25* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room25*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_u.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room26* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room26*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_vista_02.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room27* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room27*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bk_distant_horizon_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room28* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room28*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room29* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room29*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_a1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room30* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room30*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room31* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room31*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room32* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room32*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_a1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room33* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room33*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_a1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room34* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room34*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_a1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room35* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room35*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_a1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room36* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room36*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/grnd_terrain_w.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room37* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room37*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_scaffolding_modular.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room38* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room38*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room39* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room39*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room40* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room40*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room41* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room41*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room42* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room42*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room43* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room43*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room44* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room44*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room45* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room45*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room46* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room46*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room47* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room47*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room48* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room48*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_bridge_mid_crest_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room49* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room49*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_bridge_mid_crest_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room50* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room50*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room51* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room51*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/base_north_arches_periph.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room52* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room52*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Shared/Materials/white.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room53* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room53*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_C.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room54* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room54*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_south_island_c_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room55* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room55*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_south_island_c_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room56* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room56*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_e_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room57* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room57*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room58* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room58*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room59* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room59*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room60* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room60*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_crates_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room61* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room61*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Alcove_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room62* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room62*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_Alcove_Island_A.SRX_Polish.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room63* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room63*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Alcove_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room64* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room64*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Shared/Materials/white.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room65* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room65*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room66* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room66*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room67* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room67*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room68* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room68*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_north_walls_f_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room69* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room69*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_north_shop_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room70* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room70*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_D.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room71* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room71*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/BW_Prop_Sack1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room72* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room72*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room73* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room73*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_prop_pulley_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room74* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room74*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_prop_pulley_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room75* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room75*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room76* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room76*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_prop_pulley_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room77* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room77*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_prop_pulley_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room78* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room78*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room79* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room79*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_n_shop_barrier_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room80* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room80*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room81* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room81*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room82* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room82*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room83* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room83*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room84* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room84*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room85* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room85*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room86* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room86*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_ropes.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room87* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room87*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_ropes.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room88* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room88*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_coffin_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room89* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room89*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_cannonballpile.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room90* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room90*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_cannonballpile.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room91* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room91*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_cannonballpile.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room92* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room92*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_cannon_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room93* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room93*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_anchor_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room94* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room94*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room95* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room95*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room96* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room96*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room97* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room97*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_scaffolding_modular.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room98* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room98*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room99* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room99*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room100* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room100*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/jungle_north_island_fb.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room101* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room101*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/jungle_north_island_fa.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room102* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room102*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_skinny_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room103* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room103*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_skinny_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room104* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room104*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/house_tall_skinny_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room105* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room105*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_n_base_shrine.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room106* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room106*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room107* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room107*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room108* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room108*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room109* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room109*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room110* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room110*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room111* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room111*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room112* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room112*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room113* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room113*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room114* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room114*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room115* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room115*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room116* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room116*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room117* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room117*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room118* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room118*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room119* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room119*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room120* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room120*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room121* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room121*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room122* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room122*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room123* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room123*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room124* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room124*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room125* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room125*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room126* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room126*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room127* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room127*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room128* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room128*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room129* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room129*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room130* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room130*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room131* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room131*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room132* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room132*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room133* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room133*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room134* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room134*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room135* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room135*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_decor_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room136* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room136*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_props_harpoon_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room137* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room137*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/BW_Prop_Sack1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room138* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room138*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Sea-Ocean-Blue-Water-Texture-Pattern-Wallpaper.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room139* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room139*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Ryze.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room140* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room140*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Urgot_base_TX_CM.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room141* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room141*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_ropes.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room142* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room142*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/props_ropes.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room143* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room143*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/south_island_f_dragonpita.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room144* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room144*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/south_island_f_dragonpitb.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room145* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room145*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Sea-Ocean-Blue-Water-Texture-Pattern-Wallpaper1.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room146* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room146*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room147* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room147*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room148* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room148*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room149* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room149*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room150* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room150*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room151* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room151*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallSmall.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room152* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room152*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallSmall.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room153* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room153*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room154* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room154*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Pile_Anchor_Crate_Barrel.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room155* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room155*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room156* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room156*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_bridge_statue_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room157* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room157*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_bridge_statue_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room158* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room158*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_south_walls_c_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room159* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room159*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_south_walls_b_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room160* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room160*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_north_walls_d_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room161* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room161*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_base_north_walls_b_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room162* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room162*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/prop_sails.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room163* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room163*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_scaffolding_modular.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room164* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room164*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_wood_mast.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room165* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room165*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_windows_doors_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room166* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room166*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_wood_trim_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room167* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room167*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_wood_trim_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room168* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room168*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_wood_trim_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room169* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room169*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_wall_plaster_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room170* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room170*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_roof_tile_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room171* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room171*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_roof_tile_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room172* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room172*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_chimney_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room173* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room173*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_brick_base_01.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room174* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room174*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_struc_boat_roof_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room175* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room175*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_bridge_mid_cutout_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room176* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room176*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/mage_spawn_pad_b.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room177* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room177*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/pally_platform.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room178* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room178*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room179* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room179*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room180* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room180*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room181* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room181*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room182* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room182*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room183* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room183*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room184* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room184*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room185* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room185*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room186* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room186*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room187* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room187*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room188* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room188*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room189* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room189*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_perif_cliff_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room190* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room190*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room191* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room191*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room192* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room192*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room193* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room193*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room194* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room194*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/WallBig.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room195* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room195*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room196* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room196*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room197* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room197*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room198* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room198*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room199* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room199*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room200* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room200*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room201* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room201*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room202* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room202*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/bw_palm_frond_a.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room203* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room203*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room204* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room204*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_BlueCamp_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room205* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room205*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_BlueCamp_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room206* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room206*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_BlueCamp_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room207* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room207*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_BotLane_Island_C.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room208* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room208*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_BlueCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room209* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room209*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_east_island_b_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room210* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room210*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_east_island_b_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room211* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room211*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_BotLane_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room212* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room212*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_Midlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room213* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room213*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_WolfCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room214* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room214*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_east_island_h_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room215* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room215*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_Midlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room216* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room216*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_RaptorCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room217* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room217*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_Midlane_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room218* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room218*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_d_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room219* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room219*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_RedCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room220* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room220*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_TopLane_Island_E.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room221* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room221*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_North_TopLane_Island_E.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room222* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room222*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_j_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room223* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room223*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_TopJungle_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room224* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room224*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_k_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room225* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room225*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_TopJungle_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room226* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room226*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_North_TopJungle_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room227* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room227*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_l_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room228* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room228*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_l_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room229* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room229*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_north_island_i_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room230* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room230*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_River_Midlane_Island_C.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room231* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room231*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_west_island_h_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room232* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room232*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Toplane_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room233* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room233*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_BlueCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room234* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room234*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Toplane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room235* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room235*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_BlueCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room236* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room236*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Toplane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room237* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room237*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_BlueCamp_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room238* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room238*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_WolfCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room239* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room239*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Midlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room240* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room240*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Toplane_Island_C.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room241* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room241*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_River_DragonCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room242* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room242*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_River_DragonCamp_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room243* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room243*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_BotJungle_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room244* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room244*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Botlane_Island_D.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room245* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room245*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Jungle_South_BotJungle_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room246* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room246*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_RaptorCamp_Island_A.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room247* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room247*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/_chunk_jungle_south_island_d_alpha_3dcuv_atlas_color.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )
*Maps/KitPieces/Summoners_Rift/Materials/room248* = StaticMaterialDef (
        name: string = *Maps/KitPieces/Summoners_Rift/Materials/room248*
        type: u32 = 0
        defaultTechnique: string = *normal*
        samplerValues: list[embed] = (
            StaticMaterialShaderSamplerDef (
                samplerName: string = *DiffuseTexture*
                textureName: string = *ASSETS/Maps/KitPieces/SRX/bildgewater/Terrain_South_Botlane_Island_B.SRX_EnvArt.dds*
                addressW: u32 = 1
            )
        )
        paramValues: list[embed] = (
            StaticMaterialShaderParamDef (
                name: string = *AlphaTestValue*
                value: vec4 = ( 0.300000012, 0, 0, 0 )
            )
        )
        shaderMacros: map[string,string] = (
            *NO_BAKED_LIGHTING* = *1*
            *DISABLE_DEPTH_FOG* = *1*
            *PREMULTIPLIED_ALPHA* = *1*
        )
        techniques: list[embed] = (
            StaticMaterialTechniqueDef (
                name: string = *normal*
                passes: list[embed] = (
                    StaticMaterialPassDef (
                        shader: link = *Shaders/Environment/DefaultEnv_Flat_AlphaTest*
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    )
                )
            )
        )
    )

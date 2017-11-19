import json

import cloud

# Scraped from municode using http://github.com/bdougsand/ordinance_scrape_scripts
XREF = {
  "1": [
    "Purpose And Scope",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART1PUSC"
  ],
  "1.1": [
    "Title.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART1PUSC_S1.1TI"
  ],
  "1.2": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART1PUSC_S1.2PU"
  ],
  "1.3": [
    "Interpretation.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART1PUSC_S1.3IN"
  ],
  "1.4": [
    "Scope.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART1PUSC_S1.4SC"
  ],
  "2": [
    "Definitions",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART2DE"
  ],
  "2.1": [
    "General.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART2DE_S2.1GE"
  ],
  "2.2": [
    "Definitions.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART2DE_S2.2DE"
  ],
  "3": [
    "Enforcement, Board Of Appeals, And Amendments",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM"
  ],
  "3.1": [
    "Enforcement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM_S3.1EN"
  ],
  "3.2": [
    "The Board Of Appeals.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM_S3.2THBOAP"
  ],
  "3.3": [
    "Amendments.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM_S3.3AM"
  ],
  "3.4": [
    "Zoning Administrator.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM_S3.4ZOAD"
  ],
  "3.5": [
    "Planning Board.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART3ENBOAPAM_S3.5PLBO"
  ],
  "4": [
    "Nonconforming Uses And Structures",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST"
  ],
  "4.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST_S4.1PU"
  ],
  "4.2": [
    "Effective Dates.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST_S4.2EFDA"
  ],
  "4.3": [
    "Continuation Of Nonconforming Uses Or Structures.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST_S4.3CONOUSST"
  ],
  "4.4": [
    "Nonconforming Structures.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST_S4.4NOST"
  ],
  "4.5": [
    "Nonconforming Uses.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART4NOUSST_S4.5NOUS"
  ],
  "5": [
    "Administration",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD"
  ],
  "5.1": [
    "Special Permits.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.1SPPE"
  ],
  "5.2": [
    "Special Permits With Site Plan Review.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.2SPPESIPLRE"
  ],
  "5.3": [
    "Procedures For Special Permits And Special Permits With Site Plan Review.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.3PRSPPESPPESIPLRE"
  ],
  "5.4": [
    "Design And Site Plan Review.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.4DESIPLRE"
  ],
  "5.5": [
    "Variances.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.5VA"
  ],
  "5.6": [
    "Design Review Committee.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.6DERECO"
  ],
  "5.7": [
    "Neighborhood Development Plan Review.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART5AD_S5.7NEDEPLRE"
  ],
  "6": [
    "Establishment Of Zoning Districts",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI"
  ],
  "6.1": [
    "Division Of City Into Districts.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.1DIINDI"
  ],
  "6.2": [
    "Establishment Of District Boundaries.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.2ESDIBO"
  ],
  "6.3": [
    "Interpretation Of The Zoning Map.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.3INZOMA"
  ],
  "6.4": [
    "Assembly Square Mixed-Use District (Asmd).",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.4ASSQMIEDIAS"
  ],
  "6.5": [
    "Transit Oriented Districts (Tods).",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.5TRORDITO"
  ],
  "6.6": [
    "North Point Special District.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.6NOPOSPDI"
  ],
  "6.7": [
    "Powderhouse School Redevelopment District (Prd).",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART6ESZODI_S6.7POSCREDIPR"
  ],
  "7": [
    "Permitted Uses",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS"
  ],
  "7.1": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.1AP"
  ],
  "7.2": [
    "Principal Structure.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.2PRST"
  ],
  "7.3": [
    "Maximum Dwelling Units Per Lot.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.3MADWUNPELO"
  ],
  "7.4": [
    "Lots In Two Districts.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.4LOTWDI"
  ],
  "7.5": [
    "Lots In Two Or More Municipalities.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.5LOTWMOMU"
  ],
  "7.6": [
    "Use Of Symbols In Table Of Permitted Uses.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.6USSYTAPEUS"
  ],
  "7.7": [
    "Uses Not Listed In Table Of Permitted Uses Are Prohibited.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.7USNOLITAPEUSARPR"
  ],
  "7.8": [
    "More Than One Classification.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.8MOONCL"
  ],
  "7.9": [
    "Compliance With All Standards.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.9COALST"
  ],
  "7.10": [
    "Change In Use.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.10CHUS"
  ],
  "7.11": [
    "Table Of Permitted Uses.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.11TAPEUS"
  ],
  "7.12": [
    "Footnotes To Table Of Permitted Uses.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.12FOTAPEUS"
  ],
  "7.13": [
    "Table Of Use Clusters.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.13TAUSCL"
  ],
  "7.14": [
    "Pedestrian Oriented Use Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.14PEORUSRE"
  ],
  "7.15": [
    "Medical Marijuana Facilities.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART7PEUS_S7.15MEMAFA"
  ],
  "8": [
    "Dimensional Requirements",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE"
  ],
  "8.1": [
    "Content Of Table Of Dimensional Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.1COTADIRE"
  ],
  "8.2": [
    "Compliance With Dimensional Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.2CODIRE"
  ],
  "8.3": [
    "Lots In Two Districts.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.3LOTWDI"
  ],
  "8.4": [
    "Lots In Two Or More Municipalities.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.4LOTWMOMU"
  ],
  "8.5": [
    "Table Of Dimensional Requirements",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.5TADIRE"
  ],
  "8.6": [
    "Footnotes To Section 8.5.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.6FOSE8.5"
  ],
  "8.7": [
    "Dimensional Requirements Applicable To The University District.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.7DIREAPUNDI"
  ],
  "8.8": [
    "Reserved.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART8DIRE_S8.8RE"
  ],
  "9": [
    "Off-Street Parking And Loading",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO"
  ],
  "9.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.1PU"
  ],
  "9.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.2AP"
  ],
  "9.3": [
    "Changes In Numbers Of Existing Parking Or Loading Spaces.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.3CHNUEXPALOSP"
  ],
  "9.4": [
    "Nonconformity With Respect To Parking Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.4NOREPARE"
  ],
  "9.5": [
    "Number Of Parking Spaces.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.5NUPASP"
  ],
  "9.6": [
    "Special Provisions And Rules For Interpretation Of Sections 9.5 And 9.7.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.6SPPRRUINSE9.59.7"
  ],
  "9.7": [
    "Numbers Of Required Loading Bays.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.7NURELOBA"
  ],
  "9.8": [
    "Location Of Off-Street Parking, Loading Bays.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.8LOOREPALOBA"
  ],
  "9.9": [
    "Driveways, Access, And Lighting Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.9DRACLIRE"
  ],
  "9.10": [
    "Landscaping And Screening.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.10LASC"
  ],
  "9.11": [
    "Dimensions Of Parking Spaces And Maneuvering Aisles.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.11DIPASPMAAI"
  ],
  "9.12": [
    "Dimensions Of Loading Bays.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.12DILOBA"
  ],
  "9.13": [
    "Exceptions, Special Permits.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.13EXSPPE"
  ],
  "9.14": [
    "Parking Space And Loading Area Requirements In The University District.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.14PASPLOARREUNDI"
  ],
  "9.15": [
    "Bicycle Access And Parking.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.15BIACPA"
  ],
  "9.16": [
    "Parking Space And Loading Area Requirements In The Assembly Square Mixed-Use District (Asmd) And The Pud-A District.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.16PASPLOARREASSQMIEDIASPDI"
  ],
  "9.17": [
    "Parking Space And Loading Area Requirements In The Transit Oriented Districts (Tods) And Corridor Commercial Districts (Ccds).",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART9OREPALO_S9.17PASPLOARRETRORDITOCOCODICC"
  ],
  "10": [
    "Landscaping And Screening",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC"
  ],
  "10.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.1PU"
  ],
  "10.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.2AP"
  ],
  "10.5": [
    "Screening Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.5SCRE"
  ],
  "10.6": [
    "Landscaping Specifications.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.6LASP"
  ],
  "10.7": [
    "Fences And Barbed Wire.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.7FEBAWI"
  ],
  "10.8": [
    "Encroachment.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.8EN"
  ],
  "10.9": [
    "Administration And Enforcement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART10LASC_S10.9ADEN"
  ],
  "11": [
    "Noise",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART11NO"
  ],
  "12": [
    "Signs",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI"
  ],
  "12.1": [
    "Findings And Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.1FIPU"
  ],
  "12.2": [
    "General Prohibition.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.2GEPR"
  ],
  "12.3": [
    "Signs In Residence Districts.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.3SIREDI"
  ],
  "12.4": [
    "Signs In Nonresidential Districts.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.4SINODI"
  ],
  "12.5": [
    "Parking And Directional Signs.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.5PADISI"
  ],
  "12.6": [
    "Pertinence To Other Laws.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.6PEOTLA"
  ],
  "12.7": [
    "Nonconforming Signs.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.7NOSI"
  ],
  "12.8": [
    "Enforcement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.8EN"
  ],
  "12.9": [
    "Penalty For Violation.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.9PEVI"
  ],
  "12.10": [
    "Severability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART12SI_S12.10SE"
  ],
  "13": [
    "Inclusionary Housing",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO"
  ],
  "13.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.1PU"
  ],
  "13.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.2AP"
  ],
  "13.3": [
    "General Requirements.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.3GERE"
  ],
  "13.4": [
    "Alternative Methods Of Compliance.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.4ALMECO"
  ],
  "13.5": [
    "Incentives For Provision Of Additional Affordable Housing Units.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.5INPRADAFHOUN"
  ],
  "13.6": [
    "Procedures.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.6PR"
  ],
  "13.7": [
    "Implementation, Compliance And Enforcement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.7IMCOEN"
  ],
  "13.8": [
    "Needs Assessment Review.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.8NEASRE"
  ],
  "13.9": [
    "Reinstatement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART13INHO_S13.9RE"
  ],
  "14": [
    "Wireless Communication",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO"
  ],
  "14.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.1PU"
  ],
  "14.2": [
    "Applicability And Exemptions.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.2APEX"
  ],
  "14.3": [
    "Location And Design Guidelines.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.3LODEGU"
  ],
  "14.4": [
    "Application Process.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.4APPR"
  ],
  "14.5": [
    "Special Permit Review Procedures.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.5SPPEREPR"
  ],
  "14.6": [
    "Non-Use And Abandonment.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART14WICO_S14.6NEAB"
  ],
  "15": [
    "Linkage",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI"
  ],
  "15.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.1PU"
  ],
  "15.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.2AP"
  ],
  "15.3": [
    "Project Mitigation Contribution.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.3PRMICO"
  ],
  "15.4": [
    "Compliance And Enforcement.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.4COEN"
  ],
  "15.5": [
    "Formula Recalculation.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.5FORE"
  ],
  "15.6": [
    "Administration.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART15LI_S15.6AD"
  ],
  "16": [
    "Planned Unit Development (Pud)",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU"
  ],
  "16.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.1PU"
  ],
  "16.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.2AP"
  ],
  "16.3": [
    "Permit Authority And Designation Of A Planned Unit Development.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.3PEAUDEPLUNDE"
  ],
  "16.4": [
    "General Requirements And Features Of Pud.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.4GEREFEPU"
  ],
  "16.5": [
    "Pud Conformance With Standards.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.5PUCOST"
  ],
  "16.6": [
    "Pud Usable Open Space.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.6PUUSOPSP"
  ],
  "16.7": [
    "Pud Design Guidelines.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.7PUDEGU"
  ],
  "16.8": [
    "Procedures For Application For Pud.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.8PRAPPU"
  ],
  "16.9": [
    "Spga Review Of Pud Application.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.9SPREPUAP"
  ],
  "16.10": [
    "Effect Of Approval.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.10EFAP"
  ],
  "16.11": [
    "Amendments To Pud Plans.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.11AMPUPL"
  ],
  "16.12": [
    "Reserved.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART16PLUNDEPU_S16.12RE"
  ],
  "17": [
    "Usable Open Space",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP"
  ],
  "17.1": [
    "Purpose.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.1PU"
  ],
  "17.2": [
    "Applicability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.2AP"
  ],
  "17.3": [
    "General Standards For Usable Open Space.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.3GESTUSOPSP"
  ],
  "17.4": [
    "Incentives To Provide Usable Open Space.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.4INPRUSOPSP"
  ],
  "17.5": [
    "Public Dedication Of Usable Open Space.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.5PUDEUSOPSP"
  ],
  "17.6": [
    "Public Hearing.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.6PUHE"
  ],
  "17.7": [
    "Rezoning Of Usable Open Space.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART17USOPSP_S17.7REUSOPSP"
  ],
  "18": [
    "General Provisions",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART18GEPR"
  ],
  "18.1": [
    "Validity And Separability.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART18GEPR_S18.1VASE"
  ],
  "18.2": [
    "In Effect.",
    "https://library.municode.com/ma/somerville/codes/zoning_ordinances?nodeId=ZOORSOMA_ART18GEPR_S18.2INEF"
  ]
}

@cloud.aws_lambda
def getref(req):
    section = req["ordinance_section"]
    if not section:
        return (500, {"error": "ordinance_section parameter missing"})

    subsection = section
    while subsection:
        if subsection in XREF:
            (_title, url) = XREF[subsection]
            return (302, {"location": url}, "")

        if "." in subsection:
            subsection = subsection.rsplit(".", 1)[0]
        else:
            break

    return (404, {"error": f"No article {section} exists."})

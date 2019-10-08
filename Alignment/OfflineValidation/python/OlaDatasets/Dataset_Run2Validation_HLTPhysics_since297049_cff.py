import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList

lumiSecs = cms.untracked.VLuminosityBlockRange()
goodLumiSecs = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSALCA/ALCA_TRACKERALIGN/MP/MPproduction/datasetfiles/UltraLegacy/2017/brute_force_method_v2/HLTPhysics_Run2017ABCDEFGH-TkAlMinBias-PromptReco-v123_ALCARECO/Golden.json').getCMSSWString().split(',')
readFiles = cms.untracked.vstring()
source = cms.Source("PoolSource",
                    lumisToProcess = lumiSecs,
                    fileNames = readFiles)
readFiles.extend([
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/114/00000/7AA04DC6-3157-E711-9472-02163E014329.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/164/00000/7058C30E-2A57-E711-A0B5-02163E019B22.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/E4E2408A-6A56-E711-8A4E-02163E019C00.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/052/00000/A83E8822-4856-E711-8C70-02163E0120FA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/158/00000/06B469A5-2D57-E711-BC7C-02163E014348.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/E873B683-0B57-E711-8305-02163E01A354.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/068/00000/5C6E5B1E-9056-E711-A289-02163E012AEE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/1A29FB9A-EB56-E711-97D3-02163E01A590.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/144/00000/58CC0882-2E57-E711-8B6A-02163E019C43.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/983AE01D-D156-E711-88A0-02163E019D7B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/051/00000/08720715-4856-E711-81C7-02163E014252.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/067/00000/E07CA1DE-8D56-E711-8DA1-02163E01A5E2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/34B61015-6A56-E711-8039-02163E013750.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/069/00000/6850EAC4-8F56-E711-8D83-02163E01A708.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/D447B582-5356-E711-B78B-02163E01262D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/2E87BD32-1F57-E711-950B-02163E0141D8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/8E783A76-4A56-E711-9D6F-02163E01A427.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/148/00000/C8ADA71E-2957-E711-802E-02163E0145D1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/094/00000/7C9BCFB8-8E56-E711-956C-02163E019C0B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/8C17E871-6257-E711-8666-02163E011D4F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/139/00000/DCDC7631-2C57-E711-B51D-02163E01A5A3.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/150/00000/36B3DFA1-2757-E711-B709-02163E01A288.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/36845A21-0757-E711-B1AD-02163E014484.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/0037BE70-1D57-E711-9CD8-02163E0144F4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/099/00000/10CCAC89-AB58-E711-BD79-02163E01A29D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/053/00000/8A71D578-4E56-E711-B663-02163E01A4B6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/EA172915-0757-E711-9EE3-02163E011A70.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/4C28DB2B-4F56-E711-9516-02163E01189C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/108/00000/08007BF3-0757-E711-8127-02163E01A23E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/9208A61A-2357-E711-89FF-02163E01A6B4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/30CFA0AE-0257-E711-A9A3-02163E011E07.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/129/00000/6435B19B-2957-E711-B378-02163E0145D3.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/DC3D89D8-7A57-E711-AA4D-02163E01397F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/38BDC24F-6757-E711-82F1-02163E01A6B8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/44239BF2-0657-E711-96E6-02163E011806.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/056/00000/4E7C03CE-6F56-E711-B53A-02163E01A40B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/072/00000/CAEFCC3E-9656-E711-B2AE-02163E0120C8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/160CF0DF-D756-E711-B1D4-02163E019BAC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/B2D925C8-B758-E711-83D1-02163E019B95.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/093/00000/EE0E9EA1-9756-E711-9462-02163E0142EE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/138/00000/D469F92A-2B57-E711-A5B5-02163E0143D0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/667E5E9C-6C57-E711-9E82-02163E01A532.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/4271935F-6A56-E711-BE00-02163E019D49.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/6A08B52C-6256-E711-B390-02163E01A3DD.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/176/00000/6634CF1F-5457-E711-9096-02163E013481.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/2276620E-6256-E711-8D01-02163E01A6DF.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/160/00000/EA8BD82B-2C57-E711-AEC7-02163E011F53.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/C4822211-FF56-E711-819C-02163E011B0F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/763F67B9-6B57-E711-B6F8-02163E01A583.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/F03D3146-7556-E711-9939-02163E019E30.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/50093463-5C56-E711-951E-02163E013655.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/2C6F7D17-4F56-E711-86F2-02163E014318.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/B6E1532A-4656-E711-8837-02163E013876.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/114/00000/56DCB0BE-3657-E711-AA24-02163E01A69C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/CA4DF872-FB56-E711-BDC9-02163E01A288.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/104/00000/0040F8AE-0F57-E711-965F-02163E01A3AB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/942BD27A-5E56-E711-9CFD-02163E01A238.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/127/00000/EC260CAE-2957-E711-96FB-02163E011F67.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/121/00000/EA8B79C1-2757-E711-A870-02163E01A766.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/7A47CC3B-4B57-E711-B590-02163E011B0E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/112/00000/5E4CF41C-0E57-E711-94CD-02163E019CE6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/28EA9B62-2257-E711-ADBE-02163E013595.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/1C63F334-6956-E711-BEA8-02163E011E6C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/106/00000/30FB067D-0657-E711-B97E-02163E01A5BB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/120/00000/68B29A8C-2D57-E711-8481-02163E011B6B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/107/00000/5EE19E0E-0A57-E711-83A5-02163E012A00.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/7CEA4926-6256-E711-977F-02163E01398A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/065/00000/2A44CC13-9056-E711-B89B-02163E01A53E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/096/00000/D87658B5-9556-E711-B634-02163E01A2C2.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/118/00000/5820FC89-3957-E711-BCA7-02163E01A30A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/4C31E862-1A57-E711-A502-02163E019DAA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/177/00000/BA2B06BE-7E57-E711-AD58-02163E0143D0.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/EA270889-4A56-E711-95BE-02163E01A566.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/171/00000/6CB52872-6257-E711-BCFC-02163E014741.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/2E549DD2-D756-E711-AA6A-02163E013446.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/114/00000/8652FDDB-3F57-E711-BA79-02163E0145F6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/056/00000/56A9EC54-7A56-E711-BB8C-02163E014352.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/156/00000/2E73B995-2957-E711-A142-02163E01219C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/001B8ABD-A658-E711-A4CD-02163E0119F5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/28EDAD92-0F57-E711-9A9C-02163E019B92.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/161/00000/F23E10DA-2B57-E711-B43F-02163E019D8D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/061/00000/4C3DE88E-8D56-E711-927D-02163E01A545.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/6272D05D-8156-E711-8BA5-02163E011C61.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/0EA94E88-9A57-E711-B2A0-02163E0142DE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/056/00000/4481B0E7-6756-E711-A27F-02163E013586.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/117/00000/5C0F7612-3557-E711-A59D-02163E019C1F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/DC787607-8357-E711-8765-02163E012492.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/177/00000/6E56429D-6157-E711-AEE6-02163E0138FB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/162/00000/10F27175-2B57-E711-9C12-02163E01A338.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/175/00000/8631BE90-4F57-E711-9356-02163E01A1D9.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/FCE18C2D-FF56-E711-89CD-02163E014593.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/BC72A290-5E56-E711-B7CE-02163E01440C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/049/00000/2CE3C289-4156-E711-964F-02163E013481.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/114/00000/B2FAA043-5B57-E711-9881-02163E01A2FE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/119/00000/A6D7D573-3457-E711-AEEF-02163E01A6FE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/166/00000/FC3648AF-2B57-E711-A8B0-02163E012B9E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/168/00000/167EE862-4957-E711-BC45-02163E01A37D.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/16C2A50C-D156-E711-9356-02163E01A739.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/56221C72-DC56-E711-8E43-02163E014470.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/3EBD2B53-2757-E711-B707-02163E013524.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/3203D619-FF56-E711-A951-02163E0143BC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/170/00000/FC96CD2C-3757-E711-9791-02163E0145D1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/602F783B-6E56-E711-9084-02163E011D9E.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/3CB6FC6F-E356-E711-ADA4-02163E014472.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/116/00000/86069AFB-1F57-E711-B3C2-02163E0143DE.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/F43EE40A-6256-E711-A9E0-02163E01A3AC.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/C0C14A1F-0B57-E711-B2C7-02163E0128F8.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/178/00000/4AE22138-7057-E711-9D9A-02163E01A314.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/114/00000/643EA019-6357-E711-95A0-02163E019E36.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/176/00000/9A1C861D-6557-E711-923A-02163E0136BA.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/124/00000/82EE8ED0-3057-E711-A701-02163E011F14.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/0AB80720-4F56-E711-8F8F-02163E0142A6.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/056/00000/42D078B3-8B56-E711-B0AD-02163E011951.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/8C0422BA-0257-E711-92B7-02163E01186A.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/141/00000/2E25ED69-2E57-E711-BE1B-02163E01A553.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/E2295BA5-CC56-E711-BD93-02163E011A55.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/103/00000/CA0BB8A1-1757-E711-8491-02163E0118F3.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/3AA76D72-4A56-E711-B317-02163E01A6D1.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/130/00000/D034FBB1-2B57-E711-8D69-02163E014176.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/057/00000/80DAAC30-6A56-E711-83DB-02163E0141D9.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/050/00000/B4F73412-C158-E711-8E42-02163E0142C5.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/A8F4209E-1D57-E711-A385-02163E01190F.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/154/00000/10BE1B51-2A57-E711-985A-02163E011B14.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/125/00000/E80B81D5-2E57-E711-814C-02163E011B4B.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/CA195D44-2657-E711-A5FD-02163E0141F4.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/820736F7-3557-E711-B5E3-02163E0133A7.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/7ADC3DD6-D756-E711-AB29-02163E019D92.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/167/00000/58E4ECB7-2957-E711-A276-02163E019C6C.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/1E0191BB-3057-E711-9CD2-02163E01A730.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/169/00000/AE7A5733-3E57-E711-A7DB-02163E01A1DD.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/163/00000/00FF5E9A-2B57-E711-8CE0-02163E011988.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/100/00000/A0A08C78-F256-E711-9AE3-02163E012081.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/099/00000/5C06AA34-C056-E711-BE13-02163E013998.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/056/00000/509D3608-6256-E711-87C9-02163E01A354.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/123/00000/5AC92D71-2A57-E711-A85E-02163E011B37.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/101/00000/A26DA1E8-0257-E711-8774-02163E011E27.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/074/00000/7232D0B9-9656-E711-B6DA-02163E01A1DB.root',
'/store/data/Run2017B/HLTPhysics/ALCARECO/TkAlMinBias-PromptReco-v1/000/297/113/00000/927625B1-3057-E711-A7C8-02163E01A3B1.root'
])
lumiSecs.extend(goodLumiSecs)
maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

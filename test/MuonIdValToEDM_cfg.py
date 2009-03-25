import FWCore.ParameterSet.Config as cms

process = cms.Process("MUONIDVALtoEDM")

process.load("DQMServices.Components.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:/tmp/jribnik/bah.root")
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'IDEAL_30X::All'
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.CommonDetUnit.globalTrackingGeometry_cfi")

process.load("Validation.MuonIdentification.muonIdVal_cff")
process.muonIdVal.inputMuonCollection = cms.InputTag("muons")
process.muonIdVal.inputDTRecSegment4DCollection = cms.InputTag("dt4DSegments")
process.muonIdVal.inputCSCSegmentCollection = cms.InputTag("cscSegments")
process.muonIdVal.useTrackerMuons = cms.untracked.bool(True)
process.muonIdVal.useGlobalMuons = cms.untracked.bool(True)
process.muonIdVal.makeEnergyPlots = cms.untracked.bool(True)
process.muonIdVal.make2DPlots = cms.untracked.bool(True)
process.muonIdVal.makeAllChamberPlots = cms.untracked.bool(False)
process.muonIdVal.baseFolder = cms.untracked.string("Muons/MuonIdVal")
process.muonIdDQM.inputMuonCollection = process.muonIdVal.inputMuonCollection
process.muonIdDQM.inputDTRecSegment4DCollection = process.muonIdVal.inputDTRecSegment4DCollection
process.muonIdDQM.inputCSCSegmentCollection = process.muonIdVal.inputCSCSegmentCollection
process.muonIdDQM.useTrackerMuons = process.muonIdVal.useTrackerMuons
process.muonIdDQM.useGlobalMuons = process.muonIdVal.useGlobalMuons
process.muonIdDQM.baseFolder = process.muonIdVal.baseFolder

process.load("DQMServices.Components.MEtoEDMConverter_cff")

process.out = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("drop *", 
        "keep *_MEtoEDMConverter_*_*", 
        "keep *_*_*_MUONIDVALtoEDM"),
    fileName = cms.untracked.string("file:/tmp/jribnik/meh.root")
)

process.p = cms.Path(process.muonIdValDQMSeq*process.MEtoEDMConverter)
process.e = cms.EndPath(process.out)

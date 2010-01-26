# Unit test configuration file for 
# LoggerErrorsSummary() and  LoggerErrorsOnlySummary()

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

import FWCore.Framework.test.cmsExceptionsFatal_cff
process.options = FWCore.Framework.test.cmsExceptionsFatal_cff.options

process.MessageLogger = cms.Service("MessageLogger",
    default = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    statistics = cms.untracked.vstring('u31_infos'),
    u31_infos = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO'),
        noTimeStamps = cms.untracked.bool(True),
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        preEventProcessing = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        )
    ),
    categories = cms.untracked.vstring('preEventProcessing', 
        'FwkJob', 
        'timer', 
        'trace'),
    destinations = cms.untracked.vstring('u31_infos')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(16)
)

process.source = cms.Source("EmptySource")

process.ssm_1a = cms.EDAnalyzer("UTC_T1",
    identifier = cms.untracked.int32(11)
)

process.ssm_1b = cms.EDAnalyzer("UTC_T1",
    identifier = cms.untracked.int32(12)
)

process.ssm_1c = cms.EDAnalyzer("UTC_T1",
    identifier = cms.untracked.int32(13)
)

process.ssm_2a = cms.EDAnalyzer("UTC_T2",
    identifier = cms.untracked.int32(21)
)

process.ssm_2b = cms.EDAnalyzer("UTC_T2",
    identifier = cms.untracked.int32(22)
)

process.ssm_2c = cms.EDAnalyzer("UTC_T2",
    identifier = cms.untracked.int32(23)
)

process.p = cms.Path(process.ssm_1a*process.ssm_2a*process.ssm_1b*process.ssm_2b*process.ssm_1c*process.ssm_2c)

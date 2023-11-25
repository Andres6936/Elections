export type TypeCandidates = {
    Candidate: string,
    PoliticalParty: string,
    Serial: string,
}

export type TypeElectionsNational = {
    Department: string,
    Municipality: string,
    Stand: string,
    VotingTable: string,
    Votes: number,
    Candidate: string,
    Serial: string,
}

export type TypeElectionsNative = {
    Department: string,
    Municipality: string,
    Stand: string,
    VotingTable: string,
    Votes: number,
    Candidate: string,
    Serial: string,
}

export type TypeIncomeBase = {
    CandidateIdentification: number,
    Consul: string,
    TypeCandidate: string,
    Department: string,
    Municipality: string,
    Location: string,
    PoliticalParty: string,
    Candidate: string,
    TypeContributor: string,
    ContributorName: string,
    ContributionValue: string,
    TypeIdentificationContribute: string,
    ContributeIdentification: string,
    Acta: string,
    TypeContribution: string,
    Coalition: string,
    VoucherDate: string,
    Voucher: string,
    Concept: string,
    Serial: string,
}

export type TypeItems = {
    Serial: string,
    Line: number,
    Item: string,
    Price: number,
    Amount: number,
    UoM: string,
    Total: string,
    CDP: string,
}

export type TypeSenator = {
    TypeIdentification: string,
    Identification: number,
    Name: string,
    Serial: string,
}

export type TypeSenatorExpense = {
    Consul: string,
    District: string,
    Department: string,
    PoliticalParty: string,
    Concept: string,
    Name: string,
    TypePerson: string,
    Value: string,
    DescriptionConcept: string,
    TypePropaganda: string,
    Senator: string,
    Serial: string,
}

export type PaginationModel = {
    skip: number,
    limit: number,
}
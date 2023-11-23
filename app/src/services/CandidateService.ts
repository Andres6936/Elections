import {PaginationModel, TypeCandidates} from "../types/TypeCandidates";

export class CandidateService {
    private readonly BASE_URL: string = "http://127.0.0.1:8000"

    public async getAllCandidates(pagination: PaginationModel): Promise<TypeCandidates[]> {
        const stream = await fetch(`${this.BASE_URL}/candidate?skip=${pagination.skip}&limit=${pagination.limit}`, {
            method: "GET",
        })
        return stream.json()
    }
}
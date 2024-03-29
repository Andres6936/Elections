import {PaginationModel, TypeCandidates} from "../types/TypeServices";
import {BaseService} from "./BaseService";

export class CandidateService extends BaseService<TypeCandidates> {
    public async getAllCandidates(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("candidate", pagination);
    }
}
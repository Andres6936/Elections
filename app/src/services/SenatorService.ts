import {BaseService} from "./BaseService";
import {PaginationModel, TypeCandidates} from "../types/TypeCandidates";

export class SenatorService extends BaseService<any> {
    public async getAllSenator(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("senator", pagination);
    }

    public async getAllSenatorExpense(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("senatorexpense", pagination);
    }
}
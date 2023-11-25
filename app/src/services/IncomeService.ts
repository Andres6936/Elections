import {BaseService} from "./BaseService";
import {PaginationModel, TypeCandidates} from "../types/TypeCandidates";

export class IncomeService extends BaseService<any> {
    public async getAllIncome(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("incomebase", pagination);
    }
}
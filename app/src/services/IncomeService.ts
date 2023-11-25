import {BaseService} from "./BaseService";
import {PaginationModel, TypeIncomeBase} from "../types/TypeServices";

export class IncomeService extends BaseService<TypeIncomeBase> {
    public async getAllIncome(pagination: PaginationModel): Promise<TypeIncomeBase[]> {
        return this.getAll("incomebase", pagination);
    }
}
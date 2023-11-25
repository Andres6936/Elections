import {BaseService} from "./BaseService";
import {PaginationModel, TypeSenatorExpense} from "../types/TypeServices";

export class SenatorService extends BaseService<TypeSenatorExpense> {
    public async getAllSenatorExpense(pagination: PaginationModel): Promise<TypeSenatorExpense[]> {
        return this.getAll("senatorexpense", pagination);
    }
}
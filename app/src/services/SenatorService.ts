import {BaseService} from "./BaseService";
import {PaginationModel, TypeSenator} from "../types/TypeServices";

export class SenatorService extends BaseService<TypeSenator> {
    public async getAllSenator(pagination: PaginationModel): Promise<TypeSenator[]> {
        return this.getAll("senator", pagination);
    }
}
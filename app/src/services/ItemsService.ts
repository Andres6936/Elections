import {PaginationModel, TypeCandidates} from "../types/TypeCandidates";
import {BaseService} from "./BaseService";

export class ItemsService extends BaseService<any> {
    public async getAllItems(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("items", pagination);
    }
}
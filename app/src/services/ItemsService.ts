import {PaginationModel, TypeItems} from "../types/TypeServices";
import {BaseService} from "./BaseService";

export class ItemsService extends BaseService<TypeItems> {
    public async getAllItems(pagination: PaginationModel): Promise<TypeItems[]> {
        return this.getAll("items", pagination);
    }
}
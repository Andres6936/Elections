import {BaseService} from "./BaseService";
import {PaginationModel, TypeCandidates} from "../types/TypeCandidates";

export class ElectionsService extends BaseService<any> {
    public async getAllElectionsNational(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("electionsnational", pagination);
    }

    public async getAllElectionsNative(pagination: PaginationModel): Promise<TypeCandidates[]> {
        return this.getAll("electionsnative", pagination);
    }
}
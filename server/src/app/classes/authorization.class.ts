import {AuthProvider,TStringOrNumber} from "@sugoi/server";

export class Authorization extends AuthProvider<any> {
    /**
     * Verify if the user is authorized
     *
     * @returns {Promise<boolean>}
     */
    isAuthenticated(): Promise<boolean> {
        return Promise.resolve(true);
    }


    /**
    * Verify if the user has the right permissions
    *
    * @returns {Promise<boolean>}
    */
    isAllowedTo(...permissions: TStringOrNumber[]): Promise<boolean> {
            return Promise.resolve(null);
    }


    /**
    * Verify if the user is in the right role
    *
    * @returns {Promise<boolean>}
    */
    isInRole(...roles: TStringOrNumber[]): Promise<boolean> {
        return Promise.resolve(null);
    }


    /**
    * Retrieve the user and store it in cache for later use
    *
    * @returns {Promise<boolean>}
    */
    async getUser(req, res, next): Promise<any> {
        let userData = await this.getUserData();
        if(!userData){
            userData = await Promise.resolve(null).then(_userData=>{
                this.setUserData(_userData);
                return _userData;
            });
        }
        return userData;
    }




    isResourceOwner(resourceId: any): Promise<boolean> {
        return Promise.resolve(null);
    }

}

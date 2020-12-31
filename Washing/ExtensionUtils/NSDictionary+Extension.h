//
//  NSDictionary+Extension.h
//  Washing
//
//  Created by Quốc Tuyến on 12/2/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface NSDictionary (Extension)

+ (NSDictionary *)dictionaryWithJsonifiedString:(NSString *)jsonified;

@end

NS_ASSUME_NONNULL_END

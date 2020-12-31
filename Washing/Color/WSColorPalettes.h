//
//  ColorPalettes.h
//  Washing
//
//  Created by Quốc Tuyến on 12/2/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <Foundation/Foundation.h>

@class UIColor;

NS_ASSUME_NONNULL_BEGIN

@interface WSColorPalettes : NSObject

- (instancetype)initWithJsonified:(NSString *)jsonifiedString;

- (UIColor *)colorWithKey:(NSString *)key;

@end

NS_ASSUME_NONNULL_END

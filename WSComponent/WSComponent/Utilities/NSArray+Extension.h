//
//  NSArray+Extension.h
//  WSComponent
//
//  Created by Quốc Tuyến on 11/25/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface NSArray (Extension)

- (void)each:(void (^)(id obj))block;
- (NSArray *)map:(id (^)(id obj))block;
- (NSArray *)flatMap:(id (^)(id obj))block;
- (NSArray *)filter:(BOOL (^)(id obj))block;

@end

NS_ASSUME_NONNULL_END

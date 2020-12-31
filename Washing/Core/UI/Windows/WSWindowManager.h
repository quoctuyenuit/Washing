//
//  WSWindowManager.h
//  Washing
//
//  Created by Quốc Tuyến on 11/23/20.
//  Copyright © 2020 QuocTuyen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "WSMacros.h"
#import "WSWindow.h"

NS_ASSUME_NONNULL_BEGIN

@interface WSWindowManager : NSObject

sharedInstance(WSWindowManager, sharedWindow)

@property(nonatomic, strong, readonly) WSWindow *rootWindow;

@end

NS_ASSUME_NONNULL_END

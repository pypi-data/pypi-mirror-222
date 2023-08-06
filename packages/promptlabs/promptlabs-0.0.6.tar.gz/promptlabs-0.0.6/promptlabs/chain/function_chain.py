import warnings
import os
from datetime import datetime
import re

from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, Callable
from abc import ABC, abstractmethod

from pydantic import Extra, Field, root_validator, PrivateAttr 
from promptlabs.chain.base_chain import Chain
from promptlabs.scheme.template import ChainOutput, ChainLog

class FunctionChain(Chain):
    
    _function: Callable = PrivateAttr(None)
    
    def with_function(self, function: Callable) -> 'FunctionChain':
        self._function = function
        return self
    
    @root_validator(pre=True)
    def set_function(cls, values: Dict) -> Dict:
        if 'function' in values['config']:
            function = values['config']['function']
        else:
            function = None
        values['_function'] = function
        return values
    
    @property
    def _chain_type(self) -> str:
        return self.config["type"]
    
    @property
    def _have_output(self) -> bool:
        if self.config['output_keys'] == []:
            return False
        else:
            return True
    
    def run(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any] = {}
    ) -> Tuple[ChainOutput, ChainLog]:
        
        # input validate
        try:
            self._validate_inputs(inputs)
        except Exception as e:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": str(e)})
            )
            
        # function validate
        if self._function is None and outputs == {} and self.output_keys != []:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": "You should Define Function or Mock outputs"})
            ) 
        
        if self._function is not None and outputs != {}:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": "You should Define Function or Mock outputs, not both"})
            ) 
            
        if self._function is not None:
            try:
                outputs = self._function(inputs)
            except Exception as e:
                return (
                    ChainOutput(chain_success=False),
                    ChainLog(logs = {"error_log": str(e)})
                )
            
        # output validate
        try:
            self._validate_outputs(outputs)
        except Exception as e:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": str(e)})
            )
            
        return (
                ChainOutput(chain_success=True, output_variables=outputs),
                ChainLog()
            )
        
    async def arun(
        self,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any] = {}
    ) -> Tuple[ChainOutput, ChainLog]:
        
        # input validate
        try:
            self._validate_inputs(inputs)
        except Exception as e:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": str(e)})
            )
            
        # function validate
        if self._function is None and outputs == {} and self.output_keys != []:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": "You should Define Function or Mock outputs"})
            ) 
        
        if self._function is not None and outputs != {}:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": "You should Define Function or Mock outputs, not both"})
            ) 
            
        if self._function is not None:
            try:
                outputs = await self._function(inputs)
            except Exception as e:
                return (
                    ChainOutput(chain_success=False),
                    ChainLog(logs = {"error_log": str(e)})
                )
            
        # output validate
        try:
            self._validate_outputs(outputs)
        except Exception as e:
            return (
                ChainOutput(chain_success=False),
                ChainLog(logs = {"error_log": str(e)})
            )
            
        return (
                ChainOutput(chain_success=True, output_variables=outputs),
                ChainLog()
            )

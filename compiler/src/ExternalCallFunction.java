import com.google.common.collect.ImmutableSet;
import com.google.inject.Singleton;
import com.google.template.soy.pysrc.restricted.PyExpr;
import com.google.template.soy.pysrc.restricted.SoyPySrcFunction;

import java.util.List;
import java.util.Set;

@Singleton public class ExternalCallFunction implements SoyPySrcFunction {

    private static final String PATH_NAME = "utils";

    @Override public String getName() {
        return "externalCall";
    }

    @Override public Set<Integer> getValidArgsSizes() {
        return ImmutableSet.of(1);
    }

    @Override public PyExpr computeForPySrc(List<PyExpr> args) {
        // First check for the data being available in injected data, otherwise, make an external call.
        // The period in split needs to be double escaped or it will be considered regex.
        String[] components = args.get(0).toPyString().getText().replaceAll("'", "").split("\\.");
        String methodName = components[components.length - 1];
        String fileName = components[components.length - 2];
        String expr = String.format("(ijData['%s'].get('%s') if '%s' in ijData else ",
                fileName, methodName, fileName);
        expr += String.format("__import__('%s.%s', globals(), locals(), -1).%s())",
                PATH_NAME, fileName, methodName);
        return new PyExpr(expr, Integer.MAX_VALUE);
    }
}